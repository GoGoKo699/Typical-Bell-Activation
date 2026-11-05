# Learning route

This route explains how a local measurement-incompatibility certificate becomes a Bell inequality for a typical many-qubit state. It begins with the experiment and a complete two-qubit example, then connects the proof ingredients to the local-noise threshold and the resources needed to obtain evidence.

The single educational anchor is **Valerio Scarani, *Bell Nonlocality*, first edition (Oxford University Press, 2019)**. The [anchor bridge](ANCHOR.md) selects the relevant sections, translates notation, and identifies the additional arguments developed in this repository. Reading the entire book is not a prerequisite.

## Choose a route

| Reader's aim | Route |
| --- | --- |
| Understand the physical question and mechanism | Read the [worked walkthrough](walkthrough.md), then the [model and results](../science/model-and-results.md). |
| Study the complete conceptual story in order | Follow the [30 milestones](MILESTONES.md): 14 background/preliminaries targets followed by 16 narrative/innovation targets. |
| Connect familiar Bell theory to this proof | Use the [Scarani bridge](ANCHOR.md), then the [compatibility dual](../science/compatibility-dual.md), [Haar moments](../science/haar-moments.md), and [construction](../science/bell-construction.md). |
| Check the result as a specialist | Start at the [scientific account](../science/README.md); the exact assumptions and proof dependencies are authoritative there. |
| Reproduce a finite witness | Read the [six-qubit example](../science/finite-example.md) and run the [verification commands](../verification/README.md). |

The milestone map records understanding targets, dependencies, conceptual connections, and source pointers. It is a common map of the project, rather than a record of any reader's progress. The walkthrough supplies an explanatory route through its groups; the topic-based science pages retain the full technical proofs.

## Keep the distinctions visible

The measurement family is fixed, while the Bell inequality depends on the target state. Subset correlators are ordinary marginals obtained without discarding trials. The ratio uses the maximum absolute local score, including the constant term. The conclusion is ordinary Bell nonlocality with one qubit per party. A growing Bell ratio and the cost of statistically demonstrating it are separate questions.

[Repository overview](../README.md) · [Anchor bridge](ANCHOR.md) · [Milestone map](MILESTONES.md) · [Scientific reading route](../science/README.md)
