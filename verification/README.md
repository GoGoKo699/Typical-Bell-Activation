# Verification and reproduction

The arbitrary-party activation theorem, typicality probability and depolarization threshold are analytical statements proved in [science/](../science/README.md). The code checks their finite algebraic ingredients and supplies an exact finite Bell-violation example.

## Run

Install the pinned numerical dependency and run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

The command prints a JSON report and does not overwrite the stored reference output. To write a separate report, use:

```bash
python verification/run_checks.py --write-report /tmp/typical-bell-checks.json
```

The stored [results.json](results.json) was generated with NumPy 2.3.5. Integer amplitudes in [finite_state.json](finite_state.json) are the authoritative finite-example input; rerunning a random-state generator is unnecessary.

## What is checked

| Check | Independent comparison | Expected result |
|---|---|---|
| Haar moments | Sum all 24 fourth-moment permutation contractions for one- and two-qubit Pauli operators. | 18 repeated-operator fourth moments and 108 distinct pairs agree exactly with the formulas, including both commutation signs. |
| General dual construction | Assemble a noncoplanar, nonorthogonal measurement family and compare coefficient, transfer-matrix and direct tensor-operator evaluations. | Positive dual transfer eigenvalues below one; certificate strength about 1.616; discrepancy below $`10^{-12}`$. |
| Finite Bell witness | Compute Pauli expectations from integer amplitudes, enumerate every deterministic assignment using integer tensor transforms, and use exact rational score reductions. | Six-qubit ratio $`3816/3601>1`$. |
| Extremal deterministic score | Assemble the corresponding dense tensor operator independently. | Agreement with the exact extremal numerator. |
| Noise controls | Keep separate the noise in the coefficients and in physical correlators. | This witness gives no violation at $`\eta=9/10`$ or at the compatible control $`\eta=1/2`$. |

The pure-state Pauli identity $`\sum_P n_P^2=2^N S^2`$ is checked using integers. An explicit bound is tested before every local tensor transform to exclude integer overflow. The decimal values in the generic operator check are floating-point consistency checks; the finite witness ratio is an exact fraction.

## Files and limits

- [bell.py](../code/bell.py) implements Pauli-word integer expectations and exact deterministic enumeration.
- [run_checks.py](run_checks.py) contains the independent Haar-permutation and dense-matrix comparisons.
- [finite_state.json](finite_state.json) defines one specified pure state. Its integer amplitudes are not an exact Haar draw.
- [results.json](results.json) records the observed output and its scope.

Exhaustive local enumeration is used only for the six-qubit example. The general theorem uses analytical concentration bounds and does not rely on extrapolating this finite check. A witness returning a ratio below one does not establish locality of the whole behavior. No numerical claim of an optimal finite-party threshold, optimal exponent or Haar success frequency is made.

## Hosted mathematical display

The read-only **Hosted mathematics** workflow checks the exact proposed commit on GitHub at widths of 1440 and 760 pixels. It inventories all tracked Markdown pages, compiles their formulas to reference MathML, and compares that structure with the actual hosted expressions. It also checks expression counts, source identities, relations, labels, and display geometry, and saves a report, page HTML, and screenshots as an Actions artifact.

The collector is [capture_hosted_math.cjs](hosted/capture_hosted_math.cjs), with [check_rendered_math.py](hosted/check_rendered_math.py). Local reproduction needs Node.js 18 or newer, Python 3.10 or newer, Git, Playwright 1.56.1, MathJax 3.2.1, and a permitted browser connection to the public GitHub pages. From a checkout containing the desired commit, use an absolute dependency directory outside the repository:

```bash
npm install --prefix /tmp/typical-bell-browser playwright@1.56.1 mathjax-full@3.2.1
/tmp/typical-bell-browser/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/typical-bell-browser/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Typical-Bell-Activation \
  --revision "$(git rev-parse HEAD)" \
  --output /tmp/typical-bell-hosted-capture
```

The output directory must be empty. Each new attempt should retain its own report, including failures. Automated structural checks complement visual inspection of the screenshots and source; they do not establish scientific correctness or guarantee every browser's future rendering. The workflow uses a read-only repository token and does not update source files.
