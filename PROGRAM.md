# The ETM research program

Last revised 2026-10-27. Status labels follow [STANDARDS.md](STANDARDS.md).

## 1. The thesis

- **T1. A mind is an economy.** Any system that must keep, attend to, or act on more than it has room for allocates scarce resources among competing uses. Whatever rule decides what is kept, dropped, or weighted works as a price, whether anyone designed it or not.
- **T2. An economy is a mind.** A system of many participants allocating scarce resources processes information that no single participant holds, and acts on it as a whole. Prices, credit, and reputation are how it thinks.
- **T3. As above, so below.** T1 and T2 hold at every scale and recursively. A mind is an economy of smaller minds; an economy is a mind made of minds. The same structure repeats from a single function in a program, to a person, to a team, to a market, to a blockchain.

The thesis is only worth holding if it does work. Its work is **transfer**: because the structure is shared, a result about one side should translate into a correct prediction about the other. The program tests ETM by attempting transfers and recording every outcome ([TRANSFERS.md](TRANSFERS.md)).

A second claim rides on the first, and it is where ETM takes a position the prior art does not take outright:

- **T4. Worth is relational.** A held item, whether a thought, a memory, an asset, or a contribution, is worth what it does for the rest of the system, not what it is on its own. A mind or economy stays healthy to the degree its prices track that relational worth, and it degrades where they do not.

- **T5. Health is calibration (candidate, 2026-10-27).** At every scale, a mind's health is a small, stable gap between what it values and what the world outside it later does. An organism holds its internal state against its environment (homeostasis); a brain, on the predictive-processing account, keeps prediction error small; a market's prices are supposed to anticipate scarcity; a contribution economy's prices should anticipate use. T5 makes T4 measurable, and it answers the judge problem: any judge inside a system favors what the system selected (survivorship), so health has to be scored against outcomes the system does not control. *Independence* of those outcomes is a price, not a fact: an outcome counts to the degree that faking it costs more than the reward it unlocks, the same line blockchain security draws between attack cost and attack reward. Status: candidate; the brain and market legs are standard accounts not yet checked here. Adopted as Noesis's success measure (Noesis `docs/research/calibration-is-homeostasis.md`, commit `19b0dcbb`).

## 2. The translation dictionary (provisional)

A transfer needs a fixed dictionary, written down before it is used, so that a prediction cannot be bent after the fact. This is the first draft. Entries are hypotheses; each one is only as good as the transfers it supports.

| Mind side | Economy side |
|---|---|
| attention, working memory, context window | capital, goods, block space, voting weight |
| holding a thought or memory | holding an asset that carries a cost |
| recalling or using an item | demand for it; consuming or building on it |
| forgetting | depreciation; exit from the market |
| credit assignment in learning | attribution of value: profit, royalties, Shapley shares |
| a coherent but worthless line of thought; a self-citing memory | wash trading; a self-dealing ring |
| salience capturing attention | advertising and hype capturing demand |
| an old belief holding weight by size or age | incumbency; capital concentration |
| consolidation into long-term memory | capital formation |
| a module whose output nothing uses | a firm with no customers |

## 3. How ETM gets proved

"Proved" here has two meanings, and the program pursues both.

**Formal route.** Write down the abstract structure the two sides are claimed to share (bounded agents, scarce resources, allocation rules, credit flowing along dependencies). Then prove theorems about that structure once. Any theorem proved there holds on both sides at once. Example of the pattern: the Shapley value's uniqueness theorem holds for every cooperative game, so if both credit assignment in a mind and attribution in an economy are cooperative games, the same fairness result governs both. Status: the abstract structure is not yet written down. That is the first formal task.

**Empirical route.** Accumulate transfers. A transfer counts as evidence only if:
1. it uses the dictionary as written before the prediction was made;
2. the prediction is recorded before the target side is checked;
3. the target-side result was not already known to whoever made the prediction, or was checked by someone who did not see the prediction.

A transfer where both sides were already known is recorded as **consistency**, not evidence. That keeps ETM from proving itself with examples chosen after the fact.

## 4. The first prediction (P1)

Take a system. List its scarce resources and the rule that allocates each. Classify each rule:

- **Intrinsic:** prices an item by a property it has on its own. Examples: size, novelty in bits, age since creation, raw balance, number of accounts, position in a file.
- **Relational:** prices an item by its effect on the rest. Examples: use by others, downstream dependence, measured counterfactual contribution, and (per transfer X2) time since last use.

**P1:** failures with economic effect (exploits, waste, decay, capture) concentrate on resources allocated by intrinsic rules.

**P1 is false if** failures are spread evenly across intrinsic and relational rules, or concentrate on relational ones.

