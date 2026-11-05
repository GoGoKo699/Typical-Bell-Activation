# The threshold for independent local depolarization

Independent depolarization has an exact asymptotic threshold for Bell nonlocality of Haar-random multiqubit pure inputs. For every fixed visibility $`\eta>1/2`$, a finite menu of binary projective measurements, fixed independently of the state and the number of parties, detects nonlocality with probability tending to one. At $`\eta\le1/2`$, every output is Bell local for arbitrary local qubit POVMs.

The Bell functional on the nonlocal side is tailored to the input state. The measurement menu is fixed. Throughout, each Bell party holds one qubit, the identity coefficient is retained, and the local normalization is the maximum absolute deterministic score. See [the model and results](model-and-results.md) for these conventions, [the compatibility dual](compatibility-dual.md) for the norm $`\nu`$, and [the Bell construction](bell-construction.md) for the general theorem.

## 1. Statement and channel convention

For $`0\le\eta\le1`$, define

```math
\Delta_\eta(X)
=\eta X+(1-\eta)\operatorname{tr}(X)\frac{I}{2}.
```

Let $`D=2^N`$, let $`|\psi\rangle`$ be Haar distributed on $`(\mathbb C^2)^{\otimes N}`$, and set

```math
\rho_{N,\eta}(\psi)
=\Delta_\eta^{\otimes N}(|\psi\rangle\langle\psi|).
```

**Theorem.** For each fixed $`\eta>1/2`$, there is a finite menu $`\mathsf P_\eta`$ of $`m=m(\eta)`$ binary projective qubit measurements such that the following holds. All $`N`$ parties use $`\mathsf P_\eta`$, and, for a Haar-random input, a state-tailored Bell functional has an exponentially growing absolute violation ratio, except on an event whose probability is at most

```math
\varepsilon_N
=\frac{16}{2^N-1}+e^{-N}+e^{-2^N/8}.
```

In particular, the probability that these fixed-menu statistics are nonlocal tends to one. The finite menu can be chosen before $`N`$ and $`\psi`$ are specified.

For every $`\eta\le1/2`$, every $`N`$, and every input state $`\rho`$, the state $`\Delta_\eta^{\otimes N}(\rho)`$ is fully Bell local for arbitrary local qubit POVMs. Thus, if $`p_N(\eta)`$ is the Haar probability that the output admits a Bell violation with one qubit per party,

```math
p_N(\eta)=0\quad\text{for }\eta\le\frac12,
\qquad
\lim_{N\to\infty}p_N(\eta)=1\quad\text{for }\eta>\frac12.
```

The positive lower bound on success probability is understood to be zero when $`1-\varepsilon_N<0`$; the stated estimate is useful at large $`N`$.

## 2. Moving the noise to the measurements

The channel is self-adjoint for the Hilbert–Schmidt pairing. For a POVM effect $`E`$,

```math
\Delta_\eta^\dagger(E)
=\eta E+(1-\eta)\operatorname{tr}(E)\frac I2.
```

Consequently, the projective measurement with effects $`(I\pm\mathbf n_x\cdot\boldsymbol\sigma)/2`$ on the output is equivalent to the unbiased binary observable

```math
A_x=\eta\mathbf n_x\cdot\boldsymbol\sigma
```

on the pure input. A correlator supported on $`k`$ parties is attenuated by $`\eta^k`$. This support dependence is the noise model used throughout this proof.

## 3. A finite spherical quadrature with explicit size

Let $`\omega`$ be the uniform probability measure on the unit sphere $`S^2`$. Fix $`0<\epsilon<1/2`$.

Choose a maximal set of points with pairwise Euclidean distance greater than $`\epsilon`$. Its spherical caps of Euclidean chord radius $`\epsilon/2`$ are disjoint. A cap of chord radius $`r`$ on the unit sphere has area $`\pi r^2`$, so the number of points satisfies

```math
m_0\le\frac{16}{\epsilon^2}.
```

Maximality gives a covering of $`S^2`$ by the caps of chord radius $`\epsilon`$. Partition the sphere into measurable nearest-center cells $`V_x`$, resolving ties arbitrarily, and write

```math
\mathbf n_x\in S^2,
\qquad
w_x=\omega(V_x),
\qquad
\sum_xw_x=1.
```

