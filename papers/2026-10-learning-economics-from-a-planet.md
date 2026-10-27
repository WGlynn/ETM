# Learning Economics from a Planet

### A pre-registered test of whether Earth's answer to cheaters carries over to economies

*Will Glynn, with JARVIS. October 2026. Part of the Economic Theory of Mind research program (github.com/WGlynn/ETM). Status: first test, ready for critique.*

## Abstract

Economies and planets share a hard problem. Each is made of self-interested parts with no central controller, each depends on a shared good that no part owns (a stable climate, a functioning market), and each is open to cheaters who take the shared good without paying for it. Biology has studied the planetary version for forty years, under the name of the cheater objection to the Gaia hypothesis. We asked whether its answers predict anything true about economies. We wrote eight predictions, four about the planet and four about economies. Each set went into a public repository before we searched the literature on it. For each, we also recorded how likely we were to know the answer already. All four planet-side predictions held, one of them as real evidence. On the economy side, one held cleanly, three held in part, and none failed outright. The two partial results are the most useful findings: they mark exactly where a planet stops being a good model for an economy. Four design rules for economies came out of the comparison. Studying the planet does not solve economics. In this test it did produce rules that held up in economic data, faster than they are usually found, together with a precise account of where they stop applying.

## 1. One problem, two scales

A planet's climate is a shared good. Every organism benefits from a temperature that life can tolerate, and none of them owns it. In 1983 Richard Dawkins raised what became the standing objection to the Gaia hypothesis, the idea that life regulates the planet in its own favor. If regulating the climate costs an organism anything, an organism that skips the cost and enjoys the climate anyway should spread, and regulation should collapse. The objection has a second half: natural selection works by choosing among many competing units, and there is only one Earth, so nothing can select for a planet that regulates well.

An economy has the same problem. A working market, a public codebase, a functioning commons, and the security of a blockchain are all shared goods. Each is open to free riders, and a single global economy, like a single planet, is a population of one.

The Economic Theory of Mind (ETM) proposes that minds and economies are the same kind of system, and that the correspondence repeats at every scale, from a cell to a planet. That is a hypothesis this paper tests, not one it assumes. If it is true, it should be useful: what one field has learned about its version of the problem should predict what another field will find about its version. This paper tests that claim on one pairing, the planet and the economy, and on one problem, cheating.

## 2. Method

We wanted to avoid the easiest mistake in this kind of work: noticing a resemblance after the fact and calling it a discovery. Three rules applied.

- **Predictions first, in public.** Every prediction was written into the program's public repository and committed before any literature on it was searched. The commit times are the record: the planet-side predictions at commit `c5504d1`, the economy-side predictions at `4069596`, and the prior-knowledge flags for the economy side at `1358212`, all on 2026-10-27.
- **Prior knowledge declared.** The predictions were drafted with an AI collaborator that has read much of the literature. For each prediction we recorded, before checking, an estimate of how likely it was that the answer was already known. A hit on a prediction whose answer was probably known counts as consistency, not evidence.
- **Partial results kept.** A prediction that held in part is reported as partial, with the part that failed stated.

The checks were literature checks, not new experiments. Section 7 lists what that does and does not allow us to say.

## 3. What the planet does

The best-studied model of planetary regulation is Daisyworld (Watson and Lovelock 1983): a planet whose only life is black daisies, which absorb heat, and white daisies, which reflect it. As the sun brightens, the balance of the two shifts, and the planet's temperature holds steady over a wide range. The cheater objection has been tested in it repeatedly. From ETM's side, three conditions keep an economy honest: honest behavior pays the individual by construction; costs and benefits land on whoever caused them; and value is grounded outside the participants' control. We translated these into four predictions about the planet.

**Prediction G-A: regulation that survives cheaters is a by-product, not a sacrifice.** We predicted that where regulation persists, the regulating effect comes from traits that already benefit their carriers, so a cheater gains nothing by not regulating. *Result: held.* When a "cheat" daisy that paid no pigment cost was added, regulation barely changed, because the cheat only had an advantage when the climate was already mild and regulation was not needed (Lovelock 1992; Lenton 1998). More broadly, the field settled the question this way. Critics had framed Gaia as if organisms paid a cost to improve the planet for everyone, which would make it easy prey for cheats. Lenton (2025) answers that this "was never the hypothesis, and in response, a consensus emerged that Gaia must principally be built on the by-products of metabolisms originally selected for other reasons." Oxygen, a waste product of photosynthesis, is the standard example: no organism pays to make it. We estimated about a 40% chance we already knew this, so it counts as weak evidence.

