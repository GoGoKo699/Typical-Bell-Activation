# Typical Bell Activation

**How robust is the Bell nonlocality of a typical many-qubit state when every qubit is measured through the same noisy measurement menu?**

For every fixed finite family of incompatible, unbiased binary qubit measurements, Haar-typical many-qubit pure states admit exponentially growing Bell violations. The measurement family stays fixed as the number of parties increases. The Bell inequality is chosen for the target state and can use correlations involving any subset of the parties.

This gives an exact asymptotic threshold under independent local depolarization. With one qubit per Bell party and

```math
\Delta_\eta(\rho)=\eta\rho+(1-\eta)I/2,
```

every fixed $`\eta>1/2`$ admits a finite measurement menu for which the fraction of Haar input states producing nonlocal output correlations tends to one. At $`\eta\le1/2`$, the established compatibility theorem makes every output Bell local under arbitrary local qubit POVMs. The existential threshold was known; the contribution here is the typical-state construction, exponential violation, and quantitative party bounds. [Precise attribution](references/README.md).

## Main results

| Question | Result | Scientific account |
|---|---|---|
| Does any fixed incompatible unbiased binary qubit family work for typical states? | An explicit state-dependent Bell functional gives an exponential violation with an exponentially small exceptional probability. | [Model and theorem](science/model-and-results.md) |
| What controls the amplification? | The known compatibility norm $`\nu`$ gives constructive exponential base $`\sqrt{(1+\nu^2)/2}`$ and an all-state upper bound $`\nu^{N-1}`$. | [Bell construction](science/bell-construction.md), [converse](science/party-count.md) |
| What is the ultimate local-noise threshold for typical inputs? | The threshold is exactly $`\eta=1/2`$ for one qubit per party. A fixed finite menu suffices at each $`\eta>1/2`$. | [Local-noise theorem](science/local-noise-threshold.md) |
| How many parties suffice near compatibility? | A prescribed fixed violation ratio needs at least inverse distance to the boundary; the construction achieves that scale up to a logarithm. | [Party-count bounds](science/party-count.md) |
| Can a finite violation be checked exactly? | The supplied six-qubit state has ratio $`3816/3601>1`$, with all $`8^6=262144`$ deterministic local assignments enumerated using integers. | [Finite example](science/finite-example.md) |

Start with [the scientific reading route](science/README.md). The complete account includes the inherited compatibility dual, its positive transfer matrix, the Haar moment calculation, the Bell construction, the local-noise corollary, and the resource costs. [Question-to-file guide](llms.txt).

## Reproduce the finite checks

```bash
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

The checks reproduce exact Haar moment identities, compare the construction against independent dense matrices, and verify the explicit finite witness and compatible control. The arbitrary-party probability and threshold statements are proved analytically. [Commands, expected output, and scope](verification/README.md).

## Scope and resources

The state-dependent inequality is fixed before collecting Bell-test data. Marginals are obtained by ignoring outcomes, and every trial is retained. The conclusion is ordinary Bell nonlocality with one qubit at each party. The general theorem treats unbiased binary measurements; its local-noise converse also permits arbitrary local qubit POVMs.

The exponential rate is a constructive lower bound. Optimal general rates and finite-party thresholds remain open. State preparation, description, coefficient storage and statistical certification can be expensive. In particular, known noisy local acquisition bounds impose an exponential sample cost on the stated binary-projective measurement architecture at any fixed nonzero local depolarization when certification must achieve fixed confidence and power, with both error bounds strictly below one half. [Resource accounting](science/resources.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
