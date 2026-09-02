"""Pure geometry primitives for the Prime Axis simulation.

All phases are measured in *cycles*, with one full turn equal to ``1.0``.  The
model declares the cyclic quotient of order ``q`` by the equivalence relation

``x ~ y  iff  x - y = k/q (mod 1), for some integer k``.

Accordingly, the return residual is

``d_q(x, y) = circular_distance(q*x, q*y) / q``.

This is an exact declaration of the simulated geometry; it is not a claim that
primality, a quotient order, or the generated phases measure a physical system.
The implementation uses finite IEEE-754 binary floats and rejects non-finite
inputs.  Discrete opportunity indexes remain separate from timestamps.
"""

from __future__ import annotations

import math
from collections.abc import Callable, Hashable, Iterable
from dataclasses import dataclass
from typing import TypeVar

from .model import ClosureStatus, GeometrySnapshot, MAX_EXACT_QUOTIENT_ORDER


StateT = TypeVar("StateT")


@dataclass(frozen=True, slots=True)
class DescentWitness:
    """Finite-domain counterexample to a quotient update law."""

    first_index: int
    second_index: int
    current_label: Hashable
    first_next_label: Hashable
    second_next_label: Hashable


@dataclass(frozen=True, slots=True)
class DescentReport:
    """Result of checking quotient descent on one declared finite domain."""

    status: ClosureStatus
    domain_size: int
    quotient_class_count: int
    witness: DescentWitness | None = None


