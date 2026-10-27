# Can a Planet Teach an Economy?

### A Pre-Registered Test and What It Found

*Will Glynn, with JARVIS. October 2026. Part of the Economic Theory of Mind research program (github.com/WGlynn/ETM). Status: first test, revised after adversarial review, ready for critique. The first version of this paper is at commit 5686b49 and stays readable there; the scoring corrections are recorded in TRANSFERS.md under "X8 test 1: corrections after adversarial review".*

## Abstract

Planets and economies share a problem: self-interested parts, no central controller, a shared good no part owns, and cheaters who take it without paying. Biology has argued about the planetary version since the early 1980s as the cheater objection to the Gaia hypothesis. We wrote eight predictions, four about the planet and four about economies, and committed them publicly before searching the literature. A hostile review then found errors in how we scored them. Corrected, the planet side gives two partial results and two that count only as consistency; the economy side gives three partial results and one stretch. No result counts as evidence. So the answer to the title is no: in this test the planet taught economics nothing economics did not already know, and two economy predictions restate Olson's 1965 remedies. What the test did show is that two independent literatures, planetary regulation and the economics of collective action, converge on the same rules. That is consistency, not discovery. It also found two limits on the comparison and several faults in our own procedure, which we fix.

## 1. One problem, two scales

A planet's climate is a shared good. Every organism benefits from a temperature life can tolerate, and none owns it. Doolittle (1981) and Dawkins (1982) raised what became the standing objection to the Gaia hypothesis, the idea that life regulates the planet in its own favor. If regulating the climate costs an organism anything, an organism that skips the cost and enjoys the climate anyway should spread, and regulation should collapse. The objection has a second half: natural selection chooses among many competing units, and there is only one Earth, so nothing can select for a planet that regulates well.

An economy has the same problem. A working market, a public codebase, a commons, and the security of a blockchain are shared goods open to free riders, and a single global economy is also a population of one.

The Economic Theory of Mind (ETM) proposes that minds and economies are the same kind of system at every scale. This paper does not assume that. It tests a narrower consequence: if the correspondence is real, what one field has learned about its version of the problem should predict what the other finds. We tested one pairing, planet and economy, on one problem, cheating.

## 2. Method as registered

- **Predictions first, in public.** The planet-side predictions were committed at `c5504d1`, the economy-side predictions at `4069596`, and the prior-knowledge estimates for the economy side at `1358212`, all on 2026-10-27, before the literature on each was searched.
- **Prior knowledge declared.** The predictions were drafted with an AI collaborator that has read much of the literature. For each prediction we recorded, before checking, how likely it was that the answer was already known. A hit on a prediction whose answer was probably known counts as consistency, not evidence.
- **Partial results kept.** A prediction that held in part is reported as partial, with the failed part stated.

The checks were literature checks, not new experiments. Section 6 shows where this method failed.

## 3. The planet side

The standard model of planetary regulation is Daisyworld (Watson and Lovelock 1983): a planet whose only life is black daisies, which absorb heat, and white daisies, which reflect it. As the sun brightens, the balance of the two shifts and the temperature holds steady over a wide range. From ETM's side, three conditions keep an economy honest: honest behavior pays the individual by construction; costs and benefits land on whoever caused them; and value is grounded outside the participants' control. We translated these into four predictions about the planet.

