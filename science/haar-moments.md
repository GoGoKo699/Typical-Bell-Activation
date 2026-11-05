# Haar moments and concentration

The [Bell construction](bell-construction.md) needs two kinds of estimates: a lower-tail bound for a weighted sum of squared Pauli expectations, and an upper-tail bound for finitely many deterministic Bell scores. This page proves both, including the constants used in [Model and results](model-and-results.md).

Throughout, $`N\ge1`$, $`D=2^N`$, $`|\psi\rangle`$ is Haar-uniform on the unit sphere of $`\mathbb C^D`$, and $`\rho=|\psi\rangle\langle\psi|`$. Write $`\langle H\rangle_\psi=\langle\psi|H|\psi\rangle`$. All logarithms are natural.

## 1. Pure-state moment identity

For every positive integer $`k`$,

```math
\mathbb E\rho^{\otimes k}
=\frac{\displaystyle\sum_{\pi\in S_k}U_\pi}
{D(D+1)\cdots(D+k-1)},
```

where $`U_\pi`$ permutes the $`k`$ tensor factors. Indeed, the average is invariant under every $`U^{\otimes k}`$ and supported on the symmetric tensor subspace. The action on that subspace is irreducible, so the average is its normalized projector. Using

```math
P_{\mathrm{sym}}=\frac1{k!}\sum_{\pi\in S_k}U_\pi,
\qquad
\dim\mathrm{Sym}^k(\mathbb C^D)
=\binom{D+k-1}{k}
```

gives the formula.

Contracting this identity with $`H_1\otimes\cdots\otimes H_k`$ expresses the moment as a sum over permutation cycles: each cycle contributes the trace of the corresponding ordered product of operators. In particular,

```math
\mathbb E\bigl[\langle H\rangle_\psi
                 \langle K\rangle_\psi\bigr]
=\frac{\mathrm{Tr}H\mathrm{Tr}K
       +\mathrm{Tr}(HK)}{D(D+1)}.
```

These identities are also valid in any fixed local Pauli frame; no frame is selected after seeing $`\psi`$.

## 2. Exact Pauli fourth moments

Let $`\mathcal P_N=\{I,X,Y,Z\}^{\otimes N}`$ be the Hermitian tensor-product Pauli basis and let $`I_N=I^{\otimes N}`$. For $`P\ne I_N`$, define the real random variable $`r_P=\langle P\rangle_\psi`$. Tracelessness and $`P^2=I_N`$ give

```math
\mathbb E r_P^2=\frac1{D+1}.
```

For one nonidentity Pauli word, the fourth moment is

```math
\boxed{\mathbb E r_P^4=\frac3{(D+1)(D+3)}.}
```

To derive it, apply the fourth-order identity to $`P,P,P,P`$. Every permutation with a fixed point vanishes because $`\mathrm{Tr}P=0`$. The three products of two transpositions contribute $`3D^2`$, and the six four-cycles contribute $`6D`$. Division by $`D(D+1)(D+2)(D+3)`$ yields the stated expression.

For two distinct nonidentity Pauli words, put $`\chi(P,Q)=1`$ if they commute and $`\chi(P,Q)=-1`$ if they anticommute. Then

```math
\boxed{
\mathbb E(r_P^2r_Q^2)
=\frac{D+4+2\chi(P,Q)}{(D+1)(D+2)(D+3)}.}
```

Here the single nonzero pairing of the two $`P`$ factors and the two $`Q`$ factors contributes $`D^2`$. Among the six four-cycles, four have trace $`D`$ and two have trace $`\mathrm{Tr}(PQPQ)=\chi(P,Q)D`$. The other pairings contain $`\mathrm{Tr}(PQ)=0`$. These are all nonzero contributions.

## 3. A weighted variance lemma

Take arbitrary nonnegative weights $`w_P`$ on the nonidentity Pauli words and suppose

```math
S=\sum_{P\ne I_N}w_P>0,
\qquad
S_2=\sum_{P\ne I_N}w_P^2.
```

Define

```math
X=\sum_{P\ne I_N}w_Pr_P^2,
\qquad
\mu=\mathbb EX=\frac S{D+1}.
```

**Lemma 1.** The relative variance satisfies

```math
\boxed{
\frac{\mathrm{Var}X}{\mu^2}
\le
\frac{2D}{(D+2)(D+3)}
+\frac{2D(D+1)}{(D+2)(D+3)}\frac{S_2}{S^2}
\le\frac2{D+2}+2\frac{S_2}{S^2}.}
```

**Proof.** The largest distinct-Pauli fourth moment occurs for $`\chi=1`$. Therefore

