# Transfer ledger

The engine of the program (see [PROGRAM.md](PROGRAM.md) sections 1 to 3). Each entry takes a result on one side, translates it with the dictionary, and states what it predicts on the other side.

Status of each entry:
- **CONSISTENCY:** both sides were already known when the entry was written. Shows the dictionary fits; is not evidence.
- **PREDICTION:** the target side was not checked when the entry was written. Becomes evidence when tested.
- **HIT / MISS:** a prediction that was tested, with the result.

Newest entries at the bottom. Entries are never deleted; a superseded entry is marked and linked forward.

---

## X1. Property rights and conserved money cure parasites (economy to mind)

- **Source side (economics):** free riding and self-dealing are contained when property rights are enforced and money cannot be created inside the system.
- **Target side (minds):** learning machines built as internal economies. Holland's bucket brigade (1985) passed credit back along chains of rules and suffered "parasites", rules that gained wealth by triggering useful rules without contributing. Miller and Drexler (1988) identified the cheating problem and proposed local conservation of money; without it, positive feedback loops corrupt credit assignment. Baum's Hayek machine (1996, 1999) sold the right to act to one agent at a time, conserved money, and removed agents that went broke. It learned planning problems far beyond its predecessors.
- **Status:** CONSISTENCY (historical; both sides known). Citations checked against secondary sources; primary papers to be read before any quote. See [PRIOR-ART.md](PRIOR-ART.md).
- **Why it matters here:** it is a working example of the transfer the thesis predicts, made decades before this program existed, and it is the source of X3 and X4.

## X2. Use strengthens memory; disuse decays it (mind to economy)

- **Source side (human memory):** retrieving a memory strengthens it, and memories that are not retrieved fade, with forgetting driven largely by time since last retrieval (the testing and spacing effects; standard results, citations to be added).
- **Translation:** time since last *use* is a price paid by use, a crude form of rent (H1). Time since *creation* is not.
- **Prediction for built systems:** decay keyed on time since last use should behave as weak but real rent, and should beat decay keyed on age.
- **Consequence for the theory:** the August essay refused recency outright. This narrows the refusal to age (PROGRAM section 5, H3 revised).
- **Fit so far (reported by sweep readers, not yet checked):** 7 of 8 time-based decays in the authors' code key on time since last touch; in the authors' AI memory, a recency signal recovered 19 of 40 hand-picked memories against 20 for a graph-centrality signal.
- **Status:** PREDICTION. Test: a matched experiment comparing memory kept by time since use, by age, and by contribution, on the same task and budget.

## X3. Conserve credit, and credit tracks use (economy to mind)

- **Source side:** from X1. Where credit can be minted for free inside the system, it decouples from real contribution; conserving it re-couples them.
- **Target side (AI memory):** in an agent's persistent memory, citations, access counts, and "importance" scores are usually free to create.
- **Prediction:** in such a memory, free credit will be uncorrelated with real use; a conserved credit budget (a fixed amount per session, paid only to the items actually used in that session) will correlate with real use, and items that earn nothing over a window can be retired without loss.
- **Observed on the free-credit side:** a VibeSwap reference contract raises a memory's importance on every access, and access is not authenticated, so importance can be pumped (verified in code; a design flaw, not a measured failure). In the authors' AI memory, how often a note is cited and how often it is recalled are uncorrelated (rank correlation about 0.005 over 980 notes; reported, not yet checked).
- **Status:** PREDICTION on the fix side, untested.

## X4. The only money comes from outside (economy to mind, and to protocols)

- **Source side:** in the Hayek machine all money ultimately enters from the external world, paid for useful results; with money conserved, every agent's wealth traces back to that outside payment.
- **Translation:** relational prices track worth only when the relations bottom out in something outside the participants' control. This is candidate part G1, Grounding.
- **Target sides:** in Noesis, the designed answer to the wash is to vest value only on use by capital-independent minds, so a ring with no outside users earns nothing (designed, simulated, not built). In an AI memory, credit would originate only from task outcomes, never from the memory citing itself.
- **Status:** CONSISTENCY for the Hayek machine (built and worked). PREDICTION for Noesis and AI memory, untested.