**G-A: regulation that survives cheaters is a by-product, not a sacrifice. Result: PARTIAL.** When a cheat daisy that paid no pigment cost was added to Daisyworld, regulation barely changed, because the cheat had an advantage only when the climate was already mild and regulation was not needed (Lovelock 1992; Lenton 1998). Gaia researchers converged on this answer. Critics had pictured organisms paying a cost to improve the planet for all, which cheats could exploit. Lenton (2025) reports that in response "a consensus emerged that Gaia must principally be built on the by-products of metabolisms originally selected for other reasons." Put plainly, regulation comes from side effects of traits that already pay for themselves. The prediction's second half, that regulation which costs its carrier something fails, did not hold: in one model a costly symbiosis between a warming and a cooling daisy added resistance to cheaters (Boyle et al. 2011). Two cautions apply. A convergence among Gaia researchers is not agreement in the wider field: Tyrrell (2013) argues that the evidence does not show life regulating the planet at all. And a by-product explains why a trait persists, not that it benefits anyone else. Oxygen, a by-product of photosynthesis, drove the Great Oxidation, which devastated the anaerobic life of the time. We call oxygen good because we are among the organisms it selected. A by-product's value depends on who it keeps, and that is the same survivorship bias any judge inside an economy faces.

**G-B: local effects resist cheaters better than global ones. Result: CONSISTENCY.** We first scored this as our best evidence. It is not. Local effects are core to the 1983 model itself (each daisy warms or cools its own patch more than the planet), so our 30% estimate that the answer was already known is not credible. The support is also weaker than we reported. The remark that a spatial Daisyworld seeded by planet-wide proportions shows no regulation is an unpublished aside in a review (Wood et al. 2008). Fully local limiting cases also fail to regulate. And Nicholson et al. (2017) describe regulation in a well-mixed model with no spatial structure as robust to perturbation. What remains: in a spatial model with mutation, cheats arise and cause crashes, cheat-free patches survive and spread, and regulation returns in cycles (Wood, Ackland and Lenton 2006).

**G-C: planetary regulation is partial, not organism-like. Result: CONSISTENCY.** The mainstream view treats it as weaker and more fragile than regulation inside a body. We were about 80% sure of this in advance.

**G-D: economics reached the G-A answer independently. Result: PARTIAL consistency.** Olson's by-product theory (1965) says large groups supply public goods mainly as by-products of organizations held together by private benefits to members. The principle matches G-A: a shared good survives when it rides on private benefit. The difference is that Olson's organizations supply the shared good on purpose, and daisies do not.

## 4. The economy side

From the planet's answers we wrote four predictions about economies. We did not write hit and miss criteria for them, which our own standards require, so every verdict below was assigned after seeing the literature and none counts as more than consistency.

**E-1: crediting suppliers raises the supply of shared goods. Result: PARTIAL.** Lenton's account separates a side effect that helps everyone equally, which selection cannot favor, from one that especially helps its producer, which it can. We predicted that routing credit back to whoever supplies a shared good converts the first kind into the second and raises supply. This is Olson's own remedy, selective incentives, restated. Informal awards raised the productivity of the most active Wikipedia editors by about 60% (Restivo and van de Rijt 2012), but a follow-up found the effect mainly among the already active, with less active editors not responding (Restivo and van de Rijt 2014). Symbolic awards raised the share of newcomers still editing the next month from 35% to 42% (Gallus 2017). Offering invited experts public acknowledgment did not change their actual contributions (Chen et al. 2024). Credit also changes what is supplied: among about 22,900 developers, job seekers shifted open-source work toward visible projects of less direct use to the community (Abou El-Komboz and Goldbeck 2025). All of this is recognition. Credit routed to suppliers as royalties or Shapley shares, the form the prediction named, was not tested by anything we found.

**E-2: many local pools resist free riding better than one global pool. Result: PARTIAL.** This restates Olson's other remedy, small groups. Ostrom's design principles, including clear boundaries, local monitoring, and nested governance, are well supported across 91 studies (Cox, Arnold and Villamayor-Tomas 2010). Group size alone has mixed effects, and reviews call it unresolved. One natural experiment points the other way: when Wikipedia was blocked in mainland China, contributors outside the mainland cut their contributions by about 43%, because their audience had shrunk (Zhang and Zhu 2011). Boundaries and nesting protect a commons; smallness alone does not. The commons literature already said so.

