# C1: are Noesis valuations calibrated on real reuse? (pre-registered 2026-10-27, before any time-split data is built or any outcome seen)

**In short:** Price every crate with the flow part of Noesis's settlement rule, using only what was known on a given date. Then check the next year. Do the prices forecast which crates unrelated owners start to depend on? Do they beat a plain count of users?

**Origin.** On 2026-10-27 Will adopted calibration as Noesis's success measure: how well its valuations today predict independent use later (Noesis `docs/research/calibration-is-homeostasis.md`, commits `19b0dcbb`, `a2466ce6`; ETM PROGRAM.md T5 candidate). That doc proposes this test as the first measurement. Nothing computes calibration yet.

**What was already tested on this data, and is not repeated here.** A learned v(S) has come out null three times: twice on DeepFunding, then in July 2026 on this same crates.io dump. On crates, the learned score reached 0.5201 pairwise accuracy against 0.5167 for the plain breadth proxy, inside a noise band of +/-0.0144 (Noesis `data/crates/RESULTS.md`, commit `5d1a084`, 20 seeds). That test asked one question: does the shape of what a crate builds on predict how much it gets reused? It used a single snapshot. This test differs in three registered ways:
1. **Time split.** Valuations are computed from the graph as it stood at a cutoff t and graded against reuse that happened after t. That is calibration, not snapshot prediction.
2. **Independence.** Only reuse by unrelated owners counts, in the valuation and in the outcome. Here "unrelated" means the two crates share no owner. That is a weak test, since a second account is free (see limits), but it is the one the data records.
3. **It grades Noesis's own valuation rule**, the settlement form `value_v5` (downstream flow through a saturating gate), not a new learned predictor and not the ancestor features.

## Data

crates.io dump `2026-07-15-020010` (Noesis `data/crates/db-dump.tar.gz`, gitignored). Edge filter identical to `build_dataset.py`: normal dependencies (`kind = 0`), not optional, not target-gated, crate level, self-edges dropped. Edge `r -> d` means r depends on d, so r built on d.

- **Edge date:** the earliest `versions.created_at` among r's versions that declare the dependency (first adoption). Yanked versions are kept, since the adoption happened.
- **Owners:** `crate_owners.csv` as recorded in the dump, user and team ids kept apart by kind. Two crates are **independent** iff both owner sets are non-empty and disjoint. This is the rule in `periphery_grounding.py`, which mirrors `independent_use_gate` (Noesis `node/src/lib.rs:7384` at `df96405d`).
- **Cutoffs:** t in {2021-07-01, 2022-07-01, 2023-07-01, 2024-07-01, 2025-07-01}; window length 365 days. The last window ends 2026-07-01, before the dump date.
- **Population at t:** every crate created on or before t.
- **Outcome for crate d at t:** Y = the number of crates r, independent of d, whose first adoption of d falls in (t, t + 365 days]. B = [Y >= 1].

## Scorers (all computed only from edges dated on or before t)

- **V (Noesis, the graded rule):** the realized downstream flow of `value_v5` (Noesis `lib.rs` at `df96405d`: `value_v5` :1189, `downstream_flow_external` :3694, `value_flow_with_own` :3606, joint tail `RHO = 1/phi` :3646). Over independent edges only (the crates analog of "child contributor differs from parent contributor"): `flow(x) = own(x) + D * sum_j RHO^j * flow(child_j)`, children sorted by flow, descending; downstream = flow - own, clamped at 0. Constants as the code's tests use them (`lib.rs:1594-1597`): D = 0.85, HALF = 8. No parameter is tuned on this data.
  - **own = 1 for every crate.** Crates carry no content bytes here, so the novelty and semantic floors cannot be computed; every crate is treated as one novel unit.
  - **Cycle rule (fixed now, before any run).** The crate-level graph has cycles: A depends on B in one version, B on A in a later one. With D * 1/(1 - RHO) = 0.85 * 2.618 > 1, the code's iteration grows without bound around a cycle. So each cycle is merged into one node first (the strongly connected components). A merged node's own value is its member count. Its children are the crates that built on any member. Every member receives the merged node's downstream flow. This is the cycle rule already adopted on this data in July (`RESULTS.md`, "Fix: `_longest_chain_condensation`"). The merged graph has no cycles, so the flow is computed exactly, children before parents. That equals the code's 200-iteration loop whenever the graph is less than 200 levels deep (the depth is reported).
  - **Multiple parents.** A Noesis cell has one parent; a crate has many dependencies. Each child's flow counts in full toward every crate it depends on (the code's per-edge rule, applied to each edge).
  - **Ranking on flow, not on the gate.** Noesis's value is `g(f) = f / (f + HALF)` (`flow_gate`, :1157), strictly increasing in f, so every metric below is identical on f and on g(f) in exact arithmetic. Scores use f to avoid floating-point saturation of g near 1.
