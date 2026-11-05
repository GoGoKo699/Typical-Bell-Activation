# Bell construction and quantitative bounds

This page proves the finite-$`N`$ theorems stated in [Model and results](model-and-results.md). The inputs are the [compatibility dual and transfer-matrix lemma](compatibility-dual.md) and the [Haar moment and tail estimates](haar-moments.md).

Fix an incompatible finite family of unbiased binary qubit measurements, with compatibility norm $`\nu>1`$. Choose and fix an optimal aligned dual tuple $`\{\mathbf v_x\}_{x=1}^m`$, independently of the state. Thus

```math
\max_{s\in\{-1,1\}^{m}}
\left\|\sum_xs_x\mathbf v_x\right\|_2\le1,
\qquad
T=\sum_x\mathbf a_x\mathbf v_x^{\mathsf T}\succeq0,
```

and the eigenvalues of $`T`$ obey

```math
0\le\lambda_j\le1,
\qquad \sum_{j=1}^{3}\lambda_j=\nu.
```

There are $`N\ge1`$ parties, each holding one qubit, and $`D=2^N`$. We will use

```math
t_N=(m\ln2+1)N+\ln2.
```

## The coefficients and their normalization

Set $`A_0=I`$. For a scale $`\tau\ge0`$, define auxiliary Hermitian operators

```math
B_0^{(\tau)}=I,
\qquad
B_x^{(\tau)}=\tau\mathbf v_x\cdot\boldsymbol\sigma
\quad (x=1,\ldots,m).
```

The auxiliary operators specify real Bell coefficients; they are not additional measurements. In particular, their norms need not be at most one. The only physical measurements in the Bell trial are the supplied $`M_{a\mid x}`$.

For a pure state $`|\psi\rangle`$, and every word $`\mathbf x=(x_1,\ldots,x_N)\in\{0,1,\ldots,m\}^N`$, put

```math
c_{\mathbf x}^{(\tau)}(\psi)
=\left\langle\psi\left|
\bigotimes_{i=1}^{N}B_{x_i}^{(\tau)}
\right|\psi\right\rangle.
```

If $`E_{\mathbf x}`$ is the correlator of the parties for which $`x_i\ne0`$, define

```math
\mathcal B_{\psi,\tau}(E)
=\sum_{\mathbf x\in\{0,\ldots,m\}^{N}}
c_{\mathbf x}^{(\tau)}(\psi)E_{\mathbf x}.
```

An index $`0`$ asks for a marginal correlator, so it does not add a physical input. The all-zero word is retained:

```math
E_{\mathbf 0}=1,
\qquad c_{\mathbf 0}^{(\tau)}=1.
```

For a deterministic local response array $`s=(s_{i,x})`$, set $`s_{i,0}=1`$. The absolute local bound is

```math
L_{\mathrm{abs}}(c)
=\max_{s\in\{-1,1\}^{mN}}
\left|\sum_{\mathbf x}c_{\mathbf x}
                    \prod_{i=1}^{N}s_{i,x_i}\right|.
```

The convex hull of these deterministic responses is the full Bell-local set in this correlator representation. Every local behavior therefore satisfies $`|\mathcal B_c(E)|\le L_{\mathrm{abs}}(c)`$.

The quantum score on the same state used to specify the coefficients is

```math
Q_\tau(\psi)
=\sum_{\mathbf x}
\left\langle\bigotimes_iB_{x_i}^{(\tau)}\right\rangle_\psi
\left\langle\bigotimes_iA_{x_i}\right\rangle_\psi.
```

We normalize it by the actual local bound:

```math
R_N^{(\tau)}(\psi)
=\frac{Q_\tau(\psi)}
       {L_{\mathrm{abs}}(c^{(\tau)}(\psi))}.
```

The numerator will be nonnegative. The constant term is retained in both numerator and denominator throughout this page. Centering a random variable for a tail estimate below does not change the Bell functional.

## Deterministic scores are tensor quadratic forms

Expanding a tensor product gives the exact identity

```math
\begin{aligned}
L_s^{(\tau)}(\psi)
&:=\sum_{\mathbf x}c_{\mathbf x}^{(\tau)}(\psi)
                       \prod_i s_{i,x_i}\\
&=\langle\psi|F_s^{(\tau)}|\psi\rangle,
\end{aligned}
```

where

```math
F_s^{(\tau)}
=\bigotimes_{i=1}^{N}
\left[I+\tau\left(\sum_xs_{i,x}\mathbf v_x\right)
                    \cdot\boldsymbol\sigma\right].
```

There are at most $`2^{mN}`$ such operators. They are fixed before $`\psi`$ is drawn, and every one has trace $`D`$.

A uniform average over the deterministic signs eliminates every nonconstant correlator, giving

```math
2^{-mN}\sum_sL_s^{(\tau)}(\psi)=1.
```