**Prediction G-B: local effects resist cheaters better than global ones.** We predicted that regulation is more robust when the effects of an organism's traits are felt mostly by that organism and its neighbors. *Result: held, with a limit.* In a spatial version of Daisyworld where new daisies are seeded according to the planet-wide mix, no regulation appears at all; the smallest change that produces it is local seeding, where a new daisy copies a neighbor (reviewed in Wood et al. 2008). With mutation added, cheats arise and cause crashes, but patches that happen to be free of cheats survive the crash and spread again, and regulation returns in cycles (Wood, Ackland and Lenton 2006). The limit: a well-mixed model can still regulate, but it flips abruptly between states when a mutant appears (Nicholson et al.). We estimated only a 30% chance we knew this, so it is the strongest evidence in the test.

**Prediction G-C: planetary regulation is partial, not organism-like.** *Result: held.* The mainstream view treats it as weaker and more fragile than the regulation inside a body. We were fairly sure of this in advance, so it counts only as consistency.

**Prediction G-D: economics reached the same answer independently.** If G-A held, we predicted it would match Mancur Olson's by-product theory of collective action (1965), which says large groups supply public goods mainly as by-products of organizations held together by private benefits to their members. *Result: held in part.* The principle is the same: a shared good survives when it rides on private benefit, not on sacrifice. The difference is that Olson's organizations supply the shared good on purpose, and daisies do not.

## 4. Carrying it back to economies

The point of the exercise was the return trip. From the planet's answers we wrote four predictions about economies, committed them, and then checked the economics literature.

**Prediction E-1: crediting suppliers raises the supply of shared goods.** Lenton's account of Gaia distinguishes a side effect that helps everyone equally, which cannot be favored by selection, from one that especially helps the organism producing it, which can. We predicted that routing credit back to whoever supplies a shared good (open code, research, data) converts the first kind into the second and raises supply. *Result: partial.* Randomized studies on Wikipedia found that informal awards raised the productivity of the most active editors by about 60% (Restivo and van de Rijt 2012) and that symbolic awards raised the share of newcomers who kept editing from 32% to 36% (Gallus 2017). But when invited experts were offered public acknowledgment for their contributions, their actual contributions did not change (a field experiment in *Management Science*, doi 10.1287/mnsc.2023.4852). Credit also changes what people supply: a 2025 study of about 22,900 developers found that those looking for jobs shifted their open-source work toward visible projects of less direct use to the community. Credit raises supply, and it pulls supply toward whatever the credit can see.

**Prediction E-2: many local pools resist free riding better than one global pool.** *Result: partial.* Elinor Ostrom's design principles for governing shared resources, which include clear boundaries, local monitoring, and nested layers of governance, are well supported across 91 studies (Cox, Arnold and Villamayor-Tomas 2010). But group size on its own has mixed effects: in one study medium-sized villages did best, in another size made no difference, and reviews call the question unresolved. One natural experiment points the other way: when Wikipedia was blocked in mainland China, contributors outside the mainland cut their contributions by about 43%, because their audience had shrunk (Zhang and Zhu 2011). Boundaries and nesting protect a commons. Smallness alone does not.

**Prediction E-3: a federated economy contains collapse better than one well-mixed system.** *Result: held for containment.* The closest test in economics is itself a transfer from ecology. Haldane and May (2011), a central banker and an ecologist, modeled the banking system as a food web. They found three things. Connections spread small shocks thin, which makes the system safer against them; but when failures do happen in a highly connected system, they take down more banks. Homogeneity, every bank doing the same thing, can lower each bank's own risk while raising the chance that the whole system fails. And modular structure keeps contagion from reaching the whole network. Haldane had earlier pointed to forest management, where the best layout is patches of trees separated by firebreaks. This is the Daisyworld pattern: a well-mixed system absorbs small disturbances and then flips; a patched one contains them. The second half of our prediction, that the sound parts then expand and restore the whole, was not tested in the work we found.

