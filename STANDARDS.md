# Standards

The evidence rules this repository holds itself to. A claim that does not meet them is labeled as such or left out.

## Evidence labels

- **VERIFIED:** checked against code at a pinned commit, a git record, or a publisher or journal listing, with the citation given. Code citations always carry a commit hash, so the line still says what it said when cited.
- **REPORTED:** stated by a reader, a collaborator, or a secondary source, and not yet checked independently. Reported claims may appear in working notes; they are marked every time they appear.
- **INFERRED:** reasoning, not evidence. Allowed, always labeled.
- **Literature status:** *checked* (verified against a listing on a stated date) or *standard* (a widely cited result, not yet re-checked). Nothing *standard* is quoted until it is checked against the primary text.

## Status of mechanisms

- **built:** code exists and its tests pass.
- **deployed / live:** running where it has real effect. Most of what is built here is not live; the difference is always stated.
- **designed:** specified, not built.
- **measured:** a result exists from a run or a dataset, with its numbers.
- **open:** neither designed nor measured.

Never round up. "Built" is not "live," "measured on one task" is not "general," and a simulation is not a deployment.

## Strength of a correspondence

- **STRONG:** the same mechanism, literally, on both sides.
- **PARTIAL:** shared structure that differs in a way the entry names.
- **STRETCH:** analogy only. Stretches are allowed in notes; they are never presented as evidence.

## Transfers

A transfer counts as evidence only under the three rules in [PROGRAM.md](PROGRAM.md) section 3: fixed dictionary, prediction recorded before the target is checked, and a target result not already known to the predictor. Everything else is consistency.

## Pre-registration

A test is written down, with what would confirm it and what would refute it, before its data is collected. A rule is not changed after a near-miss without a new run on fresh data and a written note saying so.

## Corrections

Published texts are not silently edited. Corrections go in [ERRATA.md](ERRATA.md) with a date and evidence, and the original text stays readable.

## Counterexamples

A counterexample is the most valuable finding this program can receive. Each one is recorded in the claim ledger, next to the claim it bears on, whether or not the claim survives.

## Bias, stated

Most evidence so far comes from systems the authors designed with this theory in mind, and from documents the authors wrote through it. Finding the pattern there is partly the lens finding itself. Systems the authors did not design, blind tallies, and outside reviewers are how the program corrects for this.

## Before anything leaves this repository

Every claim that goes into a paper, a post, or a talk is first argued against by reviewers instructed to break it, and is checked against [PRIOR-ART.md](PRIOR-ART.md) so that no older idea is presented as new.
