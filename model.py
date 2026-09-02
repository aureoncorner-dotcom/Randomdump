"""Typed domain records for the Prime Axis simulation.

The project is a deterministic *simulation*, not a physical detector.  An
``opportunity_index`` labels a discrete model transition.  It is deliberately
separate from the ideal lattice time, elapsed monotonic time, and UTC wall-clock
timestamp recorded in :class:`ClockSnapshot`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
import math
from types import MappingProxyType
from typing import Any, Mapping, TypeAlias


JSONScalar: TypeAlias = None | bool | int | float | str
JSONValue: TypeAlias = JSONScalar | list["JSONValue"] | dict[str, "JSONValue"]
FrozenJSONValue: TypeAlias = (
    JSONScalar
    | tuple["FrozenJSONValue", ...]
    | Mapping[str, "FrozenJSONValue"]
)

MAX_JSON_NESTING = 64
MAX_EXACT_QUOTIENT_ORDER = 2**53


class ClosureStatus(str, Enum):
    """Outcome of a return-residual closure test."""

    CLOSED = "CLOSED"
    FAILED = "FAILED"
    UNRESOLVED = "UNRESOLVED"


class Severity(str, Enum):
    """Operational importance of a simulated tick."""

    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


def _require_int(
    name: str,
    value: object,
    *,
    minimum: int | None = None,
    maximum: int | None = None,
) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    if maximum is not None and value > maximum:
        raise ValueError(f"{name} must be <= {maximum}")
    return value


def _require_finite(
    name: str,
    value: object,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
    maximum_exclusive: bool = False,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    if minimum is not None and result < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    if maximum is not None:
        if maximum_exclusive and result >= maximum:
            raise ValueError(f"{name} must be < {maximum}")
        if not maximum_exclusive and result > maximum:
            raise ValueError(f"{name} must be <= {maximum}")
    return result


def _require_utc(name: str, value: object) -> datetime:
    if not isinstance(value, datetime):
        raise TypeError(f"{name} must be a datetime")
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError(f"{name} must be timezone-aware UTC")
    if value.utcoffset() != timedelta(0):
        raise ValueError(f"{name} must have a UTC offset of zero")
    return value.astimezone(timezone.utc)


def _freeze_json(
    value: object,
    *,
    path: str = "metadata",
    depth: int = 0,
) -> FrozenJSONValue:
    """Validate JSON data, reject non-finite numbers, and detach mutable input."""

    if depth > MAX_JSON_NESTING:
        raise ValueError(
            f"{path} exceeds the maximum JSON nesting depth of "
            f"{MAX_JSON_NESTING}"
        )
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"{path} contains a non-finite number")
        return value
    if isinstance(value, list):
        return tuple(
            _freeze_json(
                item,
                path=f"{path}[{index}]",
                depth=depth + 1,
            )
            for index, item in enumerate(value)
        )
    if isinstance(value, Mapping):
        frozen: dict[str, FrozenJSONValue] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError(f"{path} keys must be strings")
            frozen[key] = _freeze_json(
                item,
                path=f"{path}.{key}",
                depth=depth + 1,
            )
        return MappingProxyType(frozen)
    raise TypeError(f"{path} contains a non-JSON value of type {type(value).__name__}")


def thaw_json(value: object) -> JSONValue:
    """Return a detached, ordinary JSON value from validated model data."""

    if isinstance(value, Mapping):
        return {str(key): thaw_json(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [thaw_json(item) for item in value]
    if isinstance(value, list):
        return [thaw_json(item) for item in value]
    return value  # type: ignore[return-value]


def format_utc(value: datetime) -> str:
    """Serialize an aware UTC timestamp in one canonical RFC 3339 form."""

    timestamp = _require_utc("timestamp", value)
    return timestamp.isoformat(timespec="microseconds").replace("+00:00", "Z")


@dataclass(frozen=True, slots=True)
class ClockSnapshot:
    """Three distinct coordinates for one simulation opportunity.

    ``lattice_time_s`` is ideal model time. ``monotonic_time_s`` is elapsed
    duration from a monotonic clock origin. ``wall_time_utc`` is only a civil
    timestamp for correlation and must not drive interval calculations.
    """

    opportunity_index: int
    lattice_time_s: float
    monotonic_time_s: float
    wall_time_utc: datetime

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "opportunity_index", _require_int("opportunity_index", self.opportunity_index, minimum=0)
        )
        object.__setattr__(
            self, "lattice_time_s", _require_finite("lattice_time_s", self.lattice_time_s, minimum=0.0)
        )
        object.__setattr__(
            self,
            "monotonic_time_s",
            _require_finite("monotonic_time_s", self.monotonic_time_s, minimum=0.0),
        )
        object.__setattr__(self, "wall_time_utc", _require_utc("wall_time_utc", self.wall_time_utc))

    @property
    def slip_s(self) -> float:
        return self.monotonic_time_s - self.lattice_time_s

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "opportunity_index": self.opportunity_index,
            "lattice_time_s": self.lattice_time_s,
            "monotonic_time_s": self.monotonic_time_s,
            "slip_s": self.slip_s,
            "wall_time_utc": format_utc(self.wall_time_utc),
        }


@dataclass(frozen=True, slots=True)
class GeometrySnapshot:
    """Evidence and result for one explicitly simulated quotient geometry."""

    opportunity_index: int
    quotient_order: int
    quotient_label: str
    expected_phase: float
    observed_phase: float
    residual: float
    tolerance: float
    closure_status: ClosureStatus

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "opportunity_index", _require_int("opportunity_index", self.opportunity_index, minimum=0)
        )
        object.__setattr__(
            self,
            "quotient_order",
            _require_int(
                "quotient_order",
                self.quotient_order,
                minimum=1,
                maximum=MAX_EXACT_QUOTIENT_ORDER,
            ),
        )
        expected_label = f"C_{self.quotient_order}"
        if self.quotient_label != expected_label:
            raise ValueError(
                f"quotient_label must be {expected_label!r} for quotient_order "
                f"{self.quotient_order}"
            )
        object.__setattr__(
            self,
            "expected_phase",
            _require_finite("expected_phase", self.expected_phase, minimum=0.0, maximum=1.0, maximum_exclusive=True),
        )
        object.__setattr__(
            self,
            "observed_phase",
            _require_finite("observed_phase", self.observed_phase, minimum=0.0, maximum=1.0, maximum_exclusive=True),
        )
        object.__setattr__(self, "residual", _require_finite("residual", self.residual, minimum=0.0, maximum=0.5))
        object.__setattr__(
            self, "tolerance", _require_finite("tolerance", self.tolerance, minimum=0.0, maximum=0.5)
        )
        if not isinstance(self.closure_status, ClosureStatus):
            try:
                object.__setattr__(self, "closure_status", ClosureStatus(self.closure_status))
            except (TypeError, ValueError) as exc:
                raise ValueError("closure_status is not a valid ClosureStatus") from exc

        expected_scaled = (self.expected_phase * self.quotient_order) % 1.0
        observed_scaled = (self.observed_phase * self.quotient_order) % 1.0
        direct = abs(expected_scaled - observed_scaled)
        expected_residual = min(direct, 1.0 - direct) / self.quotient_order
        if not math.isclose(
            self.residual,
            expected_residual,
            rel_tol=1e-12,
            abs_tol=1e-15,
        ):
            raise ValueError(
                "residual is inconsistent with the declared cyclic quotient "
                "comparator"
            )
        if (
            self.closure_status is ClosureStatus.CLOSED
            and self.residual > self.tolerance
        ):
            raise ValueError("CLOSED requires residual <= tolerance")
        if (
            self.closure_status is ClosureStatus.FAILED
            and self.residual <= self.tolerance
        ):
            raise ValueError("FAILED requires residual > tolerance")

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "opportunity_index": self.opportunity_index,
            "quotient_order": self.quotient_order,
            "quotient_label": self.quotient_label,
            "expected_phase": self.expected_phase,
            "observed_phase": self.observed_phase,
            "residual": self.residual,
            "tolerance": self.tolerance,
            "closure_status": self.closure_status.value,
        }


@dataclass(frozen=True, slots=True)
class AxisSnapshot:
    """Arithmetic coordinate and its geometry evidence."""

    node: int
    is_prime: bool
    geometry: GeometrySnapshot

    def __post_init__(self) -> None:
        object.__setattr__(self, "node", _require_int("node", self.node, minimum=1))
        if not isinstance(self.is_prime, bool):
            raise TypeError("is_prime must be a bool")
        if not isinstance(self.geometry, GeometrySnapshot):
            raise TypeError("geometry must be a GeometrySnapshot")
        from .number_theory import is_prime as classify_prime

        if self.is_prime is not classify_prime(self.node):
            raise ValueError("is_prime is inconsistent with node")

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "node": self.node,
            "is_prime": self.is_prime,
            "geometry": self.geometry.to_dict(),
        }


@dataclass(frozen=True, slots=True)
class TickEvent:
    """One validated engine observation ready for ledger serialization."""

    clock: ClockSnapshot
    axis: AxisSnapshot
    severity: Severity
    message: str = ""
    metadata: Mapping[str, FrozenJSONValue] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.clock, ClockSnapshot):
            raise TypeError("clock must be a ClockSnapshot")
        if not isinstance(self.axis, AxisSnapshot):
            raise TypeError("axis must be an AxisSnapshot")
        if self.clock.opportunity_index != self.axis.geometry.opportunity_index:
            raise ValueError("clock and geometry opportunity indexes must match")
        if not isinstance(self.severity, Severity):
            try:
                object.__setattr__(self, "severity", Severity(self.severity))
            except (TypeError, ValueError) as exc:
                raise ValueError("severity is not a valid Severity") from exc
        if not isinstance(self.message, str):
            raise TypeError("message must be a string")
        frozen = _freeze_json(self.metadata)
        if not isinstance(frozen, Mapping):
            raise TypeError("metadata must be a mapping")
        object.__setattr__(self, "metadata", frozen)

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "event_type": "tick",
            "clock": self.clock.to_dict(),
            "axis": self.axis.to_dict(),
            "severity": self.severity.value,
            "message": self.message,
            "metadata": thaw_json(self.metadata),
        }


@dataclass(frozen=True, slots=True)
class MultiAxisTickEvent:
    """One atomic opportunity containing every synchronized axis observation."""

    clock: ClockSnapshot
    axes: Mapping[str, AxisSnapshot]
    max_severity: Severity
    message: str = ""
    metadata: Mapping[str, FrozenJSONValue] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.clock, ClockSnapshot):
            raise TypeError("clock must be a ClockSnapshot")
        if not isinstance(self.axes, Mapping):
            raise TypeError("axes must be a mapping")
        if not self.axes:
            raise ValueError("axes must contain at least one axis")
        validated_axes: dict[str, AxisSnapshot] = {}
        for label, axis in self.axes.items():
            if not isinstance(label, str) or not label or label.strip() != label:
                raise ValueError("axis labels must be non-empty strings without surrounding whitespace")
            if label in validated_axes:
                raise ValueError(f"duplicate axis label: {label}")
            if not isinstance(axis, AxisSnapshot):
                raise TypeError(f"axis {label!r} must be an AxisSnapshot")
            if axis.geometry.opportunity_index != self.clock.opportunity_index:
                raise ValueError(f"axis {label!r} does not share the clock opportunity index")
            validated_axes[label] = axis
        object.__setattr__(self, "axes", MappingProxyType(validated_axes))
        if not isinstance(self.max_severity, Severity):
            try:
                object.__setattr__(self, "max_severity", Severity(self.max_severity))
            except (TypeError, ValueError) as exc:
                raise ValueError("max_severity is not a valid Severity") from exc
        if not isinstance(self.message, str):
            raise TypeError("message must be a string")
        frozen = _freeze_json(self.metadata)
        if not isinstance(frozen, Mapping):
            raise TypeError("metadata must be a mapping")
        object.__setattr__(self, "metadata", frozen)

    @property
    def severity(self) -> Severity:
        """Compatibility alias for consumers that render a single severity."""

        return self.max_severity

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "event_type": "multi_axis_tick",
            "clock": self.clock.to_dict(),
            "axes": {label: axis.to_dict() for label, axis in sorted(self.axes.items())},
            "max_severity": self.max_severity.value,
            "message": self.message,
            "metadata": thaw_json(self.metadata),
        }


# Older design notes called this shape a parallel tick.  Keep a type alias so
# engine and CLI code can use either vocabulary without emitting two schemas.
ParallelTickEvent = MultiAxisTickEvent


__all__ = [
    "AxisSnapshot",
    "ClockSnapshot",
    "ClosureStatus",
    "FrozenJSONValue",
    "GeometrySnapshot",
    "JSONScalar",
    "JSONValue",
    "MAX_JSON_NESTING",
    "MAX_EXACT_QUOTIENT_ORDER",
    "MultiAxisTickEvent",
    "ParallelTickEvent",
    "Severity",
    "TickEvent",
    "format_utc",
    "thaw_json",
]
