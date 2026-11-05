# Model and results

Every fixed incompatible finite family of unbiased binary qubit measurements admits the following construction: draw a Haar-random multipartite state, form a Bell inequality from that state's auxiliary correlations, and use the supplied measurement family at every party. With probability tending to one, the Bell ratio grows exponentially with the number of parties.

The main guaranteed exponential base is

```math
\boxed{g(\nu)=\sqrt{\frac{1+\nu^2}{2}},}
```

where $`\nu`$ is the family's compatibility norm. Joint measurability is equivalent to $`\nu\le1`$, so the constructive bound grows exponentially exactly on the incompatible side of that threshold. The base is a lower bound supplied by this construction, not an optimality claim.

Multipartite activation from incompatible qubit measurements is known in greater measurement generality from [PGQ2025](../references/README.md#pgq2025). The results here specify a family of Bell coefficients, finite probability bounds, and a quantitative guarantee for Haar-random states in the binary unbiased setting. The compatibility norm itself is established in [BJN2022](../references/README.md#bjn2022), [BN2022](../references/README.md#bn2022), and the equivalent qubit characterization of [Grinko–Uola2025](../references/README.md#grinko-uola2025).

## Physical model

There are $`N\ge1`$ separated parties, each holding one qubit of a state on $`(\mathbb C^2)^{\otimes N}`$. The dimension is $`D=2^N`$. Each party has the same fixed finite set of $`m`$ measurement settings,

```math
M_{a\mid x}=\frac{I+aA_x}{2},
\qquad
A_x=\mathbf a_x\cdot\boldsymbol\sigma,
\qquad
\|\mathbf a_x\|_2\le1,
```

with outcomes $`a\in\{-1,1\}`$ and settings $`x=1,\ldots,m`$. The Bloch vectors may span three dimensions. The measurement family is fixed as $`N`$ grows.

The Bell trial uses independent setting choices and local measurements without communication between the parties. Every trial and outcome is retained. The constructed coefficients are specified from the state and measurement description before the test data are evaluated.

The state in the probabilistic statements is a Haar-uniform pure state $`|\psi\rangle\in\mathbb C^D`$. A different state generally gives a different coefficient tensor. Thus the probability statement concerns the prescribed pair consisting of the state and its corresponding Bell inequality.

### Marginal correlators

Set $`A_0=I`$ and index correlators by $`\mathbf x\in\{0,1,\ldots,m\}^{N}`$. In the quantum model,

```math
E_{\mathbf x}(\rho)
=\operatorname{Tr}\!\left[
\rho\bigotimes_{i=1}^{N}A_{x_i}
\right].
```

An index $`x_i=0`$ means that party's outcome is absent from the product defining the correlator. Such a marginal is obtained by summing over that outcome in the ordinary Bell data. The party may use any allowed physical setting; nonsignalling makes the marginal independent of that choice. The symbol $`0`$ therefore adds no physical measurement setting. In particular, $`E_{\mathbf0}=1`$.

The Bell expressions can include correlators of every subset of parties. There are at most $`(m+1)^N`$ coefficients, including the constant. This use of marginal correlators is part of the construction.

## Absolute local normalization

A real Bell coefficient tensor $`c=(c_{\mathbf x})`$ defines

```math
\mathcal B_c(E)=\sum_{\mathbf x}c_{\mathbf x}E_{\mathbf x}.
```

For a deterministic local response array $`s=(s_{i,x})\in\{-1,1\}^{mN}`$, put $`s_{i,0}=1`$. Define the local norm

```math
L_{\mathrm{abs}}(c)
=\max_{s\in\{-1,1\}^{mN}}
\left|\sum_{\mathbf x}c_{\mathbf x}
                    \prod_{i=1}^{N}s_{i,x_i}\right|.
```

Every Bell-local behavior satisfies $`|\mathcal B_c(E)|\le L_{\mathrm{abs}}(c)`$ by convexity. A quantum value exceeding this absolute bound certifies ordinary Bell nonlocality.

The constructed functional always has $`c_{\mathbf0}=1`$. This constant remains in both its quantum value and its local bound. Adding or removing a constant changes this normalization and requires recomputing the local bound.

For later comparison, define the optimum over all states and coefficient tensors in this same measurement scenario:

```math
\mathcal R_N(A)
=\sup_{\rho,\ c:\,L_{\mathrm{abs}}(c)>0}
\frac{|\mathcal B_c(E(\rho))|}{L_{\mathrm{abs}}(c)}.
```

The constructive ratios below are denoted by $`R_N^{(\tau)}(\psi)`$, where $`\tau`$ specifies the auxiliary-operator scale. They are particular achievable values and hence lower-bound $`\mathcal R_N(A)`$ whenever the corresponding state realizes the stated estimate.

## Compatibility norm and coefficient construction

The exact compatibility norm is

```math
\nu(A)=
\max_{\{\mathbf v_x\}}
\left\{
\sum_x\mathbf a_x\cdot\mathbf v_x:
\max_{s\in\{-1,1\}^{m}}
\left\|\sum_xs_x\mathbf v_x\right\|_2\le1
\right\}.
```

The [compatibility page](compatibility-dual.md) proves its primal representation, the equivalence $`\nu\le1`$ with joint measurability, and the physical bound $`\nu\le2`$.

An optimal dual can be chosen so that its transfer matrix satisfies

```math
T=\sum_x\mathbf a_x\mathbf v_x^{\mathsf T},
\qquad
0\preceq T\preceq I,
\qquad
\operatorname{Tr}T=\nu.
```

The three eigenvalues are denoted by $`\lambda_j`$, so $`0\le\lambda_j\le1`$ and $`\sum_j\lambda_j=\nu`$. Fix this dual independently of the Haar state.

For a scale $`\tau\ge0`$, put

```math
B_0^{(\tau)}=I,
\qquad
B_x^{(\tau)}=\tau\mathbf v_x\cdot\boldsymbol\sigma.
```

The coefficient prescription is

```math
c_{\mathbf x}^{(\tau)}(\psi)
=\left\langle\psi\left|
\bigotimes_{i=1}^{N}B_{x_i}^{(\tau)}
\right|\psi\right\rangle.
```

These auxiliary operators define numbers in a Bell inequality; they are not measured in the Bell trial. Its physical correlators still come only from the original $`A_x`$. Let

```math
Q_\tau(\psi)
=\mathcal B_{c^{(\tau)}(\psi)}(E(\psi)),
\qquad
R_N^{(\tau)}(\psi)
=\frac{Q_\tau(\psi)}{L_{\mathrm{abs}}(c^{(\tau)}(\psi))}.
```

The [construction proof](bell-construction.md) shows that $`Q_\tau\ge1`$ and $`L_{\mathrm{abs}}\ge1`$ for these coefficients.

## Main finite-party theorem

Suppose $`\nu>1`$. Define

```math
t_N=(m\ln2+1)N+\ln2,
\qquad
k_N=1+\sqrt{2t_N}+t_N,
\qquad
b=\frac{1+\nu^2}{2}.
```

**Theorem 1 — scaled dual.** Choose the coefficients above with $`\tau=\nu`$. For a Haar-uniform state, with probability at least

```math
\max\left\{0,\
1-\frac{16}{2^N-1}-e^{-N}-e^{-2^N/8}
\right\},
```

the ratio satisfies

```math
\boxed{
R_N^{(\nu)}(\psi)
\ge
\frac{\displaystyle 1+\frac{(1+\nu^2)^N-1}{2(2^N+1)}}
     {2k_N b^{N/2}}
\ge\frac{b^{N/2}}{8k_N}.}
```

All constants are explicit. For small $`N`$, the probability lower bound may be zero. For every fixed incompatible family, it tends to one, while the final ratio lower bound tends to infinity.

Consequently, for any fixed $`1<r<g(\nu)`$,

```math
\Pr\bigl[R_N^{(\nu)}(\psi)\ge r^N\bigr]
\longrightarrow1,
\qquad
g(\nu)=\sqrt{\frac{1+\nu^2}{2}}.
```

In particular,

```math
\liminf_{N\to\infty}\mathcal R_N(A)^{1/N}
\ge g(\nu).
```

The theorem is proved in [Bell construction: main scaled-dual bound](bell-construction.md#main-scaled-dual-bound).

## Simpler positive-dual theorem

**Theorem 2 — positive dual.** With the same measurements and optimal dual, choose $`\tau=1`$. With probability at least

```math
\max\left\{0,\ 1-\frac{16}{2^N-1}-e^{-N}\right\},
```

the ratio satisfies

```math
\boxed{
R_N^{(1)}(\psi)
\ge
\frac{\displaystyle1+\frac{(1+\nu)^N-1}{2(2^N+1)}}{2t_N}
\ge\frac{[(1+\nu)/2]^N}{8t_N}.}
```

Here every deterministic score is the expectation of a positive operator with trace $`D`$. A direct Haar moment bound therefore controls all local scores without the Gaussian normalization estimate needed by Theorem 1. The proof is in [Bell construction: simpler positive-dual bound](bell-construction.md#simpler-positive-dual-bound).

Both theorems establish the same compatibility threshold. The scaled version has the larger guaranteed base because

```math
\sqrt{\frac{1+\nu^2}{2}}\ge\frac{1+\nu}{2},
```

with strict inequality for $`\nu>1`$.

### Feasible certificates suffice

If an explicitly feasible aligned dual has achieved trace $`\gamma>1`$, every bound in Theorems 1 and 2 remains valid with $`\gamma`$ in place of $`\nu`$. For Theorem 1, choose scale $`\tau=\gamma`$. Exact optimization is therefore unnecessary when such a certificate is available. The [certificate statement](bell-construction.md#feasible-dual-certificates) distinguishes the achieved value $`\gamma`$ from the exact norm $`\nu`$.

## Why the proof works

The argument has four parts, each proved on the linked page.

1. **Compatibility geometry.** An incompatible family has a feasible dual with objective greater than one. Polar alignment gives a positive contraction $`T`$ whose trace is that objective. See [Compatibility norm and aligned dual certificates](compatibility-dual.md).
2. **Nonnegative quantum polynomial.** Diagonalizing $`T`$ rewrites the quantum score as a weighted sum of squared Pauli expectations, including its constant one. At scale $`\tau=\nu`$, the exact mean is $`[D+(1+\nu^2)^N]/(D+1)`$. See [Bell construction](bell-construction.md#quantum-score-as-a-nonnegative-pauli-polynomial).
3. **Quantum concentration.** Exact fourth moments bound the relative variance of the nonconstant score by $`4/(D-1)`$. This remains true even though some scaled weights exceed one. See [Haar moments](haar-moments.md#3-a-weighted-variance-lemma).
4. **Local-score control.** Each deterministic score is a quadratic form in the Haar vector. The tensor operator's Hilbert–Schmidt and operator norms, together with a union bound over $`2^{mN}`$ responses, bound the local value by $`2k_Nb^{N/2}`$. See [Bell construction](bell-construction.md#main-scaled-dual-bound).

The resulting quantum scale is $`b^N`$, while the controlled local scale is $`O_m(N)b^{N/2}`$.

## Compatible families and the converse bound

If $`\nu\le1`$, a joint parent measurement exists. Let $`G_{s_i}`$ denote its effects at party $`i`$. For any shared state $`\rho`$, the probabilities

```math
p(s_1,\ldots,s_N)
=\operatorname{Tr}\!\left[
\rho\,G_{s_1}\otimes\cdots\otimes G_{s_N}
\right]
```

are nonnegative and sum to one. Given this shared variable, party $`i`$ outputs the predetermined value $`s_{i,x_i}`$. Parent-measurement marginalization reproduces the original quantum behavior for every input tuple. Thus all such behaviors are Bell-local, and

```math
\mathcal R_N(A)=1\qquad(\nu\le1).
```

The equality follows because a constant Bell expression attains ratio one.

For $`\nu>1`$, the same absolute normalization admits the general upper bound

```math
\mathcal R_N(A)\le\nu^{N-1}.
```

The proof in [Party count](party-count.md) rescales $`N-1`$ parties to compatibility and expresses their original measurements through signed output-flip kernels. This preserves the marginal correlators and constant term. In particular, the constructive lower base and the universal upper base obey

```math
\sqrt{\frac{1+\nu^2}{2}}
\le\liminf_{N\to\infty}\mathcal R_N(A)^{1/N}
\le\limsup_{N\to\infty}\mathcal R_N(A)^{1/N}
\le\nu.
```

For a prescribed violation ratio $`R_*>1`$, the converse requires $`N\ge1+\ln R_*/\ln\nu`$. The constructive theorem gives a sufficient count of order $`O_m((\nu-1)^{-1}\ln(1/(\nu-1)))`$ near compatibility. These fixed-margin bounds and their limitations are detailed in [Party count](party-count.md).

## Orthogonal examples

For $`k\le3`$ orthogonal noisy Pauli observables $`A_j=\eta_j\sigma_j`$, the exact norm is

```math
\nu=\sqrt{\sum_{j=1}^{k}\eta_j^2}.
```

The optimal dual is $`\mathbf v_j=(\eta_j/\nu)e_j`$, so the scaled auxiliary operators coincide with the physical observables: $`B_j^{(\nu)}=\eta_j\sigma_j`$. The coefficients reduce to noise-weighted Pauli expectations. The [compatibility page](compatibility-dual.md#5-universal-qubit-bound-and-orthogonal-examples) proves the norm formula directly.

| Measurement family | Incompatibility condition | Guaranteed constructive base |
| --- | --- | --- |
| Two orthogonal axes | $`\eta_1^2+\eta_2^2>1`$ | $`\sqrt{(1+\eta_1^2+\eta_2^2)/2}`$ |
| Three orthogonal axes | $`\eta_1^2+\eta_2^2+\eta_3^2>1`$ | $`\sqrt{(1+\eta_1^2+\eta_2^2+\eta_3^2)/2}`$ |

For equal sharpness, the thresholds are $`\eta>1/\sqrt2`$ and $`\eta>1/\sqrt3`$, respectively. Three axes can therefore fall within the theorem even when every two-axis restriction is compatible; the construction uses the incompatibility of the whole supplied family.

## Scope and further consequences

The result certifies ordinary multipartite Bell nonlocality for the stated finite, unbiased, binary qubit family. It does not establish genuine $`N`$-party nonlocality, an optimal exponential rate, or an optimal first-violation party count.

The finite formulas specify a mathematical construction. Coefficient evaluation, the number of correlators, exact local-bound evaluation, state preparation, and statistical sampling are separate resource questions. The theorem itself supplies no polynomial-resource implementation claim; these costs are discussed in [Resources and interpretation](resources.md).

The same proof accepts a nonoptimal feasible certificate, which supports the explicit finite-setting construction in [Local-noise threshold](local-noise-threshold.md). That page treats the depolarizing visibility boundary and the measurement choices needed near it. The present pages establish the core Bell-construction and probability estimates on which that consequence rests.

---

Proof pages: [Compatibility dual](compatibility-dual.md), [Haar moments](haar-moments.md), and [Bell construction](bell-construction.md). Further results: [Party count](party-count.md) and [Local-noise threshold](local-noise-threshold.md). See the [references](../references/README.md) and the [repository overview](../README.md) for context.
