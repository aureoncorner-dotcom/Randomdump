"""Deterministic orchestration for synchronized prime-axis simulations.

The engine advances each active axis at most once per logical opportunity.
Routing decisions depend only on validated configuration and graph state; wall
and monotonic clocks are recorded as observations and never influence routing.
"""

from __future__ import annotations

from collections import deque
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import heapq
from itertools import count
import math
import time
from typing import Protocol

from .geometry import MAX_EXACT_QUOTIENT_ORDER, make_geometry_snapshot
from .model import (
    AxisSnapshot,
    ClockSnapshot,
    ClosureStatus,
    GeometrySnapshot,
    JSONValue,
    MultiAxisTickEvent,
    Severity,
    TickEvent,
)
from .number_theory import is_prime
from .routing import (
    MAX_FRICTION_SCALE,
    MAX_ROUTE_NODE,
    MAX_SEARCH_LIMIT,
    PrimeRoutePlanner,
    RoutePlanningError,
    SearchLimitExceeded,
    allowed_moves,
    node_friction,
)


MAX_ENGINE_TICKS = 100_000
MAX_ENGINE_AXES = 256
MAX_AXIS_TICK_BUDGET = 2_000_000


class EngineError(RuntimeError):
    """Base exception for orchestration failures."""


class ClockRegressionError(EngineError):
    """Raised when an injected monotonic clock moves backwards."""


class AxisStatus(str, Enum):
    """Explicit lifecycle of one independently routed axis."""

    ACTIVE = "ACTIVE"
    ANCHORED = "ANCHORED"
    FAILED = "FAILED"


def _strict_int(
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


def _finite_float(
    name: str,
    value: object,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
    positive: bool = False,
) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a real number")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError(f"{name} must be finite") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    if positive and result <= 0.0:
        raise ValueError(f"{name} must be > 0")
    if minimum is not None and result < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    if maximum is not None and result > maximum:
        raise ValueError(f"{name} must be <= {maximum}")
    return result


@dataclass(frozen=True, slots=True)
class AxisSpec:
    """Validated immutable input for one named axis."""

    label: str
    start: int
    target: int
    quotient_order: int = 3
    tolerance: float = 0.01

    def __post_init__(self) -> None:
        if not isinstance(self.label, str):
            raise TypeError("label must be a string")
        label = self.label.strip()
        if not label:
            raise ValueError("label must not be empty")
        if len(label) > 64:
            raise ValueError("label must be at most 64 characters")
        if any(ord(character) < 32 or ord(character) == 127 for character in label):
            raise ValueError("label must not contain control characters")
        object.__setattr__(self, "label", label)

        start = _strict_int("start", self.start, minimum=1, maximum=MAX_ROUTE_NODE)
        target = _strict_int(
            "target", self.target, minimum=1, maximum=MAX_ROUTE_NODE
        )
        if not is_prime(target):
            raise ValueError("target must be prime")
        object.__setattr__(self, "start", start)
        object.__setattr__(self, "target", target)

        order = _strict_int("quotient_order", self.quotient_order, minimum=1)
        if order > MAX_EXACT_QUOTIENT_ORDER:
            raise ValueError(
                f"quotient_order must be <= {MAX_EXACT_QUOTIENT_ORDER}"
            )
        object.__setattr__(self, "quotient_order", order)
        object.__setattr__(
            self,
            "tolerance",
            _finite_float("tolerance", self.tolerance, minimum=0.0, maximum=0.5),
        )

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "label": self.label,
            "start": self.start,
            "target": self.target,
            "quotient_order": self.quotient_order,
            "tolerance": self.tolerance,
        }


def default_axis_specs() -> tuple[AxisSpec, ...]:
    """Return fresh specifications for the historical X/Y/Z demonstration."""

    return (
        AxisSpec("X", 48, 113),
        AxisSpec("Y", 72, 139),
        AxisSpec("Z", 120, 173),
    )


