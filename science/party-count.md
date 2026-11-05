# Sufficient party counts and a fixed-ratio converse

The typical-state construction supplies an explicit sufficient number of parties. A separate signed-output-flip argument bounds the absolute Bell ratio attainable by any state with a fixed measurement menu. The converse gives a necessary party count for reaching a specified ratio above one; it does not give a lower bound on the first arbitrarily small violation.

This page uses the model of [model-and-results.md](model-and-results.md), the exact compatibility norm from [compatibility-dual.md](compatibility-dual.md), and the quantitative bounds proved in [haar-moments.md](haar-moments.md) and [bell-construction.md](bell-construction.md). All logarithms are natural unless a base is displayed.

## 1. Normalization and parameters

Every party uses the same menu of $`m`$ unbiased binary qubit observables

```math
A_x=\mathbf a_x\cdot\boldsymbol\sigma,
\qquad
\|\mathbf a_x\|\le1,
\qquad
x=1,\ldots,m.
```

Write $`\nu`$ for its compatibility norm. Joint measurability is equivalent to $`\nu\le1`$, and $`\nu\le2`$ for every such qubit menu. The activating regime is $`1<\nu\le2`$.

Let $`A_0=I`$. For a real correlator Bell functional with coefficients $`c_{x_1\ldots x_N}`$, its absolute local bound is

```math
L_{\mathrm{abs}}(c)
=\max_{s_1,\ldots,s_N\in\{\pm1\}^m}
\left|
\sum_{x_1,\ldots,x_N=0}^m
c_{x_1\ldots x_N}\prod_{i=1}^N s_{i,x_i}
\right|,
\qquad s_{i,0}=1.
```

We only form a ratio when $`L_{\mathrm{abs}}(c)>0`$. The ratio on a behavior $`p`$ is $`|\mathcal B_c(p)|/L_{\mathrm{abs}}(c)`$. Both the sufficiency theorem and the converse use this same normalization, with identity terms and subset correlators allowed. The constructive functional retains $`c_{0\ldots0}=1`$.

## 2. The finite-party sufficiency bound

Set

```math
D=2^N,
\qquad
b_\nu=\frac{1+\nu^2}{2},
\qquad
\alpha_\nu=\frac12\ln b_\nu,
\qquad
t_N=(m\ln2+1)N+\ln2.
```

For the scaled state-tailored functional of [the Bell construction](bell-construction.md), with a Haar-random input, the two estimates are

```math
Q\ge1+\frac{(1+\nu^2)^N-1}{2(D+1)}
```

and

```math
L_{\mathrm{abs}}
\le2\bigl(1+\sqrt{2t_N}+t_N\bigr)b_\nu^{N/2}.
```

They hold simultaneously except on an event of probability at most

```math
\varepsilon_N
=\frac{16}{D-1}+e^{-N}+e^{-D/8}.
```

The first estimate follows from the exact weighted Haar fourth moments. The second controls all $`2^{mN}`$ deterministic assignments at once. Its Gaussian normalization failure is a single common event, rather than a separate event for every assignment.

Since the displayed quantum lower bound is at least $`b_\nu^N/4`$, the ratio obeys

```math
R_N(\psi)
\ge
\frac{b_\nu^{N/2}}
{8\bigl(1+\sqrt{2t_N}+t_N\bigr)}.
```

Consequently, the following is an explicit sufficient condition for exceeding a target ratio $`R_\star\ge1`$ on the same event:

```math
b_\nu^{N/2}
>
8R_\star\bigl(1+\sqrt{2t_N}+t_N\bigr).
```

The original ratio bound is the appropriate finite-size estimate when numerical constants matter. The closed bound below is simpler to invert and intentionally looser.

### A sufficient integer without an implicit inequality

Define

```math
c_m=1+(m+1)\ln2,
\qquad
C_m=16c_m.
```

For $`N\ge2`$ and $`m\ge1`$, we have $`t_N\ge2+3\ln2>4`$ and $`t_N\le c_mN`$. For $`t\ge4`$, $`1+\sqrt{2t}+t\le2t`$. Thus

```math
R_N(\psi)\ge\frac{e^{\alpha_\nu N}}{C_mN}.
```

A sufficient integer is

```math
N_{\mathrm{amp}}(\nu,m,R_\star)
=\max\left\{
2,
\left\lceil
\frac{2}{\alpha_\nu}
\ln\!\left(\frac{2C_mR_\star}{\alpha_\nu}\right)
\right\rceil
\right\}.
```

For every $`N\ge N_{\mathrm{amp}}`$, the lower bound is strictly greater than $`R_\star`$. To verify the inversion, put $`y=2C_mR_\star/\alpha_\nu`$ and $`x_0=2\ln y`$. The physical range $`1<\nu\le2`$ makes $`y>e`$, and

```math
\frac{e^{x_0}}{x_0}
=\frac{y^2}{2\ln y}
>\frac y2
=\frac{C_mR_\star}{\alpha_\nu}.
```