**E-3: a federated economy recovers from collapse through its sound parts. Result: PARTIAL.** As registered: after a cheater-driven collapse, a federated economy recovers through its cheat-free parts, which survive and expand, and a well-mixed one does not. Only containment has support. Haldane and May (2011), a perspective using simplified models, treated the banking system as a food web. Connections spread small shocks thin, but when failures occur in a highly connected system they take down more banks; homogeneity can lower each bank's risk while raising the chance that the whole system fails; and modular structure keeps contagion from reaching the whole network. Haldane (2009) had pointed to forest management, where patches are separated by firebreaks. Recovery through the sound parts was not tested in anything we found.

**E-4: bounded influence stabilizes the system. Result: STRETCH.** We registered this from Lenton and Lovelock (2000), who restored regulation in a Daisyworld with adapting daisies by bounding the adaptation. The comparison does not hold. That bound limits how far a temperature optimum can adapt; it is not a bound on any individual's influence. The destabilizing result is Robertson and Robinson (1998), and Sugimoto (2002) found exact solutions in which daisies adapting without bound regulate longer, a result the 2008 review questions. On the economy side, concentration under token-weighted voting is real. In Compound, Uniswap and ENS, 8 to 18 delegates can pass any proposal (Fritsch, Muller and Wattenhofer 2024). One analysis finds a voting-power Gini above 0.94 and a token-holding Gini above 0.99 in the major protocols it studies (Messias and Ide 2025). A model tested on DAO voting data links ownership concentration to slower platform growth (Han, Lee and Li 2026). But per-account bounds fail on an open network. For voting rules that are positive, increasing, finite concave functions of wallet balance, an attacker who splits holdings across wallets gains power at least linear in holdings (Bennett et al. 2026). That is the Sybil attack (Douceur 2002), known for over two decades. The planet did not point to it.

## 5. What survives

**Two literatures agree.** Gaia researchers and Olson both say a shared good survives when it rides on private benefit. Ostrom's principles and the spatial Daisyworld results both favor bounded, nested structure. Haldane and May borrowed the modular-containment idea from ecology. Each field reached its answer without the other, which makes the agreement consistency across fields, the weakest useful kind of support. It is not discovery: no rule here is new to economics.

**Two limits.** First, structure transfers where group size does not. What protects a commons is boundaries, monitoring, and nesting, not smallness; our translation of locality into smaller pools followed Olson, and the evidence does not support it. Second, a bound only works if it is attached to something that cannot be split. An economy's bounds attach to accounts, which can be multiplied at almost no cost, and the Daisyworld bound is a different kind of bound anyway, so the planet offers no model here. We see two candidate anchors. One is a unit of verified output: a legume plant cuts supply to each root nodule that fails to deliver nitrogen, not to its bacterial partners as a whole (Kiers et al. 2003). The other is an independent participant whose existence an attacker cannot cheaply fake. Neither was tested. Closing this limit needs a test of an anchored bound against a splitting attack, which we have not run.

**Rules both literatures already agree on.** Each comes with its limit.

1. **Make the shared good a by-product of private benefit.** Limit: a by-product explains persistence, not benefit, and a costly cooperative arrangement can also resist cheaters (Boyle et al. 2011).
2. **Route credit to whoever supplies a shared good, and measure use, not visibility. Untested.** Recognition raises effort mainly among the already active and pulls effort toward what is visible. Routed credit and use-based measurement were not tested.
3. **Build boundaries and firebreaks.** Limit: containment is supported in simplified models and in commons studies; recovery through the sound parts is untested, and smallness alone does not help.
4. **Bound influence, and attach the bound to something that cannot be split. Untested.** This rule comes from the Sybil literature, not from the planet.

