"""N1: do firebreaks help Noesis finality? Pre-registration: N1-finality-firebreaks.md.
Rule: Noesis node/src/runtime.rs finalizes_pos_pom at be219951 (side-share bar 2/3 with mix 1/3:2/3; 50% floor per side).
Simplifications as registered: no capital decay, quorum floor 0, full turnout, bloc attacker."""
import numpy as np

D = 10
EPS = 1e-9


def finalizes(cap_share, st_share):
    bar = cap_share / 3 + 2 * st_share / 3 >= 2 / 3 - EPS
    return bar and cap_share >= 0.5 - EPS and st_share >= 0.5 - EPS


def well_mixed(c, f):
    return finalizes(c, f), not finalizes(1 - c, 1 - f)          # (bad finalizes, honest blocked)


def patched(c, shares):
    bad = [finalizes(c, x) for x in shares]
    ok = [finalizes(1 - c, 1 - x) for x in shares]
    need = 2 / 3 - EPS
    return sum(bad) / D >= need, sum(ok) / D < need, sum(bad) / D   # global bad, global blocked, local damage


def confined(f, k):
    x = min(1.0, f * D / k)
    return [x] * k + [0.0] * (D - k)


grid = np.round(np.arange(0, 1.0001, 0.01), 2)


def first(pred):
    for f in grid:
        if pred(f):
            return float(f)
    return None


def strategic_min_f(c, goal):
    """Smallest total share that achieves goal by placing the per-domain minimum in the fewest domains."""
    best = None
    for m in range(1, D + 1):
        xs = first(lambda x: (finalizes(c, x) if goal == "bad" else not finalizes(1 - c, 1 - x)))
        if xs is None:
            return None
        shares = [xs] * m + [0.0] * (D - m)
        g_bad, g_block, _ = patched(c, shares)
        if (goal == "bad" and g_bad) or (goal == "block" and g_block):
            tot = xs * m / D
            best = tot if best is None else min(best, tot)
    return best


print("well-mixed thresholds (smallest f):")
for c in (0.1, 0.3, 0.5, 0.6):
    print(f"  c={c}: bad finalizes at f={first(lambda f: well_mixed(c, f)[0])}, honest blocked at f={first(lambda f: well_mixed(c, f)[1])}")
print("patched, confined attacker (k domains):")
res = {}
for c in (0.1, 0.3, 0.5, 0.6):
    for k in (1, 2, 3, 5, 10):
        gb = first(lambda f: patched(c, confined(f, k))[0])
        bl = first(lambda f: patched(c, confined(f, k))[1])
        dmg = first(lambda f: patched(c, confined(f, k))[2] > 0)
        res[(c, k)] = (gb, bl, dmg)
        print(f"  c={c} k={k:2d}: global bad at f={gb}, global blocked at f={bl}, first local damage at f={dmg}")
print("patched, strategic attacker:")
for c in (0.1, 0.5, 0.6):
    print(f"  c={c}: min f for global bad {strategic_min_f(c, 'bad')}, min f to block {strategic_min_f(c, 'block')}")

wm_bad_05 = first(lambda f: well_mixed(0.5, f)[0])
wm_blk_01 = first(lambda f: well_mixed(0.1, f)[1])
a = [res[(0.5, k)][0] for k in (1, 2, 3)]
a_hit = all(x is not None and wm_bad_05 - x >= 0.10 for x in a)
b_hit = any(res[(0.5, k)][2] is not None and wm_bad_05 - res[(0.5, k)][2] >= 0.10 for k in (1, 2, 3))
cc = [res[(0.1, k)][1] for k in (1, 2, 3)]
c_hit = all(x is not None and wm_blk_01 - x >= 0.10 for x in cc)
d_hit = all(first(lambda f: well_mixed(c, f)[0]) is None and all(res[(c, k)][0] is None for k in (1, 2, 3, 5, 10))
            for c in (0.1, 0.3))
print(f"N1-a {'HIT' if a_hit else 'MISS'} (patched global-bad thresholds k<=3 {a} vs well-mixed {wm_bad_05})")
print(f"N1-b {'HIT' if b_hit else 'MISS'} (first local damage k<=3 {[res[(0.5,k)][2] for k in (1,2,3)]} vs well-mixed {wm_bad_05})")
print(f"N1-c {'HIT' if c_hit else 'MISS'} (patched block thresholds k<=3 {cc} vs well-mixed {wm_blk_01})")
print(f"N1-d {'HIT' if d_hit else 'MISS'} (no bad finalization with c<0.5 in either design)")
