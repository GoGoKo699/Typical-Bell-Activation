# Compatibility norm and aligned dual certificates

This page gives the compatibility criterion and the dual certificate used by the [Bell construction](bell-construction.md). The physical model and normalization are fixed in [Model and results](model-and-results.md).

The compatibility norm is established background. For unbiased effects on a centrally symmetric state space, its identification with a projective tensor norm follows from Bluhm, Jenčová, and Nechita, especially Proposition 10.1, Corollary 10.2, and Lemma 10.4 of [BJN2022](../references/README.md#bjn2022). The general quantum compatibility norm and its witnesses are developed in [BN2022](../references/README.md#bn2022). Grinko and Uola give an equivalent finite qubit criterion through Fourier coefficients and a second-order cone program in [Grinko–Uola2025](../references/README.md#grinko-uola2025). A direct proof in the normalization used here follows.

## 1. Measurements and the primal norm

Let $`m\ge1`$ be finite. Write the binary unbiased qubit measurements as

```math
M_{a\mid x}=\frac{I+aA_x}{2},
\qquad A_x=\mathbf a_x\cdot\boldsymbol\sigma,
\qquad \mathbf a_x\in\mathbb R^3,
\quad \|\mathbf a_x\|_2\le1,
```

where $`a\in\{-1,1\}`$ and $`x=1,\ldots,m`$. Let

```math
\mathcal S_m=\{s\in\{-1,1\}^m:s_1=1\}
```

contain one representative of each antipodal sign pair. Define

```math
\nu(A)=
\min_{\{\mathbf g_s\}_{s\in\mathcal S_m}}
\left\{
\sum_{s\in\mathcal S_m}\|\mathbf g_s\|_2:
\mathbf a_x=\sum_{s\in\mathcal S_m}s_x\mathbf g_s
\quad\text{for every }x
\right\}.
```

The constraint is always feasible. For example,

```math
\mathbf g_s=2^{-(m-1)}\sum_{x=1}^{m}s_x\mathbf a_x
```

works because

```math
\sum_{s\in\mathcal S_m}s_xs_y=2^{m-1}\delta_{xy}.
```

The minimum is attained: the feasible set is closed, and every bounded objective sublevel set is bounded in this finite-dimensional space. The resulting function is a norm on the tuple of Bloch vectors. It is homogeneous, and its unit ball is the compact, centrally symmetric convex set

```math
\mathcal C=
\mathrm{conv}
\left\{s\otimes\mathbf u:
s\in\mathcal S_m,\ \|\mathbf u\|_2\le1\right\}.
```

To see the unit-ball description, write each nonzero $`\mathbf g_s`$ as its length times a unit vector; any unused total weight can be placed at the origin. Conversely, group the terms in a convex decomposition by their sign vector and use the triangle inequality. The sign vectors span $`\mathbb R^m`$, so $`\mathcal C`$ has nonempty interior.

## 2. Exact equivalence with joint measurability

The family is jointly measurable exactly when there are positive operators $`G_s`$, indexed by all $`s\in\{-1,1\}^m`$, such that

```math
\sum_sG_s=I,
\qquad
A_x=\sum_s s_xG_s.
```

This is the usual parent-measurement definition. A parent followed by stochastic responses can be refined to this form: for each parent outcome, draw a complete response string with the product of its conditional response probabilities, and group equal strings.

**Proposition 1.** The measurements are jointly measurable if and only if $`\nu(A)\le1`$.

**Proof, sufficient direction.** Suppose a primal decomposition satisfies
$`\sum_s\|\mathbf g_s\|_2\le1`$. Choose numbers $`p_s\ge\|\mathbf g_s\|_2`$ with $`\sum_s p_s=1`$. For each representative $`s\in\mathcal S_m`$, define the two parent effects

```math
G_s=\frac{p_sI+\mathbf g_s\cdot\boldsymbol\sigma}{2},
\qquad
G_{-s}=\frac{p_sI-\mathbf g_s\cdot\boldsymbol\sigma}{2}.
```

Their eigenvalues are nonnegative. They sum to the identity over all sign pairs, and

```math
\sum_{s\in\{-1,1\}^m}s_xG_s
=\sum_{s\in\mathcal S_m}s_x(G_s-G_{-s})
=\mathbf a_x\cdot\boldsymbol\sigma.
```

They therefore form a parent for the stated measurements.

**Proof, necessary direction.** Let $`\{G_s\}`$ be any parent. On Hermitian qubit operators, define

```math
J(H)=\mathrm{Tr}(H)I-H.
```

This positive, unital involution reverses the Bloch vector. It satisfies $`J(A_x)=-A_x`$ because the observables are traceless. Symmetrize the parent by setting

```math
\widetilde G_s=\frac{G_s+J(G_{-s})}{2}.
```

The new effects remain positive and sum to $`I`$. Their observables are unchanged:

```math
\sum_s s_x\widetilde G_s
=\frac{A_x-J(A_x)}2=A_x.
```

They also obey $`\widetilde G_{-s}=J(\widetilde G_s)`$. Consequently each pair has the form

```math
\widetilde G_{\pm s}
=\frac{p_sI\pm\mathbf g_s\cdot\boldsymbol\sigma}{2},
\qquad
p_s\ge\|\mathbf g_s\|_2,
\qquad
\sum_{s\in\mathcal S_m}p_s=1.
```

The unchanged observables give a primal decomposition with total norm at most one. Hence $`\nu(A)\le1`$. Only positivity of $`J`$ on a single qubit was used; no application of this map to an entangled system is required. $`\square`$

Homogeneity also gives the exact relation

```math
\nu(\eta A)=\eta\nu(A),\qquad \eta\ge0.
```

In particular, for a uniform visibility $`0\le\eta\le1`$, an incompatible family becomes jointly measurable precisely when $`\eta\nu(A)\le1`$.

## 3. Dual formula and tensor-norm attribution

Pair tuples by $`\langle A,V\rangle=\sum_x\mathbf a_x\cdot\mathbf v_x`$. The support function of $`\mathcal C`$ is

```math
h_{\mathcal C}(V)
=\max_{s\in\mathcal S_m}
\sup_{\|\mathbf u\|_2\le1}
\mathbf u\cdot\sum_xs_x\mathbf v_x
=\max_{s\in\{-1,1\}^{m}}
\left\|\sum_xs_x\mathbf v_x\right\|_2.
```

The last maximum can use the full sign cube because the norm is unchanged under $`s\mapsto-s`$. Unit-ball polarity in finite dimensions now gives

```math
\boxed{
\nu(A)=
\max_{\{\mathbf v_x\}}
\left\{
\sum_x\mathbf a_x\cdot\mathbf v_x:
\left\|\sum_xs_x\mathbf v_x\right\|_2\le1
\quad\text{for every }s\in\{-1,1\}^{m}
\right\}.}
```

For completeness, weak duality is the direct inequality

```math
\sum_x\mathbf a_x\cdot\mathbf v_x
=\sum_{s\in\mathcal S_m}
\mathbf g_s\cdot\sum_xs_x\mathbf v_x
\le\sum_{s\in\mathcal S_m}\|\mathbf g_s\|_2.
```

Equality of the two optima follows by a supporting hyperplane to $`\mathcal C`$ at $`A/\nu(A)`$ when $`A\ne0`$; the zero tuple is immediate. The dual optimum is attained. Indeed, averaging over the full sign cube gives

```math
\mathbf v_x
=2^{-m}\sum_{s\in\{-1,1\}^m}
s_x\sum_ys_y\mathbf v_y,
```

so every feasible tuple has $`\|\mathbf v_x\|_2\le1`$. Its feasible set is therefore closed and bounded.

In tensor language, this is the established identity

```math
\nu(A)=
\left\|\sum_{x=1}^{m}e_x\otimes\mathbf a_x\right\|
_{\ell_\infty^m\otimes_\pi\ell_2^3}.
```

Every primal decomposition is a projective-norm decomposition because $`\|s\|_\infty=1`$. Conversely, the unit ball of $`\ell_\infty^m`$ is the convex hull of the sign vectors, so any projective decomposition can be refined to a sign-vector decomposition without increasing its cost. This proves the identity directly. Its dual is the injective norm on $`\ell_1^m\otimes\ell_2^3`$, giving exactly the signed-sum constraint above.

In the notation of [BJN2022](../references/README.md#bjn2022), an unbiased effect is $`f_x=(I+\mathbf a_x\cdot\boldsymbol\sigma)/2`$. Their traceless tensor $`2\sum_xe_x\otimes\overline f_x`$ is therefore $`\sum_xe_x\otimes\mathbf a_x`$ in Bloch coordinates. This fixes the factor of two in transferring their compatibility result to the convention used here.

## 4. Polar alignment and the transfer matrix

Fix a feasible dual tuple $`\{\mathbf v_x\}`$, independently of the Haar state that will later be drawn, and define

```math
T=\sum_{x=1}^{m}\mathbf a_x\mathbf v_x^{\mathsf T}.
```

The identity $`\mathrm{Tr}T=\sum_x\mathbf a_x\cdot\mathbf v_x`$ relates this matrix to the dual objective.

**Proposition 2.** A common orthogonal rotation of the dual vectors produces a feasible tuple for which

```math
T\succeq0,
\qquad 0\preceq T\preceq I,
\qquad
\gamma:=\mathrm{Tr}T\ge
\sum_x\mathbf a_x\cdot\mathbf v_x^{\mathrm{old}}.
```

For an optimal initial tuple, $`\gamma=\nu(A)`$.

**Proof.** For $`R\in O(3)`$, the replacement $`\mathbf v_x\mapsto R\mathbf v_x`$ preserves all signed-sum norms and replaces $`T`$ by $`TR^{\mathsf T}`$. Take a singular-value decomposition $`T=U\Sigma V^{\mathsf T}`$ and choose $`R=UV^{\mathsf T}`$. Then

```math
TR^{\mathsf T}=U\Sigma U^{\mathsf T}\succeq0,
\qquad
\mathrm{Tr}(TR^{\mathsf T})=\|T\|_*
\ge\mathrm{Tr}T.
```

Here $`\|T\|_*`$ is the sum of singular values. Since the rotated tuple is feasible, its objective cannot exceed $`\nu(A)`$; equality therefore holds if the initial tuple was optimal. This rotation changes only mathematical witness vectors. It does not rotate or replace the physical measurement family.

For the aligned tuple and any unit vector $`\mathbf u`$,

```math
\begin{aligned}
\mathbf u^{\mathsf T}T\mathbf u
&=\sum_x(\mathbf u\cdot\mathbf a_x)
          (\mathbf u\cdot\mathbf v_x)\\
&\le\sum_x|\mathbf u\cdot\mathbf v_x|\\
&=\max_s\mathbf u\cdot\sum_xs_x\mathbf v_x
\le1.
\end{aligned}
```

The first inequality uses $`|\mathbf u\cdot\mathbf a_x|\le1`$, and the last uses dual feasibility. Thus $`T\preceq I`$. $`\square`$

Write the three eigenvalues of an optimal aligned matrix as $`\lambda_1,\lambda_2,\lambda_3`$. The properties used by the Bell proof are exactly

```math
0\le\lambda_j\le1,
\qquad
\lambda_1+\lambda_2+\lambda_3=\nu.
```

An exact optimizer is not essential for activation. Any feasible tuple with dual objective greater than one can be aligned, giving an achieved trace $`1<\gamma\le\nu`$ and the same eigenvalue bounds with sum $`\gamma`$. The [feasible-certificate version](bell-construction.md#feasible-dual-certificates) of the Bell theorem uses this achieved value directly.

## 5. Universal qubit bound and orthogonal examples

Dual feasibility also implies $`\nu\le2`$. For every unit $`\mathbf u`$,

```math
\sum_x|\mathbf u\cdot\mathbf v_x|\le1.
```

A uniform spherical average satisfies

```math
\mathbb E_{\mathbf u\in S^2}|\mathbf u\cdot\mathbf v|
=\frac12\|\mathbf v\|_2.
```

This follows by rotational invariance and the uniform distribution of the polar coordinate on $`[-1,1]`$. Averaging the preceding inequality therefore gives

```math
\sum_x\|\mathbf v_x\|_2\le2,
\qquad
\sum_x\mathbf a_x\cdot\mathbf v_x
\le\sum_x\|\mathbf v_x\|_2\le2.
```

Maximizing proves $`0\le\nu\le2`$ for every physical family in this model.

For $`k\le3`$ orthogonal axes, $`A_j=\eta_j\sigma_j`$, put $`r=(\sum_j\eta_j^2)^{1/2}`$. The dual choice $`\mathbf v_j=(\eta_j/r)e_j`$ is feasible and has objective $`r`$ when $`r>0`$. The primal choice

```math
\mathbf g_s=2^{-(k-1)}
\sum_{j=1}^{k}s_j\eta_je_j
```

has total norm $`r`$. Hence

```math
\nu=r,
\qquad
T=\mathrm{diag}(\eta_1^2/r,\ldots,\eta_k^2/r,0,\ldots,0).
```

The two-axis and three-axis thresholds are consequently $`\eta_1^2+\eta_2^2>1`$ and $`\eta_1^2+\eta_2^2+\eta_3^2>1`$, respectively. The [scaled Bell construction](bell-construction.md#main-scaled-dual-bound) reduces in these examples to the corresponding noise-weighted Pauli coefficients.

---

Continue with [Haar moments and concentration](haar-moments.md) or the [Bell construction](bell-construction.md). The [reference list](../references/README.md) records the compatibility and nonlocality literature.
