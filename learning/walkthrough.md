# From fixed measurements to typical Bell activation

A Bell experiment distributes a quantum state among separated laboratories. Each laboratory chooses a measurement setting and records an outcome. A local model can use a shared random variable, but each laboratory's response depends only on that variable and its own setting. A Bell inequality bounds every such local explanation of the observed correlations.

This project asks what a fixed measurement menu can reveal when the number of laboratories grows. If the menu is incompatible, does a carefully engineered state have to be found, or do typical pure states work? The result shows that almost all sufficiently large Haar-random states work, with an inequality constructed from the chosen state's description.

The [Scarani bridge](ANCHOR.md) supplies the Bell-theory foundation. This walkthrough follows the settled [milestone map](MILESTONES.md), with the full proofs linked at each step.

## 1. A single qubit and a fixed menu

**Milestones M01–M05.** A qubit state is described by a density matrix $`\rho`$: a positive matrix with trace one. A binary measurement has two positive effects that sum to the identity. The probability of outcome $`a`$ is $`\operatorname{Tr}(\rho M_a)`$.

The measurements considered here have outcomes $`a=\pm1`$ and effects

```math
M_{a\mid x}=\frac{I+aA_x}{2},
\qquad
A_x=\mathbf a_x\cdot\boldsymbol\sigma,
\qquad
\|\mathbf a_x\|_2\le1.
```

The label $`x`$ selects one of $`m`$ available settings. The three Pauli matrices in $`\boldsymbol\sigma=(X,Y,Z)`$ describe the three Bloch-coordinate directions. The vector's direction selects an axis, while its length describes sharpness. Shortening it toward zero makes the measurement less informative. The measurements are unbiased because the two effects have equal trace.

Joint measurability means that one parent measurement, followed by a setting-dependent classical response, can reproduce every measurement in the menu. It is a property of the whole family. Different settings need not commute for a noisy family to be jointly measurable.

The established compatibility norm $`\nu`$ measures this property in the present model: joint measurability holds exactly when $`\nu\le1`$. Scaling all Bloch vectors by $`\eta`$ scales the norm by the same factor. For sharp $`X`$ and $`Z`$, $`\nu=\sqrt2`$; their uniformly noisy versions are compatible precisely when $`\eta\le1/\sqrt2`$.

The norm and its dual are inherited mathematical ingredients. The project's task is to convert their incompatibility certificate into quantitative typical-state Bell nonlocality. [Compatibility proof and attribution](../science/compatibility-dual.md).

## 2. Bell data, local bounds, and a complete small example

**Milestones M06–M10.** Give one qubit to each of $`N`$ separated parties. For a chosen setting tuple, multiply the recorded $`\pm1`$ outcomes and average over repeated trials. This gives a correlator. One may also ignore some parties' outcomes to obtain a subset correlator. Ignoring an outcome does not discard the trial.

Write $`A_0=I`$ to denote an omitted party in a correlator. The label $`0`$ is bookkeeping; it is not an additional measurement setting. The all-zero correlator is the constant one.

A deterministic local strategy assigns one sign $`s_{i,x}`$ to every setting of every party. A local behavior is a mixture of these strategies, so a linear Bell expression reaches its largest absolute local value at a deterministic strategy. For coefficients $`c_{\mathbf x}`$, the normalization used here is

```math
L_{\mathrm{abs}}(c)
=\max_s\left|
\sum_{\mathbf x}c_{\mathbf x}\prod_i s_{i,x_i}
\right|,
\qquad s_{i,0}=1.
```

The coefficients are numbers chosen before evaluating the test data. A quantum score greater than $`L_{\mathrm{abs}}`$ has no fully local explanation. In a multipartite experiment, this conclusion is ordinary Bell nonlocality; stronger claims about genuine multipartite nonlocality require a different comparison set.

### Two parties with the same sharp X/Z menu

Both parties measure either $`X`$ or $`Z`$. Supply the state

```math
|\psi\rangle
=\frac{1}{\sqrt2}
\left[
u|00\rangle+v|01\rangle-v|10\rangle+u|11\rangle
\right],
\qquad
u=\cos\frac{\pi}{8},\quad v=\sin\frac{\pi}{8}.
```

It is a Bell state with a fixed rotation on the second qubit. Its one-party Pauli expectations vanish. Its measured two-party correlations are

| Correlator | Value |
| --- | --- |
| $`E_{XX}`$ | $`1/\sqrt2`$ |
| $`E_{XZ}`$ | $`-1/\sqrt2`$ |
| $`E_{ZX}`$ | $`1/\sqrt2`$ |
| $`E_{ZZ}`$ | $`1/\sqrt2`$ |

For this menu, the scaled-dual construction described below has auxiliary operators equal to the physical observables. Its coefficients are therefore these same state expectations. The resulting expression is

```math
\mathcal B
=1+\frac{E_{XX}-E_{XZ}+E_{ZX}+E_{ZZ}}{\sqrt2}.
```

The four-correlator combination is a CHSH expression. For deterministic signs it equals

