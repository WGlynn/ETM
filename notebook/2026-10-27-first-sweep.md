# 2026-10-27: the first sweep, and the thesis restated

## The question

Is the Economic Theory of Mind a pattern that recurs everywhere, as a fractal should? The August essay described one specific mechanism (scarcity, rent paid by continuing contribution, and value flowing along a provenance graph) and found it in three kinds of mind. If the theory is right, that shape should show up across the authors' whole body of work, not only where it was put on purpose.

## Method

Eight readers worked through every kind of document in the authors' projects: research notes, concept and architecture docs, smart-contract and node source code, the memory library of an AI collaborator, experiment write-ups, other papers, and past public posts. Each reader logged three things:

- **instances,** where the shape appears, with its scale and a strength rating (STRONG, PARTIAL, STRETCH);
- **misses,** where something scarce goes unpriced by contribution, and whether a known failure sits there;
- **counterexamples,** where something works well while contradicting the theory.

Known bias: the readers knew the theory, and most documents were written by the same author through the same lens. This sweep can find candidates; it cannot confirm the theory.

## What the sweep found (reader reports, key items checked)

1. **The three-part mechanism is not running anywhere as built code.** Every reader reached this independently. The parts appear separately, and almost never wired together.
2. **Rent paid by contribution is the rarest part.** In Noesis the decay operation exists but is only called from tests (verified). In VibeSwap's contracts, the rents that exist are paid in age, liveness, or capital. The AI memory measures which memories are used but does not act on it (ERRATA E4).
3. **Value along a provenance graph exists as built code**, in a VibeSwap reference contract that passes credit back through an influence graph at 30% decay per hop (verified), and in Noesis's attribution functions (built, deliberately kept off the live path).
4. **Failures cluster where something is priced by a property of its own.** Examples, each checked in code:
   - VibeSwap's reference consensus contract counts stake linearly and contribution on a capped logarithm, so above about 510 tokens of stake, capital outweighs the largest contribution score possible. Noesis fixed the same problem on 2026-10-21 by comparing each side's share of its own total; the fix was not carried over to the contract.
   - A per-account reward floor was found profitable to split into many accounts in 200 of 200 adversarial search rounds (code comment at `ShapleyDistributor.sol:295`).
   - A reference contract raises a memory's importance on every access, and access is not authenticated, so importance can be pumped.
   - A retention curve cited as following the Ebbinghaus forgetting curve has the opposite shape: slow decay first, then a cliff.
5. **Counterexamples worth keeping:** a batch auction that ignores all trading history is fairer for it; Noesis deliberately keeps its relational value signals off the consensus safety path because they can be gamed; and in the AI memory, a simple recency signal recovered nearly as many hand-picked memories as a graph signal (19 against 20 of 40, reported).
6. **Five errors in the August essay** (ERRATA E1 to E5).

## The thesis, restated

During the sweep the thesis was restated in its stronger, two-way form: a mind is an economy, **and an economy is a mind**, at every scale. The test of a two-way claim is transfer: what is known about one side should predict something true about the other. That reframing turned the sweep's main negative result into a direction. The specific mechanism was a guess about the right prices. The correspondence itself is what the program now tests.

## What history and nature already show

- **A transfer that already happened.** Holland's 1985 learning system, built as an internal economy, suffered "parasites" that grew rich without contributing. Baum's Hayek machine (1996, 1999) fixed this by importing property rights and conserved money from economics, and went on to solve problems its predecessors could not. Economics repaired a mind. (TRANSFERS X1.)
- **The wash is the cheater problem, and biology has studied it at every scale.** Cancer is cheating by cells. A higher level of individuality exists when cheating by its parts is suppressed. Plants sanction the root nodules that do not deliver, per nodule. Plant and fungus partners reward each other in both directions. Each of these is now a transfer candidate. (SUBSTRATES.md.)
- **A measured limit.** Organisms and cities both follow scaling laws from network structure, but organisms slow down as they grow and cities speed up. The structure transfers; the dynamics flip. ETM has to say which of its claims are which.

## Next

1. Write down the abstract structure shared by both sides, precisely enough to prove a theorem about it.
2. Run a blind tally for P1 on a system the authors did not design.
3. Read the primary texts behind every *standard* citation, and the 2026 Economy of Minds paper, before any novelty claim.
4. Design the first matched experiment for X2 and X3 (memory kept by use, by age, and by conserved credit).