```math
\mathbb EX^2
\le
\frac{D+6}{(D+1)(D+2)(D+3)}(S^2-S_2)
+\frac3{(D+1)(D+3)}S_2.
```

Divide by $`\mu^2=S^2/(D+1)^2`$ and subtract one. The two coefficients reduce exactly to

```math
\frac{(D+6)(D+1)}{(D+2)(D+3)}-1
=\frac{2D}{(D+2)(D+3)}
```

and

```math
\frac{3(D+1)}{D+3}
-\frac{(D+6)(D+1)}{(D+2)(D+3)}
=\frac{2D(D+1)}{(D+2)(D+3)}.
```

Bounding these by $`2/(D+2)`$ and $`2`$, respectively, proves the second inequality. $`\square`$

Whenever $`S_2/S^2\le1/(D-1)`$, this implies

```math
\frac{\mathrm{Var}X}{\mu^2}
\le\frac2{D+2}+\frac2{D-1}
\le\frac4{D-1}.
```

Chebyshev's inequality consequently gives

```math
\boxed{
\Pr\!\left[X<\frac{\mathbb EX}{2}\right]
\le\frac{16}{D-1}.}
```

This bound may exceed one for small $`D`$; it remains a valid, then uninformative, probability bound.

## 4. The two product-weight families

