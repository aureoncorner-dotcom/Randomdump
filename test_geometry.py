from __future__ import annotations

from datetime import datetime, timezone
import math
import unittest

from prime_axis_engine.geometry import (
    accumulate_cocycle,
    analyze_quotient_descent,
    circular_distance,
    cocycle_increment,
    compose_cocycle,
    evaluate_closure,
    make_geometry_snapshot,
    normalize_phase,
    quotient_label,
    return_residual,
)
from prime_axis_engine.model import (
    AxisSnapshot,
    ClockSnapshot,
    ClosureStatus,
    MultiAxisTickEvent,
    Severity,
)


class GeometryTests(unittest.TestCase):
    def test_phase_normalization_and_wrap_distance(self) -> None:
        self.assertAlmostEqual(normalize_phase(1.25), 0.25)
        self.assertAlmostEqual(normalize_phase(-0.25), 0.75)
        self.assertEqual(normalize_phase(-0.0), 0.0)
        self.assertEqual(math.copysign(1.0, normalize_phase(-0.0)), 1.0)
        self.assertAlmostEqual(circular_distance(0.99, 0.01), 0.02)
        self.assertAlmostEqual(circular_distance(-0.01, 1.01), 0.02)

    def test_phase_functions_reject_non_finite_values(self) -> None:
        for bad in (math.nan, math.inf, -math.inf):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    normalize_phase(bad)
                with self.assertRaises(ValueError):
                    circular_distance(0.0, bad)

    def test_quotient_return_residual_identifies_orbit_rotations(self) -> None:
        self.assertEqual(quotient_label(3), "C_3")
        self.assertAlmostEqual(return_residual(0.1, 0.1 + 1.0 / 3.0, 3), 0.0, places=14)
        self.assertAlmostEqual(return_residual(0.1, 0.12, 3), 0.02)

    def test_closure_has_closed_failed_and_unresolved_states(self) -> None:
        self.assertIs(evaluate_closure(0.01, 0.01), ClosureStatus.CLOSED)
        self.assertIs(evaluate_closure(0.0101, 0.01), ClosureStatus.FAILED)
        self.assertIs(evaluate_closure(0.0, 0.01, evidence_complete=False), ClosureStatus.UNRESOLVED)

    def test_integer_cocycle_composition_and_accumulation_are_exact(self) -> None:
        modulus = 11
        a, b, c = 9, 2, 7
        ab = cocycle_increment(a, b, modulus)
        bc = cocycle_increment(b, c, modulus)
        ac = cocycle_increment(a, c, modulus)
        self.assertEqual(compose_cocycle(ab, bc, modulus), ac)
        self.assertEqual(accumulate_cocycle(a, [ab, bc], modulus), c % modulus)
        self.assertEqual(accumulate_cocycle(-2, [15, -7, 22], modulus), (-2 + 15 - 7 + 22) % modulus)

    def test_finite_domain_descent_reports_proof_scope_and_counterexample(self) -> None:
        closed = analyze_quotient_descent(
            range(8),
            quotient=lambda value: value % 2,
            update=lambda value: value + 2,
        )
        self.assertIs(closed.status, ClosureStatus.CLOSED)
        self.assertEqual(closed.domain_size, 8)
        self.assertEqual(closed.quotient_class_count, 2)
        self.assertIsNone(closed.witness)

        failed = analyze_quotient_descent(
            range(8),
            quotient=lambda value: value % 2,
            update=lambda value: value // 2,
        )
        self.assertIs(failed.status, ClosureStatus.FAILED)
        self.assertIsNotNone(failed.witness)
        self.assertEqual(failed.witness.current_label, 0)  # type: ignore[union-attr]
        self.assertNotEqual(
            failed.witness.first_next_label,  # type: ignore[union-attr]
            failed.witness.second_next_label,  # type: ignore[union-attr]
        )

        unresolved = analyze_quotient_descent(
            [], quotient=lambda value: value, update=lambda value: value
        )
        self.assertIs(unresolved.status, ClosureStatus.UNRESOLVED)

    def test_snapshots_distinguish_index_and_clocks_and_validate_ranges(self) -> None:
        clock = ClockSnapshot(
            opportunity_index=4,
            lattice_time_s=1.0,
            monotonic_time_s=1.125,
            wall_time_utc=datetime(2026, 9, 2, 18, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(clock.opportunity_index, 4)
        self.assertAlmostEqual(clock.slip_s, 0.125)
        with self.assertRaisesRegex(ValueError, "timezone-aware UTC"):
            ClockSnapshot(0, 0.0, 0.0, datetime(2026, 9, 2))
        with self.assertRaisesRegex(ValueError, "finite"):
            ClockSnapshot(0, math.nan, 0.0, datetime.now(timezone.utc))

    def test_multi_axis_tick_is_atomic_and_opportunity_synchronized(self) -> None:
        clock = ClockSnapshot(7, 1.75, 1.8, datetime.now(timezone.utc))
        first_geometry = make_geometry_snapshot(
            opportunity_index=7,
            expected_phase=0.1,
            observed_phase=0.11,
            quotient_order=2,
            tolerance=0.02,
        )
        second_geometry = make_geometry_snapshot(
            opportunity_index=7,
            expected_phase=0.7,
            observed_phase=0.9,
            quotient_order=1,
            tolerance=0.02,
            evidence_complete=False,
        )
        event = MultiAxisTickEvent(
            clock=clock,
            axes={
                "prime": AxisSnapshot(11, True, first_geometry),
                "return": AxisSnapshot(12, False, second_geometry),
            },
            max_severity=Severity.WARNING,
            metadata={"source": "simulation"},
        )
        encoded = event.to_dict()
        self.assertEqual(encoded["event_type"], "multi_axis_tick")
        self.assertEqual(list(encoded["axes"]), ["prime", "return"])
        self.assertEqual(encoded["max_severity"], "WARNING")
        with self.assertRaises(TypeError):
            event.axes["new"] = AxisSnapshot(13, True, first_geometry)  # type: ignore[index]

        mismatched = make_geometry_snapshot(
            opportunity_index=8,
            expected_phase=0.0,
            observed_phase=0.0,
        )
        with self.assertRaisesRegex(ValueError, "does not share"):
            MultiAxisTickEvent(
                clock=clock,
                axes={"bad": AxisSnapshot(13, True, mismatched)},
                max_severity=Severity.INFO,
            )

    def test_geometry_snapshot_normalizes_inputs_and_carries_typed_status(self) -> None:
        snapshot = make_geometry_snapshot(
            opportunity_index=2,
            expected_phase=1.9,
            observed_phase=-0.09,
            quotient_order=4,
            tolerance=0.02,
        )
        self.assertAlmostEqual(snapshot.expected_phase, 0.9)
        self.assertAlmostEqual(snapshot.observed_phase, 0.91)
        self.assertAlmostEqual(snapshot.residual, 0.01)
        self.assertIs(snapshot.closure_status, ClosureStatus.CLOSED)

    def test_snapshot_invariants_and_nested_metadata_are_immutable(self) -> None:
        clock = ClockSnapshot(0, 0.0, 0.0, datetime.now(timezone.utc))
        geometry = make_geometry_snapshot(
            opportunity_index=0,
            expected_phase=0.1,
            observed_phase=0.1,
        )
        with self.assertRaisesRegex(ValueError, "is_prime is inconsistent"):
            AxisSnapshot(12, True, geometry)

        supplied = {"nested": [1, 2]}
        event = MultiAxisTickEvent(
            clock=clock,
            axes={"main": AxisSnapshot(11, True, geometry)},
            max_severity=Severity.INFO,
            metadata=supplied,
        )
        supplied["nested"].append(3)
        frozen_nested = event.metadata["nested"]
        self.assertIsInstance(frozen_nested, tuple)
        self.assertEqual(frozen_nested, (1, 2))
        self.assertEqual(event.to_dict()["metadata"], {"nested": [1, 2]})
        with self.assertRaises(AttributeError):
            frozen_nested.append(4)  # type: ignore[union-attr]


if __name__ == "__main__":
    unittest.main()