@dataclass(frozen=True, slots=True)
class EngineConfig:
    """Validated finite bounds and deterministic engine policy."""

    lower_bound: int = 1
    upper_bound: int = 250
    friction_scale: int = 15
    search_limit: int = 10_000
    max_ticks: int = 10_000
    max_axes: int = 64
    max_incidents: int = 64
    reroute_after_incidents: int = 3
    lattice_period_s: float = 0.2
    pace: bool = False

    def __post_init__(self) -> None:
        lower = _strict_int(
            "lower_bound", self.lower_bound, minimum=1, maximum=MAX_ROUTE_NODE
        )
        upper = _strict_int(
            "upper_bound", self.upper_bound, minimum=1, maximum=MAX_ROUTE_NODE
        )
        if upper < lower:
            raise ValueError("upper_bound must be >= lower_bound")
        object.__setattr__(self, "lower_bound", lower)
        object.__setattr__(self, "upper_bound", upper)
        object.__setattr__(
            self,
            "friction_scale",
            _strict_int(
                "friction_scale",
                self.friction_scale,
                minimum=1,
                maximum=MAX_FRICTION_SCALE,
            ),
        )
        object.__setattr__(
            self,
            "search_limit",
            _strict_int(
                "search_limit",
                self.search_limit,
                minimum=1,
                maximum=MAX_SEARCH_LIMIT,
            ),
        )
        ticks = _strict_int(
            "max_ticks", self.max_ticks, minimum=1, maximum=MAX_ENGINE_TICKS
        )
        axes = _strict_int(
            "max_axes", self.max_axes, minimum=1, maximum=MAX_ENGINE_AXES
        )
        if ticks * axes > MAX_AXIS_TICK_BUDGET:
            raise ValueError(
                f"max_ticks * max_axes must be <= {MAX_AXIS_TICK_BUDGET}"
            )
        object.__setattr__(self, "max_ticks", ticks)
        object.__setattr__(self, "max_axes", axes)
        incidents = _strict_int(
            "max_incidents",
            self.max_incidents,
            minimum=1,
            maximum=MAX_ENGINE_TICKS,
        )
        reroute_after = _strict_int(
            "reroute_after_incidents", self.reroute_after_incidents, minimum=1
        )
        if reroute_after > incidents:
            raise ValueError("reroute_after_incidents must be <= max_incidents")
        object.__setattr__(self, "max_incidents", incidents)
        object.__setattr__(self, "reroute_after_incidents", reroute_after)
        period = _finite_float(
            "lattice_period_s", self.lattice_period_s, positive=True
        )
        if not math.isfinite((ticks - 1) * period):
            raise ValueError("lattice period overflows the configured tick horizon")
        object.__setattr__(self, "lattice_period_s", period)
        if not isinstance(self.pace, bool):
            raise TypeError("pace must be a bool")

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "lower_bound": self.lower_bound,
            "upper_bound": self.upper_bound,
            "friction_scale": self.friction_scale,
            "search_limit": self.search_limit,
            "max_ticks": self.max_ticks,
            "max_axes": self.max_axes,
            "max_incidents": self.max_incidents,
            "reroute_after_incidents": self.reroute_after_incidents,
            "lattice_period_s": self.lattice_period_s,
            "pace": self.pace,
        }


@dataclass(frozen=True, slots=True)
class AxisTick:
    """One axis's state in a synchronized logical opportunity."""

    label: str
    status: AxisStatus
    node: int
    advanced: bool
    incident_count: int
    rerouted: bool
    message: str
    event: TickEvent

    def to_dict(self) -> dict[str, JSONValue]:
        payload: dict[str, JSONValue] = {
            "label": self.label,
            "status": self.status.value,
            "node": self.node,
            "advanced": self.advanced,
            "incident_count": self.incident_count,
            "rerouted": self.rerouted,
            "message": self.message,
        }
        payload["event"] = self.event.to_dict()
        return payload


