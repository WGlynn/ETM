# Errata

Corrections to published ETM texts. The original texts in [papers/](papers/) are never edited; corrections are recorded here with evidence, dated, and linked from the paper's header.

Pinned commits used below:
- Noesis: `be219951` (github.com/WGlynn/noesis, branch master).
- VibeSwap: `243280eb` (github.com/WGlynn/VibeSwap).

## Economic Theory of Mind (essay, August 2026)

### E1. Finality is not given to contribution "rather than" stake (2026-10-27)
The essay says Noesis "earns the right to finalize through a Proof-of-Mind score, so influence goes to demonstrated contribution rather than to purchased stake."
**Correction:** Noesis finality weighs capital (proof of stake) at one third and contribution (proof of mind) at two thirds, with proof of work excluded (`node/src/runtime.rs:1664`, `FINALITY_MIX`). Each side must also independently supply at least 50% of its own total for a checkpoint to finalize (`runtime.rs:1676`, `MIN_DIM_BPS = 5000`). Capital keeps a third of the finality vote, and neither side can finalize alone. Accurate statement: capital cannot finalize without the consent of contribution, and contribution cannot finalize without the consent of capital.

### E2. The test count is out of date (2026-10-27)
The essay cites "a 358-test suite." At `be219951` the repository contains 613 functions marked `#[test]` (a count of test functions, not of a test run).

### E3. The wash was found before the essay, not predicted by it (2026-10-27)
The essay says a real theory "earns trust by predicting where its own hard problem will sit, and then being right," and presents the wash as that prediction.
**Correction:** the Noesis work that identified the wash as the open problem (commit `2c361bff`, 2026-07-20) predates the essay (commit `2b2e5141`, 2026-08-02). For this essay, the wash is a retrodiction. It would count as a prediction only if an earlier ETM text named it; none has been found yet (open question in PROGRAM.md).

### E4. JARVIS's memory does not yet prune by rent (2026-10-27)
The essay says a JARVIS primitive "pays rent to stay, and is pruned when it stops being applied, with credit flowing to the primitives that other primitives are built on," and that "it runs."
**Correction:** the system's own documentation says the opposite: "The corpus grows monotonically. Every session adds. Nothing decays unless it's explicitly contradicted." (VibeSwap `docs/jarvis-substrate/papers/how-jarvis-works.md:77` at `243280eb`). A sweep reader's audit of the memory's history found that rent-like scores are measured at startup but no code acts on them, and that almost nothing has been pruned (reported, not yet checked independently). Accurate statement: JARVIS measures which memories are used; it does not yet enforce rent.

### E5. Noesis does not yet implement state rent (2026-10-27)
The essay says Noesis "uses state-rent on a cell model ... so that persistence costs something and dead weight is pruned."
**Correction:** a search of `node/src` at `be219951` finds no state-rent or carrying-cost code; a carrying cost is designed (`ARCHITECTURE.md`, periphery section), not built. The one decay operation (`Op::Decay`, `node/src/lib.rs:644`) is called only from tests (`lib.rs:734`, `:817`). The code does pin the rule any future decay must follow: "any future decay must run on use, never on age" (`lib.rs:1150-1156`).

### Revisions (not errors of fact)
- **The refusal of recency** is narrowed by transfer X2 ([TRANSFERS.md](TRANSFERS.md)): time since last use is consistent with rent; time since creation is not.
- **The scope of "built"**: the essay's "what is actually built" section should be read against [CLAIMS.md](CLAIMS.md), which gives the current status of each mechanism.