```math
s_{1,X}(s_{2,X}-s_{2,Z})
+s_{1,Z}(s_{2,X}+s_{2,Z}).
```

Exactly one parenthesis vanishes; the other is $`\pm2`$. Thus every deterministic Bell score is $`1\pm\sqrt2`$, and the maximum absolute local score is $`1+\sqrt2`$. On the supplied state the four terms add to $`2\sqrt2`$, giving

```math
Q=3,
\qquad
\frac{Q}{L_{\mathrm{abs}}}
=\frac{3}{1+\sqrt2}
=3(\sqrt2-1)>1.
```

This example retains the constant one in both scores. Removing it would produce a different ratio and require a new local normalization. The state is explicitly chosen, so the example illustrates the construction without asserting any two-party Haar success probability. The CHSH mechanism is standard Bell theory; the many-party typicality guarantee is the result developed here. [Exact general conventions](../science/model-and-results.md).

## 3. What “typical” means

**Milestones M11–M14.** Haar sampling is the unitary-invariant distribution on normalized pure states. For $`N`$ qubits, the state space has dimension $`D=2^N`$. A claim that an event is typical means its Haar probability tends to one as $`N`$ grows. It does not identify an efficient state-preparation procedure.

The order of choices matters. Fix the measurement menu and a compatibility certificate first. Then draw the state and compute its Bell coefficients from its description. The final probability concerns this pair: the drawn state and the inequality prescribed for it. It is not a claim that one state-independent inequality detects almost all Haar states.

The main finite bound has an exceptional probability at most

```math
\varepsilon_N
=\frac{16}{2^N-1}+e^{-N}+e^{-2^N/8}.
```

When this exceeds one, the probability estimate is uninformative; the success guarantee is interpreted as $`\max\{0,1-\varepsilon_N\}`$. A conservative small-system probability bound does not prevent an explicitly chosen small state from violating, as the two-party example shows.

## 4. Turning local incompatibility into Bell coefficients

**Milestones M15–M18.** The dual description of the compatibility norm uses vectors $`\mathbf v_x`$ satisfying

```math
\max_{s\in\{\pm1\}^m}
\left\|\sum_xs_x\mathbf v_x\right\|_2\le1,
\qquad
\sum_x\mathbf a_x\cdot\mathbf v_x=\nu.
```

The signed-sum constraint controls every possible local response table. A common orthogonal alignment of the mathematical witness vectors makes

```math
T=\sum_x\mathbf a_x\mathbf v_x^{\mathsf T}
```

a positive contraction with trace $`\nu`$. Its eigenvalues $`\lambda_j`$ lie between zero and one and sum to $`\nu`$. This alignment changes the certificate, not the experiment's measurement menu.

Choose a scale $`\tau`$, define $`B_0=I`$ and $`B_x=\tau\mathbf v_x\cdot\boldsymbol\sigma`$, and set

```math
c_{x_1\ldots x_N}(\psi)
=\langle\psi|
B_{x_1}\otimes\cdots\otimes B_{x_N}
|\psi\rangle.
```

The $`B_x`$ are auxiliary operators used to compute coefficients. The laboratories continue to measure the supplied $`A_x`$. For the two-axis example, $`\mathbf v_X=\mathbf e_X/\sqrt2`$ and $`\mathbf v_Z=\mathbf e_Z/\sqrt2`$. With $`\tau=\nu=\sqrt2`$, this gives $`B_X=X`$ and $`B_Z=Z`$, explaining the coefficients above.

Two identities now organize the proof. For a deterministic strategy, the score becomes the expectation of a product operator:

```math
L_s(\psi)
=\left\langle\psi\left|
\bigotimes_{i=1}^N
\left[I+\tau\sum_xs_{i,x}\mathbf v_x\cdot\boldsymbol\sigma\right]
\right|\psi\right\rangle.
```

The quantum score, in the fixed eigenbasis of $`T`$, is a nonnegative weighted sum of squared Pauli expectations:

```math
Q_\tau(\psi)
=\sum_{P\in\{I,X,Y,Z\}^{\otimes N}}
w_P\langle P\rangle_\psi^2.
```

The weight is the product of local factors $`1,\tau\lambda_1,\tau\lambda_2,\tau\lambda_3`$. The identity term contributes one. Positivity of the weights makes the quantum growth accessible to a variance estimate, while the deterministic form lets one control the entire local set. [Construction identities](../science/bell-construction.md).

## 5. Why the separation grows on almost all states

**Milestones M19–M23.** Every nonidentity Pauli word has Haar second moment $`\mathbb E\langle P\rangle_\psi^2=1/(D+1)`$. The product weights therefore give the exact mean

```math
\mathbb E Q_\tau
=\frac{D+(1+\tau\nu)^N}{D+1}.
```

An increasing mean alone would be insufficient: rare states might carry it. The exact fourth moments control that possibility. For the two scale choices used in the proof, the variance of $`Q_\tau-1`$ divided by its squared mean is at most $`4/(D-1)`$. Consequently, the quantum score is at least half of its nonconstant mean, plus the retained constant, outside an event of probability at most $`16/(D-1)`$.