Every point in $`V_x`$ is at distance at most $`\epsilon`$ from $`\mathbf n_x`$. For any unit vector $`\mathbf u`$, the function $`\mathbf n\mapsto|\mathbf u\cdot\mathbf n|`$ is 1-Lipschitz, and

```math
\int_{S^2}|\mathbf u\cdot\mathbf n|\,d\omega(\mathbf n)
=\frac12.
```

Therefore the quadrature obeys the uniform estimate

```math
\sup_{\|\mathbf u\|=1}
\sum_xw_x|\mathbf u\cdot\mathbf n_x|
\le\frac12+\epsilon.
```

### Exact isotropy by cube symmetrization

Let $`\mathcal G`$ be the 24 proper rotational symmetries of a cube: the signed permutation matrices with determinant $`+1`$. Replace every weighted direction $`(\mathbf n_x,w_x)`$ by the directions $`(R\mathbf n_x,w_x/24)`$ for $`R\in\mathcal G`$. Identical directions may be merged. Relabel the resulting weighted menu by $`x=1,\ldots,m`$. It satisfies

```math
m\le\frac{384}{\epsilon^2},
\qquad
\sum_xw_x=1,
\qquad
\sup_{\|\mathbf u\|=1}\sum_xw_x|\mathbf u\cdot\mathbf n_x|
\le\frac12+\epsilon.
```

The last estimate follows by applying the preceding bound to each $`R^T\mathbf u`$ and averaging. In addition,

```math
\sum_xw_x\mathbf n_x\mathbf n_x^T=\frac{I_3}{3}.
```

To see this, the group average of any symmetric matrix commutes with the cube rotations. The rotations that reverse two coordinate axes remove its off-diagonal entries; coordinate permutations make its diagonal entries equal. Its trace is preserved, so the group average of $`\mathbf n\mathbf n^T`$ is exactly $`I_3/3`$.

The weights are part of the Bell coefficient construction. They do not impose a probability distribution on the measurement choices of the Bell experiment.

## 4. A feasible compatibility certificate

Set

```math
h=\frac12+\epsilon,
\qquad
\mathbf v_x=\frac{w_x}{h}\mathbf n_x.
```

For any finite collection of vectors,

```math
\max_{s\in\{\pm1\}^m}
\left\|\sum_xs_x\mathbf v_x\right\|
=\max_{\|\mathbf u\|=1}\sum_x|\mathbf u\cdot\mathbf v_x|.
```

Indeed, write the norm as a maximum of the inner product with $`\mathbf u`$ and interchange the two maxima. For fixed $`\mathbf u`$, choose each sign to match $`\mathbf u\cdot\mathbf v_x`$. The quadrature estimate consequently makes $`\{\mathbf v_x\}`$ feasible for the dual in [compatibility-dual.md](compatibility-dual.md).

For the noisy measurement menu, the achieved dual value and cross matrix are

```math
\mu:=\sum_x\eta\mathbf n_x\cdot\mathbf v_x
=\frac\eta h,
\qquad
T:=\sum_x\eta\mathbf n_x\mathbf v_x^T
=\frac\mu3 I_3.
```

Here $`\mu`$ is the value of this explicit certificate; $`\nu`$ continues to denote the optimum compatibility norm. In particular,

```math
\nu(\{\eta\mathbf n_x\})\ge\mu.
```

Choose $`0<\epsilon<\eta-1/2`$. Then $`1<\mu<2`$ and $`0\preceq T\preceq I_3`$. The certificate therefore satisfies the hypotheses of the feasible-certificate version of the Bell construction without solving a dual optimization problem.

### Why the limiting norm is two

The same argument at visibility one gives finite projective menus with $`\nu\ge1/(1/2+\epsilon)`$. Conversely, any dual-feasible family obeys

```math
\sum_x|\mathbf u\cdot\mathbf v_x|\le1
\quad\text{for every unit }\mathbf u.
```

Spherical averaging gives $`\frac12\sum_x\|\mathbf v_x\|\le1`$. Since every qubit observable in the present class has $`\|\mathbf a_x\|\le1`$, its dual objective is at most two. Hence

```math
\sup_{\text{finite projective qubit menus}}\nu=2,
\qquad
\nu(\eta\mathsf P)=\eta\nu(\mathsf P).
```