The function $`e^x/x`$ is increasing for $`x\ge1`$. Therefore $`\alpha_\nu N\ge x_0`$ implies $`e^{\alpha_\nu N}>C_mR_\star N`$, as required. In particular, taking $`R_\star=1`$ gives a sufficient count for a strict Bell violation.

### Specifying a success probability

The amplitude condition and the failure probability are separate. Given a requested failure probability $`0<\varepsilon_{\mathrm{fail}}<1`$, it is enough to choose

```math
N\ge\max\{N_{\mathrm{amp}},N_{\mathrm{prob}}\},
\qquad
N_{\mathrm{prob}}
=\max\left\{
6,
\left\lceil\log_2\frac{34}{\varepsilon_{\mathrm{fail}}}\right\rceil
\right\}.
```

Indeed, for $`N\ge6`$,

```math
\frac{16}{2^N-1}\le32\,2^{-N},
\qquad
e^{-N}\le2^{-N},
\qquad
e^{-2^N/8}\le2^{-N},
```

so $`\varepsilon_N\le34\,2^{-N}`$. This proves the claimed success probability, with no independence assumption between the quantum-score and local-bound events.

## 3. Scaling close to joint measurability

In this section define $`\delta=\nu-1\in(0,1]`$. Then

```math
\alpha_\nu
=\frac12\ln\left(1+\delta+\frac{\delta^2}{2}\right),
\qquad
\frac\delta4\le\alpha_\nu\le\frac\delta2.
```

The lower bound follows from $`\ln(1+\delta)\ge\delta/(1+\delta)`$. The upper bound follows from $`e^\delta\ge1+\delta+\delta^2/2`$. In particular, $`\alpha_\nu=\delta/2+O(\delta^3)`$.

The explicit amplitude inversion therefore gives

```math
N_{\mathrm{amp}}
=O\!\left(
\frac1\delta
\ln\frac{(m+1)R_\star}{\delta}
\right).
```

For fixed $`m`$, fixed target ratio, and fixed success probability, this is

```math
N=O\!\left(\delta^{-1}\ln\frac1\delta\right).
```

For example, the more conservative but elementary sufficient condition

```math
N\ge
\left\lceil
\frac8\delta
\ln\!\left(\frac{8C_mR_\star}{\delta}\right)
\right\rceil
```

follows by replacing $`\alpha_\nu`$ by $`\delta/4`$ in the inversion. Increasing $`N`$ further to satisfy $`N_{\mathrm{prob}}`$ gives the desired confidence.

## 4. Explicit count for local depolarization

For this subsection define $`\delta=\eta-1/2\in(0,1/2]`$, the distance above the physical visibility boundary. The construction in [local-noise-threshold.md](local-noise-threshold.md) chooses a spherical net with radius $`\epsilon=\delta/2`$, followed by the 24 cube rotations. It supplies

```math
m\le\frac{1536}{\delta^2},
\qquad
\mu=\frac{1+2\delta}{1+\delta}>1,
\qquad
\mu-1=\frac\delta{1+\delta}.
```

The symbol $`\mu`$ is the achieved feasible dual value, not the optimum $`\nu`$. The feasible-certificate theorem gives exactly the same amplitude and probability bounds with $`\mu`$ substituted for $`\nu`$. Hence the sufficient integer $`N_{\mathrm{amp}}(\mu,m,R_\star)`$ is directly applicable.

To express a sufficient count using only the visibility gap, set

```math
C_\delta
=16\left[1+\left(1+\frac{1536}{\delta^2}\right)\ln2\right].
```

Since $`C_m\le C_\delta`$, the following is sufficient for the amplitude condition:

```math
N\ge
\left\lceil
\frac{8(1+\delta)}{\delta}
\ln\!\left(
\frac{8(1+\delta)C_\delta R_\star}{\delta}
\right)
\right\rceil.
```

Combine it with $`N\ge N_{\mathrm{prob}}`$ for a specified success probability. For fixed target ratio and confidence this proves

```math
m=O(\delta^{-2}),
\qquad
N=O\!\left(\delta^{-1}\ln\frac1\delta\right).
```

At each fixed $`\eta`$, the finite menu is chosen once and is independent of $`N`$ and the Haar input state. Only the Bell coefficients are tailored to the input. These size bounds are not claims of an efficient experiment or efficient coefficient determination.

## 5. A signed-flip converse for every state

**Proposition.** Let $`\mathsf A`$ be a menu of unbiased binary qubit observables with compatibility norm $`\nu>1`$. For every $`N`$-qubit state $`\rho`$ and every real Bell functional $`\mathcal B_c`$ in this measurement scenario,

```math
\left|\mathcal B_c(p_{\rho,\mathsf A})\right|
\le\nu^{N-1}L_{\mathrm{abs}}(c).
```

If $`\nu\le1`$, the behavior is local and the corresponding bound is simply $`L_{\mathrm{abs}}(c)`$. Equivalently, a uniform statement for all menus is

```math
\left|\mathcal B_c(p_{\rho,\mathsf A})\right|
\le\max\{1,\nu\}^{N-1}L_{\mathrm{abs}}(c).
```

