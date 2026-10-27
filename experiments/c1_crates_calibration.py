#!/usr/bin/env python3
"""C1: calibration of Noesis valuations on crates.io. Registration: C1-crates-calibration.md (ETM b3a21b8).

Two steps:
  build    one streaming pass over the crates.io dump -> dated edges, crate creation dates, owner sets
  analyze  per cutoff: scorers V (value_v5 downstream flow, independent edges), N1, N2, S1;
           outcome = new independent adopters in the next 365 days; registered metrics.

Usage: python c1_crates_calibration.py --dump PATH/db-dump.tar.gz --cache DIR
"""
import argparse, csv, datetime as dt, json, os, sys, tarfile, time
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.stats import spearmanr
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import roc_auc_score

# Noesis lib.rs at df96405d: test constants :1594-1597, joint tail RHO :3646
D, HALF, RHO = 0.85, 8.0, 0.6180339887498949
CUTOFFS = ["2021-07-01", "2022-07-01", "2023-07-01", "2024-07-01", "2025-07-01"]
WINDOW = 365
BOOT, SEED = 1000, 0
T0 = time.time()


def log(m):
    print(f"[{time.time() - T0:7.1f}s] {m}", flush=True)


# ============ build ============

def rows(tar, member):
    f = tar.extractfile(member)
    rd = csv.reader(line.decode("utf-8") for line in f)
    head = next(rd)
    return {k: i for i, k in enumerate(head)}, rd


def build(dump, cache):
    csv.field_size_limit(1 << 30)
    day = {}

    def ordinal(s):  # "2019-03-04 12:34:56..." -> date ordinal, cached on the date prefix
        k = s[:10]
        v = day.get(k)
        if v is None:
            v = day[k] = dt.date.fromisoformat(k).toordinal()
        return v

    created, owners, ver = {}, {}, {}
    first = {}  # (src, dst) -> earliest adoption ordinal
    kept = dropped = 0
    with tarfile.open(dump, "r|gz") as tar:  # members arrive crates, crate_owners, versions, dependencies
        for m in tar:
            if m.name.endswith("/data/crates.csv"):
                h, rd = rows(tar, m)
                for r in rd:
                    created[int(r[h["id"]])] = ordinal(r[h["created_at"]])
                log(f"crates {len(created):,}")
            elif m.name.endswith("/data/crate_owners.csv"):
                h, rd = rows(tar, m)
                for r in rd:
                    owners.setdefault(int(r[h["crate_id"]]), set()).add(r[h["owner_kind"]] + ":" + r[h["owner_id"]])
                log(f"owned crates {len(owners):,}")
            elif m.name.endswith("/data/versions.csv"):
                h, rd = rows(tar, m)
                for r in rd:
                    ver[int(r[h["id"]])] = (int(r[h["crate_id"]]), ordinal(r[h["created_at"]]))
                log(f"versions {len(ver):,}")
            elif m.name.endswith("/data/dependencies.csv"):
                assert ver, "versions.csv must precede dependencies.csv in the archive"
                h, rd = rows(tar, m)
                ik, io_, it, iv, ic = h["kind"], h["optional"], h["target"], h["version_id"], h["crate_id"]
                for r in rd:  # same filter as noesis data/crates/build_dataset.py
                    if r[ik] != "0" or r[io_] in ("t", "true", "1") or r[it]:
                        dropped += 1; continue
                    v = ver.get(int(r[iv]))
                    dst = int(r[ic])
                    if v is None or v[0] == dst:
                        dropped += 1; continue
                    key = (v[0], dst)
                    old = first.get(key)
                    if old is None or v[1] < old:
                        first[key] = v[1]
                    kept += 1
                log(f"dep rows kept {kept:,} dropped {dropped:,}; crate edges {len(first):,}")
    os.makedirs(cache, exist_ok=True)
    e = np.array([(s, d, t) for (s, d), t in first.items()], dtype=np.int64)
    np.save(os.path.join(cache, "edges.npy"), e)
    c = np.array(sorted(created.items()), dtype=np.int64)
    np.save(os.path.join(cache, "created.npy"), c)
    with open(os.path.join(cache, "owners.json"), "w") as f:
        json.dump({str(k): sorted(v) for k, v in owners.items()}, f)
    log("build cached")


# ============ analyze ============

