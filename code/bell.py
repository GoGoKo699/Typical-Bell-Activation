"""Finite Bell witnesses for the mathematical model in science/.

Exact integer Pauli expectations and deterministic local enumeration are used
for the supplied finite example. Haar asymptotics are proved analytically.
"""
from itertools import product
from fractions import Fraction
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULI = (I, X, Y, Z)
SIGNS = np.array(list(product((-1, 1), repeat=3)), dtype=np.int64)
LOCAL_TRANSFORM = np.column_stack((np.ones(8, dtype=np.int64), SIGNS))


def kron_all(matrices):
    out = np.ones((1, 1), dtype=complex)
    for matrix in matrices:
        out = np.kron(out, matrix)
    return out


def pauli_integer_numerators(real, imag):
    """Return z* P z for every Pauli word, using only Python integers."""
    real, imag = tuple(map(int, real)), tuple(map(int, imag))
    d = len(real)
    if len(imag) != d or d == 0 or d & (d - 1):
        raise ValueError("The two amplitude arrays must have power-of-two length")
    n = d.bit_length() - 1
    norm = sum(a*a + b*b for a, b in zip(real, imag))
    if norm == 0:
        raise ValueError("Zero state")
    values = []
    for word in product(range(4), repeat=n):
        flip = phase = number_y = 0
        for site, p in enumerate(word):
            bit = 1 << (n - 1 - site)
            if p in (1, 2):
                flip |= bit
            if p in (2, 3):
                phase |= bit
            number_y += p == 2
        sr = si = 0
        for b in range(d):
            a = b ^ flip
            rr = real[a]*real[b] + imag[a]*imag[b]
            ii = real[a]*imag[b] - imag[a]*real[b]
            rr, ii = ((rr, ii), (-ii, rr), (-rr, -ii), (ii, -rr))[number_y % 4]
            sign = -1 if (b & phase).bit_count() % 2 else 1
            sr += sign*rr
            si += sign*ii
        if si:
            raise ArithmeticError("A Hermitian Pauli expectation was not real")
        values.append(sr)
    if max(map(abs, values)) > np.iinfo(np.int64).max:
        raise OverflowError("Integer coefficient exceeds int64 storage")
    return np.array(values, dtype=np.int64).reshape((4,)*n), norm


def tensor_transform(tensor, matrix):
    """Apply one linear coefficient transform on each site."""
    result = tensor
    for axis in range(tensor.ndim):
        result = np.moveaxis(np.tensordot(matrix, result, axes=(1, axis)), 0, axis)
    return result


def exact_pauli_witness(real, imag, visibility=(1, 1)):
    """Exact ratio for c_P=eta**|P| <P>, all three noisy Pauli settings.

    All local deterministic scores are enumerated. Integer overflow is checked
    before the tensor transform. The quantum score and ratio use Fraction.
    """
    p, q = map(int, visibility)
    if not 0 <= p <= q or q <= 0:
        raise ValueError("Require rational visibility in [0,1]")
    numerators, norm = pauli_integer_numerators(real, imag)
    n, d = numerators.ndim, len(real)
    flat = list(map(int, numerators.flat))
    if sum(x*x for x in flat) != d*norm*norm:
        raise ArithmeticError("Exact Pauli purity identity failed")
    weighted, quantum_numerator = [], 0
    for word, value in zip(product(range(4), repeat=n), flat):
        weight = sum(x != 0 for x in word)
        factor = p**weight * q**(n-weight)
        weighted.append(factor*value)
        quantum_numerator += factor*factor*value*value
    if sum(map(abs, weighted)) > np.iinfo(np.int64).max:
        raise OverflowError("Local enumeration might overflow int64")
    local = tensor_transform(np.array(weighted, dtype=np.int64).reshape((4,)*n), LOCAL_TRANSFORM)
    lo, hi = int(local.min()), int(local.max())
    local_absolute = max(abs(lo), abs(hi))
    scale = q**n * norm
    quantum = Fraction(quantum_numerator, scale*scale)
    bound = Fraction(local_absolute, scale)
    ratio = quantum/bound
    maximum_index = tuple(map(int, np.unravel_index(np.argmax(np.abs(local)), local.shape)))
    return {
        "parties": n, "settings_per_party": 3, "visibility": [p, q],
        "state_norm_squared": norm, "deterministic_assignments": 8**n,
        "local_min": str(Fraction(lo, scale)), "local_max": str(Fraction(hi, scale)),
        "absolute_local_bound": str(bound), "quantum_value": str(quantum),
        "ratio": str(ratio), "ratio_decimal": float(ratio),
        "violation": ratio > 1,
        "maximizing_assignment": [SIGNS[i].tolist() for i in maximum_index],
        "absolute_maximum_numerator": local_absolute,
        "normalization_denominator": scale,
    }
