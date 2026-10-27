# Claim ledger

Every claim the program makes, with its current status and the evidence behind it. Labels are defined in [STANDARDS.md](STANDARDS.md). A claim's status changes only with a dated note and a link to the evidence that changed it.

Last revised 2026-10-27.

## Thesis

| ID | Claim | Status | Evidence |
|---|---|---|---|
| T1 | A mind is an economy. | open | A frame, consistent with prior art (Minsky, Holland, Baum). Untested as a claim that predicts anything on its own. |
| T2 | An economy is a mind. Graded form (from X6): an economy is a mind to the degree it suppresses cheating by its parts. | open | Consistent with Hayek (1945) and the major-transitions literature. The graded form is new to this program and untested. |
| T3 | T1 and T2 hold at every scale and recursively ("as above, so below"). | open | Criteria for support are set in PROGRAM.md section 8 and are not yet met. Known limit: structure can transfer while dynamics flip (X7, scaling laws). |
| T4 | Worth is relational; a system stays healthy to the degree its prices track relational worth. | open | Supporting cases from the first sweep (notebook); no blind test yet. |

| T5 | Health is calibration at every scale: a small, stable gap between internal valuation and later external outcome; outcomes count by cost to fake. | candidate | PROGRAM.md section 1. Adopted for Noesis 2026-10-27. Planet leg checked (homeostasis, Lovelock and Margulis 1974); brain and market legs standard, not checked. First measurement, C1 (crates.io, 2026-10-27, `experiments/C1-crates-calibration.md`): the gauge is computable and stable year to year; owner-independent use forecasts better than all use; Noesis's `value_v5` flow is beaten by a plain count of independent users in 4 of 4 windows (registered expectation held). C2 (same data, transitive use): the flow beats the direct count but loses to a plain transitive count, 5 of 5 windows each, with gaps of a few thousandths of a rank correlation. |

## Predictions

| ID | Claim | Status | Evidence |
|---|---|---|---|
| P1 | Failures with economic effect concentrate on resources priced by intrinsic rules. | pre-registered, untested | Supporting cases in the authors' code (notebook), collected with known bias. Needs a blind tally. |
| X2 | Decay keyed on time since last use behaves as weak rent and beats decay keyed on age. | prediction, untested | TRANSFERS.md. |
| X3 | Conserved credit tracks use; free credit does not. | prediction, untested | TRANSFERS.md. Free-credit side observed (verified code instance; reported correlation). |
| X5 | Each exploit in a contribution economy breaks at least one of the five foundations of multicellular cooperation, as translated. | prediction, untested | SUBSTRATES.md. |
| X8 | Gaia test 1: ETM's economy-side conditions predict how planetary regulation survives cheaters (by-products, local feedback). | corrected after adversarial review: no evidence; partial consistency on both sides; two limits found | TRANSFERS.md, X8 test 1 and its corrections. |
| E-1 to E-4 | Gaia's answers predict for economies: attribution turns shared benefits into selected ones; local pools resist free riders better than one global pool; federations recover from cheater crashes; bounded weights stabilize. | corrected after review: E-1, E-2, E-3 partial, E-4 stretch; criteria were not registered, so all are consistency at most | TRANSFERS.md, X8 test 1, economy side. |
| M1 | Keep rules for a fixed memory budget, scored against a curator's choices (tests X2, X3, P1). | run; 3 of 3 registered predictions missed | experiments/M1-boot-keep-rules.md. The current loader's size rule recovered 0 of 40 (worst tested; random 1.4); link-based rules about 8; use is not recorded, so X2 was not testable; conserved and free credit tied, so X3 restated as an adversarial claim. |
| X9 | Rules that pay per identity are exploitable by splitting; pricing per unit of output fixes it. | prediction, partly observed | SUBSTRATES.md. Observed instance: a per-account reward floor found profitable to split (VibeSwap `contracts/incentives/ShapleyDistributor.sol:295` at `243280eb`, verified comment). |
| X11 | User choice prices out worthless contributions only when users sufficiently outnumber contributors and judging is cheap. | prediction, untested | SUBSTRATES.md, after Noe and Hammerstein (1994). |

## Normative hypotheses (what the right prices are)

| ID | Claim | Status | Evidence |
|---|---|---|---|
| H1 | Rent: a held item keeps its place by continuing to contribute. | designed in several systems; enforced in none of the authors' live systems | Noesis keeps the rule as a constraint, pinned by a test (`node/src/lib.rs:1150-1156` at `be219951`), but its decay operation has no production caller (`lib.rs:644`; calls only at `:734`, `:817`). JARVIS measures use but does not enforce rent (ERRATA E4). Built and working in prior art: the Hayek machine removes agents that go broke. |
| H2 | Provenance value: what enables later work accrues part of the worth of what it enabled. | built in a reference contract; not deployed | VibeSwap `contracts/incentives/FractalShapley.sol:82,141` at `243280eb`: credit flows back through a declared influence graph, 30% decay per hop (verified). Prior art: Holland's bucket brigade (1985). |
| H3 | Age, surprise in bits, and query-time attention are inadequate as the only price of a held item (revised: time since last use is allowed). | open, revised | Revision from X2. Counter-evidence to weigh: on public jury labels, a popularity-heavy learned judge scored about 0.60 against about 0.54 for graph-topology features alone (Noesis `ARCHITECTURE.md:224-225` at `be219951`, verified). |
| G1 | Grounding: relational prices track worth only when the relations bottom out in minds outside the contributor's control. | candidate | Consistent with the Hayek machine (all money enters from the world), host sanctions, and biological markets. Designed, not built, in Noesis. |

## The wash

| ID | Claim | Status | Evidence |
|---|---|---|---|
| W1 | The wash (cheating that looks like contribution) appears at every scale of the correspondence. | supported by known cases at several scales; not a prediction | Parasites in Holland's classifier systems; cancer as cheating (Aktipis et al. 2015); wash trading; Noesis's measured result that structural signals inside a contribution graph do not separate a competent wash; a VibeSwap reference contract whose "importance" score anyone can pump (verified). |
| W2 | Every fix that has worked uses an outside anchor and a comparison against a fake. | candidate | Reported by a sweep reader across several systems; to be checked case by case. |