**Prediction E-4: bounded influence stabilizes the system.** On Daisyworld, letting daisies adapt their temperature preferences without limit destabilized regulation, and physical bounds restored it (Lenton and Lovelock 2000). We predicted that influence that can grow without bound destabilizes an economy's governance, and that bounds restore it. *Result: partial, with a disanalogy.* The first half holds. In major protocols governed by token-weighted voting, eight to eighteen delegates can pass any proposal (Fritsch, Muller and Wattenhofer), a later analysis finds voting power more unequal than wealth in national economies, and concentration is associated with slower platform growth (a DAO governance study in *Management Science*). The second half fails in an instructive way. On an open network, any rule that limits influence per account can be beaten by splitting holdings across many accounts; a 2026 result shows that an attacker who splits gains voting power at least in proportion to holdings, whatever the limiting formula, unless the number of identities is itself limited.

## 5. Where the planet stops being a good model

The two partial results matter more than the hits, because they show where the analogy breaks.

**Structure transfers; size does not.** What protects a planet's regulation is local structure: daisies copy their neighbors, so cooperative patches can hold together. What protects a human commons is also structure: boundaries, monitoring, nesting. Size is not the variable on either side. The planet taught the right lesson, and our translation of it into "smaller pools" was the mistake.

**A planet's bounds cannot be split. An economy's can.** The bounds that stabilize Daisyworld are physical: water freezes and boils, and no daisy escapes that by dividing itself in two. The bounds an economy places on influence attach to accounts, and accounts can be multiplied at almost no cost. A bound stabilizes an economy only when it is attached to something that cannot be split. Two candidates came out of the wider research program: a unit of verified output (plants sanction each root nodule that fails to deliver, not the partner as a whole; Kiers et al. 2003), and an independent participant whose existence the attacker cannot cheaply fake. This is a real difference between planets and economies, and any claim that one simply mirrors the other has to state it.

## 6. Four design rules

Taken together, the results suggest four rules for anyone designing an economy, a protocol, or an institution. Each held in at least one field's evidence, and each comes with the limit the test found.

1. **Make the shared good a by-product of private benefit.** Do not ask participants to pay a private cost for a common good. Arrange things so that doing well for oneself produces the shared good as a side effect, as photosynthesis produces oxygen. A cheater then has nothing to skip.
2. **Route credit back to whoever supplies a shared good, and measure use, not visibility.** Credit raises supply, and it also pulls effort toward whatever the credit can see. If the credit counts visibility, it will get visibility.
3. **Build boundaries and firebreaks.** Prefer nested, bounded units with local monitoring over one well-mixed pool. Expect a well-mixed system to absorb small shocks and then fail all at once.
4. **Bound influence, and attach the bound to something that cannot be split.** A limit per account is no limit on an open network. Attach limits to verified output or to independent participants.

These rules are not new to economics one at a time. Olson, Ostrom, and the systemic-risk literature each contain one or more of them. What the planet adds is that all four appear together, in one well-studied system, as answers to one problem, and that the places where they fail to carry over are just as specific.

One example from our own work, labeled by status. In Noesis, a contribution-based protocol we are building, finality requires both capital and contribution to supply at least half of their own totals, and each side is weighed by its share of its own total, so neither can outgrow the other without bound (built in the reference implementation). In an earlier contract we wrote for another project, stake was counted linearly and without bound, and a holder of more than about 510 tokens can outweigh the largest contribution score possible (found during this research, not yet fixed). The second design breaks rule 4; the first follows it, but its bound is still attached to stake held by accounts, so the splitting problem in section 5 remains open there too.

## 7. Limits

- **One test.** Eight predictions on one problem is a start, not a record. Its value depends on more tests, including ones that fail.
- **We chose the predictions.** Someone who did not know the hoped-for answer might have written different ones. A stronger version of this test would have predictions written by one team and checked by another.
- **Prior knowledge.** The AI collaborator that helped draft the predictions has read widely. We recorded our estimates of prior knowledge, but those estimates are themselves judgments.
- **Literature, not primary data.** Most results were checked against published summaries and abstracts. The two direct quotations in this paper were checked against the primary texts or their abstracts; other findings are paraphrased and should be checked against the full papers before being relied on.
- **Analogy is not mechanism.** That a planet and an economy face the same problem and arrive at similar answers does not prove they are the same kind of system. It shows the comparison is productive. ETM's stronger claim needs the formal work described in the program.
- **Dynamics can differ even where structure matches.** Elsewhere in the program we note that organisms and cities follow similar scaling laws from similar network structure, yet organisms slow down as they grow and cities speed up (West, Brown and Enquist 1997; Bettencourt et al. 2007). Rules that transfer in structure may not transfer in their effects over time.