def downstream_flow(n, src, dst, own_unit=1.0):
    """value_v5 realized downstream flow over edges src->dst (src built on dst), with the
    registered cycle rule: merge strongly connected components, own = member count, children =
    distinct crates outside the component that built on any member, each contributing its
    component's flow; joint geometric tail RHO^j over children sorted by flow descending.
    Returns (per-crate downstream flow, condensed DAG depth in levels, nontrivial SCC count)."""
    g = csr_matrix((np.ones(len(src)), (src, dst)), shape=(n, n))
    ncomp, comp = connected_components(g, directed=True, connection="strong")
    size = np.bincount(comp, minlength=ncomp).astype(float)
    cs, cd = comp[src], comp[dst]
    keep = cs != cd
    # children of a component = distinct child CRATES (registration wording), not components
    pairs = np.unique(np.stack([cd[keep], src[keep]], axis=1), axis=0)
    order = np.argsort(pairs[:, 0], kind="stable")
    pairs = pairs[order]
    starts = np.searchsorted(pairs[:, 0], np.arange(ncomp + 1))
    # topological order on the component DAG, children before parents (Kahn over child->parent)
    cedges = np.unique(np.stack([cs[keep], cd[keep]], axis=1), axis=0)
    indeg = np.bincount(cedges[:, 1], minlength=ncomp)  # number of child components per parent
    par_of = [[] for _ in range(ncomp)]
    for a, b in cedges:
        par_of[a].append(b)
    level = np.zeros(ncomp, dtype=np.int64)
    stack = list(np.flatnonzero(indeg == 0))
    flow = size * own_unit
    done = 0
    while stack:
        c = stack.pop()
        done += 1
        lo, hi = starts[c], starts[c + 1]
        if hi > lo:
            f = np.sort(flow[comp[pairs[lo:hi, 1]]])[::-1]
            flow[c] = size[c] * own_unit + D * float(np.dot(RHO ** np.arange(len(f)), f))
        for p in par_of[c]:
            level[p] = max(level[p], level[c] + 1)
            indeg[p] -= 1
            if indeg[p] == 0:
                stack.append(p)
    assert done == ncomp, "condensation must be acyclic"
    down = np.maximum(flow - size * own_unit, 0.0)
    return down[comp], int(level.max()), int((size > 1).sum())


def fit_iso(x, y):
    return IsotonicRegression(y_min=0.0, y_max=1.0, increasing=True, out_of_bounds="clip").fit(x, y)