Status: pre-registered here, **untested**. The first sweep found supporting cases, but it cannot test P1, because its readers knew the theory and its documents were written through this lens. The test P1 needs is a blind tally: someone who has not seen ETM codes a system's resources, rules and failures, and only then is the classification applied.

Known scope limits (open):
- **Design versus implementation.** In one VibeSwap audit set the lens accounted for 6 of 10 economic-design findings and 0 of 4 critical code bugs (reported by a sweep reader, not yet checked). P1 may be a claim about design failures only.
- **Deliberately neutral rules.** A batch auction that ignores every trader's history, and a consensus safety path that refuses relational signals because they can be gamed, are intrinsic by this definition and work as intended. P1 may hold only where a resource exists to hold or reward worth, not where it exists to give fair access or to stay ungameable.

## 5. The normative layer (what the right prices are)

The August essay proposed specific prices. They are hypotheses about good design, tested by building them against the rules they would replace, under matched conditions.

- **H1 Rent.** A held item keeps its place by continuing to contribute, and is dropped when it stops.
- **H2 Provenance value.** What enables later work accrues part of the worth of what it enabled. (Holland's bucket brigade, 1985, is an early built instance; see PRIOR-ART.)
- **H3 Refusals, revised.** The essay refused recency outright. Transfer X2 narrows that: time since last *use* is a crude form of rent and is consistent with H1; time since *creation* is not. The refusal now covers age, surprise in bits, and query-time attention used as the only price of a held item.
- **G1 Grounding (candidate).** Relational prices track worth only when the relations come from independent minds. Use that a participant can manufacture for itself is the wash (section 6).
- **Open simplification.** Where rent is priced by contribution at all, it is measured through downstream use, which is H2 plus a clock. Rent may not be an independent part.

## 6. The hard problem: the wash

An economy of contribution can be fooled by work that is distinct, individually plausible, and collectively worthless, citing or using itself into apparent value. This failure is old, and it appears on both sides:

- **Mind side:** Holland's classifier systems suffered "parasites", rules that grew rich by triggering useful rules without contributing (PRIOR-ART). In the authors' AI memory, how often a note is cited and how often it is recalled are uncorrelated (reported, not yet checked).
- **Economy side:** wash trading; self-dealing rings in contribution graphs. In Noesis, no structural signal inside the graph cleanly separates a competent wash from a real collaboration (measured; see the Noesis repository).
- **Function scale:** a VibeSwap reference contract raises a memory's "importance" on every access, and anyone can call that access (verified; see the notebook).

Every tested fix so far shares one form: an outside anchor (use by minds outside the contributor's control, or property rights that stop free riding) plus a fake to compare against. That is the evidence behind G1.

## 7. Methods

- **Transfers:** section 3, logged in TRANSFERS.md.
- **Blind tallies:** the test for P1.
- **Matched experiments:** a relational rule against an intrinsic one, on the same task, budget, and seeds. Example: memory kept by use against memory kept by age, in a small learning brain. Planned, not started.
- **Sweeps:** reading code and documents for instances, misses and counterexamples. Good for finding candidates; weak as evidence when the documents were written by the people testing the theory.
- **Adversarial review:** every claim that leaves this repository is first argued against by reviewers instructed to break it.

## 8. What would count as the fractal claim

ETM will call T3 supported only when all of these hold:
1. transfers that count as evidence (section 3) in **both** directions, mind to economy and economy to mind;
2. at **three or more distinct scales** (for example a program, a person or AI agent, and a market or protocol);
3. at least one transfer whose target is a system the authors did not design;
4. a recorded failure rate, so that the hits can be compared with what loose analogy alone would produce.

As of 2026-10-27: one historical transfer (X1, consistency, not evidence under rule 3), one proposed refinement (X2), and several predictions waiting for tests.

## 9. Open questions

1. What is the abstract structure the two sides share, stated precisely enough to prove a theorem about it?
2. Is "a mind is an economy" distinguishable from "a mind is a control system" or "an optimizer under constraints"? What does the economic framing predict that those do not?
3. What is the right baseline for transfer success, so that ETM can be compared with analogy by chance?
4. Where should ETM explicitly not apply (section 4, scope limits)?
5. Did any ETM text before 2026-07-20 name the wash? (ERRATA E3.)

## 10. Test beds

Most evidence so far comes from the authors' own systems: [Noesis](https://github.com/WGlynn/noesis) (a contribution economy built to survive adversaries), [VibeSwap](https://github.com/WGlynn/VibeSwap) (reference contracts), and JARVIS (an AI collaborator's persistent memory). They are convenient because every rule can be read. They are also the main source of bias, because they were designed with ETM in mind. Systems the authors did not design, and the published literature on both sides, are the priority for the next round.