**Our own code, labeled by status.** In Noesis, a contribution-based protocol we are building (github.com/WGlynn/noesis, commit `be219951`), finality weighs each side by its share of its own total (`node/src/runtime.rs:1664`) and requires capital and contribution each to supply at least half of their own totals (`node/src/runtime.rs:1676`). This is built in the reference implementation, not deployed. Moving stake across many accounts does not change its share of the total; whether contribution scores resist splitting one contributor into many identities is not settled here (inferred, not tested). In an earlier reference contract for VibeSwap (github.com/WGlynn/VibeSwap, commit `243280eb`, `contracts/consensus/NakamotoConsensusInfinity.sol`), stake weight is linear (`POS_SCALE = 1`, line 164; `posWeight`, lines 959-960) while mind weight is a base-2 logarithm (`calculatePoMWeight`, line 879), which cannot exceed 255 units for a 256-bit score. With weights of 30% for stake and 60% for mind (lines 146-147), more than about 510 tokens outweigh the largest mind score possible. That contract breaks rule 4; it was found during this research and is not fixed at that commit.

## 6. What went wrong in our own test

A hostile review found four faults. Each made the result look stronger than it was.

- **E-3 was scored on its passing half.** It was registered as recovery and scored as a hit on containment alone.
- **The economy predictions had no criteria.** Without registered hit and miss conditions, every economy verdict was a judgment made after reading the literature.
- **Commit times are author-set, and the gaps were minutes.** Git records whatever time the author's machine reports. The commits show order, not independent proof, and the same people registered and checked within minutes.
- **The G-B prior was not credible.** Locality is in the founding model, and an AI collaborator that has read that literature very likely knew it. Prior-knowledge estimates made by the party that benefits from low estimates are weak protection.

The procedure we now use:

1. **Criteria written in advance.** Every prediction gets written hit and miss conditions before any checking.
2. **Real separation.** Registering and checking are separated by a real interval, or done by different people.
3. **Score only as registered.** A prediction is scored as written, never on its passing half.

## 7. Other limits

- **One test.** Eight predictions on one problem is a start, not a record.
- **We chose the predictions.** Someone who did not know the hoped-for answer might have written different ones.
- **Literature, not primary data.** Most results were checked against summaries and abstracts. The one direct quotation in this paper (Lenton 2025) was checked against the primary text or its abstract; other findings are paraphrased and should be checked against the full papers before being relied on.
- **Analogy is not mechanism.** Two systems that face the same problem and reach similar answers are not thereby the same kind of system. ETM's stronger claim needs formal work.

## 8. Conclusion

Can a planet teach an economy? In this test, no. Every rule we carried back from the planet was already in Olson, Ostrom, the systemic-risk literature, or the Sybil literature, and two of our four economy predictions restate Olson's own remedies. The test did show that the two fields reached the same rules independently, which is consistency and nothing stronger. It found two places where the comparison breaks. Structure carries over; group size does not. And a bound protects an economy only if it is attached to something that cannot be split, while the Daisyworld bound is a bound on adaptation, not on influence. Finally, it showed how to run such tests better, mostly by showing how this one went wrong. The next tests in the program (cancer and the economy, biological markets and contribution protocols, and the brain's economy of energy and attention) will use the procedure in section 6.

## References