@dataclass(frozen=True, slots=True)
class EngineTick:
    """Atomic in-memory view of all axes at one opportunity."""

    clock: ClockSnapshot
    axes: tuple[AxisTick, ...]

    @property
    def max_severity(self) -> Severity:
        """Return the highest event severity without axis-order dependence."""

        rank = {Severity.INFO: 0, Severity.WARNING: 1, Severity.CRITICAL: 2}
        severities = (axis.event.severity for axis in self.axes)
        return max(severities, key=rank.__getitem__, default=Severity.INFO)

    def to_multi_axis_event(self) -> MultiAxisTickEvent:
        """Build the typed atomic ledger event for this opportunity."""

        return MultiAxisTickEvent(
            clock=self.clock,
            axes={axis.label: axis.event.axis for axis in self.axes},
            max_severity=self.max_severity,
            message=f"synchronized opportunity {self.clock.opportunity_index}",
            metadata={
                "axis_states": {
                    axis.label: {
                        "status": axis.status.value,
                        "advanced": axis.advanced,
                        "incident_count": axis.incident_count,
                        "rerouted": axis.rerouted,
                        "message": axis.message,
                    }
                    for axis in self.axes
                },
                "phase_basis": "normalized bounded-route position",
            },
        )

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "event_type": "synchronized_tick",
            "clock": self.clock.to_dict(),
            "max_severity": self.max_severity.value,
            "axes": [axis.to_dict() for axis in self.axes],
        }


@dataclass(frozen=True, slots=True)
class AxisResult:
    """Terminal summary for one axis."""

    label: str
    start: int
    target: int
    status: AxisStatus
    current_node: int
    incidents: int
    reroutes: int
    visited_nodes: tuple[int, ...]
    breached_nodes: tuple[int, ...]
    error: str | None = None

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "label": self.label,
            "start": self.start,
            "target": self.target,
            "status": self.status.value,
            "current_node": self.current_node,
            "incidents": self.incidents,
            "reroutes": self.reroutes,
            "visited_nodes": list(self.visited_nodes),
            "breached_nodes": list(self.breached_nodes),
            "error": self.error,
        }


@dataclass(frozen=True, slots=True)
class SimulationResult:
    """Complete immutable result of one bounded simulation run."""

    config: EngineConfig
    ticks: tuple[EngineTick, ...]
    axes: tuple[AxisResult, ...]

    @property
    def succeeded(self) -> bool:
        return bool(self.axes) and all(
            axis.status is AxisStatus.ANCHORED for axis in self.axes
        )

    @property
    def opportunities(self) -> int:
        return len(self.ticks)

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "succeeded": self.succeeded,
            "opportunities": self.opportunities,
            "config": self.config.to_dict(),
            "axes": [axis.to_dict() for axis in self.axes],
            "ticks": [tick.to_dict() for tick in self.ticks],
        }

    def summary_dict(self) -> dict[str, JSONValue]:
        """Return a bounded completion record without duplicating tick history."""

        return {
            "event_type": "simulation_complete",
            "succeeded": self.succeeded,
            "opportunities": self.opportunities,
            "axes": [axis.to_dict() for axis in self.axes],
        }


class LedgerSink(Protocol):
    """Small structural interface accepted by :class:`SimulationEngine`."""

    def append(
        self,
        event: TickEvent | MultiAxisTickEvent | Mapping[str, JSONValue],
        *,
        timestamp_utc: datetime | None = None,
    ) -> object: ...


class EngineRenderer(Protocol):
    def render_start(
        self, specs: tuple[AxisSpec, ...], config: EngineConfig
    ) -> None: ...

    def render_tick(self, tick: EngineTick) -> None: ...

    def render_complete(self, result: SimulationResult) -> None: ...


@dataclass(slots=True)
class _MutableAxis:
    spec: AxisSpec
    status: AxisStatus
    current_node: int
    future_nodes: deque[int] = field(default_factory=deque)
    incidents: int = 0
    reroutes: int = 0
    visited_nodes: list[int] = field(default_factory=list)
    breached_nodes: set[int] = field(default_factory=set)
    error: str | None = None