This proves the finite-menu approximation needed at every fixed $`\eta>1/2`$.

## 5. The state-tailored Bell functional

Use the scaled construction, with

```math
B_0=I,
\qquad
B_x=\mu\,\mathbf v_x\cdot\boldsymbol\sigma,
\qquad
c_{x_1\ldots x_N}(\psi)
=\langle\psi|B_{x_1}\otimes\cdots\otimes B_{x_N}|\psi\rangle.
```

The index $`0`$ denotes omission of a party from that correlator. In particular, $`c_{0\ldots0}=1`$. All physical measurements remain the projective menu $`\mathsf P_\eta`$. The coefficients are determined by the intended pure input and fixed before the Bell test.

Put $`P_0=I`$ and $`P_x=\mathbf n_x\cdot\boldsymbol\sigma`$ for the physical projective observables. The score on the noisy output is

```math
Q(\psi,\eta)
=\sum_{x_1,\ldots,x_N=0}^m
c_{x_1\ldots x_N}(\psi)
\operatorname{tr}\!\left[
\rho_{N,\eta}(\psi)
P_{x_1}\otimes\cdots\otimes P_{x_N}
\right].
```

The scaled cross matrix is $`\mu T=(\mu^2/3)I_3`$. Moving the channel to the observables and expanding in the Pauli basis gives

```math
Q(\psi,\eta)
=\sum_{P\in\{I,X,Y,Z\}^N}
\left(\frac{\mu^2}{3}\right)^{|P|}
\langle\psi|P|\psi\rangle^2.
```

This identity also follows directly from the transfer-matrix formula in [the Bell construction](bell-construction.md). It uses all subset correlators, including the identity term.

### Quantum concentration

Write

```math
W=(1+\mu^2)^N-1,
\qquad
W_2=\left(1+\frac{\mu^4}{3}\right)^N-1.
```

The weighted Haar-moment identities in [haar-moments.md](haar-moments.md) give

```math
\mathbb E(Q-1)=\frac{W}{D+1},
\qquad
\frac{\operatorname{Var}(Q-1)}{[\mathbb E(Q-1)]^2}
\le\frac2D+2\frac{W_2}{W^2}.
```

These identities apply even when $`\mu^2/3>1`$. The needed weight estimate is obtained as follows. For $`\mu\ge1`$,

```math
2\left(1+\frac{\mu^4}{3}\right)
\le(1+\mu^2)^2.
```

Let $`X=(1+\mu^2)^N\ge D`$. Then

```math
\frac{W_2}{W^2}
\le\frac{X^2/D-1}{(X-1)^2}
\le\frac1{D-1},
```

where the second inequality is equivalent to $`(X-D)^2\ge0`$. It follows that the relative variance is at most $`4/(D-1)`$. Chebyshev's inequality yields

```math
Q\ge1+\frac{(1+\mu^2)^N-1}{2(D+1)}
```

except with probability $`16/(D-1)`$.

### Uniform classical control

For a deterministic local assignment $`s_i\in\{\pm1\}^m`$ at party $`i`$, define

```math
\mathbf b_{s_i}=\sum_xs_{i,x}\mathbf v_x,
\qquad
O_{\mathbf s}
=\bigotimes_{i=1}^N
\left(I+\mu\,\mathbf b_{s_i}\cdot\boldsymbol\sigma\right).
```

The deterministic Bell score is $`\langle\psi|O_{\mathbf s}|\psi\rangle`$. Dual feasibility gives $`\|\mathbf b_{s_i}\|\le1`$. Set

```math
b=\frac{1+\mu^2}{2},
\qquad
t_N=(m\ln2+1)N+\ln2,
\qquad
f(t)=1+\sqrt{2t}+t.
```

The operator estimates underlying the uniform bound are

```math
\operatorname{tr}O_{\mathbf s}=D,
\qquad
\|O_{\mathbf s}\|_{\mathrm{HS}}\le D b^{N/2},
\qquad
\|O_{\mathbf s}\|_{\mathrm{op}}
\le(1+\mu)^N\le D b^{N/2}.
```

The Hilbert–Schmidt estimate uses $`\operatorname{tr}(I+\mu\mathbf b\cdot\boldsymbol\sigma)^2=2(1+\mu^2\|\mathbf b\|^2)`$. The last inequality follows from $`(1+\mu)^2\le2(1+\mu^2)`$.

