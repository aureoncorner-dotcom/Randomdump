from __future__ import annotations

import unittest

from prime_axis_engine.number_theory import (
    MAX_DIVISOR_INPUT,
    MAX_PRIME_INPUT,
    divisor_count,
    is_prime,
)


class IsPrimeTests(unittest.TestCase):
    def test_known_values(self) -> None:
        for value in (-17, -1, 0, 1, 4, 9, 25, 121):
            with self.subTest(value=value):
                self.assertFalse(is_prime(value))
        for value in (2, 3, 5, 17, 97, 113):
            with self.subTest(value=value):
                self.assertTrue(is_prime(value))

    def test_rejects_bool_and_non_integer(self) -> None:
        for value in (True, 3.0, "3", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    is_prime(value)  # type: ignore[arg-type]

    def test_deterministic_64_bit_primality_and_declared_cap(self) -> None:
        self.assertTrue(is_prime((1 << 61) - 1))
        self.assertFalse(is_prime(341_550_071_728_321))
        with self.assertRaisesRegex(ValueError, str(MAX_PRIME_INPUT)):
            is_prime(MAX_PRIME_INPUT + 1)


class DivisorCountTests(unittest.TestCase):
    def test_counts_positive_divisors(self) -> None:
        expected = {1: 1, 2: 2, 12: 6, 36: 9, 97: 2, 360: 24}
        for value, count in expected.items():
            with self.subTest(value=value):
                self.assertEqual(divisor_count(value), count)

    def test_rejects_non_positive_integer(self) -> None:
        for value in (0, -1, -100):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    divisor_count(value)

    def test_rejects_bool_and_non_integer(self) -> None:
        for value in (False, 12.0, "12", None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    divisor_count(value)  # type: ignore[arg-type]

    def test_declared_factorization_cap(self) -> None:
        with self.assertRaisesRegex(ValueError, str(MAX_DIVISOR_INPUT)):
            divisor_count(MAX_DIVISOR_INPUT + 1)


if __name__ == "__main__":
    unittest.main()
