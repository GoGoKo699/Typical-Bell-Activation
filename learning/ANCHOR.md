# From Scarani's Bell Nonlocality to typical Bell activation

The selected educational anchor is **Valerio Scarani, _Bell Nonlocality_, first edition, Oxford University Press (2019)**. The book supplies the language of Bell behaviors, local models, quantum realizations, and multipartite locality. This page translates that language into the experiment studied here and identifies the additional arguments needed for the typical-state theorem.

**Source:** [Oxford Academic edition](https://academic.oup.com/book/36528), DOI [10.1093/oso/9780198788416.001.0001](https://doi.org/10.1093/oso/9780198788416.001.0001), print ISBN 9780198788416, online ISBN 9780191830327. The [publisher's copyright record](https://academic.oup.com/book/36528/chapter/321331146) identifies the first edition; the [edition and contents preview](https://api.pageplace.de/preview/DT0400.9780191092640_A38096857/preview-9780191092640_A38096857.pdf) provides the same printed section numbering. The Oxford online publication date is 7 August 2019. The open-access distribution is the same selected first edition.

Use the passages below alongside the [project walkthrough](walkthrough.md) and the [30-milestone map](MILESTONES.md). They are a focused route into this result, not a whole-book prerequisite. The canonical theorem and its proofs remain in [science/](../science/README.md).

<a id="selected-reading"></a>

## Selected reading

| Passage in the first edition | Purpose in this project | Project connection |
| --- | --- | --- |
| [Sections 2.1–2.4](https://academic.oup.com/book/36528/chapter/321331393), beginning on pp. 25, 27, 29, and 33 | Introduce a behavior as conditional probabilities, distinguish nonsignalling from locality, and express the local set through deterministic responses. | [M07–M09](MILESTONES.md#M07): behaviors, marginals, and the local bound. |
| [Section 3.1](https://academic.oup.com/book/36528/chapter/321331577), beginning on p. 43 | Connect a shared state and local measurements to a behavior. | [M01–M03](MILESTONES.md#M01) and [M06](MILESTONES.md#M06): qubits, measurements, and tensor-product parties. |
| [Section 5.1.1](https://academic.oup.com/book/36528/chapter/321331831), in the section beginning on p. 65 | Extend the fully local decomposition to an arbitrary number of parties. | [M10](MILESTONES.md#M10): the precise local set excluded by the theorem. |
| [Sections 5.3.1–5.3.2](https://academic.oup.com/book/36528/chapter/321331831), in the section beginning on p. 70 | Compare full locality with models that permit correlations within groups. | [M10](MILESTONES.md#M10) and [M30](MILESTONES.md#M30): ordinary versus genuine multipartite claims. |
| [Section 2.6.2](https://academic.oup.com/book/36528/chapter/321331393), within the section on pp. 40–42 | Distinguish a statement about an exact behavior from certification using finitely many observations. | [M29](MILESTONES.md#M29): evidence, confidence, power, and copy cost. |

Within the same book, [Appendix C](https://academic.oup.com/book/36528/chapter/321332881) is a useful refresher when needed: C.1.2–C.1.3 cover Bloch coordinates and partial traces; C.3.1–C.3.3 cover POVMs, binary observables, and joint measurability. These passages support [M01–M04](MILESTONES.md#M01). The exact compatibility norm used by this project is supplied by the [research sources and direct derivation](../science/compatibility-dual.md), rather than assumed from this appendix.

<a id="notation"></a>

## Notation and assumptions

The book treats general Bell scenarios. This repository specializes to one qubit at each of $`N`$ parties, two outcomes per setting, and the same finite measurement menu at every party.

| Source concept or notation | Convention in this repository |
| --- | --- |
| Bipartite probabilities $`P(a,b\mid x,y)`$ and their multipartite extension | $`p(a_1,\ldots,a_N\mid x_1,\ldots,x_N)`$, with $`a_i\in\{-1,+1\}`$ and $`x_i\in\{1,\ldots,m\}`$. |
| Input and output counts $`M_A,M_B`$ and $`m_A,m_B`$ in Chapter 2 | The lowercase $`m`$ here counts **settings**; the number of outcomes is always two. |
| Number of players $`n`$ in Chapter 5 | $`N`$ parties, total Hilbert-space dimension $`D=2^N`$. |
| A quantum state $`\rho`$ and local POVM effects | $`M_{a\mid x}=(I+aA_x)/2`$, with $`A_x=\mathbf a_x\cdot\boldsymbol\sigma`$ and $`\lVert\mathbf a_x\rVert_2\le1`$. |
| A hidden variable $`\lambda`$ and local response probabilities | A complete deterministic sign table $`s=(s_{i,x})`$ can label each vertex of the local set. The transfer eigenvalues $`\lambda_j`$ used in the proof are unrelated to hidden variables. |
| A linear inequality $`I(\mathcal P)\le I_L`$ | A correlator functional $`\mathcal B_c(E)`$ with a two-sided local bound $`\lvert\mathcal B_c(E)\rvert\le L_{\mathrm{abs}}(c)`$. |
| Bloch coordinates describing a state | The vector $`\mathbf a_x`$ here describes a **measurement observable**. The quantities $`r_P=\langle\psi\rvert P\lvert\psi\rangle`$ describe the target state. |

The recorded outcome is always $`+1`$ or $`-1`$. For an unsharp measurement, the eigenvalues of $`A_x`$ are $`\pm\|\mathbf a_x\|_2`$, which may lie strictly inside that interval. The relation $`\operatorname{Tr}(\rho A_x)=p(+1\mid x)-p(-1\mid x)`$ connects the observable to the average recorded sign. The unbiased assumption makes these probabilities equal on the maximally mixed qubit. A Bloch vector of unit length gives a sharp projective measurement.

The settings are selected independently of the source and its hidden variables. Parties do not communicate during a Bell trial, and every trial is retained. The menu is fixed independently of both the target state and $`N`$. Knowledge of the target is used to choose the coefficients before collecting test data. These restrictions, and the distinction between state preparation and measurement, are stated in [Model and results](../science/model-and-results.md).

<a id="marginals"></a>

## From probabilities to subset correlators

The book's behavior contains probabilities for every allowed input tuple. For binary outcomes, one can encode the same nonsignalling behavior using averages of products of outcomes from all subsets of parties. The two-party case makes the translation explicit:

```math
p(a,b\mid x,y)
=\frac14\left[1+aE_{x0}+bE_{0y}+abE_{xy}\right].
```

Here $`E_{xy}`$ is the average of the product $`ab`$, while $`E_{x0}`$ and $`E_{0y}`$ are the two individual averages. Summing this formula over $`b`$ leaves the marginal probability for $`a`$. Nonsignalling makes $`E_{x0}`$ independent of Bob's choice $`y`$.

In the general construction, the mathematical label $`0`$ means omission from the product. Thus $`A_0=I`$ and

```math
E_{\mathbf x}(\rho)
=\operatorname{Tr}\!\left[\rho\bigotimes_{i=1}^{N}A_{x_i}\right],
\qquad \mathbf x\in\{0,1,\ldots,m\}^{N}.
```

The all-zero correlator is one. An omitted party can still perform any permitted setting; its outcome is simply ignored in that correlator. No trial is discarded because of its outcomes, so this is marginalization rather than conditioning on a favorable outcome. The distinction is essential: the theorem uses the full behavior, whereas some earlier random-state Bell results concern only products involving every party. See the [model's marginal convention](../science/model-and-results.md#marginal-correlators) and the [full-correlation comparison](../references/README.md#drumond-oliveira2012).

<a id="absolute-bound"></a>

## Local vertices and the absolute bound

A deterministic local strategy specifies one sign for every party and every possible setting. It may assign $`+1`$ to all three Pauli questions at one site; classical local response tables are not constrained to be Bloch vectors. There are $`2^{mN}`$ such tables, and arbitrary local behaviors are their convex mixtures.

For coefficients $`c_{\mathbf x}`$, put $`s_{i,0}=1`$. The project's normalization is

```math
L_{\mathrm{abs}}(c)
=\max_s\left|\sum_{\mathbf x}c_{\mathbf x}
                          \prod_i s_{i,x_i}\right|.
```

The absolute value controls both signs of a local score. This matters for the [signed-output-flip converse](../science/party-count.md#5-a-signed-flip-converse-for-every-state), whose expansion coefficients can be negative. A one-sided bound alone does not support that argument.

The constructed functional retains $`c_{\mathbf0}=1`$. Adding a constant changes both the quantum value and this absolute local norm, so ratios must be recomputed after such a change. The precise ratio is in [Absolute local normalization](../science/model-and-results.md#absolute-local-normalization); it should not be inferred from an arbitrary affine version of a familiar inequality.

<a id="state-tailoring"></a>

## Fixed measurements and state-tailored coefficients

For each target state, the construction supplies a linear functional of the observed behavior. Its coefficients are calculated using auxiliary Hermitian operators:

```math
B_0=I,
\qquad B_x=\nu\,\mathbf v_x\cdot\boldsymbol\sigma,
\qquad
c_{\mathbf x}(\psi)
=\langle\psi|B_{x_1}\otimes\cdots\otimes B_{x_N}|\psi\rangle.
```

The vectors $`\mathbf v_x`$ form a fixed, aligned optimal dual certificate, and $`\nu`$ is the compatibility norm. The operators $`B_x`$ only generate numerical coefficients; they are not extra measurement settings and need not represent physical binary observables. The trial still uses the original $`A_x`$.

The order of choices is therefore: fix the physical menu and a dual certificate; specify the target state; compute its coefficients; then evaluate that fixed functional using Bell-test data. A different target generally gives different coefficients. The theorem says that the resulting matched state-and-functional pair has a large ratio with high probability over the Haar target. It does not assert that a single fixed inequality has that property for almost every state. See [The coefficients and their normalization](../science/bell-construction.md#the-coefficients-and-their-normalization).

Haar typicality also differs from random measurement selection. Here the state is drawn from the unitary-invariant distribution on the full $`2^N`$-dimensional pure-state space, while the physical measurement menu remains fixed. The sampling assumption and its moment consequences are developed in [Haar moments](../science/haar-moments.md).

<a id="multipartite-scope"></a>

## Ordinary and genuine multipartite nonlocality

The fully local model from Section 5.1.1 has the form

```math
p(a_1,\ldots,a_N\mid x_1,\ldots,x_N)
=\int q(d\lambda)\prod_{i=1}^{N}p_i(a_i\mid x_i,\lambda).
```

Violating a bound valid for all these models proves ordinary Bell nonlocality. Stronger multipartite notions consider larger comparison sets, for example mixtures of models allowing parties within a group to share nonlocal correlations or communicate. Scarani's Sections 5.3.1–5.3.2 explain why these are different questions.

A Bell-nonlocal pair accompanied by additional independent systems already gives an example of the logical distinction: the whole behavior fails full locality, but its nonlocal resource can be confined to a smaller group. The present theorem excludes the fully local decomposition above. Its increasing number of parties does not by itself certify genuine $`N`$-party nonlocality. See [Scope and further consequences](../science/model-and-results.md#scope-and-further-consequences).

<a id="beyond-the-anchor"></a>

## The additional steps to the project's theorem

The selected source makes the experiment and its local comparison set precise. The quantitative activation result requires the following additional steps. The milestone references connect these steps to the single settled [project map](MILESTONES.md).

| Additional argument | What it accomplishes | Authoritative source and map connection |
| --- | --- | --- |
| Exact compatibility norm and its signed-sum dual | Quantifies how far the entire finite measurement menu lies beyond joint measurability. The norm and duality are inherited research inputs. | [Compatibility dual](../science/compatibility-dual.md); [BN/BJN attribution](../references/README.md#bjn2022); [M04–M05](MILESTONES.md#M04). |
| Polar alignment of the dual transfer matrix | Produces $`0\preceq T\preceq I`$ and $`\operatorname{Tr}T=\nu`$ by changing mathematical witness vectors, while keeping the physical menu fixed. | [Transfer-matrix proof](../science/compatibility-dual.md#4-polar-alignment-and-the-transfer-matrix); [M15](MILESTONES.md#M15). |
| Two representations of the same tailored functional | Each deterministic score becomes a product-operator expectation; the quantum score becomes a nonnegative weighted sum of squared Pauli expectations. | [Bell construction](../science/bell-construction.md); [M16–M18](MILESTONES.md#M16). |
| Quantitative Haar estimates | Second and fourth moments give growth and lower concentration of the quantum score. A simultaneous upper bound controls all classical assignments on the same target. A mean alone would not establish typical violation. | [Haar moments](../science/haar-moments.md); [M19–M20](MILESTONES.md#M19). |
| Positive and scaled constructions | Positive auxiliary factors give the simpler proof. Scaling the dual improves the guaranteed exponential base and requires the bound for Hermitian factors that may be indefinite. | [Two constructions](../science/bell-construction.md#simpler-positive-dual-bound), [main theorem](../science/model-and-results.md#main-finite-party-theorem); [M21–M23](MILESTONES.md#M21). |
| Noise, finite menus, and party counts | Moving independent depolarization to the measurements and building a finite direction set yields the typical-state half-visibility threshold. The signed-flip argument supplies the fixed-ratio party converse. | [Local noise](../science/local-noise-threshold.md), [party count](../science/party-count.md); [M25–M28](MILESTONES.md#M25). |

The final constructive exponential base is $`\sqrt{(1+\nu^2)/2}>1`$ for $`\nu>1`$. The theorem supplies an explicit polynomial prefactor and an exceptional probability tending to zero; it does not claim the optimal exponent. The [six-qubit example](../science/finite-example.md) and [M24](MILESTONES.md#M24) give a separate finite illustration with exact local enumeration, not a measurement of Haar success frequency.

Qualitative activation and the existence of some nonlocal noisy output above visibility one half were established by [Plávala–Gühne–Quintino](../references/README.md#pgq2025). The all-POVM compatibility endpoint comes from [Renner](../references/README.md#renner2024) and related primary work. The repository's contribution is the typical-state construction with quantitative bounds in the stated binary unbiased model. These research attributions remain separate from Scarani's role as the educational anchor.

<a id="resources"></a>

## What the ratio says about resources

Section 2.6.2 is the source passage to revisit when passing from exact probabilities to experimental evidence. In this project, $`N`$ counts parties and qubits **per source copy**. The number of copies used to collect evidence is a different resource, denoted $`K`$. Increasing the former can amplify the Bell ratio while the latter remains expensive.

The theorem supplies neither an efficient description of a Haar state nor an efficient way to prepare it or evaluate all its coefficients. A large ratio also does not determine the range or variance of a single-trial estimator. Under the specified noisy destructive local-acquisition model, an inherited discrimination lower bound imposes exponential copy cost on certification with fixed soundness and miss-error bounds below one half. These are necessary evidence costs, not an optimal Bell-test sample law.

The high-probability analytic bound on the local score likewise needs its exceptional probability accounted for if used statistically. A certificate valid unconditionally for one particular target needs a valid bound for that instance. The full assumptions and reduction are in [Resources and interpretation](../science/resources.md), linked to [M29](MILESTONES.md#M29). The [M30 synthesis](MILESTONES.md#M30) joins these limits to the theorem's mathematical meaning.

---

Continue through the [learning overview](README.md), [walkthrough](walkthrough.md), or [milestone map](MILESTONES.md). For exact claims and proof dependencies, use the [scientific account](../science/README.md); for primary attribution, use the [research references](../references/README.md).
