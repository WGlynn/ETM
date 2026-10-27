#!/usr/bin/env python3
"""C2: does Noesis's flow price transitive use? Registration: C2-crates-transitive-use.md (ETM cc90b37).

Reuses C1's cache, loader rules, V (value_v5 downstream flow) and isotonic map unchanged.
New: Y_T = new crates (created in the window) that reach d through owner-independent chains by
window end; NC = crates reaching d at the cutoff. Both counted with a k-min reachability sketch
(Cohen 1997): 128 exponential ranks per crate, seed 0, estimate (k-1)/sum(minimums).

Usage: python c2_crates_transitive.py --cache DIR   (the C1 cache)
"""
import argparse, datetime as dt, json, os, sys, time
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.stats import rankdata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # C1's code, unchanged
from c1_crates_calibration import downstream_flow, fit_iso, CUTOFFS, WINDOW

K, BOOT, SEED, CHUNK = 128, 1000, 0, 200_000
T0 = time.time()


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


def reach_count(n, src, dst, member, ranks):
    """Estimated number of `member` crates that reach each crate through edges src->dst (src built
    on dst), cycles merged (a merged node's reach excludes its own members). Exactly 0 iff empty."""
    k = ranks.shape[1]
    g = csr_matrix((np.ones(len(src)), (src, dst)), shape=(n, n))
    ncomp, comp = connected_components(g, directed=True, connection="strong")
    # incl[c] = min rank over member crates of component c
    incl = np.full((ncomp, k), np.inf, dtype=np.float32)
    mi = np.flatnonzero(member)
    order = np.argsort(comp[mi], kind="stable")
    mc, mr = comp[mi][order], ranks[mi][order]
    if len(mc):
        u, starts = np.unique(mc, return_index=True)
        incl[u] = np.minimum.reduceat(mr, starts, axis=0)
    cs, cd = comp[src], comp[dst]
    keep = cs != cd
    ce = np.unique(np.stack([cs[keep], cd[keep]], axis=1), axis=0)  # (child comp, parent comp)
    level = np.zeros(ncomp, dtype=np.int64)
    while True:  # longest path from a childless component; terminates because the condensation is a DAG
        new = level.copy()
        np.maximum.at(new, ce[:, 1], level[ce[:, 0]] + 1)
        if np.array_equal(new, level):
            break
        level = new
    S = np.full((ncomp, k), np.inf, dtype=np.float32)
    lev_e = level[ce[:, 1]]
    for L in range(1, int(level.max()) + 1):
        eL = ce[lev_e == L]
        eL = eL[np.argsort(eL[:, 1], kind="stable")]
        for a in range(0, len(eL), CHUNK):
            ch = eL[a:a + CHUNK]
            vals = np.minimum(S[ch[:, 0]], incl[ch[:, 0]])
            u, starts = np.unique(ch[:, 1], return_index=True)
            S[u] = np.minimum(S[u], np.minimum.reduceat(vals, starts, axis=0))
    tot = S.sum(axis=1, dtype=np.float64)
    est = np.where(np.isfinite(tot), (k - 1) / np.where(np.isfinite(tot), tot, 1.0), 0.0)
    return est[comp], int(level.max())


def boot_spearman_diff(a, b, y, rng):
    n = len(y)
    out = []
    for _ in range(BOOT):
        i = rng.integers(0, n, n)
        ry = rankdata(y[i])
        out.append(np.corrcoef(rankdata(a[i]), ry)[0, 1] - np.corrcoef(rankdata(b[i]), ry)[0, 1])
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))


def spearman(a, y):
    return float(np.corrcoef(rankdata(a), rankdata(y))[0, 1])