def _finite(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _quotient_order(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("quotient_order must be an integer")
    if value < 1:
        raise ValueError("quotient_order must be >= 1")
    if value > MAX_EXACT_QUOTIENT_ORDER:
        raise ValueError(f"quotient_order must be <= {MAX_EXACT_QUOTIENT_ORDER}")
    return value


def _integer(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    return value


def _modulus(value: object) -> int:
    modulus = _integer("modulus", value)
    if modulus < 1:
        raise ValueError("modulus must be >= 1")
    return modulus


def normalize_phase(phase: float) -> float:
    """Normalize a finite phase in cycles into the half-open interval [0, 1)."""

    normalized = _finite("phase", phase) % 1.0
    # Canonicalize negative zero so JSON output and hashes remain stable.
    return 0.0 if normalized == 0.0 else normalized


def circular_distance(left_phase: float, right_phase: float) -> float:
    """Return the shortest circular distance in cycles, always in [0, 0.5]."""

    left = normalize_phase(left_phase)
    right = normalize_phase(right_phase)
    direct = abs(left - right)
    distance = min(direct, 1.0 - direct)
    return 0.0 if distance == 0.0 else distance


def quotient_label(quotient_order: int) -> str:
    """Return the stable ASCII label for the cyclic order used by the model."""

    order = _quotient_order(quotient_order)
    return f"C_{order}"


def cocycle_increment(start_state: int, end_state: int, modulus: int) -> int:
    """Return the exact oriented increment in the additive group ``Z/modulus``."""

    order = _modulus(modulus)
    start = _integer("start_state", start_state)
    end = _integer("end_state", end_state)
    return (end - start) % order


def compose_cocycle(first_increment: int, second_increment: int, modulus: int) -> int:
    """Compose two exact modular increments.

    For states ``a, b, c`` this implements the cocycle law
    ``inc(a,b) + inc(b,c) == inc(a,c) (mod modulus)``.
    """

    order = _modulus(modulus)
    first = _integer("first_increment", first_increment)
    second = _integer("second_increment", second_increment)
    return (first + second) % order


def accumulate_cocycle(initial_state: int, increments: Iterable[int], modulus: int) -> int:
    """Apply an iterable of modular increments and return the exact final state."""

    order = _modulus(modulus)
    state = _integer("initial_state", initial_state) % order
    try:
        iterator = iter(increments)
    except TypeError as exc:
        raise TypeError("increments must be an iterable of integers") from exc
    for index, increment in enumerate(iterator):
        state = (state + _integer(f"increments[{index}]", increment)) % order
    return state


def analyze_quotient_descent(
    domain: Iterable[StateT],
    quotient: Callable[[StateT], Hashable],
    update: Callable[[StateT], StateT],
    *,
    max_states: int = 100_000,
) -> DescentReport:
    """Check whether an update descends on one explicitly enumerated domain.

    The condition is ``q(x) == q(y) -> q(T(x)) == q(T(y))``. ``CLOSED`` means
    it holds for every supplied representative, not for any larger unstated
    domain. ``FAILED`` includes the first deterministic counterexample, and an
    empty domain is ``UNRESOLVED``.
    """

    if not callable(quotient) or not callable(update):
        raise TypeError("quotient and update must be callable")
    if isinstance(max_states, bool) or not isinstance(max_states, int):
        raise TypeError("max_states must be an integer")
    if max_states < 1:
        raise ValueError("max_states must be >= 1")
    try:
        iterator = iter(domain)
    except TypeError as exc:
        raise TypeError("domain must be iterable") from exc

    class_updates: dict[Hashable, tuple[Hashable, int]] = {}
    domain_size = 0
    for index, state in enumerate(iterator):
        if index >= max_states:
            raise ValueError(f"domain exceeds max_states={max_states}")
        current_label = quotient(state)
        next_label = quotient(update(state))
        try:
            hash(current_label)
            hash(next_label)
        except TypeError as exc:
            raise TypeError("quotient labels must be hashable") from exc
        previous = class_updates.get(current_label)
        if previous is not None and previous[0] != next_label:
            return DescentReport(
                status=ClosureStatus.FAILED,
                domain_size=index + 1,
                quotient_class_count=len(class_updates),
                witness=DescentWitness(
                    first_index=previous[1],
                    second_index=index,
                    current_label=current_label,
                    first_next_label=previous[0],
                    second_next_label=next_label,
                ),
            )
        class_updates.setdefault(current_label, (next_label, index))
        domain_size += 1

    if domain_size == 0:
        return DescentReport(
            status=ClosureStatus.UNRESOLVED,
            domain_size=0,
            quotient_class_count=0,
        )
    return DescentReport(
        status=ClosureStatus.CLOSED,
        domain_size=domain_size,
        quotient_class_count=len(class_updates),
    )


# Explicit aliases make the arithmetic domain obvious at call sites.
modular_cocycle_increment = cocycle_increment
accumulate_modular_cocycle = accumulate_cocycle


def return_residual(
    expected_phase: float,
    observed_phase: float,
    quotient_order: int = 1,
) -> float:
    """Measure return error after identifying rotations by ``1 / q`` cycles."""

    order = _quotient_order(quotient_order)
    expected = normalize_phase(expected_phase)
    observed = normalize_phase(observed_phase)
    residual = circular_distance(expected * order, observed * order) / order
    return 0.0 if residual == 0.0 else residual


def evaluate_closure(
    residual: float,
    tolerance: float,
    evidence_complete: bool = True,
) -> ClosureStatus:
    """Classify a residual using an explicit tolerance and evidence state."""

    measured = _finite("residual", residual)
    threshold = _finite("tolerance", tolerance)
    if not 0.0 <= measured <= 0.5:
        raise ValueError("residual must be in [0, 0.5]")
    if not 0.0 <= threshold <= 0.5:
        raise ValueError("tolerance must be in [0, 0.5]")
    if not isinstance(evidence_complete, bool):
        raise TypeError("evidence_complete must be a bool")
    if not evidence_complete:
        return ClosureStatus.UNRESOLVED
    return ClosureStatus.CLOSED if measured <= threshold else ClosureStatus.FAILED


def make_geometry_snapshot(
    *,
    opportunity_index: int,
    expected_phase: float,
    observed_phase: float,
    quotient_order: int = 1,
    tolerance: float = 0.01,
    evidence_complete: bool = True,
) -> GeometrySnapshot:
    """Normalize evidence, calculate its quotient residual, and type the result."""

    if isinstance(opportunity_index, bool) or not isinstance(opportunity_index, int):
        raise TypeError("opportunity_index must be an integer")
    if opportunity_index < 0:
        raise ValueError("opportunity_index must be >= 0")
    order = _quotient_order(quotient_order)
    expected = normalize_phase(expected_phase)
    observed = normalize_phase(observed_phase)
    residual = return_residual(expected, observed, order)
    threshold = _finite("tolerance", tolerance)
    status = evaluate_closure(residual, threshold, evidence_complete)
    return GeometrySnapshot(
        opportunity_index=opportunity_index,
        quotient_order=order,
        quotient_label=quotient_label(order),
        expected_phase=expected,
        observed_phase=observed,
        residual=residual,
        tolerance=threshold,
        closure_status=status,
    )


__all__ = [
    "MAX_EXACT_QUOTIENT_ORDER",
    "DescentReport",
    "DescentWitness",
    "accumulate_cocycle",
    "accumulate_modular_cocycle",
    "circular_distance",
    "analyze_quotient_descent",
    "cocycle_increment",
    "compose_cocycle",
    "evaluate_closure",
    "make_geometry_snapshot",
    "normalize_phase",
    "modular_cocycle_increment",
    "quotient_label",
    "return_residual",
]
