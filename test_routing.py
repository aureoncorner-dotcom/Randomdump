from __future__ import annotations

import unittest

from prime_axis_engine.routing import (
    InvalidRouteRequest,
    PrimeRoutePlanner,
    RouteNotFound,
    SearchLimitExceeded,
    allowed_moves,
    node_friction,
)


class AllowedMovesTests(unittest.TestCase):
    def test_moves_are_bounded_deduplicated_and_stable(self) -> None:
        self.assertEqual(allowed_moves(1, upper_bound=10), (2,))
        self.assertEqual(allowed_moves(2, upper_bound=10), (3, 1, 4))
        self.assertEqual(allowed_moves(10, upper_bound=10), (9, 5))

    def test_rejects_invalid_or_out_of_bounds_values(self) -> None:
        with self.assertRaises(InvalidRouteRequest):
            allowed_moves(-1, upper_bound=10)
        with self.assertRaises(InvalidRouteRequest):
            allowed_moves(True, upper_bound=10)
        with self.assertRaises(InvalidRouteRequest):
            allowed_moves(2, lower_bound=5, upper_bound=4)


class FrictionTests(unittest.TestCase):
    def test_prime_and_composite_friction(self) -> None:
        self.assertEqual(node_friction(113, scale=15), 0)
        self.assertEqual(node_friction(12, scale=15), 90)

    def test_rejects_invalid_scale(self) -> None:
        with self.assertRaises(InvalidRouteRequest):
            node_friction(12, scale=0)


class RoutePlannerTests(unittest.TestCase):
    def test_chosen_prime_route_is_typed_and_multi_criteria_optimal(self) -> None:
        planner = PrimeRoutePlanner(upper_bound=20)
        result = planner.route_to_prime(4, 7)

        # 4 -> 8 -> 7 costs the same as longer alternatives, so hops win.
        self.assertEqual(result.nodes, (4, 8, 7))
        self.assertEqual(tuple(step.move for step in result.steps), (None, "*2", "-1"))
        self.assertEqual(result.total_friction, 4)
        self.assertEqual(result.hops, 2)
        self.assertEqual(result.steps[-1].cumulative_friction, 4)
        self.assertTrue(result.steps[-1].prime)
        self.assertEqual(result.mode, "chosen_prime")

    def test_nearest_prime_uses_stable_move_tie_break(self) -> None:
        planner = PrimeRoutePlanner(upper_bound=10)
        first = planner.route_to_nearest_prime(4)
        second = planner.route_to_nearest_prime(4)

        # Nodes 5, 3, and 2 are all zero-friction, one-hop primes. +1 wins.
        self.assertEqual(first.nodes, (4, 5))
        self.assertEqual(first, second)
        self.assertEqual(first.mode, "nearest_prime")

    def test_prime_start_is_a_zero_hop_nearest_route(self) -> None:
        result = PrimeRoutePlanner(upper_bound=20).route_to_nearest_prime(17)
        self.assertEqual(result.nodes, (17,))
        self.assertEqual(result.total_friction, 0)
        self.assertEqual(result.hops, 0)

    def test_validates_target_and_bounds_before_search(self) -> None:
        planner = PrimeRoutePlanner(upper_bound=20)
        with self.assertRaises(InvalidRouteRequest):
            planner.route_to_prime(4, 9)
        with self.assertRaises(InvalidRouteRequest):
            planner.route_to_prime(-1, 7)
        with self.assertRaises(InvalidRouteRequest):
            planner.route_to_prime(4, 23)

    def test_search_limit_is_enforced(self) -> None:
        planner = PrimeRoutePlanner(upper_bound=100)
        with self.assertRaises(SearchLimitExceeded) as caught:
            planner.route_to_prime(48, 97, search_limit=1)
        self.assertEqual(caught.exception.limit, 1)
        self.assertEqual(caught.exception.explored_nodes, 1)

    def test_reports_no_prime_in_bounded_graph(self) -> None:
        planner = PrimeRoutePlanner(lower_bound=14, upper_bound=16)
        with self.assertRaises(RouteNotFound):
            planner.route_to_nearest_prime(15)


if __name__ == "__main__":
    unittest.main()

