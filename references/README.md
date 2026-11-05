# References and relation to earlier work

This project studies a fixed finite family of unbiased binary qubit measurements, used at every party of a growing Bell experiment. The measurement alphabet is fixed independently of the Haar-random target state; the Bell coefficients may depend on that state. The Bell expression uses correlators of all subset sizes, including marginals. Ratios are normalized by the maximum **absolute** deterministic local score.

The contribution is a quantitative conversion from measurement incompatibility to Haar-typical, exponentially growing Bell violations. Its local-depolarization corollary makes the already-known existential visibility threshold of one half a typical-state threshold. Qualitative activation, the existential threshold itself, compatibility norms, tomography-derived Bell inequalities, and concentration of product-state overlaps are established results credited below.

Bibliographic records are provided in [references.bib](references.bib). The explicit anchors and citation keys on this page are stable targets for the mathematical notes.

## Educational anchor

The learning route uses Valerio Scarani, **Bell Nonlocality**, first edition (Oxford University Press, 2019), DOI [10.1093/oso/9780198788416.001.0001](https://doi.org/10.1093/oso/9780198788416.001.0001). The [source-to-project bridge](../learning/ANCHOR.md) identifies the selected passages and their role. This educational source is distinct from the primary research ingredients and comparisons below; its structured citation key is `scarani2019`.

## Closest comparisons

| Earlier result | Relation to this project |
| --- | --- |
| Plávala–Gühne–Quintino: every incompatible finite qubit POVM family gives Bell nonlocality for some number of parties and some state; the ultimate local-depolarization visibility is already $`1/2`$. [1](#pgq2025) | The present result identifies a typical class of states, explicit state-dependent coefficients, exponential ratios, and a sufficient party count. Its measurement scope is narrower: unbiased binary qubit families. It does not replace the arbitrary-POVM existence theorem. |
| Bluhm–Jenčová–Nechita and Bluhm–Nechita: compatibility norms, their tensor descriptions, and dual witnesses. Grinko–Uola: a complementary exact finite-qubit characterization using Fourier analysis and second-order cone programming. [2](#bjn2022), [3](#bn2022), [4](#grinko-uola2025) | The compatibility criterion and its dual optimization are inherited inputs. The new step is their quantitative conversion into a Bell witness for a typical many-qubit state. |
| Loulidi–Nechita: tensor-norm comparison between incompatibility and fixed bipartite correlation games. [5](#ln2022) | The present setting tensors a fixed measurement family over an increasing number of qubit parties and allows subset correlators. Its conclusion concerns Haar-typical multipartite states. |
| Renner; Zhang–Chitambar: the visibility-one-half boundary for general noisy qubit measurements and the associated steering problem. [6](#renner2024), [7](#zhang-chitambar2024) | Compatibility supplies the all-state local side of the depolarization threshold. This endpoint is prior work. |
| Cieśliński et al.: Bell inequalities tailored to fixed Pauli tomography, including numerical studies of Haar four-qubit states. [8](#cieslinski2026) | State-dependent Bell coefficients from fixed measurements are prior. The present construction adds an analytic guarantee for every incompatible unbiased binary qubit family, an asymptotic typicality bound, and independent-local-noise robustness. |
| Drumond–Oliveira: typical small violations for two-setting, full-correlation Bell inequalities. [9](#drumond-oliveira2012) | The present witness includes marginals and other proper-subset correlators. The older theorem does not exclude exponential violations for these full behaviors, even when there are only two settings. |
| Drumond–Duarte–Oliveira: general Bell inequalities with bounded coefficients and dimension-dependent random-state bounds. [10](#drumond-duarte-oliveira2018) | Their many-party suppression condition requires local dimension $`d>mv(2m-1)^2`$, where $`m`$ is the number of settings and $`v`$ the number of outcomes. It does not apply to the qubit limit used here. |
| Gross–Flammia–Eisert: Haar states have small maximum overlap with product states. [11](#gross-flammia-eisert2009) | This established geometric-entanglement estimate provides an alternative classical-bound estimate for the positive-dual construction. It is not a new concentration theorem of this project. |
| de Rosier et al.; Barasiński et al.: numerical prevalence of nonlocality for small random multipartite states and multisetting tests. [12](#derosier2017), [13](#barasinski2021) | Qualitative numerical genericity is established. The present claim is an analytic many-party theorem at fixed local noise, with the exact asymptotic compatibility boundary. |

### Noise and quantifier distinctions

The local channel is

```math
\Delta_\eta(\rho)=\eta\rho+(1-\eta)I/2.
```

Independent noise means $`\Delta_\eta^{\otimes N}`$. It differs from global white-noise admixture $`v\rho+(1-v)I/2^N`$, used in several of the numerical comparisons. The value $`\eta`$ here is a visibility, not a Pauli-error probability.

The typicality statement fixes the physical measurement family first and then assigns a suitable Bell functional to each target state. It does not assert that one state-independent Bell functional works for almost all Haar states. The conclusion is ordinary Bell nonlocality; it does not establish genuine multipartite nonlocality. Large Bell ratios also do not establish efficient state preparation, coefficient computation, or statistical certification.

## Related repository results

These comparisons refer to the pinned scientific documents below. They describe different mathematical tasks, even where the same measurement geometry or local noise appears.

| Pinned project | Established result and boundary of the comparison |
| --- | --- |
| [Planar-GHZ-Bell-Amplification](#planar-ghz) | For finite coplanar unbiased binary qubit families, the project identifies the exact optimal asymptotic **full-correlation** rate using GHZ states and the planar compatibility geometry. Typical-Bell-Activation adds Haar typicality, noncoplanar families, and subset correlators. It does not improve the established planar optimal-rate result. |
| [Noisy-Local-Certification](#noisy-local) | Known-target discrimination under noisy local acquisition can require exponentially many copies. This is relevant to the resources needed to obtain statistical Bell evidence. Constructing a large Bell ratio is a different task and supplies no new sample-complexity theorem by itself. |

## Primary references

<a id="pgq2025"></a>

### [1] `pgq2025`

Martin Plávala, Otfried Gühne, and Marco Túlio Quintino, **All Incompatible Measurements on Qubits Lead to Multiparticle Bell Nonlocality**, *Physical Review Letters* **134**, 200201 (2025). [DOI](https://doi.org/10.1103/PhysRevLett.134.200201) · [Author version, v4](https://arxiv.org/html/2403.10564v4).

Relevant passages: Theorem 3 gives qualitative activation; Corollaries 6–7 give the limiting visibility and local-depolarization existence result. The discussion asks for identifiable state families and bounds on the number of parties. The existential half-visibility threshold is credited to this work.

<a id="bjn2022"></a>

### [2] `bjn2022`

Andreas Bluhm, Anna Jenčová, and Ion Nechita, **Incompatibility in General Probabilistic Theories, Generalized Spectrahedra, and Tensor Norms**, *Communications in Mathematical Physics* **393**, 1125–1198 (2022). [DOI](https://doi.org/10.1007/s00220-022-04379-w) · [Author version, v3](https://arxiv.org/abs/2011.06497v3).

Relevant passages: Proposition 10.1, Corollary 10.2, and Lemma 10.4 in the author version give the centrally symmetric compatibility norm and its dual. Unbiased binary qubit measurements specialize this framework to the Euclidean Bloch ball. The projective-norm formulation and compatibility equivalence are inherited.

<a id="bn2022"></a>

### [3] `bn2022`

Andreas Bluhm and Ion Nechita, **A tensor norm approach to quantum compatibility**, *Journal of Mathematical Physics* **63**, 062201 (2022). [DOI](https://doi.org/10.1063/5.0089770) · [Author version](https://arxiv.org/abs/2202.13993).

Relevant passages: Theorem 3.4 and Proposition 4.1 provide the compatibility-norm and dual-witness formulations. The Euclidean sign constraint used in this project is a traceless-qubit specialization, not a new general incompatibility criterion.

<a id="grinko-uola2025"></a>

### [4] `grinko-uola2025`

Dmitry Grinko and Roope Uola, **Compatibility of Binary Qubit Measurements**, *Physical Review Letters* **135**, 200201 (2025). [DOI](https://doi.org/10.1103/vv1h-5mf9) · [Author version](https://arxiv.org/abs/2407.07711).

The author version is titled *On compatibility of binary qubit measurements*. Its Theorems 1–2 and equation (16) give an exact finite-family characterization for unbiased measurements and a second-order cone formulation. This is a complementary source for the measurement-compatibility input; it does not state the growing-party Haar Bell theorem considered here.

<a id="ln2022"></a>

### [5] `ln2022`

Faedi Loulidi and Ion Nechita, **Measurement Incompatibility versus Bell Nonlocality: An Approach via Tensor Norms**, *PRX Quantum* **3**, 040325 (2022). [DOI](https://doi.org/10.1103/PRXQuantum.3.040325) · [Author version](https://arxiv.org/abs/2205.12668).

Relevant passages: Theorems VII.3, VIII.1, and VIII.2 develop norm comparisons for fixed bipartite correlation games. This establishes the earlier use of tensor norms to relate incompatibility and Bell nonlocality.

<a id="renner2024"></a>

### [6] `renner2024`

Martin J. Renner, **Compatibility of Generalized Noisy Qubit Measurements**, *Physical Review Letters* **132**, 250202 (2024). [DOI](https://doi.org/10.1103/PhysRevLett.132.250202) · [Author version, v2](https://arxiv.org/abs/2309.12290v2).

The universal joint-measurability result at visibility $`1/2`$ applies to all qubit POVMs. Applied to the Heisenberg-picture images of local measurements, it provides the all-state Bell-local converse for independent depolarization at or below one half. The linked author revision is dated 2026; the journal result was published in 2024.

<a id="zhang-chitambar2024"></a>

### [7] `zhang-chitambar2024`

Yujie Zhang and Eric Chitambar, **Exact Steering Bound for Two-Qubit Werner States**, *Physical Review Letters* **132**, 250201 (2024). [DOI](https://doi.org/10.1103/PhysRevLett.132.250201) · [Author version](https://arxiv.org/abs/2309.09960).

This parallel resolution of the general-measurement Werner steering boundary is relevant through the connection between steering and joint measurability. The operational task in that paper is steering, not the typical-state Bell activation theorem of this project.

<a id="cieslinski2026"></a>

### [8] `cieslinski2026`

Paweł Cieśliński, Lukas Knips, Harald Weinfurter, and Wiesław Laskowski, **No-cost Bell nonlocality certification from quantum tomography and its applications in quantum-magic-resource witnessing**, *Physical Review A* **113**, 052404 (2026). [DOI](https://doi.org/10.1103/1nkl-sphd) · [Author version, v2](https://arxiv.org/html/2512.25068v2).

Equation (4) gives a linear-programming construction from fixed Pauli tomography. Section III.4 studies 100,000 Haar four-qubit states. This is direct prior work for state-tailored Bell inequalities with Pauli data and marginal terms. The present theorem supplies an analytic asymptotic guarantee for general unbiased binary qubit families and independent local depolarization.

<a id="drumond-oliveira2012"></a>

### [9] `drumond-oliveira2012`

R. C. Drumond and R. I. Oliveira, **Small violations of full-correlation Bell inequalities for multipartite pure random states**, *Physical Review A* **86**, 012117 (2012). [DOI](https://doi.org/10.1103/PhysRevA.86.012117) · [Author version](https://arxiv.org/abs/1209.1755).

The theorem concerns two dichotomic settings per party and full correlations. It bounds typical violation growth and discusses suppression under local noise. Proper-subset correlators are outside that theorem's test class and are part of the construction here.

<a id="drumond-duarte-oliveira2018"></a>

### [10] `drumond-duarte-oliveira2018`

Raphael C. Drumond, Cristhiano Duarte, and Roberto I. Oliveira, **Small violations of Bell inequalities for multipartite pure random states**, *Journal of Mathematical Physics* **59**, 052202 (2018). [DOI](https://doi.org/10.1063/1.5026690) · [Author version, v2](https://arxiv.org/abs/1801.07523v2).

Relevant passages: Theorem 1, equation (30), and Corollary 2 in the author version. The fixed-setting many-party suppression condition $`d>mv(2m-1)^2`$ excludes local dimension two. The separate limit of fixed party number and growing local dimension is also distinct. The journal author order is used here; the arXiv metadata lists Duarte first.

<a id="gross-flammia-eisert2009"></a>

### [11] `gross-flammia-eisert2009`

David Gross, Steven T. Flammia, and Jens Eisert, **Most Quantum States Are Too Entangled To Be Useful As Computational Resources**, *Physical Review Letters* **102**, 190501 (2009). [DOI](https://doi.org/10.1103/PhysRevLett.102.190501) · [Author version, v3](https://arxiv.org/abs/0810.4331v3).

Theorem 2 bounds the geometric entanglement of Haar $`N`$-qubit states. For $`N\ge11`$, the maximum squared product-state overlap is at most $`8N^2/2^N`$, except on an event of probability at most $`e^{-N^2}`$. Positive trace-two local score factors turn this known estimate into an alternative classical bound independent of the number of measurement settings.

<a id="derosier2017"></a>

### [12] `derosier2017`

Anna de Rosier, Jacek Gruca, Fernando Parisio, Tamás Vértesi, and Wiesław Laskowski, **Multipartite nonlocality and random measurements**, *Physical Review A* **96**, 012101 (2017). [DOI](https://doi.org/10.1103/PhysRevA.96.012101) · [Author version](https://arxiv.org/abs/1704.00346).

The numerical linear-programming study examines small multipartite systems and the probability that random measurements reveal nonlocality. It provides earlier evidence of generic nonlocality, without the asymptotic fixed-local-noise theorem established here.

<a id="barasinski2021"></a>

### [13] `barasinski2021`

Artur Barasiński, Antonín Černoch, Wiesław Laskowski, Karel Lemr, Tamás Vértesi, and Jan Soubusta, **Experimentally friendly approach towards nonlocal correlations in multisetting $`N`$-partite Bell scenarios**, *Quantum* **5**, 430 (2021). [DOI and open article](https://doi.org/10.22331/q-2021-04-14-430) · [Author version](https://arxiv.org/abs/2009.11691).

The paper studies accessible families of Bell tests, including lifted CHSH inequalities, numerical typicality, and noise robustness. Its global white-noise visibility is different from the independent local depolarization parameter of this project.

## Pinned repository references

<a id="planar-ghz"></a>

### [14] `planar-ghz`

**Planar-GHZ-Bell-Amplification**, GoGoKo699, revision `3df38e1e0c0ef4f6f872996877e5a91ef0f26911`.

- [Theorem](https://github.com/GoGoKo699/Planar-GHZ-Bell-Amplification/blob/3df38e1e0c0ef4f6f872996877e5a91ef0f26911/docs/THEOREM.md)
- [Model and claims](https://github.com/GoGoKo699/Planar-GHZ-Bell-Amplification/blob/3df38e1e0c0ef4f6f872996877e5a91ef0f26911/research/MODEL_AND_CLAIMS.md)
- [Overview](https://github.com/GoGoKo699/Planar-GHZ-Bell-Amplification/blob/3df38e1e0c0ef4f6f872996877e5a91ef0f26911/README.md)

<a id="noisy-local"></a>

### [15] `noisy-local`

**Noisy-Local-Certification**, GoGoKo699, revision `acb50259a26db221f08820480ee3b044cd8e9c0a`.

- [Model and results](https://github.com/GoGoKo699/Noisy-Local-Certification/blob/acb50259a26db221f08820480ee3b044cd8e9c0a/science/model-and-results.md)
- [Overview](https://github.com/GoGoKo699/Noisy-Local-Certification/blob/acb50259a26db221f08820480ee3b044cd8e9c0a/README.md)

The repository links preserve the versions used for these scientific comparisons. They are research records, not substitutes for the primary literature above.
