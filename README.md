# Economic Theory of Mind (ETM)

A research program testing a two-way claim: **a mind is an economy, and an economy is a mind.**

Every bounded mind has more demands on it than room for them. A person has limited attention, an AI agent a limited context window, a team limited time. Every economy has the same problem at a larger scale: limited capital, goods, block space, and votes, spread across many participants, none of whom sees the whole. ETM claims these are the same kind of system: a mind is an economy of its parts, and an economy is a mind made of minds. As above, so below.

If that is true, it is useful. Anything we understand about one side should tell us something true about the other. ETM is tested exactly that way: take a known result about minds, translate it, and predict the matching result about economies, or the reverse. Then check. Each attempt is recorded in a transfer ledger, hits and misses alike.

This repository is where that work happens in the open. Nothing here is settled. Every claim carries an evidence label. Predictions are written down before they are tested. Corrections are published as errata, never quietly edited.

## Where it stands (2026-10-27)

- The idea is not new, and this program says so first: Hayek treated the price system as a distributed mind (1945), Minsky treated the mind as a society (1986), and Holland (1985) and Baum (1996) built learning machines as internal economies. See [PRIOR-ART.md](PRIOR-ART.md).
- History already holds one clean transfer. Holland's machine failed through "parasites" that grew rich without contributing. Baum imported property rights and conserved money from economics, and the failure went away. See [TRANSFERS.md](TRANSFERS.md), entry X1.
- The August 2026 essay ([papers/](papers/)) proposed a specific mechanism (scarcity, rent paid by continuing contribution, and value that flows along a provenance graph). A first sweep of the authors' own code and documents did not find that mechanism working as built code at any scale, and found several errors in the essay ([ERRATA.md](ERRATA.md), [notebook/](notebook/2026-10-27-first-sweep.md)).
- What the sweep did find, repeatedly: failures cluster where something scarce is priced by a property it has on its own (size, age, raw stake, account count) instead of by what it does for the rest of the system. That is now the program's first testable prediction.

## Read in this order

1. [PROGRAM.md](PROGRAM.md): the thesis, the translation dictionary, the first prediction, and the methods.
2. [TRANSFERS.md](TRANSFERS.md): every attempted transfer between minds and economies, with its status.
3. [SUBSTRATES.md](SUBSTRATES.md): the same economy in organisms, colonies, cities, and the planet, and nature's solutions to cheating.
4. [CLAIMS.md](CLAIMS.md): every claim with its current status and evidence.
5. [PRIOR-ART.md](PRIOR-ART.md): who got here first, and what ETM would have to add.
6. [ERRATA.md](ERRATA.md): what the August essay got wrong, with evidence.
7. [notebook/](notebook/): dated research entries, negative results included.
8. [papers/](papers/): the essays, unedited, with their errata linked.
9. [STANDARDS.md](STANDARDS.md): the evidence rules this repository holds itself to.

## How to help

Two contributions are worth the most. A **transfer**: a known result about minds that predicts something about economies (or the reverse), with the evidence on both sides. A **counterexample**: a place where the translation clearly fails, or a system that prices scarce resources by intrinsic properties and does not degrade. Open an issue with the details and the evidence.

## Authorship

Will Glynn, open source contributor to VibeSwap and Noesis. Research assistance from JARVIS, an AI collaborator built on Claude; commits it co-authored carry a co-author line.

## License

Text is licensed under [CC BY 4.0](LICENSE).