Abou El-Komboz L, Goldbeck M (2025). Career concerns as a public good: the role of signaling for open source software development. *Labour Economics* 97: 102800.
Bennett A, Vander Vos P, Le DV, Belenkiy M (2026). Concave is the new linear: the impossibility of anti-plutocratic DAO governance. arXiv:2605.18990.
Boyle RA, Lenton TM, Watson AJ (2011). Symbiotic physiology promotes homeostasis in Daisyworld. *J. Theor. Biol.* 274: 170-182.
Chen Y, Farzan R, Kraut R, YeckehZaare I, Zhang AF (2024). Motivating experts to contribute to digital public goods: a personalized field experiment on Wikipedia. *Management Science* 70(5): 3264-3280.
Cox M, Arnold G, Villamayor-Tomas S (2010). A review of design principles for community-based natural resource management. *Ecology and Society* 15(4): 38.
Dawkins R (1982). *The Extended Phenotype*. Oxford: W. H. Freeman.
Doolittle WF (1981). Is nature really motherly? *CoEvolution Quarterly* 29: 58-63.
Douceur JR (2002). The Sybil attack. In *Peer-to-Peer Systems (IPTPS 2002)*, LNCS 2429: 251-260. Springer.
Fritsch R, Muller M, Wattenhofer R (2024). Analyzing voting power in decentralized governance: who controls DAOs? *Blockchain: Research and Applications* 5: 100208.
Gallus J (2017). Fostering public good contributions with symbolic awards: a large-scale natural field experiment at Wikipedia. *Management Science* 63(12): 3999-4015.
Haldane AG (2009). Rethinking the financial network. Speech, Financial Student Association, Amsterdam, April 2009. Bank of England.
Haldane AG, May RM (2011). Systemic risk in banking ecosystems. *Nature* 469: 351-355.
Han J, Lee J, Li T (2026). Decentralized autonomous organization governance. *Management Science*, early access, doi 10.1287/mnsc.2024.07033.
Kiers ET, Rousseau RA, West SA, Denison RF (2003). Host sanctions and the legume-rhizobium mutualism. *Nature* 425: 78-81.
Lenton TM (1998). Gaia and natural selection. *Nature* 394: 439-447.
Lenton TM (2025). The evolution of Gaia(s). *Phil. Trans. R. Soc. B* 380(1931): 20240095.
Lenton TM, Lovelock JE (2000). Daisyworld is Darwinian: constraints on adaptation are important for planetary self-regulation. *J. Theor. Biol.* 206: 109-114.
Lovelock JE (1992). A numerical model for biodiversity. *Phil. Trans. R. Soc. B* 338: 383-391.
Messias J, Ide A (2025). Fairness in token delegation: mitigating voting power concentration in DAOs. arXiv:2510.05830.
Nicholson AE, Wilkinson DM, Williams HTP, Lenton TM (2017). Multiple states of environmental regulation in well-mixed model biospheres. *J. Theor. Biol.* 414: 17-34.
Olson M (1965). *The Logic of Collective Action*. Harvard University Press.
Restivo M, van de Rijt A (2012). Experimental study of informal rewards in peer production. *PLOS ONE* 7(3): e34358.
Restivo M, van de Rijt A (2014). No praise without effort: experimental evidence on how rewards affect Wikipedia's contributor community. *Information, Communication & Society* 17(4): 451-462.
Robertson D, Robinson J (1998). Darwinian Daisyworld. *J. Theor. Biol.* 195: 129-134.
Sugimoto T (2002). Darwinian evolution does not rule out the Gaia hypothesis. *J. Theor. Biol.* 218: 447-455.
Tyrrell T (2013). *On Gaia: A Critical Investigation of the Relationship between Life and Earth*. Princeton University Press.
Watson AJ, Lovelock JE (1983). Biological homeostasis of the global environment: the parable of Daisyworld. *Tellus B* 35: 284-289.
Wood AJ, Ackland GJ, Lenton TM (2006). Mutation of albedo and growth response produces oscillations in a spatial Daisyworld. *J. Theor. Biol.* 242: 188-198.
Wood AJ, Ackland GJ, Dyke JG, Williams HTP, Lenton TM (2008). Daisyworld: a review. *Reviews of Geophysics* 46: RG1001.
Zhang XM, Zhu F (2011). Group size and incentives to contribute: a natural experiment at Chinese Wikipedia. *American Economic Review* 101(4): 1601-1615.

Note on references: page ranges for Dawkins 1982, Doolittle 1981, Douceur 2002, Haldane 2009, Kiers et al. 2003, Lenton 1998, Lovelock 1992, Watson and Lovelock 1983, Wood et al. 2006, Wood et al. 2008 and Zhang and Zhu 2011 are from standard citations and have not been rechecked against the publishers' pages. The other entries were checked against publisher or index listings on 2026-10-27.
