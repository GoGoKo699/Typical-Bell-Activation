# Scientific account

Measurement incompatibility is necessary for Bell nonlocality. For qubits, it is also known to be sufficient when a suitable number of parties and a suitable state can be chosen. This account asks what happens for typical states and quantifies the resulting separation from local correlations.

The experiment uses one qubit at each of $`N`$ parties, with the same fixed menu of $`m`$ unbiased binary measurements. A classical local model may assign unrelated outcomes to every setting; the proof bounds all such assignments. Quantum correlations are evaluated on a Haar-random pure state using an inequality tailored to that state. The inequality includes subset correlators, which remain ordinary marginals of the same Bell experiment.

## Reading route

1. [Model and results](model-and-results.md): physical experiment, quantifiers, normalization, and the main finite bound.
2. [Compatibility and its dual](compatibility-dual.md): the inherited compatibility norm and the positive-contraction property of an optimal dual transfer matrix.
3. [Haar moments](haar-moments.md): exact second and fourth moments, the weighted Pauli sum, and its lower concentration bound.
4. [Bell construction](bell-construction.md): explicit coefficients, deterministic product operators, and exponential violation.
5. [Local depolarization](local-noise-threshold.md): finite spherical measurement menus and the exact typical-state threshold $`1/2`$.
6. [Party-count bounds](party-count.md): an all-state converse and sufficient bounds for a prescribed violation ratio.
7. [An exact finite witness](finite-example.md): a reproducible six-qubit example.
8. [Resources and interpretation](resources.md): preparation, coefficient computation, marginal acquisition and statistical evidence.

The [related-work account](../references/README.md) identifies which ingredients and qualitative conclusions are inherited. The [verification guide](../verification/README.md) separates finite arithmetic checks from the analytical theorems.

## The mechanism

An incompatibility witness provides dual vectors whose every signed sum lies in the unit Bloch ball. For the simplest scaling, each classical deterministic assignment therefore produces a positive product operator with trace $`2^N`$. Its expectation in a typical pure state remains small, even after taking a maximum over all deterministic assignments.

The same dual witness produces a positive transfer matrix in Pauli coordinates. The quantum score is consequently a weighted sum of squared Pauli expectations. Its mean grows exponentially when the measurements are incompatible, and a fourth-moment estimate shows that almost all states realize this growth. Rescaling the dual improves the quantitative exponential bound while preserving concentration.

The physical conclusion follows by choosing sufficiently many fixed spin directions. Finite direction sets approach the maximal qubit compatibility norm two, so every local depolarizing visibility above one half admits typical activation. The already-known universal compatibility theorem supplies the opposite side, including the endpoint.
