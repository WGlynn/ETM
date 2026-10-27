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