For $`\tau=1`$, every deterministic product operator is positive and has trace $`D`$. A Haar tail estimate controls its expectation. A union bound over all $`2^{mN}`$ strategies then bounds the maximum by a quantity proportional to $`N`$ at fixed $`m`$. The quantum scale grows as $`[(1+\nu)/2]^N`$, so every $`\nu>1`$ gives exponential separation.

Scaling instead by $`\tau=\nu`$ improves the guaranteed rate. The deterministic operators can now be indefinite, so the proof controls their absolute quadratic forms. Put

```math
b=\frac{1+\nu^2}{2},
\qquad
t_N=(m\ln2+1)N+\ln2.
```

The quantum scale is $`b^N`$, while the controlled local scale is proportional to $`Nb^{N/2}`$. Combining the estimates yields

```math
R_N\ge
\frac{b^{N/2}}{8(1+\sqrt{2t_N}+t_N)}
```

with probability at least $`\max\{0,1-\varepsilon_N\}`$. Its denominator grows only linearly in $`N`$ at fixed menu size, so the achieved exponential base is $`\sqrt b>1`$. This is a constructive rate, not an optimality theorem. [Exact moments and tails](../science/haar-moments.md) · [Finite theorem](../science/model-and-results.md).

## 6. A finite check with an exact local maximum

**Milestone M24.** The repository also specifies a six-qubit state with integer real and imaginary amplitudes. Every party uses sharp $`X,Y,Z`$. The construction's coefficients are the state's Pauli expectations, and purity gives quantum score $`64`$.

At each site there are eight deterministic sign triples. Enumerating all $`8^6=262144`$ assignments with integer arithmetic gives the exact absolute local maximum $`28808/477`$. The resulting ratio is

```math
\frac{64}{28808/477}=\frac{3816}{3601}>1.
```

This is an independently reproducible illustration. The asymptotic theorem is proved by the moments and tail bounds, rather than by extrapolating the six-qubit outcome. [State, arithmetic, noise controls, and reproduction](../science/finite-example.md).

## 7. Why independent local noise has a half-visibility boundary

**Milestones M25–M27.** Local depolarization contracts each qubit's Bloch vector by $`\eta`$. Measuring a sharp direction on the noisy output is equivalent to measuring the observable $`\eta\mathbf n\cdot\boldsymbol\sigma`$ on the pure input. A correlator involving $`k`$ parties is attenuated by $`\eta^k`$. This is different from mixing one global white-noise state into the whole system.

Finite projective direction sets can approach compatibility norm two. Therefore, at every fixed $`\eta>1/2`$, a sufficiently rich finite menu has an incompatible noisy image. Applying the typical-state theorem then detects nonlocality for a Haar fraction tending to one. The menu may depend on $`\eta`$, but it is fixed independently of $`N`$ and the state.

At $`\eta\le1/2`$, the established universal noisy-qubit compatibility theorem supplies a parent measurement for any local POVM family. Applying those parents to the input state defines a shared classical distribution; each party subsequently responds locally. Every input state is consequently Bell local across the individual qubits.

The boundary is exact in this one-qubit-per-party model. The existence of some nonlocal state above one half was already known. The present construction makes that side typical and quantitative. [Noise theorem, finite menu, endpoint proof, and attribution](../science/local-noise-threshold.md).

## 8. Party counts, evidence costs, and the complete result

**Milestones M28–M30.** For an incompatible menu, $`\nu>1`$, an all-state converse bounds every absolute Bell ratio by $`\nu^{N-1}`$. To reach a prescribed fixed ratio greater than one as $`\nu\downarrow1`$, the party count must therefore grow at least as $`1/(\nu-1)`$. The Haar construction supplies a sufficient count of order $`(\nu-1)^{-1}\ln(1/(\nu-1))`$ at fixed menu size and confidence. These bounds leave a logarithmic gap. They do not give a diverging lower bound for the first violation when its size may shrink toward one. [Party-count account](../science/party-count.md).

A Bell ratio compares expectation values. It does not measure the number of trials needed to estimate them. The state description, coefficient tensor, setting space and generic Haar preparation can all be costly. The resource account also transfers an existing noisy-local discrimination lower bound to Bell tests with fixed soundness and power. It does not claim a matching sample upper bound for testing against the entire local set.

There is a further distinction between the theorem and an individual experimental certificate. The analytical local-score estimate holds on a stated high-probability Haar event. A statistical protocol using it must account for that exceptional probability. A supplied individual state needs a valid bound for that instance. [Resources and interpretation](../science/resources.md).

The result joins three statements: compatibility prevents all Bell violations in this setting; incompatibility supplies a state-dependent witness whose violation grows on typical large pure states; and finite direction menus translate that construction into an exact typical-state local-noise boundary. Its open quantitative questions concern optimal rates, sharp finite-party behavior, and more efficient preparation and certification within clearly specified architectures.

[Learning overview](README.md) · [Scarani bridge](ANCHOR.md) · [30-milestone map](MILESTONES.md) · [Complete scientific account](../science/README.md)