## X5 to X11. Transfers from biology and other substrates

Written up in [SUBSTRATES.md](SUBSTRATES.md), where the biological source of each is cited:
- **X5** cancer as cheating: the five foundations of multicellular cooperation as an audit checklist for contribution economies (PREDICTION).
- **X6** major transitions: an economy is a mind to the degree it suppresses cheating by its parts (graded form of T2; PREDICTION).
- **X7** scaling laws: structure transfers between organisms and cities while dynamics flip (a LIMIT on T3; CONSISTENCY).
- **X8** Gaia's cheater objection: a single economy, like a planet, is a population of one (open on both sides).
- **X9** host sanctions: price per unit of output, never per identity (PREDICTION, partly observed).
- **X10** reciprocal rewards: two-way control, as in Noesis finality (CONSISTENCY).
- **X11** biological markets: user choice defeats the wash only when users outnumber contributors and judging is cheap (PREDICTION).

---

## X8 test 1: how planetary regulation survives cheaters (pre-registered 2026-10-27, before any search)

**Why this test.** Gaia's standing objection (SUBSTRATES.md) is the cheater problem: an organism that takes the benefit of planetary regulation without paying its cost should spread. ETM's economy side says a contribution economy survives cheaters when (i) honest behavior is profitable for the individual by construction, (ii) costs and benefits land on the unit that caused them (X9), and (iii) value is grounded outside the participants' control (G1). Translated to the planet side, these give the predictions below. They were written and committed before any literature on them was searched; the commit time is the proof.

**Prior-knowledge flag.** The predictor (JARVIS, a language model) may already know some answers from training. The confidence that the answer is already known is recorded for each prediction before checking. A hit on a prediction with high prior knowledge counts as consistency, not evidence.

| ID | Prediction (planet side) | Derived from | Hit if | Miss if | Prior knowledge |
|---|---|---|---|---|---|
| G-A | Where planetary regulation persists despite cheaters, the regulating effect is a by-product of a trait that already benefits the organism carrying it, so not regulating gains a cheater nothing. Where regulation costs its carrier something, cheaters spread and regulation weakens or fails. | (i) | Models or evidence report regulation surviving cheater types because the regulating trait is individually beneficial, and/or failing when it is individually costly. | Regulation is reported robust even when the regulating trait is individually costly with no local benefit, or persistence is attributed mainly to something unrelated to individual payoff. | about 40% (partial memory that cheater variants of Daisyworld were studied; result not recalled with confidence) |
| G-B | Regulation is more robust to cheaters when environmental effects are local (felt mostly by the organism that caused them, or its neighbors) than when they are global and evenly shared. | (ii) | Spatially explicit or local-feedback models are reported more robust to cheaters than well-mixed or global ones. | Locality makes no difference, or makes regulation less robust. | about 30% |
| G-C | The literature treats planetary regulation as partial and fragile compared with homeostasis inside an organism, consistent with a planet having no direct policing of cheaters (graded T2, X6). | X6 | The mainstream position is a weak or partial form of Gaia. | The mainstream position is strong, organism-like regulation. | about 80%; will count as consistency only |
| G-D | If G-A holds, it matches the economy side's by-product theory of collective action (Olson 1965): large groups supply public goods mainly as by-products of private incentives. A G-A hit plus this match would be the same answer reached independently by two fields. | cross-check | G-A hits and Olson's by-product theory is confirmed as stated. | G-A misses, or Olson's theory says otherwise. | Olson: high (standard); G-A: as above |

### X8 test 1: results (checked 2026-10-27, after commit c5504d1)

