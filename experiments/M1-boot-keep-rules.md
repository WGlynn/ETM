# M1: which keep rule recovers what a curator judged worth loading? (pre-registered 2026-10-27, before any run)

**Why.** An AI collaborator's memory (JARVIS) loads a fixed byte budget of memory at startup. Its loader keeps the safety index first and then the smallest files first; on 2026-10-27 this dropped the largest index file, which held the entries the system itself labels canonical. That is an intrinsic price (size) on a scarce resource, the pattern P1 predicts will fail ([PROGRAM.md](../PROGRAM.md)). This experiment compares keep rules on the same memory, as a first test of X2 and X3 ([TRANSFERS.md](../TRANSFERS.md)).

**What counts as worth (the target).** The memory files linked from the hand-curated top-level index (`MEMORY.md`): the curator's own judgment of what deserves startup space. This is a proxy for worth, not worth itself; real use in sessions is not logged (only 3 explicit memory reads appear in the 48 surviving session transcripts), which is itself a finding: rent paid by use cannot be enforced on a signal that is not recorded.

**Universe.** Top-level memory files in the memory library (private; only aggregate numbers are published). Links that originate in `MEMORY.md` or any `MEMORY_INDEX_*` file are excluded from every feature, so the curation cannot leak into the predictors.

**Keep rules** (each ranks the universe; the top K are kept; K = 40, the harness default):
- **random:** 1,000 draws; mean and 95% band.
- **size (current loader's principle):** smallest file first.
- **age, newest:** most recently created first (first commit date in the library's git history).
- **age, oldest:** earliest created first.
- **last touch (X2):** most recently changed first (last commit date). Proxy for time since last use.
- **inbound links (free credit):** number of other files linking to it.
- **PageRank (conserved credit):** each file splits one unit of credit among the files it links to, iterated (damping 0.85).

**Predictions** (a difference counts only if it is at least 2 of the 40 slots; a tie is a miss):
- **M1-a (X2):** last touch recovers more of the target than either age rule.
- **M1-b (X3):** PageRank (conserved credit) recovers more than raw inbound links (free credit).
- **M1-c (P1):** the size rule recovers no more than the top of the random band, and fewer than last touch, inbound links, and PageRank.

**Prior knowledge.** A sweep reader reported, before this registration, that a recency signal recovered 19 of 40 and a centrality blend 20 of 40 in an earlier run of the same harness. So the last-touch level is roughly known (that run used file modification time, not commit dates). The age rules, the size rule, and PageRank versus raw inbound links separately were not known.

**Known confounds.** Bulk commits (automated backups, mass reformatting) move many files' last-commit dates at once and blur last touch; the number of distinct last-commit dates is reported as a diagnostic. The curated set was written by the same person whose edits drive last-touch dates, which may favor last touch for reasons unrelated to use.

**Results.** To be appended below, after the run, without editing anything above.

---

## Results (run 2026-10-27, after pre-registration commit 4606644)

Script: `m1_keep_rules.py`; raw output: `M1-run-2026-10-27.out`. Universe 1,076 files; target 39 files; K = 40; random baseline mean 1.40 of 40, 95% band 0 to 4.

| Keep rule | Target recovered (of 40 kept) |
|---|---|
| size, smallest first (the current loader's principle) | 0.00 |
| age, oldest first | 0.00 |
| last touch (last commit date) | 1.00 |
| age, newest first | 5.00 |
| PageRank (conserved credit) | 8.00 |
| inbound links (free credit) | 8.18 |

**Verdicts as registered:**
- **M1-a (X2): MISS.** Last touch (1.0) did not beat the best age rule (newest first, 5.0). The pre-registered confound is the likely cause: 1,075 files share only 184 distinct last-commit times, because automated backups and bulk edits commit many files at once. Commit dates measure the backup schedule, not use. This run does not test X2; it shows that this library has no usable record of use.
- **M1-b (X3): MISS.** Conserved credit (8.00) and free credit (8.18) are tied. Both recover about six times the random rate.
- **M1-c (P1): MISS as registered.** The size rule recovered nothing (0 of 40, below the random mean), the worst of all rules, and 8 below both link-based rules. It missed the registered condition only because last touch, which failed for the reason above, scored 1.

**What the run does show:**
1. **The current loader's principle is the worst rule tested.** Keeping the smallest files first recovered none of the curated set. This is the direction P1 predicts; the registered prediction still counts as a miss.
2. **Conservation does not improve ranking in an honest graph.** That is a refinement of X3, not a refutation: conservation was imported from the Hayek machine as a defense against parasites, not as a better quality signal. Its value should appear only when someone pumps free credit. X3 is restated accordingly in TRANSFERS.md.
3. **Use is not recorded, so rent by use cannot be priced.** Commit dates are swamped by bulk commits, and only 3 explicit memory reads appear in 48 surviving session transcripts. Recording which memories are surfaced and used, per session, is the prerequisite for any test of X2 or X3 on this substrate.
4. **An earlier, unregistered result was inflated.** The library's own allocator harness reported centrality recovering 20 of 40 of a hand-curated set. That harness used a 191-file target (random about 7 of 40) and its link graph includes 80 links that originate in the curated index files themselves, so its features partly encode the curation they are scored against. This run excluded those links.