### Step 1: compatible measurements at all but one party give a local behavior

By homogeneity and exactness of the compatibility norm, the menu $`A_x/\nu`$ is jointly measurable. Write its effects as

```math
C_{a|x}=\frac12\left(I+a\frac{A_x}{\nu}\right),
\qquad a\in\{\pm1\}.
```

Use this compatible menu at the first $`N-1`$ parties and leave the original menu at the last party. Let $`\{G_{s_i}\}`$ be a parent POVM for the compatible menu at party $`i`$, where $`s_i\in\{\pm1\}^m`$ records the joint outcomes. The tuple $`\mathbf s=(s_1,\ldots,s_{N-1})`$ has probability

```math
q_{\mathbf s}
=\mathrm{tr}\!\left[
\rho\left(G_{s_1}\otimes\cdots\otimes G_{s_{N-1}}\otimes I\right)
\right].
```

Conditioned on a tuple with nonzero probability, the final qubit has a valid conditional density matrix. For example, it is obtained by sandwiching $`\rho`$ with the square roots of the first $`N-1`$ parent effects and taking the partial trace. The first parties output their recorded values $`s_{i,x_i}`$, and the final party uses the Born probabilities of its conditional state. This is a fully local hidden-variable model. Denote the resulting local behavior by $`p_0`$.

### Step 2: recover each original menu by a signed outcome flip

The original effect $`M_{a|x}=(I+aA_x)/2`$ satisfies

```math
M_{a|x}
=q_+C_{a|x}+q_-C_{-a|x},
\qquad
q_+=\frac{1+\nu}{2},
\qquad
q_-=\frac{1-\nu}{2}.
```

The coefficients obey

```math
q_++q_-=1,
\qquad
|q_+|+|q_-|=\nu.
```

Let $`F_i`$ flip the binary output of party $`i`$ for every setting. Applying the effect identity independently at the first $`N-1`$ parties gives the exact affine expansion

```math
p_{\rho,\mathsf A}
=\sum_{\epsilon\in\{+,-\}^{N-1}}
\left(\prod_{i=1}^{N-1}q_{\epsilon_i}\right)
F_1^{[\epsilon_1=-]}\cdots
F_{N-1}^{[\epsilon_{N-1}=-]}p_0.
```

Each flipped behavior is local, because output relabeling preserves locality. The absolute sum of the expansion coefficients is $`\nu^{N-1}`$. Applying any linear Bell functional and the triangle inequality proves

```math
\left|\mathcal B_c(p_{\rho,\mathsf A})\right|
\le
\sum_\epsilon
\left|\prod_iq_{\epsilon_i}\right|
L_{\mathrm{abs}}(c)
=\nu^{N-1}L_{\mathrm{abs}}(c).
```

The expansion coefficients sum to one, so this proof includes the identity coefficient as well as all subset correlators. The absolute local bound controls both signs of every local score, which is essential when $`q_-<0`$.

## 6. What the converse says about party count

Suppose a ratio at least $`R_\star>1`$ is required. The all-state bound implies the necessary condition

```math
N\ge
1+\left\lceil\frac{\ln R_\star}{\ln\nu}\right\rceil.
```

For a fixed target ratio and $`\delta=\nu-1\downarrow0`$, this is $`\Omega(\delta^{-1})`$. Together with the sufficient typical-state bound, the established comparison is

| Task | Proven party-count statement |
| --- | --- |
| Reach a fixed absolute ratio $`R_\star>1`$, with any state and the given menu | Necessary: $`N\ge1+\lceil\ln R_\star/\ln\nu\rceil`$ |
| Reach the same fixed ratio on Haar-typical states, at fixed menu size | Sufficient: $`N=O((\nu-1)^{-1}\ln(1/(\nu-1)))`$ |
| Obtain any strict violation, however small | The construction gives a sufficient count; this converse gives no diverging lower count |

The final distinction follows directly from the inequality. For every $`\nu>1`$ and $`N\ge2`$, its upper bound $`\nu^{N-1}`$ already exceeds one. If a violation is allowed to approach one as $`\nu\downarrow1`$, the fixed-ratio lower bound need not diverge. The logarithmic gap between the necessary and sufficient estimates above concerns fixed amplification, and is not a proved scaling law for the first violation.

### Consequence for the binary projective noise construction

For projective measurements after local depolarization,

```math
\nu(\eta\mathsf P)=\eta\nu(\mathsf P)\le2\eta.
```

Thus every state and every finite binary projective menu in this noise model obey

```math
R\le(2\eta)^{N-1}\qquad(\eta>1/2).
```

For a fixed target ratio, a necessary condition is

```math
N\ge
1+\left\lceil\frac{\ln R_\star}{\ln(2\eta)}\right\rceil
=\Omega\!\left((\eta-1/2)^{-1}\right).
```

This is a fixed-ratio converse for the specified binary-measurement setting. The all-POVM locality statement at $`\eta\le1/2`$ is the separate endpoint result proved in [local-noise-threshold.md](local-noise-threshold.md).
