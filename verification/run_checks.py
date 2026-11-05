"""Independent finite checks; run from any working directory.

The universal statements and typicality bounds are analytical results. This
script checks exact Haar moment identities, a generic operator construction,
and a reproducible exact six-qubit Bell witness with compatible controls.
"""
import argparse
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))
from bell import PAULI, I, SIGNS, exact_pauli_witness, kron_all


def permutation_moment(matrices):
    """Haar fourth moment from its 24 permutation contractions."""
    d = len(matrices[0])
    numerator = 0
    for permutation in permutations(range(4)):
        seen, term = set(), 1
        for start in range(4):
            if start in seen:
                continue
            current, matrix = start, np.eye(d, dtype=complex)
            while current not in seen:
                seen.add(current)
                matrix = matrix @ matrices[current]
                current = permutation[current]
            trace = np.trace(matrix)
            if abs(trace.imag) > 1e-12 or abs(trace.real-round(trace.real)) > 1e-12:
                raise AssertionError("Expected integer Pauli trace")
            term *= int(round(trace.real))
        numerator += term
    return Fraction(numerator, d*(d+1)*(d+2)*(d+3))


def moment_checks():
    cases = []
    for n in (1, 2):
        words = list(product(range(4), repeat=n))[1:]
        matrices = [kron_all([PAULI[x] for x in word]) for word in words]
        d = 2**n
        for i, p in enumerate(matrices):
            actual = permutation_moment([p, p, p, p])
            expected = Fraction(3, (d+1)*(d+3))
            assert actual == expected
            for j in range(i+1, len(matrices)):
                q = matrices[j]
                commute = np.array_equal(p @ q, q @ p)
                chi = 1 if commute else -1
                actual = permutation_moment([p, p, q, q])
                expected = Fraction(d+4+2*chi, (d+1)*(d+2)*(d+3))
                assert actual == expected
                cases.append((n, chi))
    return {"distinct_pairs_checked": len(cases), "fourth_moments_checked": 18,
            "commuting_and_anticommuting": sorted(set(chi for _, chi in cases))}


def generic_operator_check():
    # Noncoplanar, nonorthogonal directions; a feasible positive dual suffices.
    a = np.array([[1, 0, 0], [0.2, 1, 0], [-0.1, 0.15, 1]], dtype=float)
    a /= np.linalg.norm(a, axis=1)[:, None]
    signed_radius = max(np.linalg.norm(s @ a) for s in SIGNS)
    v = a / signed_radius
    transfer = a.T @ v
    strength = float(np.trace(transfer))
    eigenvalues = np.linalg.eigvalsh(transfer)
    assert strength > 1 and eigenvalues.min() >= -1e-12 and eigenvalues.max() <= 1+1e-12
    observables = [I] + [sum(row[j]*PAULI[j+1] for j in range(3)) for row in a]
    duals = [I] + [sum(row[j]*PAULI[j+1] for j in range(3)) for row in v]
    rng = np.random.default_rng(20261104)
    state = rng.normal(size=4)+1j*rng.normal(size=4)
    state /= np.linalg.norm(state)
    expectation = lambda op: float(np.vdot(state, op @ state).real)
    coefficients = np.array([[expectation(np.kron(b, c)) for c in duals] for b in duals])
    physical = np.array([[expectation(np.kron(b, c)) for c in observables] for b in observables])
    direct_quantum = float(np.sum(coefficients*physical))
    pauli = np.array([expectation(np.kron(p, q)) for p in PAULI for q in PAULI])
    k = np.zeros((4, 4)); k[0, 0] = 1; k[1:, 1:] = transfer
    transferred_quantum = float(pauli @ np.kron(k, k) @ pauli)
    discrepancy = abs(direct_quantum-transferred_quantum)
    local_min = float("inf")
    for s, t in product(SIGNS, repeat=2):
        left, right = np.r_[1, s], np.r_[1, t]
        score = float(left @ coefficients @ right)
        direct = expectation(np.kron(sum(left[i]*duals[i] for i in range(4)),
                                     sum(right[i]*duals[i] for i in range(4))))
        discrepancy = max(discrepancy, abs(score-direct))
        local_min = min(local_min, score)
    assert discrepancy < 1e-12 and local_min >= -1e-12
    return {"certificate_strength": strength, "transfer_eigenvalues": eigenvalues.tolist(),
            "maximum_direct_identity_discrepancy": discrepancy,
            "minimum_deterministic_positive_dual_score": local_min,
            "scope": "Feasible dual certificate, not a numerical computation of the optimum norm."}


def finite_example():
    fixture = json.loads((ROOT / "verification/finite_state.json").read_text())
    real, imag = fixture["amplitudes_real"], fixture["amplitudes_imag"]
    rows = [exact_pauli_witness(real, imag, visibility) for visibility in [(1, 1), (9, 10), (1, 2)]]
    assert rows[0]["violation"]
    assert not rows[-1]["violation"]
    # An independently assembled dense matrix verifies an extremal local score.
    for row in rows:
        p, q = row["visibility"]
        z = np.array(real, dtype=complex) + 1j*np.array(imag, dtype=complex)
        factors = [q*I + p*sum(s[j]*PAULI[j+1] for j in range(3))
                   for s in row["maximizing_assignment"]]
        direct = np.vdot(z, kron_all(factors) @ z)
        assert abs(direct.imag) < 1e-9
        assert abs(int(round(direct.real))) == row["absolute_maximum_numerator"]
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-report", type=Path, help="Write an optional JSON report at this path")
    args = parser.parse_args()
    report = {"status": "pass", "numpy_version": np.__version__,
              "moments": moment_checks(), "generic_operator": generic_operator_check(),
              "finite_examples": finite_example(),
              "scope": "Exact finite witness and analytical identity checks; not a numerical proof of asymptotic typicality or optimality."}
    if args.write_report:
        args.write_report.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
