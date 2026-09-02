"""Bounded and deterministic route planning over the prime-axis graph."""

from __future__ import annotations

from dataclasses import dataclass
import heapq
from itertools import count
from typing import Any, Final, Literal, TypeAlias

from .number_theory import divisor_count, is_prime

MoveName: TypeAlias = Literal["+1", "-1", "*2", "//2"]
RouteMode: TypeAlias = Literal["chosen_prime", "nearest_prime"]

_MOVE_ORDER: Final[tuple[MoveName, ...]] = ("+1", "-1", "*2", "//2")
MAX_ROUTE_NODE: Final[int] = 10_000_000
MAX_FRICTION_SCALE: Final[int] = 1_000_000
MAX_SEARCH_LIMIT: Final[int] = 1_000_000


class RoutePlanningError(Exception):
    """Base exception for route-planning failures."""


class InvalidRouteRequest(RoutePlanningError, ValueError):
    """Raised when bounds, endpoints, costs, or limits are invalid."""


class SearchLimitExceeded(RoutePlanningError):
    """Raised when a route search exhausts its permitted node expansions."""

    def __init__(self, *, limit: int, explored_nodes: int) -> None:
        self.limit = limit
        self.explored_nodes = explored_nodes
        super().__init__(
            f"search limit of {limit} node expansions was reached "
            f"after exploring {explored_nodes} nodes"
        )


class RouteNotFound(RoutePlanningError):
    """Raised when no requested prime destination exists in the bounded graph."""


@dataclass(frozen=True, slots=True)
class RouteStep:
    """One immutable point in a planned route."""

    index: int
    node: int
    move: MoveName | None
    friction: int
    cumulative_friction: int
    prime: bool


@dataclass(frozen=True, slots=True)
class RouteResult:
    """A complete route and the search metadata needed by a CLI or API."""

    mode: RouteMode
    start: int
    target: int
    lower_bound: int
    upper_bound: int
    steps: tuple[RouteStep, ...]
    total_friction: int
    hops: int
    explored_nodes: int

    @property
    def nodes(self) -> tuple[int, ...]:
        """Return the route as a compact node sequence."""

        return tuple(step.node for step in self.steps)


def _require_integer(
    value: Any,
    *,
    name: str,
    minimum: int | None = None,
    maximum: int | None = None,
) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InvalidRouteRequest(
            f"{name} must be an integer, not {type(value).__name__}"
        )
    if minimum is not None and value < minimum:
        raise InvalidRouteRequest(f"{name} must be at least {minimum}")
    if maximum is not None and value > maximum:
        raise InvalidRouteRequest(f"{name} must be at most {maximum}")
    return value


def _validate_bounds(lower_bound: int, upper_bound: int) -> tuple[int, int]:
    lower = _require_integer(
        lower_bound, name="lower_bound", minimum=1, maximum=MAX_ROUTE_NODE
    )
    upper = _require_integer(
        upper_bound, name="upper_bound", minimum=1, maximum=MAX_ROUTE_NODE
    )
    if upper < lower:
        raise InvalidRouteRequest("upper_bound must be greater than or equal to lower_bound")
    return lower, upper