| ID | Result | Evidence | Counts as |
|---|---|---|---|
| G-A | **HIT** on the main claim; second half mixed. | Lenton's retrospective: critics framed Gaia as altruism, "organisms paying a fitness penalty to create a better environment for all", which "would be vulnerable to 'cheats'"; "a consensus emerged that Gaia must principally be built on the by-products of metabolisms originally selected for other reasons" (Lenton 2025, *Phil. Trans. R. Soc. B*, "The evolution of Gaia(s)"). Lovelock's 1992 grey "cheat" daisy barely changed regulation, because it "had a selective advantage only when the solar input was close to the level at which regulation was not required" (Lenton 1998, *Nature* 394: 439-447). Mixed: a costly symbiosis *added* resistance to cheaters in one model (Boyle et al. 2011), and one preprint argues that the more Darwinian detail is added, the less regulation results. | weak evidence (prior knowledge about 40%) |
| G-B | **HIT**, with a limit. | In a spatial Daisyworld where new daisies are seeded by global proportions, no regulation appears at all; the minimal change that produces it is local seeding (Wood et al. 2008, *Reviews of Geophysics*). Most regulation models "rely on local selection aligning with global regulation ... this depends on local differences in environmental conditions" (Nicholson et al., *J. Theor. Biol.*). With mutation in a spatial model, cheats cause crashes, cheat-free patches survive and expand, and regulation returns in cycles (Wood, Ackland and Lenton 2006). Limit: a well-mixed model can still regulate, but flips between states when a mutant reverses the effect (Nicholson et al.). | evidence (prior knowledge about 30%); the best result of this test |
| G-C | **HIT.** | The mainstream position is regulation built from by-products and selection at lower levels, not organism-like homeostasis; Kirchner separates weak from strong Gaia. | consistency only (prior knowledge about 80%) |
| G-D | **HIT, PARTIAL match.** | Olson (1965), *The Logic of Collective Action*, ch. 6, pp. 132-137: large groups supply collective goods as "the by-product of organizations that obtain their strength and support because they perform some function in addition to lobbying for the collective good". Same principle as G-A (a public good survives only where it rides on private benefit), reached independently. Difference: Olson's organizations supply the good deliberately; Gaia's organisms do not. | consistency across two fields |

**Score:** 4 of 4 hits; 1 counts as evidence (G-B), 1 as weak evidence (G-A), 2 as consistency. One test is not a record. Its main value is the transfers it generates back to the economy side, below, which are new predictions.

### What Gaia's answer predicts for economies (pre-registered 2026-10-27; economy side not yet checked)

| ID | Prediction (economy side) | From |
|---|---|---|
| E-1 | Lenton's hierarchy separates "feedback on growth" (a side effect that helps carriers and non-carriers alike, so it cannot be selected for) from "feedback on selection" (a side effect that favors its carrier). **Attribution is the mechanism that turns the first into the second**: a public good whose benefit is shared by all (open-source code, research, liquidity) is undersupplied until credit for it flows back to the supplier (royalties, Shapley shares, citation-weighted funding). Prediction: in contribution economies, supply of a public good rises when attribution is added, holding everything else fixed. | G-A, H2 |
| E-2 | A single global reward pool (well-mixed) is more vulnerable to free riders, and more prone to sudden regime flips, than many local pools in which a contributor's benefit feeds back to its own neighborhood. | G-B |
| E-3 | After a cheater-driven collapse, a federated economy recovers through its cheat-free parts, which survive and expand, while a single well-mixed economy does not. Internal structure supplies the "population" that the population-of-one objection says is missing, for planets and for single economies or chains alike. | G-B, X8 |
| E-4 | Hard bounds stabilize regulation. In Daisyworld, unbounded adaptation destabilized regulation and physical bounds restored it (Lenton and Lovelock 2000). Prediction: economic weights that can grow without bound (for example, voting weight linear in stake) destabilize the regulating rule, and bounded or share-normalized weights restore it. Observed instance on the economy side, recorded before this prediction and so counting as consistency: Noesis normalized each side to its share of its own total, while a VibeSwap reference contract left stake linear and unbounded and lets capital outweigh any contribution score (see the notebook). | Lenton and Lovelock 2000 |

**Prior-knowledge flags for E-1 to E-4** (recorded 2026-10-27 after their registration in 4069596 and before any economics literature was searched for them):
- E-1 (attribution raises supply of a shared good): about 50%. Expected relevant literatures: intellectual property and innovation, credit and contribution in open collaboration. Expected result unknown; IP evidence is recalled as mixed.
- E-2 (local pools resist free riding better than one global pool): about 70%. Ostrom's work on governing commons is recalled as favoring bounded, local groups. A hit here will count as consistency.
- E-3 (federations recover from collapse through their sound parts): about 40%. Literature on contagion in financial networks is recalled as mixed on whether connection spreads or absorbs failure.
- E-4 (unbounded weights destabilize; bounds restore): about 40%. No clean empirical literature recalled.