Let $`0\le\lambda_j\le1`$ for $`j=1,2,3`$, with $`\sum_j\lambda_j=\nu\ge1`$. These are the eigenvalue properties proved in [Compatibility norm and aligned dual certificates](compatibility-dual.md#4-polar-alignment-and-the-transfer-matrix).

For local weights $`q_0=1`$ and $`q_j\ge0`$, assign

```math
w_P=\prod_{i=1}^{N}q_{p_i},
\qquad P=\sigma_{p_1}\otimes\cdots\otimes\sigma_{p_N}.
```

Including the identity word, the first and second weight sums factorize:

```math
W=\sum_{P\in\mathcal P_N}w_P
=\left(1+\sum_{j=1}^{3}q_j\right)^N,
\qquad
V=\sum_{P\in\mathcal P_N}w_P^2
=\left(1+\sum_{j=1}^{3}q_j^2\right)^N.
```

Since $`w_{I_N}=1`$, the nonidentity sums in Lemma 1 are $`S=W-1`$ and $`S_2=V-1`$.

### Positive dual: $`q_j=\lambda_j`$

Every product weight is at most one, so $`S_2\le S`$. Moreover,

```math
W=(1+\nu)^N\ge2^N=D.
```

It follows that

```math
\frac{S_2}{S^2}\le\frac1S\le\frac1{D-1}.
```

### Scaled dual: $`q_j=\nu\lambda_j`$

Individual weights may now exceed one. Instead use $`\sum_j\lambda_j^2\le\nu`$ and

```math
2(1+\nu^3)\le(1+\nu^2)^2,
\qquad \nu\ge1.
```

The difference between right and left sides factors as

```math
(\nu-1)(\nu^3-\nu^2+\nu+1)\ge0.
```

Consequently,

```math
W=(1+\nu^2)^N\ge D,
\qquad
V=\left(1+\nu^2\sum_j\lambda_j^2\right)^N
\le\frac{W^2}{D}.
```

For $`W\ge D>1`$,

```math
\frac{V-1}{(W-1)^2}
\le\frac{W^2/D-1}{(W-1)^2}
\le\frac1{D-1}.
```

The last inequality is equivalent to $`(W-D)^2\ge0`$. Thus the same relative-variance and lower-tail estimates apply to the scaled weights.

In either case, $`Q=1+X`$ obeys

```math
\mathbb EQ=1+\frac{W-1}{D+1}
=\frac{D+W}{D+1},
```

and, except with probability at most $`16/(D-1)`$,

```math
\boxed{
Q\ge1+\frac{W-1}{2(D+1)}
\ge\frac{W}{4D}.}
```

The first expression is the retained-constant bound. The last, simpler expression follows from $`D+1\le2D`$. All these statements remain valid if $`\nu`$ is replaced by the achieved trace $`\gamma\ge1`$ of a feasible positive transfer matrix.

## 5. Positive quadratic forms have an exponential tail

**Lemma 2.** If $`F\succeq0`$ and $`\mathrm{Tr}F=D`$, then for every $`u\ge0`$,

```math
\Pr[\langle F\rangle_\psi\ge u]\le2e^{-u/2}.
```

**Proof.** Diagonalize $`F`$ with eigenvalues $`f_j\ge0`$ and $`\sum_jf_j=D`$. For an integer $`k\ge1`$, convexity gives

```math
\left(\sum_jf_j|\psi_j|^2\right)^k
\le D^k\sum_j\frac{f_j}{D}|\psi_j|^{2k}.
```

The pure-state moment identity applied to a rank-one projector gives

```math
\mathbb E|\psi_j|^{2k}
=\frac{k!}{D(D+1)\cdots(D+k-1)}.
```

Hence

```math
\mathbb E\langle F\rangle_\psi^k
\le\frac{k!D^k}{D(D+1)\cdots(D+k-1)}
\le k!.
```

Using the nonnegative exponential series, for $`0<\theta<1`$,

```math
\mathbb E e^{\theta\langle F\rangle_\psi}
\le\sum_{k=0}^{\infty}\theta^k
=\frac1{1-\theta}.
```

Markov's inequality with $`\theta=1/2`$ proves the claim. $`\square`$

For a fixed collection of at most $`2^{mN}`$ such operators, define

```math
t_N=(m\ln2+1)N+\ln2.
```

A union bound gives the especially simple estimate

```math
\boxed{
\Pr\!\left[\max_s\langle F_s\rangle_\psi>2t_N\right]
\le 2^{mN}\,2e^{-t_N}=e^{-N}.}
```

No Gaussian normalization event is needed for this positive-operator bound.

## 6. Hermitian quadratic forms and Gaussian normalization

The scaled Bell construction has Hermitian operators that need not be positive. Let $`z\in\mathbb C^D`$ have independent standard complex Gaussian coordinates, normalized so that $`\mathbb E|z_j|^2=1`$. Then $`\psi=z/\|z\|_2`$ is Haar-uniform.

**Lemma 3.** For a Hermitian operator $`F`$ and $`t>0`$,

```math
\boxed{
\Pr\!\left[
|z^\dagger Fz-\mathrm{Tr}F|
>\sqrt{2t}\,\|F\|_{\mathrm{HS}}
+t\,\|F\|_{\mathrm{op}}
\right]\le2e^{-t}.}
```

**Proof.** Unitary invariance lets us diagonalize $`F`$. Its eigenvalues $`f_j`$ are real, and $`E_j=|z_j|^2`$ are independent mean-one exponential variables. Thus

```math
Y=z^\dagger Fz-\mathrm{Tr}F
=\sum_j f_j(E_j-1).
```

Put $`v=\sum_jf_j^2=\|F\|_{\mathrm{HS}}^2`$ and $`c=\max_j|f_j|=\|F\|_{\mathrm{op}}`$. For $`|\theta|<1/c`$,

```math
\begin{aligned}
\log\mathbb E e^{\theta Y}
&=\sum_j[-\theta f_j-\ln(1-\theta f_j)]\\
&\le\frac{\theta^2v}{2(1-|\theta|c)}.
\end{aligned}
```

The inequality follows by expanding $`-\ln(1-x)-x`$ and bounding the absolute series by $`x^2/[2(1-|x|)]`$. If $`v>0`$, choose

```math
\theta=
\frac{\sqrt{2t/v}}{1+c\sqrt{2t/v}}
```

in the Chernoff bound. Substitution gives

```math
\Pr[Y>\sqrt{2vt}+ct]\le e^{-t}.
```

Apply the same argument to $`-Y`$ and combine the tails. If $`F=0`$, the stated strict-inequality event is empty. $`\square`$

There is also a common normalization bound for all operators evaluated on this same $`z`$:

```math
\Pr[\|z\|_2^2\lt D/2]
\le e^{D/2}\mathbb E e^{-\|z\|_2^2}
=e^{-(\ln2-1/2)D}
\le e^{-D/8}.
```

If $`\mathrm{Tr}F=D`$, then on the simultaneous good events,

```math
|\langle F\rangle_\psi|
\le2\left[
1+\sqrt{2t}\frac{\|F\|_{\mathrm{HS}}}{D}
+t\frac{\|F\|_{\mathrm{op}}}{D}
\right].
```

Consequently, for a fixed collection of at most $`2^{mN}`$ Hermitian operators of trace $`D`$, the preceding inequality holds simultaneously with $`t=t_N`$ except on an event of probability at most

```math
2^{mN}\,2e^{-t_N}+e^{-D/8}
=e^{-N}+e^{-D/8}.
```

The normalization event is counted once, because the same Gaussian vector generates every score. No independence among the scores is assumed.

---

The [Bell construction](bell-construction.md) supplies the transfer-matrix weights and operator-norm bounds to which these lemmas apply. See the [model and theorem statements](model-and-results.md) and the [reference list](../references/README.md) for the surrounding measurement-incompatibility framework.
