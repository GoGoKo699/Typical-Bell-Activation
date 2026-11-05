# Resources and interpretation

The activation theorem concerns the geometry of quantum and local behaviors. Its resource assumptions distinguish that statement from the cost of preparing and experimentally certifying such a behavior.

## What is fixed and what is chosen

For the general theorem, the measurement family is known and fixed as $`N`$ grows. Every party receives one qubit and uses that same family. Its compatibility witness can be found before choosing the state. For the local-depolarization corollary, the finite menu may depend on the prescribed visibility $`\eta`$, but it is independent of $`N`$ and of the particular Haar state.

The Bell coefficients depend on the target state. The theorem supplies a rule for computing them from its full description; it does not supply that description at no experimental cost. In a statistical Bell test, the functional must be fixed before using the test data, or its data-dependent selection must be included in a valid statistical analysis. The construction here uses the former convention.

The state is supplied as a mathematical input. Exact Haar sampling and a generic full state description are not efficient preparation assumptions. Transferring the result to a particular circuit ensemble would require its own approximation and moment-error analysis; it is not part of the theorem.

## Measurement and description counts

There are $`m^N`$ joint setting strings, $`2^N`$ possible outcome strings per setting, and up to $`(m+1)^N`$ coefficients when the identity label is used to represent omitted parties. These are description counts, not compulsory lower bounds on a particular sampling implementation. The proof does not establish a sparse representation or an efficient coefficient-evaluation algorithm.

A marginal correlator requires no additional quantum measurement. For a given joint trial, ignore the outcomes of the omitted parties. Each such estimate remains unconditional: no outcome is used to decide whether to retain a trial. One joint record can therefore contribute to several subset correlators. The exponential number of formal correlators does not make them statistically independent observations.

The analytical local-score estimate controls all $`2^{mN}`$ deterministic strategies on the stated high-probability Haar event, without an exact local-polytope optimization. Using this estimate in a statistical certification protocol requires accounting for its exceptional probability. An unconditional certificate for a particular supplied state requires a valid local bound for that instance. Computing the state-dependent coefficients, arranging suitable setting samples, and establishing a desired statistical confidence are separate tasks.

## Large violation and evidence per copy

The Bell ratio is invariant under multiplying every coefficient by the same nonzero scalar. It therefore does not, by itself, specify the variance or range of a single-trial estimator. An exponentially increasing ratio can coexist with exponentially costly evidence acquisition.

A direct comparison follows from the existing [Noisy Local Certification theorem](../references/README.md#noisy-local). Let $`N`$ be the number of qubits in each independent source copy and let $`K`$ be a deterministic worst-case cap on the number of source copies accessed. Restrict acquisition to one destructive binary projective measurement per input qubit, with target-dependent axes and arbitrary classical processing. This includes the measurement architecture used here; the cited result even permits additional classical adaptivity, interleaved copies, and bounded stopping.

Measuring a state after $`\Delta_\eta^{\otimes N}`$ is statistically equivalent to measuring its pure input and independently flipping each reported binary outcome with probability

```math
q=\frac{1-\eta}{2},\qquad
b_\eta=(1-q)^2+q^2=\frac{1+\eta^2}{2}.
```

For each fixed $`0<\eta<1`$ and all sufficiently large $`N`$, that theorem gives, for a typical known Haar target and both binary-discrimination errors bounded by a fixed $`0<\alpha<1/2`$, the necessary copy bound

```math
K\ge \frac{c}{N^2}\,b_\eta^{-N},
```

where $`c>0`$ depends on the fixed noise and error parameters. Consider a Bell test in this acquisition model whose probability of certifying a local behavior is at most $`\alpha`$ and whose miss probability on the target is also at most $`\alpha`$. It must distinguish the target behavior from the behavior of the maximally mixed state, which is local and unchanged by depolarization. The same necessary copy bound therefore applies. Different fixed soundness and miss-error bounds are covered by taking their maximum as $`\alpha<1/2`$. A requirement of statistical validity without a corresponding power guarantee does not imply this lower bound.

This reduction uses an existing discrimination lower bound. Its matching binary-discrimination upper bound does not establish an equally efficient test against the entire local set. The Bell problem has a larger null hypothesis. The result above is a necessary evidence cost under the stated acquisition architecture, not an optimal Bell-test sample law. Collective quantum acquisition or a different measurement architecture requires a separate resource comparison.

## Meaning of the threshold

The local-noise result concerns ordinary Bell nonlocality: the behavior lies outside the fully local polytope. It does not assert genuine multipartite nonlocality, a secret-key rate, or a device-independent randomness rate. Those tasks impose additional conditions.

The partition into separate qubit parties is essential. Giving several noisy qubits to one party and permitting a collective measurement changes the effective measurement family. The universal-locality endpoint established here is for local single-qubit POVMs, as in the underlying compatibility theorem.

The contribution is an exact typicality boundary and a quantitative construction for this experiment. The party-count and exponential-rate bounds describe achieved and forbidden values within it; their remaining gaps are stated in the [party-count account](party-count.md).