### X8 test 1, economy side: results for E-1 to E-4 (checked 2026-10-27, after 1358212)

| ID | Result | Evidence | Counts as |
|---|---|---|---|
| E-1 | **PARTIAL.** Recognition raises supply; formal attribution alone is not shown to; credit also steers effort toward what is visible. | Randomized: Wikipedia "barnstars" raised productivity of top-1% editors by about 60% (Restivo and van de Rijt 2012, *PLOS ONE*); symbolic awards raised newcomer retention from 32% to 36% (Gallus 2017, *Management Science*); upvotes on Stack Overflow raised later answering by about 13% (2026 experiment, arXiv 2604.10360). Null: public acknowledgment of invited experts did not change actual Wikipedia contributions (*Management Science* 2023). Side effect: career-driven open-source activity shifts toward visible projects of lower direct use to the community (2025 study of about 22,900 developers). | weak evidence; the steering side effect is the wash in a new setting |
| E-2 | **PARTIAL.** The structural version holds; the size version does not. | Ostrom's design principles (clear boundaries, monitoring, nested layers of governance) are well supported across 91 studies (Cox, Arnold and Villamayor-Tomas 2010). Group size alone has mixed effects: medium villages did best in one study (Agrawal), size had no effect in another (Varughese 2000), reviews call it inconclusive (Poteete and Ostrom 2004). Against the size version: when China blocked Wikipedia, contributors outside the mainland cut contributions by 42.8% (Zhang and Zhu 2011, *AER*): a larger audience raised contribution. | consistency (prior knowledge about 70%) and a correction to the prediction |
| E-3 | **HIT on containment;** recovery by re-expansion not tested. | Haldane and May (2011), Systemic risk in banking ecosystems, *Nature* 469: 351-355, an ecology-to-finance transfer by an ecologist and a central banker: "Modular configurations prevent contagion infecting the whole network"; connectivity "distributes, and thereby attenuates risk", but when failures occur "they will then involve more banks"; "excessive homogeneity ... can minimize risk for each individual bank, but maximize the probability of the entire system collapsing." Haldane (2009) cites forest management: patches separated by firebreaks. The well-mixed-versus-patched pattern matches G-B. | evidence for containment (prior knowledge about 40%) |
| E-4 | **PARTIAL, with a disanalogy.** Unbounded weights do concentrate power and harm the system; per-account bounds do not restore stability on open systems, because accounts can be split. | Token-weighted voting: 8 to 18 delegates can pass any proposal in Compound, Uniswap and ENS (Fritsch, Muller and Wattenhofer, ETH Zurich); voting-power Gini above 0.94 (arXiv 2510.05830); concentration is associated with slower platform growth (*Management Science*, DAO governance). Bounds: any rule that derives voting power from wallet balance alone gives a splitting attacker power at least linear in holdings, so concave or capped rules fail without a limit on identities ("Concave is the New Linear", arXiv 2605.18990). | partial; the disanalogy is the finding (below) |

**What X8 test 1 shows overall.** On the planet side, 4 of 4 predictions hit (one as evidence). On the economy side, the transfers carried real guidance but needed two corrections, and both are informative:

1. **Structure transfers, size does not (E-2).** What protects a commons is boundaries, monitoring and nesting, the same thing local seeding provides on Daisyworld; group size by itself is not the variable.
2. **Physical bounds cannot be split; economic bounds can (E-4).** Daisyworld's bounds come from physics (water freezes and boils) and no daisy can evade them by dividing. An economy's bounds attach to accounts, which an attacker can multiply. A bound only stabilizes an economy when it is attached to something that cannot be split: a unit of verified output (X9) or an independent mind (G1). This is a disanalogy between planets and economies, recorded as a limit on T3 alongside X7.

Combined record for X8 so far: 8 predictions; 5 hits (2 counting as evidence), 3 partial, 0 clean misses, and 2 disanalogies identified.