def boot_ci(diff, rng):
    n = len(diff)
    means = np.array([diff[rng.integers(0, n, n)].mean() for _ in range(BOOT)])
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def analyze(cache):
    e = np.load(os.path.join(cache, "edges.npy"))
    c = np.load(os.path.join(cache, "created.npy"))
    with open(os.path.join(cache, "owners.json")) as f:
        owners = {int(k): frozenset(v) for k, v in json.load(f).items()}
    ids = c[:, 0]
    idx = {int(k): i for i, k in enumerate(ids)}
    n = len(ids)
    created = c[:, 1]
    ok = np.array([s in idx and d in idx for s, d in e[:, :2]])
    e = e[ok]
    src = np.array([idx[int(s)] for s in e[:, 0]])
    dst = np.array([idx[int(d)] for d in e[:, 1]])
    date = e[:, 2]
    EMPTY = frozenset()
    indep = np.array([bool(owners.get(int(s), EMPTY)) and bool(owners.get(int(d), EMPTY))
                      and owners[int(s)].isdisjoint(owners[int(d)]) for s, d in e[:, :2]])
    log(f"crates {n:,}; edges {len(e):,} (dropped {int((~ok).sum())} with unknown endpoint); "
        f"independent {indep.mean():.3f}")

    win = []
    for cut in CUTOFFS:
        t = dt.date.fromisoformat(cut).toordinal()
        pop = created <= t
        past = date <= t
        nxt = (date > t) & (date <= t + WINDOW) & indep
        Y = np.bincount(dst[nxt], minlength=n)[pop]
        B = (Y >= 1).astype(float)
        N2 = np.bincount(dst[past], minlength=n).astype(float)
        N1 = np.bincount(dst[past & indep], minlength=n).astype(float)
        V, depth, scc = downstream_flow(n, src[past & indep], dst[past & indep])
        S1, depth_all, scc_all = downstream_flow(n, src[past], dst[past])
        sc = {"V": V[pop], "N1": N1[pop], "N2": N2[pop], "S1": S1[pop]}
        w = {"cutoff": cut, "n": int(pop.sum()), "base_rate": float(B.mean()), "mean_Y": float(Y.mean()),
             "depth_V": depth, "scc_V": scc, "depth_S1": depth_all, "scc_S1": scc_all,
             "auc": {k: float(roc_auc_score(B, v)) for k, v in sc.items()},
             "spearman": {k: float(spearmanr(v, Y).statistic) for k, v in sc.items()},
             "any_use": int((N2[pop] > 0).sum())}
        # descriptive, unregistered: AUC among crates already used at t (where scorers disagree)
        used = N2[pop] > 0
        w["auc_used_unregistered"] = {k: float(roc_auc_score(B[used], v[used])) for k, v in sc.items()}
        win.append((w, sc, B))
        log(f"{cut}: n {w['n']:,} base {w['base_rate']:.4f} depth {depth} scc {scc} AUC "
            + " ".join(f"{k} {a:.4f}" for k, a in w["auc"].items()))

    rng = np.random.default_rng(SEED)
    for k in range(1, len(win)):
        (wp, scp, Bp), (w, sc, B) = win[k - 1], win[k]
        clim = np.full_like(B, Bp.mean())
        w["brier_clim"] = float(((clim - B) ** 2).mean())
        loss = {}
        w["brier_oot"], w["brier_hind"], w["bss"] = {}, {}, {}
        for s in sc:
            p = fit_iso(scp[s], Bp).predict(sc[s])
            loss[s] = (p - B) ** 2
            w["brier_oot"][s] = float(loss[s].mean())
            w["brier_hind"][s] = float(((fit_iso(sc[s], B).predict(sc[s]) - B) ** 2).mean())
            w["bss"][s] = 1.0 - w["brier_oot"][s] / w["brier_clim"]
        for a, b in (("V", "N1"), ("N1", "N2"), ("V", "S1")):
            d = loss[a] - loss[b]
            w[f"diff_{a}_minus_{b}"] = {"mean": float(d.mean()), "ci95": boot_ci(d, rng)}
        log(f"{w['cutoff']}: Brier oot " + " ".join(f"{s} {v:.5f}" for s, v in w["brier_oot"].items())
            + f" | clim {w['brier_clim']:.5f}")

    W = [w for w, _, _ in win]
    G = W[1:]

    def verdict(key):
        lo_hi = [w[key]["ci95"] for w in G]
        better = sum(1 for lo, hi in lo_hi if hi < 0)
        worse = sum(1 for lo, hi in lo_hi if lo > 0)
        return "HIT" if better >= 3 else "REVERSED" if worse >= 3 else "NULL", better, worse

    res = {
        "C1-a": {"verdict": "HIT" if all(w["auc"]["V"] >= 0.70 for w in W) else "MISS",
                 "auc_V": [round(w["auc"]["V"], 4) for w in W]},
        "C1-b": {"verdict": "HIT" if all(w["brier_oot"]["V"] <= 1.10 * w["brier_hind"]["V"] and w["bss"]["V"] > 0
                                         for w in G) else "MISS",
                 "oot_over_hind_V": [round(w["brier_oot"]["V"] / w["brier_hind"]["V"], 4) for w in G],
                 "bss_V": [round(w["bss"]["V"], 4) for w in G]},
        "C1-c": dict(zip(("verdict", "windows_V_better", "windows_N1_better"), verdict("diff_V_minus_N1"))),
        "C1-d": dict(zip(("verdict", "windows_N1_better", "windows_N2_better"), verdict("diff_N1_minus_N2"))),
        "S1_vs_V_unregistered": dict(zip(("verdict", "windows_V_better", "windows_S1_better"),
                                         verdict("diff_V_minus_S1"))),
        "windows": W,
    }
    print(json.dumps(res, indent=1))
    with open(os.path.join(cache, "c1_results.json"), "w") as f:
        json.dump(res, f, indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dump", required=True)
    ap.add_argument("--cache", required=True)
    a = ap.parse_args()
    if not os.path.exists(os.path.join(a.cache, "edges.npy")):
        build(a.dump, a.cache)
    analyze(a.cache)