- **N1 (null, form-matched):** the count of independent crates that depend on d at t. Same edges, same cutoff, no propagation.
- **N2 (null, no independence filter):** the count of all crates that depend on d at t.
- **S1 (secondary, not part of any prediction):** V's flow over all edges, identity-blind. This approximates `value_v8`'s canonical flow (`downstream_flow_canonical`, :3712) without its learned outcome factor, which was null on this data.

## Metrics

- **Discrimination:** AUC of each score for B, ties averaged; Spearman of each score with Y as a secondary figure.
- **Calibration (proper scoring rule, out of time):** for each graded window k (cutoffs 2022 to 2025), a monotone map from score to P(B) is fitted by isotonic regression on the previous window (score at t(k-1) against B in window k-1), then applied to the scores at t(k). Brier score on window k. The same procedure runs for every scorer. Two references: **climatology** (predict the previous window's base rate for every crate) and **hindsight** (isotonic fitted on window k itself, the best monotone map in hindsight). The first cutoff (2021) only supplies the first map.
- **Noise:** paired bootstrap over crates, 1,000 resamples, seed 0, 95% percentile interval on per-crate Brier differences. The isotonic maps are held fixed inside the bootstrap.

## Predictions, with hit and miss criteria

- **C1-a (sanity floor, not evidence for Noesis):** V's AUC for B is at least 0.70 in all 5 windows. Hit if so; miss otherwise. Expected: hit, because established dependencies tend to attract more dependents (preferential attachment; INFERRED, literature not checked).
- **C1-b (calibration holds across years):** in all 4 graded windows, V's out-of-time Brier is at most 1.10 times its hindsight Brier, and its Brier skill score against climatology is positive. Hit if both hold in all 4; miss otherwise. The 1.10 bound is a judgment made now: a 10% loss for pricing with last year's map. Expectation: uncertain, because the ecosystem's growth shifts the base rate every year.
- **C1-c (does Noesis's propagation add anything over the count?):** V's out-of-time Brier is lower than N1's, with the bootstrap interval of the difference excluding zero, in at least 3 of 4 graded windows. Hit if so. **Reversed** if N1 is lower with the interval excluding zero in at least 3 of 4. **Null** otherwise. Registered expectation: null or reversed (INFERRED: in citation networks, raw citation counts tend to forecast future citations about as well as PageRank-style scores; not checked against the literature).
- **C1-d (does pricing out same-owner use help?):** N1's out-of-time Brier is lower than N2's, with the interval excluding zero, in at least 3 of 4 graded windows. Hit if so; reversed or null as in C1-c. Registered expectation: lean hit, uncertain. Same-owner use may still signal an active project that outsiders later adopt.
- **Reading, fixed now.** C1-a and C1-b both hit: the calibration measure works on real data and V passes it. C1-c is the only test of whether Noesis's propagation rule earns its complexity; if it is null or reversed, the plain independent count is the better price on this evidence, and the report says so.

## What this test cannot show (written before the run)

1. **No content.** The novelty and semantic floors are skipped (own = 1). What is graded is the flow-and-gate core of the settlement rule only.
2. **No standing, no outcome factor.** On this data v5, v6 and v7 coincide if every crate counts as vested and legible; v8 differs by canonical flow and its learned factor (S1 approximates the first).
3. **Honest world, not attack.** Owner-disjointness is an identity signal, free to fake with a second account. Nobody was paid for crates.io reuse, so nobody had a reason to fake it. Calibration under attack, half of the homeostasis definition, is not tested.
4. **No self-fulfilling exposure.** Noesis valuations had no influence on crates.io adoption. Good for a clean test; a live system would need randomized exposure.
5. **Counting, not measuring.** A new dependent is an upper bound on dependence (a substitute might have served it), as the code's own comment says (`lib.rs:1151`).
6. **Owner sets are as of the dump date,** a small anachronism for earlier cutoffs.

## Prior knowledge (flagged)

Known before registering: the July null on ancestor features; the periphery figures on this dump (21.2% of crates with any reuse have at least one independent user; same-owner edges are 15.4% of all reuse edges; `RESULTS-PERIPHERY.md`); the dump's column headers, including that versions and owners carry dates. Not known: any time-split statistic, any base rate, any window's outcome, or the depth of the condensed graph.

**Results.** To be appended below after the run, without editing anything above.

---

## Results (run 2026-10-27, after registration commit `b3a21b8`)

Script `c1_crates_calibration.py`; output `C1-run-2026-10-27.out`. Data: 1,940,630 crate-level edges (same count as `build_dataset.py`), 84.6% of them between owner-disjoint crates. Condensed graph depth 17 to 20 levels (under 200, so the exact computation equals the code's loop); 6 to 10 cycles merged per cutoff on independent edges. Population grows from 58,653 crates (2021) to 183,433 (2025); the share that gains at least one new independent dependent in the next year falls from 8.6% to 6.1%.

| Registered prediction | Verdict | Numbers |
|---|---|---|
| C1-a V's AUC >= 0.70 in all 5 windows (sanity floor) | **HIT** | 0.818, 0.823, 0.830, 0.844, 0.836 |
| C1-b out-of-time Brier <= 1.10 x hindsight, and skill > 0, in all 4 graded windows | **HIT** | out-of-time / hindsight 1.002, 1.003, 1.005, 1.002; skill vs climatology 0.363, 0.365, 0.367, 0.352 |
| C1-c V beats the plain independent count N1 | **REVERSED** | N1 better in 4 of 4 windows, every interval excludes zero. V's Brier is higher by 0.0021 to 0.0022 (5 to 6%); skill 0.36 vs 0.39 to 0.40 |
| C1-d N1 beats the all-use count N2 | **HIT** | N1 better in 4 of 4, every interval excludes zero; N2's Brier is higher by 0.0058 to 0.0072 (15 to 18%) |

Out-of-time Brier by window (lower is better; climatology in the last column):

| cutoff | V | N1 | N2 | S1 | climatology |
|---|---|---|---|---|---|
| 2022-07-01 | 0.04712 | **0.04490** | 0.05185 | 0.06004 | 0.07399 |
| 2023-07-01 | 0.04233 | **0.04022** | 0.04740 | 0.05487 | 0.06662 |
| 2024-07-01 | 0.03692 | **0.03487** | 0.04072 | 0.04774 | 0.05835 |
| 2025-07-01 | 0.03720 | **0.03502** | 0.04081 | 0.04726 | 0.05745 |

**Not registered, reported for reading only.**
- S1 (the same flow over all edges, identity-blind) is the worst scorer in every window; V beats it in 4 of 4 with intervals excluding zero. On flows as on counts, dropping same-owner use is what helps.
- AUC over the whole population ranks N2 slightly above N1 (for example 0.825 vs 0.820 in 2021): having any use at all, including same-owner use, separates "will be adopted" from "will not" a little better at the zero boundary. Among crates already in use at the cutoff, N1 ranks far better (AUC 0.865 vs 0.797 in 2021). Spearman with the number of new adopters: N1 0.54 to 0.56, V about 0.003 lower, N2 and S1 0.33 to 0.38.
- The last window's mean number of new independent dependents per crate jumps to 3.90 (1.58 to 1.81 before) while the adopted share stays near 6%. It is broad, not a few accounts: 721,776 new independent edges from 100,450 adopting crates under 27,212 owners; the largest single owner made 1.0% of them.

## Reading

1. **The gauge works on real data.** Calibration, as Noesis now defines success, can be computed from a public dependency graph with a time split. It separates rival pricing rules with intervals that exclude zero in every window, and a price map fitted on one year transfers to the next with at most 0.5% loss while the number of crates grew threefold. That stability belongs to past independent use as a signal, not to Noesis's rule in particular: the plain count is just as stable.
2. **Noesis's propagation rule did not earn its complexity here.** Counting a crate's independent users forecasts its next year of independent adoption better than `value_v5`'s damped flow, in every window. The registered expectation (null or reversed) held. The flow is not far behind (AUC within 0.002), so propagation costs a little accuracy rather than breaking the price.
3. **Independence is where the signal is.** Removing same-owner use cuts the Brier score by 13 to 15% for counts and 21 to 23% for flows. This is the cost-to-fake line showing up as forecasting power in honest data. The identity-level test used here is free to fake, so this says nothing yet about an attacker.
4. **A scope point found after the run, recorded rather than used.** The outcome registered here is new *direct* dependents. The flow credits a crate for *transitive* use too (a crate deep under a popular one gets credit for that one's users). Those are different things, and it is possible that propagation is the right price for transitive use and the wrong forecaster of direct adoption. That would be a new question, needing its own registration; it does not change C1-c.

What this result supports, in the calibration doc's own terms: rival v(S) rules can be ranked by track record, and here the simpler rule ranked first.