Apply the Gaussian quadratic-form estimate proved in [haar-moments.md](haar-moments.md), with the operator estimates above, and union bound over the $`2^{mN}`$ deterministic assignments. It gives

```math
L_{\mathrm{abs}}
:=\max_{\mathbf s}
\left|\langle\psi|O_{\mathbf s}|\psi\rangle\right|
\le2f(t_N)b^{N/2}
```

except with probability $`e^{-N}+e^{-D/8}`$. The Gaussian normalization event is common to all assignments and is counted once. A uniform average of the deterministic scores is $`c_{0\ldots0}=1`$, so $`L_{\mathrm{abs}}\ge1`$ and the ratio below is well-defined.

Combining the quantum and classical estimates proves that, outside an event of probability at most $`\varepsilon_N`$,

```math
R_N(\psi,\eta)
:=\frac{Q(\psi,\eta)}{L_{\mathrm{abs}}}
\ge\frac{b^{N/2}}{8f(t_N)}.
```

Since $`b>1`$ and $`t_N=O(N)`$ at fixed menu, this bound grows exponentially. The menu and the certificate are fixed once $`\eta`$ and $`\epsilon`$ are chosen.

## 6. Locality at and below the endpoint

[Renner's joint-measurability theorem](../references/README.md#renner2024) applies to precisely the map $`E\mapsto\eta E+(1-\eta)\operatorname{tr}(E)I/2`$. At $`\eta\le1/2`$, all noisy qubit POVMs admit a parent measurement and classical postprocessing.

For arbitrary local POVM families at the $`N`$ parties, write

```math
\Delta_\eta^\dagger(M^{(i)}_{a|x})
=\int p_i(a|x,\lambda_i)\,G_i(d\lambda_i).
```

For an arbitrary input state $`\rho`$, define the hidden-variable probability measure

```math
q(d\lambda_1\cdots d\lambda_N)
=\operatorname{tr}\!\left[
\rho\,
G_1(d\lambda_1)\otimes\cdots\otimes G_N(d\lambda_N)
\right].
```

It is nonnegative because the product effects are positive, and it is normalized because each parent POVM integrates to the identity. The output probabilities consequently have the fully local form

```math
p(a_1,\ldots,a_N|x_1,\ldots,x_N)
=\int q(d\boldsymbol\lambda)
\prod_{i=1}^N p_i(a_i|x_i,\lambda_i).
```

This proves the endpoint assertion for every input state, including mixed states, and for arbitrary finite Bell scenarios built from local qubit POVMs.

## 7. Settings and parties near the boundary

In this section let $`\delta=\eta-1/2\in(0,1/2]`$ and choose $`\epsilon=\delta/2`$. The explicit construction gives

```math
m\le\frac{1536}{\delta^2},
\qquad
\mu=\frac{1+2\delta}{1+\delta},
\qquad
\mu-1=\frac\delta{1+\delta}.
```

The certificate gap is therefore of order $`\delta`$. The finite-$`N`$ inversion in [party-count.md](party-count.md) applies with the certificate value $`\mu`$ in place of the optimum $`\nu`$. For any fixed target absolute ratio above one and fixed success probability, it gives the sufficient scaling

```math
N=O\!\left(\delta^{-1}\log\frac1\delta\right)
\quad\text{as }\delta\downarrow0,
```

with one finite menu at each fixed $`\delta`$. The cited page supplies an explicit sufficient integer $`N`$ and the signed-flip converse for a fixed ratio.

## 8. Scope and relation to the existential result

The nonlocality certified here is failure of a fully local model across the $`N`$ individual qubits. It does not establish genuine multipartite nonlocality. Grouping several noisy qubits into one party and allowing collective measurements changes the measurement model and is outside the endpoint proof.

The existence of some nonlocal output for every $`\eta>1/2`$ is already [Corollary 7 of Plávala–Gühne–Quintino](../references/README.md#pgq2025). Their discussion asks for identified input states and bounds on the number of parties. The results above give Haar-typical inputs, a finite measurement menu independent of the input and party count, an explicit sufficient party count, and exponential growth of an absolute Bell ratio. These statements place no efficiency assumption on preparation or determination of the state-tailored coefficients.
