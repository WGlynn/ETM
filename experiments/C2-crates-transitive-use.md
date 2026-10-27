# C2: does Noesis's flow price transitive use? (pre-registered 2026-10-27, after C1, before any transitive statistic is computed)

**In short:** C1 found that a plain count of a crate's independent users forecasts its next year of direct adoption better than Noesis's flow. But the flow also credits a crate for use further down the chain. Does the flow forecast that transitive use? And does it beat a plain transitive count?

**Why this is a new test, not a rescue of C1.** C1-c stays as scored (REVERSED, `C1-crates-calibration.md`). The scope point that motivates C2 was written down after C1 ran, in C1's "Reading" item 4. **C2 uses the same dump, cutoffs and scorers as C1, so it is not fresh data.** It asks a different question about the same graph and is weaker evidence than a test on new data would be. The move that closes this gap: re-run C1 and C2 unchanged on a later crates.io dump (published daily), grading only the window that starts after 2026-07-15, once a full year of it exists.

## What is the same as C1

Everything below is unchanged from C1 and computed by the same code (`c1_crates_calibration.py`, ETM commit `fb2c1a5`):
- the dump (`2026-07-15-020010`), its edge filter, and how edges are dated;
- the owner rule for independence;
- the five cutoffs and the 365-day windows;
- the population: every crate created on or before the cutoff;
- scorer V, Noesis's `value_v5` flow over independent edges with cycles merged;
- scorer N1, the count of a crate's independent direct users.

## What is new

- **Chain of independent use.** Crate r reaches crate d if a chain of dependencies leads from r to d and every link in it joins two crates with no owner in common. This is the graph V already runs on. Owner-independence is checked per link, not between r and d themselves (a deliberate simplification, stated as a limit below).
- **Outcome.** Y_T(d) = the number of crates created in (t, t + 365 days] that reach d by the end of the window. Every such crate is new to d by construction, because it did not exist at t. B_T = [Y_T >= 1].
- **New null, NC (plain transitive count).** The number of crates that reach d at t. This is the transitive analog of N1. Without it, a flow win over N1 could just mean that transitive beats direct.
- **Counting method.** Distinct reachable crates cannot be counted by plain propagation, because a crate reached by two paths would count twice. Both Y_T and NC use the k-min reachability sketch (Cohen 1997): 128 independent exponential ranks per crate (seed 0), the minimum over each reachable set propagated children before parents, size estimated as 127 / (sum of the 128 minimums). The estimate is unbiased with about 9% relative error. It is exactly zero when the set is empty, so B_T is exact. Cycles are merged as in C1. A merged node's reach includes every crate that reaches any member, minus the members themselves.

## Metrics

- **Magnitude (primary):** Spearman rank correlation of each score with Y_T, in all 5 windows. A paired bootstrap over crates (1,000 resamples, seed 0, re-ranked each time) gives a 95% interval on the difference between two scorers' correlations.
- **Calibration (secondary):** Brier score on B_T, with the score-to-probability map fitted on the previous window as in C1, in the 4 graded windows.

## Predictions, with hit and miss criteria

- **C2-a (flow vs direct count, on transitive use):** V's Spearman with Y_T exceeds N1's, with the interval excluding zero, in at least 4 of 5 windows. Hit if so. **Reversed** if N1 exceeds V that way in at least 4 of 5. **Null** otherwise. Expectation: hit, because a crate deep under popular crates has few direct users and many transitive ones, and only the flow sees that.
- **C2-b (flow vs plain transitive count):** V's Spearman with Y_T exceeds NC's, by the same rule. Expectation: null or reversed, by analogy with C1. Damping and the geometric tail are what V adds over NC, and C1 gave no sign that they help.
- **C2-c (calibration holds):** in all 4 graded windows, V's out-of-time Brier on B_T is at most 1.10 times its hindsight Brier, and its skill against climatology is positive. Hit if so.
- **Reading, fixed now.** If C2-a and C2-b both hit, the flow prices transitive use better than either plain count, and it earns its place for that job. If C2-a hits and C2-b does not, the transitive signal is real but a plain transitive count captures it, so the damped flow is not supported. If C2-a misses, the flow does not even beat the direct count on the use it claims to price.

## Limits (written before the run)

All of C1's limits apply: honest world, no attacker; owner-disjointness is free to fake; no content floors; counting, not measuring. In addition:
1. **Per-link independence.** A crate can reach d through a chain of owner-disjoint links while sharing an owner with d.
2. **New crates only.** Existing crates that newly come to reach d during the window are not counted. That keeps "new user" unambiguous, at the cost of missing that adoption.
3. **Estimated counts.** Y_T and NC carry about 9% sketch noise. The noise is the same for every scorer, so it widens intervals without favoring any scorer.
4. **Same data as C1.** See above.

## Prior knowledge (flagged)

Everything in C1, including its results: on direct adoption, V and N1 were close (AUC within 0.002), and N1 won on Brier. The last window had a broad surge of new crates (100,450 adopting crates, 27,212 owners). Not known: any reach count, any transitive outcome, or any C2 statistic.

**Results.** To be appended below after the run, without editing anything above.