class SimulationEngine:
    """Advance independent routes on one deterministic synchronized scheduler."""

    def __init__(
        self,
        config: EngineConfig | None = None,
        *,
        monotonic_clock: Callable[[], float] = time.monotonic,
        wall_clock: Callable[[], datetime] | None = None,
        sleeper: Callable[[float], object] = time.sleep,
    ) -> None:
        self.config = config if config is not None else EngineConfig()
        if not isinstance(self.config, EngineConfig):
            raise TypeError("config must be an EngineConfig")
        for name, function in (
            ("monotonic_clock", monotonic_clock),
            ("sleeper", sleeper),
        ):
            if not callable(function):
                raise TypeError(f"{name} must be callable")
        if wall_clock is not None and not callable(wall_clock):
            raise TypeError("wall_clock must be callable")
        self._monotonic_clock = monotonic_clock
        self._wall_clock = wall_clock or (lambda: datetime.now(timezone.utc))
        self._sleeper = sleeper
        self._planner = PrimeRoutePlanner(
            lower_bound=self.config.lower_bound,
            upper_bound=self.config.upper_bound,
            friction_scale=self.config.friction_scale,
            search_limit=self.config.search_limit,
        )

    def run(
        self,
        axis_specs: Iterable[AxisSpec] | None = None,
        *,
        ledger: LedgerSink | None = None,
        renderer: EngineRenderer | None = None,
    ) -> SimulationResult:
        specs = self._validated_specs(
            default_axis_specs() if axis_specs is None else axis_specs
        )
        states = [self._initialize_axis(spec) for spec in specs]
        ticks: list[EngineTick] = []
        origin = self._read_monotonic("initial monotonic clock")
        previous_monotonic = origin

        if ledger is not None:
            ledger.append(
                {
                    "event_type": "simulation_start",
                    "config": self.config.to_dict(),
                    "axes": [spec.to_dict() for spec in specs],
                    "phase_basis": "normalized bounded-route position",
                    "clock_contract": {
                        "opportunity": "discrete logical index",
                        "lattice": "configured ideal model time",
                        "monotonic": "elapsed execution observation",
                        "utc": "human correlation only",
                    },
                }
            )

        if renderer is not None:
            renderer.render_start(specs, self.config)

        for opportunity_index in range(self.config.max_ticks):
            if not any(state.status is AxisStatus.ACTIVE for state in states):
                break
            if self.config.pace and opportunity_index > 0:
                self._sleeper(self.config.lattice_period_s)

            observed = self._read_monotonic("monotonic clock")
            if observed < previous_monotonic:
                raise ClockRegressionError(
                    "monotonic clock moved backwards during the simulation"
                )
            previous_monotonic = observed
            clock = ClockSnapshot(
                opportunity_index=opportunity_index,
                lattice_time_s=opportunity_index * self.config.lattice_period_s,
                monotonic_time_s=observed - origin,
                wall_time_utc=self._wall_clock(),
            )

            axis_ticks = tuple(self._advance_axis(state, clock) for state in states)
            tick = EngineTick(clock=clock, axes=axis_ticks)
            ticks.append(tick)
            if ledger is not None:
                ledger.append(
                    tick.to_multi_axis_event(), timestamp_utc=clock.wall_time_utc
                )
            if renderer is not None:
                renderer.render_tick(tick)

        for state in states:
            if state.status is AxisStatus.ACTIVE:
                state.status = AxisStatus.FAILED
                state.error = (
                    f"maximum of {self.config.max_ticks} logical opportunities reached"
                )

        result = SimulationResult(
            config=self.config,
            ticks=tuple(ticks),
            axes=tuple(self._axis_result(state) for state in states),
        )
        if ledger is not None:
            completion_time = (
                ticks[-1].clock.wall_time_utc if ticks else None
            )
            ledger.append(result.summary_dict(), timestamp_utc=completion_time)
        if renderer is not None:
            renderer.render_complete(result)
        return result

    def _validated_specs(self, axis_specs: Iterable[AxisSpec]) -> tuple[AxisSpec, ...]:
        try:
            specs = tuple(axis_specs)
        except TypeError as exc:
            raise TypeError("axis_specs must be an iterable of AxisSpec values") from exc
        if not specs:
            raise ValueError("at least one axis specification is required")
        if len(specs) > self.config.max_axes:
            raise ValueError(
                f"axis specification count must not exceed {self.config.max_axes}"
            )
        if any(not isinstance(spec, AxisSpec) for spec in specs):
            raise TypeError("every axis specification must be an AxisSpec")

        seen: set[str] = set()
        for spec in specs:
            folded = spec.label.casefold()
            if folded in seen:
                raise ValueError(f"duplicate axis label: {spec.label}")
            seen.add(folded)
            if not self.config.lower_bound <= spec.start <= self.config.upper_bound:
                raise ValueError(
                    f"axis {spec.label} start must be within inclusive bounds "
                    f"[{self.config.lower_bound}, {self.config.upper_bound}]"
                )
            if not self.config.lower_bound <= spec.target <= self.config.upper_bound:
                raise ValueError(
                    f"axis {spec.label} target must be within inclusive bounds "
                    f"[{self.config.lower_bound}, {self.config.upper_bound}]"
                )
        return specs

    def _initialize_axis(self, spec: AxisSpec) -> _MutableAxis:
        try:
            route = self._planner.route_to_prime(spec.start, spec.target)
        except RoutePlanningError as exc:
            return _MutableAxis(
                spec=spec,
                status=AxisStatus.FAILED,
                current_node=spec.start,
                visited_nodes=[spec.start],
                error=str(exc),
            )
        status = (
            AxisStatus.ANCHORED if spec.start == spec.target else AxisStatus.ACTIVE
        )
        return _MutableAxis(
            spec=spec,
            status=status,
            current_node=spec.start,
            future_nodes=deque(route.nodes[1:]),
            visited_nodes=[spec.start],
        )

    def _advance_axis(self, state: _MutableAxis, clock: ClockSnapshot) -> AxisTick:
        if state.status is not AxisStatus.ACTIVE:
            return self._event_tick(
                state,
                clock,
                advanced=False,
                rerouted=False,
                severity=(
                    Severity.CRITICAL
                    if state.status is AxisStatus.FAILED
                    else Severity.INFO
                ),
                message=state.error or "axis already anchored",
            )

        if not state.future_nodes:
            state.status = AxisStatus.FAILED
            state.error = "route ended before the target was reached"
            return self._event_tick(
                state,
                clock,
                advanced=False,
                rerouted=False,
                severity=Severity.CRITICAL,
                message=state.error,
            )

        previous_node = state.current_node
        state.current_node = state.future_nodes.popleft()
        state.visited_nodes.append(state.current_node)
        geometry = self._geometry(state, clock.opportunity_index)
        incident = geometry.closure_status is ClosureStatus.FAILED
        rerouted = False
        severity = Severity.INFO
        message = f"advanced from {previous_node} to {state.current_node}"

        if state.current_node == state.spec.target:
            state.status = AxisStatus.ANCHORED
            message = f"anchored at target {state.spec.target}"
        elif incident:
            severity = Severity.WARNING
            state.incidents += 1
            state.breached_nodes.add(state.current_node)
            message = (
                f"closure residual exceeded tolerance at node {state.current_node} "
                f"(incident {state.incidents}/{self.config.max_incidents})"
            )
            if state.incidents >= self.config.max_incidents:
                state.status = AxisStatus.FAILED
                state.error = "maximum incident count reached"
                severity = Severity.CRITICAL
                message = state.error
            elif state.incidents % self.config.reroute_after_incidents == 0:
                try:
                    route = self._route_avoiding_breaches(state)
                except RoutePlanningError as exc:
                    state.status = AxisStatus.FAILED
                    state.error = f"reroute failed: {exc}"
                    severity = Severity.CRITICAL
                    message = state.error
                else:
                    # The route begins at the already processed breach node.
                    # Starting at index one prevents processing that node twice.
                    state.future_nodes = deque(route[1:])
                    state.reroutes += 1
                    rerouted = True
                    message += "; route recalculated from the next decision point"

        return self._event_tick(
            state,
            clock,
            advanced=True,
            rerouted=rerouted,
            severity=severity,
            message=message,
            geometry=geometry,
            previous_node=previous_node,
        )

    def _event_tick(
        self,
        state: _MutableAxis,
        clock: ClockSnapshot,
        *,
        advanced: bool,
        rerouted: bool,
        severity: Severity,
        message: str,
        geometry: GeometrySnapshot | None = None,
        previous_node: int | None = None,
    ) -> AxisTick:
        geometry_snapshot = geometry or self._geometry(state, clock.opportunity_index)
        event = TickEvent(
            clock=clock,
            axis=AxisSnapshot(
                node=state.current_node,
                is_prime=is_prime(state.current_node),
                geometry=geometry_snapshot,
            ),
            severity=severity,
            message=message,
            metadata={
                "axis_label": state.spec.label,
                "axis_status": state.status.value,
                "advanced": advanced,
                "previous_node": previous_node,
                "incident_count": state.incidents,
                "reroute_count": state.reroutes,
                "rerouted": rerouted,
                "remaining_route_nodes": len(state.future_nodes),
                "breached_nodes": sorted(state.breached_nodes),
            },
        )
        return AxisTick(
            label=state.spec.label,
            status=state.status,
            node=state.current_node,
            advanced=advanced,
            incident_count=state.incidents,
            rerouted=rerouted,
            message=message,
            event=event,
        )

    def _geometry(
        self,
        state: _MutableAxis,
        opportunity_index: int,
        *,
        evidence_complete: bool = True,
    ) -> GeometrySnapshot:
        """Compare target and node positions in the declared cyclic route geometry.

        The phase coordinates come from normalized positions in the configured
        graph bounds. They are not derived from either recorded clock.
        """
        span = self.config.upper_bound - self.config.lower_bound + 1
        expected_phase = (state.spec.target - self.config.lower_bound) / span
        observed_phase = (state.current_node - self.config.lower_bound) / span
        return make_geometry_snapshot(
            opportunity_index=opportunity_index,
            expected_phase=expected_phase,
            observed_phase=observed_phase,
            quotient_order=state.spec.quotient_order,
            tolerance=state.spec.tolerance,
            evidence_complete=evidence_complete,
        )

    def _route_avoiding_breaches(self, state: _MutableAxis) -> tuple[int, ...]:
        """Run a bounded deterministic Dijkstra search around breached nodes."""

        start = state.current_node
        target = state.spec.target
        if start == target:
            return (start,)

        blocked = frozenset(state.breached_nodes)
        labels: dict[int, tuple[int, int]] = {start: (0, 0)}
        predecessors: dict[int, int] = {}
        serial = count()
        queue: list[tuple[int, int, int, int]] = [(0, 0, next(serial), start)]
        explored = 0

        while queue:
            friction, hops, _, current = heapq.heappop(queue)
            if labels.get(current) != (friction, hops):
                continue
            if explored >= self.config.search_limit:
                raise SearchLimitExceeded(
                    limit=self.config.search_limit, explored_nodes=explored
                )
            explored += 1
            if current == target:
                nodes = [target]
                while nodes[-1] != start:
                    nodes.append(predecessors[nodes[-1]])
                return tuple(reversed(nodes))

            for neighbor in allowed_moves(
                current,
                lower_bound=self.config.lower_bound,
                upper_bound=self.config.upper_bound,
            ):
                if neighbor in blocked:
                    continue
                next_label = (
                    friction
                    + node_friction(neighbor, scale=self.config.friction_scale),
                    hops + 1,
                )
                if next_label >= labels.get(neighbor, (math.inf, math.inf)):
                    continue
                labels[neighbor] = next_label
                predecessors[neighbor] = current
                heapq.heappush(queue, (*next_label, next(serial), neighbor))

        raise RoutePlanningError(
            f"no route from {start} to {target} avoids the breached nodes"
        )

    def _read_monotonic(self, name: str) -> float:
        return _finite_float(name, self._monotonic_clock(), minimum=0.0)

    @staticmethod
    def _axis_result(state: _MutableAxis) -> AxisResult:
        return AxisResult(
            label=state.spec.label,
            start=state.spec.start,
            target=state.spec.target,
            status=state.status,
            current_node=state.current_node,
            incidents=state.incidents,
            reroutes=state.reroutes,
            visited_nodes=tuple(state.visited_nodes),
            breached_nodes=tuple(sorted(state.breached_nodes)),
            error=state.error,
        )


__all__ = [
    "AxisResult",
    "AxisSpec",
    "AxisStatus",
    "AxisTick",
    "ClockRegressionError",
    "EngineConfig",
    "EngineError",
    "EngineTick",
    "SimulationEngine",
    "SimulationResult",
    "default_axis_specs",
]