In particular, $`L_{\mathrm{abs}}(c^{(\tau)}(\psi))\ge1`$, so the ratio is always well-defined.

## Quantum score as a nonnegative Pauli polynomial

Let $`\sigma_0=I`$ and let $`\sigma_1,\sigma_2,\sigma_3`$ be a fixed Pauli frame. Expanding the physical and auxiliary operators in this basis, the one-site coefficient contraction is the real matrix

```math
C_\tau=
\begin{pmatrix}
1&0\\
0&\tau T
\end{pmatrix}.
```

For example, its traceless block has entries

```math
(C_\tau)_{jk}
=\tau\sum_x(\mathbf a_x)_j(\mathbf v_x)_k
=\tau T_{jk}.
```

If $`r_{\boldsymbol\alpha}=\langle\sigma_{\alpha_1}\otimes\cdots\otimes\sigma_{\alpha_N}\rangle_\psi`$, direct expansion of the definition of $`Q_\tau`$ gives

```math
Q_\tau(\psi)
=\sum_{\boldsymbol\alpha,\boldsymbol\beta}
r_{\boldsymbol\alpha}r_{\boldsymbol\beta}
\prod_{i=1}^{N}(C_\tau)_{\alpha_i\beta_i}.
```

Choose the fixed Pauli frame along eigenvectors of the real symmetric matrix $`T`$. The frame can be chosen with a consistent orientation by changing an eigenvector's sign if needed. In this frame, $`C_\tau`$ is diagonal, so

```math
\boxed{
Q_\tau(\psi)=
\sum_{P\in\mathcal P_N}w_P^{(\tau)}\langle P\rangle_\psi^2
=1+X_\tau(\psi),}
```

where the local weights are

```math
q_0=1,
\qquad q_j=\tau\lambda_j,
\qquad
w_P^{(\tau)}=\prod_{i=1}^{N}q_{p_i}.
```

All weights are nonnegative; hence $`Q_\tau(\psi)\ge1`$ for every state. The frame change is only a coordinate choice for the proof, not an additional operation in the Bell trial.

The first total weight is

```math
W_\tau=(1+\tau\nu)^N.
```

The second-order Haar identity therefore gives the exact mean

```math
\boxed{
\mathbb E Q_\tau
=\frac{D+(1+\tau\nu)^N}{D+1}.}
```