## 8. Conclusion

We asked whether studying a planet could teach us anything reliable about economies. In this test, it did. Earth's answer to cheaters, as worked out in forty years of Gaia research, predicted four things about economies; one held cleanly, three held in part, and none failed outright. The partial results did not weaken the comparison. They sharpened it into two precise limits: structure carries over and size does not, and a bound protects an economy only if it cannot be split.

Studying the planet will not solve economics. It is, on this evidence, a faster way to find rules worth testing, with the planet's own failures marking the places to be careful. The method matters as much as the result: write the prediction down before looking, say what you already knew, and keep the partial results. The next tests in the program use the same method on other pairings: cancer and the economy, biological markets and contribution protocols, and the brain's own economy of energy and attention.

## References

Bettencourt LMA, Lobo J, Helbing D, Kuhnert C, West GB (2007). Growth, innovation, scaling, and the pace of life in cities. *PNAS* 104(17): 7301-7306.
Cox M, Arnold G, Villamayor-Tomas S (2010). A review of design principles for community-based natural resource management. *Ecology and Society* 15(4): 38.
Fritsch R, Muller M, Wattenhofer R. Analyzing voting power in decentralized governance: who controls DAOs? ETH Zurich.
Gallus J (2017). Fostering public good contributions with symbolic awards: a large-scale natural field experiment at Wikipedia. *Management Science*.
Haldane AG, May RM (2011). Systemic risk in banking ecosystems. *Nature* 469: 351-355.
Kiers ET, Rousseau RA, West SA, Denison RF (2003). Host sanctions and the legume-rhizobium mutualism. *Nature* 425: 78-81.
Lenton TM (1998). Gaia and natural selection. *Nature* 394: 439-447.
Lenton TM (2025). The evolution of Gaia(s). *Phil. Trans. R. Soc. B* 380(1931): 20240095.
Lenton TM, Lovelock JE (2000). Daisyworld is Darwinian. *J. Theor. Biol.* 206: 109-114.
Lovelock JE (1992). A numerical model for biodiversity. *Phil. Trans. R. Soc. B* 338: 383-391.
Lovelock JE, Margulis L (1974). Atmospheric homeostasis by and for the biosphere: the Gaia hypothesis. *Tellus* 26: 2-10.
Olson M (1965). *The Logic of Collective Action*. Harvard University Press.
Restivo M, van de Rijt A (2012). Experimental study of informal rewards in peer production. *PLOS ONE* 7(3): e34358.
Watson AJ, Lovelock JE (1983). Biological homeostasis of the global environment: the parable of Daisyworld. *Tellus B* 35: 284-289.
West GB, Brown JH, Enquist BJ (1997). A general model for the origin of allometric scaling laws in biology. *Science* 276: 122-126.
Wood AJ, Ackland GJ, Lenton TM (2006). Mutation of albedo and growth response produces oscillations in a spatial Daisyworld. *J. Theor. Biol.* 242.
Wood AJ, Ackland GJ, Dyke JG, Williams HTP, Lenton TM (2008). Daisyworld: a review. *Reviews of Geophysics* 46.
Zhang XM, Zhu F (2011). Group size and incentives to contribute: a natural experiment at Chinese Wikipedia. *American Economic Review* 101(4): 1601-1615.
Concave is the New Linear: The Impossibility of Anti-Plutocratic DAO Governance (2026). arXiv:2605.18990.
Motivating Experts to Contribute to Digital Public Goods: A Personalized Field Experiment on Wikipedia. *Management Science*, doi 10.1287/mnsc.2023.4852.
Decentralized Autonomous Organization Governance. *Management Science*, doi 10.1287/mnsc.2024.07033.
Career concerns as a public good: the role of signaling for open source software development (2025). *Labour Economics*.

Note on references: page ranges for Lovelock 1992, Watson and Lovelock 1983, West et al. 1997, Lenton and Lovelock 2000 and Zhang and Zhu 2011 are from standard citations and have not been rechecked against the publishers' pages.