def _move_options(
    current: int,
    *,
    lower_bound: int,
    upper_bound: int,
) -> tuple[tuple[int, MoveName], ...]:
    candidates: tuple[tuple[MoveName, int | None], ...] = (
        ("+1", current + 1),
        ("-1", current - 1),
        ("*2", current * 2),
        ("//2", current // 2 if current % 2 == 0 else None),
    )

    seen: set[int] = set()
    result: list[tuple[int, MoveName]] = []
    for move, candidate in candidates:
        if (
            candidate is not None
            and lower_bound <= candidate <= upper_bound
            and candidate not in seen
        ):
            seen.add(candidate)
            result.append((candidate, move))
    return tuple(result)


def allowed_moves(
    current: int,
    *,
    lower_bound: int = 1,
    upper_bound: int,
) -> tuple[int, ...]:
    """Return bounded, deduplicated neighbors in stable operation order.

    The operation order is ``+1``, ``-1``, ``*2``, then exact-even ``//2``.
    Duplicate destinations keep the earliest operation in that order.
    """

    lower, upper = _validate_bounds(lower_bound, upper_bound)
    node = _require_integer(current, name="current")
    if not lower <= node <= upper:
        raise InvalidRouteRequest(
            f"current must be within the inclusive bounds [{lower}, {upper}]"
        )
    return tuple(
        destination
        for destination, _ in _move_options(
            node,
            lower_bound=lower,
            upper_bound=upper,
        )
    )


def node_friction(node: int, /, *, scale: int = 1) -> int:
    """Return zero for a prime node, otherwise divisor count times *scale*."""

    value = _require_integer(
        node, name="node", minimum=1, maximum=MAX_ROUTE_NODE
    )
    multiplier = _require_integer(
        scale,
        name="scale",
        minimum=1,
        maximum=MAX_FRICTION_SCALE,
    )
    return 0 if is_prime(value) else divisor_count(value) * multiplier


class PrimeRoutePlanner:
    """Plan deterministic routes inside a finite, positive-integer graph.

    Routes minimize total destination-node friction, then hop count. Remaining
    ties retain first deterministic discovery under the stable move order
    documented by :func:`allowed_moves`. Starting-node friction is excluded.
    """

    def __init__(
        self,
        *,
        upper_bound: int,
        lower_bound: int = 1,
        friction_scale: int = 1,
        search_limit: int = 10_000,
    ) -> None:
        self.lower_bound, self.upper_bound = _validate_bounds(
            lower_bound,
            upper_bound,
        )
        self.friction_scale = _require_integer(
            friction_scale,
            name="friction_scale",
            minimum=1,
            maximum=MAX_FRICTION_SCALE,
        )
        self.search_limit = _require_integer(
            search_limit,
            name="search_limit",
            minimum=1,
            maximum=MAX_SEARCH_LIMIT,
        )

    def route_to_prime(
        self,
        start: int,
        target: int,
        *,
        search_limit: int | None = None,
    ) -> RouteResult:
        """Plan a minimum-friction route to a chosen prime target."""

        start_node = self._validate_node(start, name="start")
        target_node = self._validate_node(target, name="target")
        if not is_prime(target_node):
            raise InvalidRouteRequest("target must be prime")
        return self._search(
            start=start_node,
            mode="chosen_prime",
            target=target_node,
            search_limit=search_limit,
        )

    def route_to_nearest_prime(
        self,
        start: int,
        *,
        search_limit: int | None = None,
    ) -> RouteResult:
        """Plan to the best reachable prime under the route ordering."""

        start_node = self._validate_node(start, name="start")
        return self._search(
            start=start_node,
            mode="nearest_prime",
            target=None,
            search_limit=search_limit,
        )

    def _validate_node(self, node: int, *, name: str) -> int:
        value = _require_integer(node, name=name)
        if not self.lower_bound <= value <= self.upper_bound:
            raise InvalidRouteRequest(
                f"{name} must be within the inclusive bounds "
                f"[{self.lower_bound}, {self.upper_bound}]"
            )
        return value

    def _resolved_limit(self, override: int | None) -> int:
        if override is None:
            return self.search_limit
        return _require_integer(
            override,
            name="search_limit",
            minimum=1,
            maximum=MAX_SEARCH_LIMIT,
        )

    def _friction(self, node: int) -> int:
        return node_friction(node, scale=self.friction_scale)

    def _search(
        self,
        *,
        start: int,
        mode: RouteMode,
        target: int | None,
        search_limit: int | None,
    ) -> RouteResult:
        limit = self._resolved_limit(search_limit)

        # Labels compare total friction then hops. Stable neighbor order plus a
        # monotonic queue serial makes remaining ties deterministic without an
        # exponentially growing encoded path key.
        start_label = (0, 0)
        labels: dict[int, tuple[int, int]] = {start: start_label}
        predecessors: dict[int, tuple[int, MoveName, int]] = {}
        serial = count()
        queue: list[tuple[int, int, int, int]] = [(0, 0, next(serial), start)]
        explored_nodes = 0

        while queue:
            friction, hops, _, current = heapq.heappop(queue)
            label = (friction, hops)
            if labels.get(current) != label:
                continue

            if explored_nodes >= limit:
                raise SearchLimitExceeded(
                    limit=limit,
                    explored_nodes=explored_nodes,
                )
            explored_nodes += 1

            goal_reached = (
                current == target if mode == "chosen_prime" else is_prime(current)
            )
            if goal_reached:
                return self._build_result(
                    mode=mode,
                    start=start,
                    target=current,
                    predecessors=predecessors,
                    labels=labels,
                    explored_nodes=explored_nodes,
                )

            for neighbor, move in _move_options(
                current,
                lower_bound=self.lower_bound,
                upper_bound=self.upper_bound,
            ):
                step_friction = self._friction(neighbor)
                next_label = (
                    friction + step_friction,
                    hops + 1,
                )
                if next_label >= labels.get(neighbor, (float("inf"),) * 2):
                    continue

                labels[neighbor] = next_label
                predecessors[neighbor] = (current, move, step_friction)
                heapq.heappush(
                    queue,
                    (*next_label, next(serial), neighbor),
                )

        destination = f"prime target {target}" if target is not None else "any prime"
        raise RouteNotFound(
            f"no route from {start} to {destination} exists within inclusive bounds "
            f"[{self.lower_bound}, {self.upper_bound}]"
        )

    def _build_result(
        self,
        *,
        mode: RouteMode,
        start: int,
        target: int,
        predecessors: dict[int, tuple[int, MoveName, int]],
        labels: dict[int, tuple[int, int]],
        explored_nodes: int,
    ) -> RouteResult:
        reversed_nodes = [target]
        while reversed_nodes[-1] != start:
            reversed_nodes.append(predecessors[reversed_nodes[-1]][0])
        nodes = tuple(reversed(reversed_nodes))

        steps: list[RouteStep] = []
        for index, node in enumerate(nodes):
            if index == 0:
                move: MoveName | None = None
                friction = 0
            else:
                _, move, friction = predecessors[node]
            steps.append(
                RouteStep(
                    index=index,
                    node=node,
                    move=move,
                    friction=friction,
                    cumulative_friction=labels[node][0],
                    prime=is_prime(node),
                )
            )

        total_friction, hops = labels[target]
        return RouteResult(
            mode=mode,
            start=start,
            target=target,
            lower_bound=self.lower_bound,
            upper_bound=self.upper_bound,
            steps=tuple(steps),
            total_friction=total_friction,
            hops=hops,
            explored_nodes=explored_nodes,
        )