For $`\tau=1`$ and $`\tau=\nu`$, the weighted variance calculation in [Haar moments](haar-moments.md#4-the-two-product-weight-families) proves

```math
\Pr\!\left[
Q_\tau<1+\frac{W_\tau-1}{2(D+1)}
\right]\le\frac{16}{D-1}.
```

## Simpler positive-dual bound

Take $`\tau=1`$. Dual feasibility gives

```math
\left\|\sum_xs_{i,x}\mathbf v_x\right\|_2\le1.
```

Every local factor of $`F_s^{(1)}`$ is consequently positive semidefinite, with trace two, so $`F_s^{(1)}\succeq0`$ and $`\operatorname{Tr}F_s^{(1)}=D`$. Its deterministic score is nonnegative. The positive quadratic-form tail and the union bound from [Haar moments](haar-moments.md#5-positive-quadratic-forms-have-an-exponential-tail) yield

```math
L_{\mathrm{abs}}(c^{(1)}(\psi))
=\max_s L_s^{(1)}(\psi)
\le2t_N
```

except on an event of probability at most $`e^{-N}`$.

Intersect this event with the quantum lower-tail event. No independence is required. With probability at least

```math
\max\left\{0,\ 1-\frac{16}{D-1}-e^{-N}\right\},
```

the retained-constant ratio satisfies

```math
\boxed{
R_N^{(1)}(\psi)
\ge
\frac{\displaystyle 1+\frac{(1+\nu)^N-1}{2(D+1)}}{2t_N}
\ge\frac{[(1+\nu)/2]^N}{8t_N}.}
```

The final inequality uses $`Q_1\ge W_1/(4D)`$. This gives an elementary positive-operator proof of exponential activation for every $`\nu>1`$.

## Main scaled-dual bound

Now take $`\tau=\nu`$ and put

```math
b=\frac{1+\nu^2}{2}>1,
\qquad
k_N=1+\sqrt{2t_N}+t_N.
```

The operators $`F_s^{(\nu)}`$ are generally indefinite. For
$`\mathbf u_i=\sum_xs_{i,x}\mathbf v_x`$, their one-site factors have eigenvalues $`1\pm\nu\|\mathbf u_i\|_2`$. Since $`\|\mathbf u_i\|_2\le1`$, multiplicativity of tensor-product norms gives

```math
\begin{aligned}
\frac{\|F_s^{(\nu)}\|_{\mathrm{HS}}^2}{D^2}
&=\prod_{i=1}^{N}\frac{1+\nu^2\|\mathbf u_i\|_2^2}{2}
\le b^N,\\
\frac{\|F_s^{(\nu)}\|_{\mathrm{op}}}{D}
&=\prod_{i=1}^{N}\frac{1+\nu\|\mathbf u_i\|_2}{2}
\le\left(\frac{1+\nu}{2}\right)^N
\le b^{N/2}.
\end{aligned}
```

The last inequality is $`(1+\nu)^2\le2(1+\nu^2)`$.

Apply the Hermitian Gaussian tail and common normalization estimate from [Haar moments](haar-moments.md#6-hermitian-quadratic-forms-and-gaussian-normalization) to all deterministic operators. Except with probability at most $`e^{-N}+e^{-D/8}`$,

```math
\begin{aligned}
L_{\mathrm{abs}}(c^{(\nu)}(\psi))
&\le2\left[1+(\sqrt{2t_N}+t_N)b^{N/2}\right]\\
&\le2k_N b^{N/2}.
\end{aligned}
```

The second line uses $`b\ge1`$. Independently of this upper-tail argument, the weighted fourth moments give

```math
Q_\nu(\psi)
\ge1+\frac{(1+\nu^2)^N-1}{2(D+1)}
\ge\frac{b^N}{4}
```

except with probability at most $`16/(D-1)`$. Combining the events proves the main finite-$`N`$ statement:

```math
\boxed{
R_N^{(\nu)}(\psi)
\ge
\frac{\displaystyle 1+\frac{(1+\nu^2)^N-1}{2(D+1)}}
     {2k_N b^{N/2}}
\ge
\frac{b^{N/2}}{8k_N}}
```

with probability at least

```math
\boxed{
\max\left\{0,\
1-\frac{16}{2^N-1}-e^{-N}-e^{-2^N/8}
\right\}.}
```

These are exact finite inequalities with conservative constants. A negative untruncated probability estimate at small $`N`$ carries no existence information; the displayed maximum states that limitation explicitly.

For fixed $`m`$ and $`\nu>1`$, $`k_N=O_m(N)`$ and the failure probability tends to zero. The guaranteed constructive exponential base is therefore

```math
g(\nu)=\sqrt{\frac{1+\nu^2}{2}}>1.
```

More explicitly, for every fixed $`1\lt r\lt g(\nu)`$,

```math
\Pr\bigl[R_N^{(\nu)}(\psi)\ge r^N\bigr]\longrightarrow1.
```

This is a lower bound furnished by this construction. It is not an assertion that $`g(\nu)`$ is the optimal Bell-violation rate.

### Why scale by $`\nu`$?

For a general scalar $`\tau\ge1`$, the exponential factor in the quantum mean is $`(1+\tau\nu)/2`$, while the same uniform Hilbert–Schmidt estimate has factor $`\sqrt{(1+\tau^2)/2}`$. Their ratio is

```math
g_\tau(\nu)=\frac{1+\tau\nu}{\sqrt{2(1+\tau^2)}}.
```

Its logarithmic derivative is

```math
\frac{d}{d\tau}\ln g_\tau(\nu)
=\frac{\nu-\tau}{(1+\tau\nu)(1+\tau^2)}.
```

Thus this comparison of exponential factors is optimized at $`\tau=\nu`$. The proof above establishes the required quantum concentration at that choice. This one-parameter calculation optimizes the scalar rescaling in this estimate, not all Bell functionals or states.

## Feasible dual certificates

The proofs do not require exact optimization. Suppose a fixed feasible tuple has a positive transfer matrix

```math
T=\sum_x\mathbf a_x\mathbf v_x^{\mathsf T}\succeq0,
\qquad \gamma=\operatorname{Tr}T>1.
```

Proposition 2 of [Compatibility norm and aligned dual certificates](compatibility-dual.md#4-polar-alignment-and-the-transfer-matrix) gives $`T\preceq I`$ and $`\gamma\le\nu(A)`$. It also shows how to obtain such a positive matrix by polar alignment from any feasible tuple whose original objective exceeds one.

Every step on this page depends only on feasibility and

```math
0\le\lambda_j\le1,
\qquad \sum_j\lambda_j=\gamma.
```

Therefore all positive-dual bounds hold with $`\gamma`$ in place of $`\nu`$. All scaled-dual bounds hold with the same replacement and the scale choice $`\tau=\gamma`$. In particular, setting

```math
b_\gamma=\frac{1+\gamma^2}{2}
```

gives

```math
R_N^{(\gamma)}(\psi)
\ge\frac{b_\gamma^{N/2}}{8k_N}
```

with the same displayed failure bound. Here $`\gamma`$ is a certified achieved value, not a redefinition of the compatibility norm. This version applies directly to the explicit measurement family in [Local-noise threshold](local-noise-threshold.md).

---

See [Model and results](model-and-results.md) for the operational assumptions and theorem summary, [Party count](party-count.md) for sufficient and necessary bounds at a fixed violation margin, and the [reference list](../references/README.md) for the prior compatibility and nonlocality results.