def main(cache):
    e = np.load(os.path.join(cache, "edges.npy"))
    c = np.load(os.path.join(cache, "created.npy"))
    with open(os.path.join(cache, "owners.json")) as f:
        owners = {int(k): frozenset(v) for k, v in json.load(f).items()}
    idx = {int(k): i for i, k in enumerate(c[:, 0])}
    n, created = len(c), c[:, 1]
    src = np.array([idx[int(s)] for s in e[:, 0]])
    dst = np.array([idx[int(d)] for d in e[:, 1]])
    date = e[:, 2]
    EMPTY = frozenset()
    indep = np.array([bool(owners.get(int(s), EMPTY)) and bool(owners.get(int(d), EMPTY))
                      and owners[int(s)].isdisjoint(owners[int(d)]) for s, d in e[:, :2]])
    ranks = np.random.default_rng(SEED).standard_exponential((n, K), dtype=np.float32)
    boot_rng = np.random.default_rng(SEED)
    log(f"crates {n:,} edges {len(e):,} independent {indep.mean():.3f}")

    win = []
    for cut in CUTOFFS:
        t = dt.date.fromisoformat(cut).toordinal()
        pop = created <= t
        past = (date <= t) & indep
        end = (date <= t + WINDOW) & indep
        V, _, _ = downstream_flow(n, src[past], dst[past])
        N1 = np.bincount(dst[past], minlength=n).astype(float)
        NC, depth_t = reach_count(n, src[past], dst[past], created <= t, ranks)
        YT, depth_e = reach_count(n, src[end], dst[end], (created > t) & (created <= t + WINDOW), ranks)
        sc = {"V": V[pop], "N1": N1[pop], "NC": NC[pop]}
        Y = YT[pop]
        B = (Y > 0).astype(float)
        w = {"cutoff": cut, "n": int(pop.sum()), "base_rate_BT": float(B.mean()), "mean_YT": float(Y.mean()),
             "p99_YT": float(np.percentile(Y, 99)), "max_YT": float(Y.max()), "depth_t": depth_t, "depth_end": depth_e,
             "spearman": {s: spearman(v, Y) for s, v in sc.items()}}
        for a, b in (("V", "N1"), ("V", "NC")):
            w[f"sp_{a}_minus_{b}"] = {"mean": w["spearman"][a] - w["spearman"][b],
                                      "ci95": boot_spearman_diff(sc[a], sc[b], Y, boot_rng)}
        win.append((w, sc, B))
        log(f"{cut}: n {w['n']:,} base {w['base_rate_BT']:.4f} meanYT {w['mean_YT']:.1f} Spearman "
            + " ".join(f"{s} {v:.4f}" for s, v in w["spearman"].items())
            + f" | V-N1 {w['sp_V_minus_N1']['ci95']} V-NC {w['sp_V_minus_NC']['ci95']}")

    for k in range(1, len(win)):
        (wp, scp, Bp), (w, sc, B) = win[k - 1], win[k]
        w["brier_clim"] = float(((Bp.mean() - B) ** 2).mean())
        w["brier_oot"], w["brier_hind"] = {}, {}
        for s in sc:
            w["brier_oot"][s] = float(((fit_iso(scp[s], Bp).predict(sc[s]) - B) ** 2).mean())
            w["brier_hind"][s] = float(((fit_iso(sc[s], B).predict(sc[s]) - B) ** 2).mean())
        log(f"{w['cutoff']}: Brier oot " + " ".join(f"{s} {v:.5f}" for s, v in w["brier_oot"].items())
            + f" | hind V {w['brier_hind']['V']:.5f} | clim {w['brier_clim']:.5f}")

    W = [w for w, _, _ in win]
    G = W[1:]

    def verdict(key):
        better = sum(1 for w in W if w[key]["ci95"][0] > 0)
        worse = sum(1 for w in W if w[key]["ci95"][1] < 0)
        return {"verdict": "HIT" if better >= 4 else "REVERSED" if worse >= 4 else "NULL",
                "windows_V_better": better, "windows_other_better": worse}

    res = {"C2-a": verdict("sp_V_minus_N1"), "C2-b": verdict("sp_V_minus_NC"),
           "C2-c": {"verdict": "HIT" if all(w["brier_oot"]["V"] <= 1.10 * w["brier_hind"]["V"]
                                            and w["brier_oot"]["V"] < w["brier_clim"] for w in G) else "MISS",
                    "oot_over_hind_V": [round(w["brier_oot"]["V"] / w["brier_hind"]["V"], 4) for w in G],
                    "bss_V": [round(1 - w["brier_oot"]["V"] / w["brier_clim"], 4) for w in G]},
           "windows": W}
    print(json.dumps(res, indent=1))
    with open(os.path.join(cache, "c2_results.json"), "w") as f:
        json.dump(res, f, indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", required=True)
    main(ap.parse_args().cache)
