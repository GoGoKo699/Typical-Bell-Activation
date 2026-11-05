# An exact six-qubit Bell witness

The asymptotic theorem is supported by an explicit finite illustration whose local bound can be exhaustively checked with integer arithmetic. This example uses all three sharp Pauli measurements at each of six parties. It is a particular specified pure state; no claim about a finite Haar success frequency is inferred from it.

## State and coefficients

The file [finite_state.json](../verification/finite_state.json) specifies integer arrays $`a_b,b_b`$ for $`b\in\{0,1\}^6`$. Define

```math
z_b=a_b+i b_b,\qquad
S=\sum_b |z_b|^2=954,\qquad
|\psi\rangle=S^{-1/2}\sum_b z_b|b\rangle.
```

For each six-qubit Pauli word $`P\in\{I,X,Y,Z\}^{\otimes6}`$, put

```math
n_P=z^\dagger Pz\in\mathbb Z,\qquad c_P=n_P/S.
```

The Bell functional uses coefficient $`c_P`$ on the correlator indexed by the nonidentity factors of $`P`$. In particular $`c_I=1`$. These are the scaled-dual coefficients for the sharp Pauli triple, whose compatibility norm is $`\nu=\sqrt3`$.

The quantum score is exact:

```math
Q=\sum_P \langle P\rangle_\psi^2=2^6=64.
```

The last identity is the Pauli expansion of the pure-state Hilbert–Schmidt norm.

## Exact local bound

At each site a deterministic local strategy chooses three signs. There are $`8^6=262144`$ complete assignments. For each one the Bell score is an integer divided by $`954`$. The supplied code enumerates the complete set using an integer tensor transform and obtains

```math
\min L=-\frac{14728}{477},\qquad
\max L=\frac{28808}{477}.
```

The maximum absolute local value is therefore $`28808/477`$. Hence

```math
\frac{Q}{\max |L|}=\frac{3816}{3601}
\approx1.0597056373>1.
```

The exact numerator/denominator, one maximizing assignment, and the independent direct-matrix check are in [results.json](../verification/results.json). Before each integer tensor transform, the implementation checks a sufficient bound excluding signed 64-bit overflow. Pauli expectations and rational score reductions use Python integers and exact fractions.

## Two noise controls

For rational $`\eta=p/q`$, the same code implements the coefficients

```math
c_P(\eta)=\eta^{|P|}\langle P\rangle_\psi
```

and evaluates them on the noisy Pauli observables $`\eta X,\eta Y,\eta Z`$. The quantum score has attenuation $`\eta^{2|P|}`$, whereas a deterministic local score contains $`\eta^{|P|}`$ from the coefficient alone. This distinction is important when checking normalization.

| Visibility | Exact-witness ratio, approximately | Interpretation |
|---|---:|---|
| $`1`$ | 1.059706 | The displayed functional violates its local bound. |
| $`9/10`$ | 0.642254 | This particular finite witness does not certify nonlocality. |
| $`1/2`$ | 0.220461 | A compatible control, consistent with universal locality at this visibility. |

The middle row is a statement about this witness, not a local model for the behavior. The general theorem concerns sufficiently large party number at a fixed incompatible family and does not assert that every small system or every witness violates.

## Reproduction

```bash
python verification/run_checks.py
```

This also evaluates the fourth Haar moments through all 24 permutation contractions and checks the operator identities for a noncoplanar, nonorthogonal measurement family. See the [verification guide](../verification/README.md).
