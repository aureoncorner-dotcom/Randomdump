"""Validated, cached number-theory primitives used by the route engine."""

from __future__ import annotations

from functools import lru_cache
from typing import Any


MAX_PRIME_INPUT = (1 << 64) - 1
MAX_DIVISOR_INPUT = 1_000_000_000_000


def _require_integer(value: Any, *, name: str) -> int:
    """Return *value* as an exact integer, rejecting bool and coercion."""

    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer, not {type(value).__name__}")
    return value


@lru_cache(maxsize=65_536)
def _is_prime_cached(n: int) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for prime in small_primes:
        if n == prime:
            return True
        if n % prime == 0:
            return False

    # Deterministic Miller-Rabin for all unsigned 64-bit integers. These bases
    # are sufficient on exactly this declared domain.
    odd_part = n - 1
    powers_of_two = 0
    while odd_part % 2 == 0:
        powers_of_two += 1
        odd_part //= 2
    for base in (2, 325, 9_375, 28_178, 450_775, 9_780_504, 1_795_265_022):
        if base % n == 0:
            continue
        witness = pow(base, odd_part, n)
        if witness in (1, n - 1):
            continue
        for _ in range(powers_of_two - 1):
            witness = pow(witness, 2, n)
            if witness == n - 1:
                break
        else:
            return False
    return True


def is_prime(n: int, /) -> bool:
    """Return whether *n* is prime.

    Negative integers, zero, and one are valid inputs and are not prime.
    Values are never coerced: booleans and non-integers raise ``TypeError``.
    Results are cached behind the validated public boundary. The supported
    exact domain is the unsigned 64-bit range; larger positive values raise
    ``ValueError`` instead of starting an unbounded trial-division search.
    """

    value = _require_integer(n, name="n")
    if value > MAX_PRIME_INPUT:
        raise ValueError(f"n must be <= {MAX_PRIME_INPUT}")
    return _is_prime_cached(value)


@lru_cache(maxsize=65_536)
def _divisor_count_cached(n: int) -> int:
    if n == 1:
        return 1

    remaining = n
    total = 1

    exponent = 0
    while remaining % 2 == 0:
        remaining //= 2
        exponent += 1
    if exponent:
        total *= exponent + 1

    factor = 3
    while factor * factor <= remaining:
        exponent = 0
        while remaining % factor == 0:
            remaining //= factor
            exponent += 1
        if exponent:
            total *= exponent + 1
        factor += 2

    if remaining > 1:
        total *= 2
    return total


def divisor_count(n: int, /) -> int:
    """Return the number of positive divisors of positive integer *n*.

    ``ValueError`` is raised for zero or negative integers. Values are never
    coerced, and validated results are cached.
    """

    value = _require_integer(n, name="n")
    if value < 1:
        raise ValueError("n must be a positive integer")
    if value > MAX_DIVISOR_INPUT:
        raise ValueError(f"n must be <= {MAX_DIVISOR_INPUT}")
    return _divisor_count_cached(value)


__all__ = [
    "MAX_DIVISOR_INPUT",
    "MAX_PRIME_INPUT",
    "divisor_count",
    "is_prime",
]
