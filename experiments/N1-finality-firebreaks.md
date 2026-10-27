# N1: do firebreaks help Noesis finality? (pre-registered 2026-10-27, before any run)

**Origin.** The X8 Gaia test suggested (consistency level only) that well-mixed systems spread small shocks thin but fail all at once, while patched systems contain failure (Daisyworld local seeding; Haldane and May 2011 on banking). Noesis finality is one well-mixed vote. Question: would splitting it into patches (domains, each with its own vote) contain an attacker who controls part of the contribution side?

**The rule modeled (from code).** Noesis `node/src/runtime.rs` at commit `be219951`, `finalizes_pos_pom` (lines 1730-1772): a checkpoint finalizes iff (a) on side shares (each side divided by its own registered total), capital_share/3 + contribution_share*2/3 >= 2/3 (`FINALITY_MIX` 1/3 : 2/3, `TWO_THIRDS_BPS` 6667), and (b) the voters for it hold at least 50% of all stake and at least 50% of all standing (`MIN_DIM_BPS` 5000). Simplifications: no capital time-decay, quorum floor 0 (the default), everyone votes, the attacker votes as one bloc, honest voters vote for honest checkpoints and against bad ones.

**Designs compared.**
- **Well-mixed (Noesis today):** one vote over everyone.
- **Patched (hypothetical):** 10 equal domains, each running the same rule over its own members; a checkpoint is globally final iff domains holding at least 2/3 of total standing finalize it. A domain whose local vote the attacker controls can finalize bad local state there (local damage).

**Attacker.** Capital share c (spread evenly over domains, since capital is not domain-specific) and contribution share f, concentrated in k of the 10 domains (k = 10 is spread evenly; smaller k is more concentrated). c in {0.1, 0.3, 0.5, 0.6}; f from 0 to 1.

**Predictions, with hit and miss criteria.** Thresholds are the smallest f at which the event happens, found on a 0.01 grid.
- **N1-a (global safety):** at c = 0.5 and k <= 3, the patched design is captured globally (a bad checkpoint finalizes) at a total contribution share at least 0.10 lower than the well-mixed design. Hit if the gap is >= 0.10; miss otherwise.
- **N1-b (graded local damage):** at c = 0.5 and k <= 3, there is a range of f in which the patched design suffers local damage (some domains finalize bad state) while the well-mixed design suffers none. Hit if that range has width >= 0.10; miss otherwise.
- **N1-c (liveness):** at c = 0.1 and k <= 3, the attacker halts global finality in the patched design at a total contribution share at least 0.10 lower than in the well-mixed design. Hit if the gap is >= 0.10.
- **N1-d (capital floor):** with c < 0.5, no contribution share lets the attacker finalize a bad checkpoint in either design. Hit if zero bad finalizations occur for every f when c in {0.1, 0.3}.
- **Overall:** the X8 firebreak suggestion transfers to Noesis finality only if N1-a and N1-c both miss (patching does not weaken global safety or liveness). Registered expectation: it does not transfer.

**Prior knowledge.** High. These values follow from the rule by hand calculation, done while writing this registration. The run is a numerical check of that reasoning and a map of the trade-off, not independent evidence for ETM. Its value is design guidance for Noesis.

**Results.** To be appended below after the run, without editing anything above.

**Addendum before any run (2026-10-27).** The registration did not say what happens when a concentrated attacker's standing exceeds what its k domains can hold. Defined now, before running: a k-concentrated attacker holds standing only in its k domains, up to 100% of each; standing beyond k/10 of the total cannot be placed (this models a wash ring confined to its niche). Separately, and NOT part of the registered predictions, the run also reports a **strategic attacker** who places standing in whatever domains minimize the total needed. Reason for adding it: Noesis's adversary model is strategic, so the confined case alone could mislead design.

---

## Results (run 2026-10-27, after the addendum)

Script `n1_finality_firebreaks.py`; output `N1-run-2026-10-27.out`.

| Registered prediction | Verdict | Numbers |
|---|---|---|
| N1-a patched easier to capture globally (c = 0.5, k <= 3) | **MISS** | A confined attacker (k <= 3) cannot capture patched finality at any share; well-mixed falls at f = 0.75. |
| N1-b graded local damage | **HIT** | Patched suffers local damage from f = 0.08 (k = 1), 0.15 (k = 2), 0.23 (k = 3); well-mixed suffers none below 0.75. |
| N1-c patched easier to halt (c = 0.1, k <= 3) | **MISS** | A confined attacker (k <= 3) cannot halt patched finality; well-mixed halts at f = 0.46. |
| N1-d capital floor | **HIT** | With c < 0.5, no bad finalization in either design at any f. |
| Overall (transfers iff N1-a and N1-c both miss) | **TRANSFERS, against a confined attacker** | The registered expectation (does not transfer) was wrong under the registered model. |

**Strategic attacker (not registered; reported because Noesis's adversary is strategic):** patched finality falls to a bad checkpoint at f = 0.525 (well-mixed 0.75) and halts at f = 0.104 (well-mixed 0.26) at c = 0.5; at c = 0.1 it halts at f = 0.184 (well-mixed 0.46). Against an attacker who can choose where to place standing, patching is much weaker on both safety and liveness.

**Well-mixed liveness (the current rule):** finality halts when the attacker holds f >= 0.46 of standing with 10% of capital, f >= 0.36 with 30%, f >= 0.26 with 50%, and with more than 50% of capital alone (the capital veto, by design per the code's own comment).

**Reading.** Firebreaks help exactly when an attacker cannot choose its domain, and hurt when it can. So the transfer from Daisyworld and banking holds only if standing is confined by construction: standing earned in one domain counts only in that domain, the way a cell belongs to its tissue. Then a wash ring is stuck in its niche, and patching contains it. Without that, Noesis should keep its well-mixed finality. Design candidate (not built, Will-gated): domain-bound standing with patched finality, tested against a strategic attacker who must farm standing separately in each domain it wants to influence. Separately: the current rule's soft spot is liveness, not safety (halting needs far less standing than capturing).
