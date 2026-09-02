from __future__ import annotations

from datetime import datetime, timezone
import json
import math
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from prime_axis_engine.engine import AxisSpec, EngineConfig, SimulationEngine
from prime_axis_engine.geometry import make_geometry_snapshot
from prime_axis_engine.ledger import (
    GENESIS_HASH,
    SCHEMA_VERSION,
    DurabilityPolicy,
    LedgerWriter,
    audit_ledger,
    canonical_json,
)
from prime_axis_engine.model import (
    AxisSnapshot,
    ClockSnapshot,
    MultiAxisTickEvent,
    Severity,
)
from prime_axis_engine.number_theory import is_prime


def _event(index: int = 0) -> MultiAxisTickEvent:
    node = 12 + index
    if index == 0:
        status = "ACTIVE"
        axis_message = "advanced from 11 to 12"
    elif index == 1:
        status = "ANCHORED"
        axis_message = "anchored at target 13"
    else:
        status = "ACTIVE"
        axis_message = f"advanced to fixture node {node}"
    clock = ClockSnapshot(
        opportunity_index=index,
        lattice_time_s=index * 0.25,
        monotonic_time_s=index * 0.25 + 0.01,
        wall_time_utc=datetime(2026, 9, 2, 18, 0, index, tzinfo=timezone.utc),
    )
    geometry = make_geometry_snapshot(
        opportunity_index=index,
        expected_phase=0.12,
        observed_phase=(node - 1) / 100,
        quotient_order=3,
        tolerance=0.01,
    )
    return MultiAxisTickEvent(
        clock=clock,
        axes={"main": AxisSnapshot(node=node, is_prime=is_prime(node), geometry=geometry)},
        max_severity=Severity.INFO,
        message=f"synchronized opportunity {index}",
        metadata={
            "axis_states": {
                "main": {
                    "status": status,
                    "advanced": True,
                    "incident_count": 0,
                    "rerouted": False,
                    "message": axis_message,
                }
            },
            "phase_basis": "normalized bounded-route position",
        },
    )


def _simulation_start() -> dict[str, object]:
    return {
        "event_type": "simulation_start",
        "config": {
            "lower_bound": 1,
            "upper_bound": 100,
            "friction_scale": 100,
            "search_limit": 1_000,
            "max_ticks": 10,
            "max_axes": 4,
            "max_incidents": 3,
            "reroute_after_incidents": 2,
            "lattice_period_s": 0.25,
            "pace": False,
        },
        "axes": [
            {
                "label": "main",
                "start": 11,
                "target": 13,
                "quotient_order": 3,
                "tolerance": 0.01,
            }
        ],
        "phase_basis": "normalized bounded-route position",
        "clock_contract": {
            "opportunity": "discrete logical index",
            "lattice": "configured ideal model time",
            "monotonic": "elapsed execution observation",
            "utc": "human correlation only",
        },
    }


def _simulation_complete(*, opportunities: int = 2, label: str = "main") -> dict[str, object]:
    return {
        "event_type": "simulation_complete",
        "succeeded": True,
        "opportunities": opportunities,
        "axes": [
            {
                "label": label,
                "start": 11,
                "target": 13,
                "status": "ANCHORED",
                "current_node": 13,
                "incidents": 0,
                "reroutes": 0,
                "visited_nodes": [11, 12, 13],
                "breached_nodes": [],
                "error": None,
            }
        ],
    }


class LedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self._temporary_directory.name)

    def tearDown(self) -> None:
        self._temporary_directory.cleanup()

    def test_writer_emits_canonical_chained_records_and_valid_seal(self) -> None:
        path = self.root / "events.jsonl"
        with LedgerWriter(path, run_id="run-001", durability=DurabilityPolicy.FLUSH) as writer:
            first = writer.append(_event(0))
            second = writer.append(_event(1))
        self.assertEqual(first["schema_version"], SCHEMA_VERSION)
        self.assertEqual(first["seq"], 0)
        self.assertEqual(first["prev_hash"], GENESIS_HASH)
        self.assertEqual(second["seq"], 1)
        self.assertEqual(second["prev_hash"], first["record_hash"])

        raw_lines = path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(raw_lines), 3)
        for line in raw_lines:
            self.assertEqual(line, canonical_json(json.loads(line)))

        report = audit_ledger(path)
        self.assertTrue(report.valid)
        self.assertTrue(report.ok)
        self.assertTrue(report.sealed)
        self.assertFalse(report.truncated)
        self.assertFalse(report.tampered)
        self.assertEqual(report.run_id, "run-001")
        self.assertEqual(report.record_count, 3)
        self.assertEqual(report.event_count, 2)
        self.assertEqual(report.last_seq, 2)
        self.assertEqual(report.issues, ())

    def test_writer_accepts_arbitrary_validated_mapping_and_rejects_nan(self) -> None:
        path = self.root / "mapping.jsonl"
        with LedgerWriter(path, run_id="mapping") as writer:
            record = writer.append({"kind": "custom", "values": [1, 2.5, None]})
            self.assertEqual(record["payload"]["kind"], "custom")
            with self.assertRaisesRegex(ValueError, "NaN or Infinity"):
                writer.append({"bad": math.nan})
        self.assertTrue(audit_ledger(path).valid)

    def test_deep_json_and_semantically_invalid_ticks_return_findings(self) -> None:
        deep_path = self.root / "deep.jsonl"
        deep_path.write_text(
            '{"x":' + ('[' * 1_000) + '0' + (']' * 1_000) + '}\n',
            encoding="utf-8",
        )
        deep_report = audit_ledger(deep_path)
        self.assertFalse(deep_report.valid)
        self.assertIn("JSON_NESTING", {issue.code for issue in deep_report.issues})

        semantic_path = self.root / "semantic.jsonl"
        invalid = _event(0).to_dict()
        invalid["axes"] = {}
        invalid["max_severity"] = "INVENTED"
        with LedgerWriter(semantic_path, run_id="semantic-test") as writer:
            writer.append(invalid)
        semantic_report = audit_ledger(semantic_path)
        self.assertFalse(semantic_report.valid)
        codes = {issue.code for issue in semantic_report.issues}
        self.assertIn("SEMANTIC_AXES", codes)
        self.assertIn("SEMANTIC_SEVERITY", codes)

    def test_audit_enforces_cross_record_simulation_consistency(self) -> None:
        valid_path = self.root / "valid-simulation.jsonl"
        with LedgerWriter(valid_path, run_id="valid-simulation") as writer:
            writer.append(_simulation_start())
            writer.append(_event(0))
            writer.append(_event(1))
            writer.append(_simulation_complete())
        self.assertTrue(audit_ledger(valid_path).valid)

        cases = (
            (
                "swapped-ticks.jsonl",
                (_simulation_start(), _event(1), _event(0), _simulation_complete()),
                "SEMANTIC_OPPORTUNITY_SEQUENCE",
            ),
            (
                "false-count.jsonl",
                (_simulation_start(), _event(0), _event(1), _simulation_complete(opportunities=999)),
                "SEMANTIC_COMPLETION_COUNT",
            ),
            (
                "changed-axis.jsonl",
                (_simulation_start(), _event(0), _event(1), _simulation_complete(label="other")),
                "SEMANTIC_AXIS_SET_CHANGED",
            ),
        )
        for filename, events, expected_code in cases:
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    for event in events:
                        writer.append(event)
                report = audit_ledger(path)
                self.assertFalse(report.valid)
                self.assertIn(expected_code, {issue.code for issue in report.issues})

    def test_audit_requires_one_terminal_completion_after_a_start(self) -> None:
        missing_path = self.root / "missing-completion.jsonl"
        with LedgerWriter(missing_path, run_id="missing-completion") as writer:
            writer.append(_simulation_start())
            writer.append(_event(0))
        missing_report = audit_ledger(missing_path)
        self.assertFalse(missing_report.valid)
        self.assertIn(
            "SEMANTIC_MISSING_COMPLETION",
            {issue.code for issue in missing_report.issues},
        )

        after_path = self.root / "event-after-completion.jsonl"
        with LedgerWriter(after_path, run_id="event-after-completion") as writer:
            writer.append(_simulation_start())
            writer.append(_event(0))
            writer.append(_simulation_complete(opportunities=1))
            writer.append(_event(1))
        after_report = audit_ledger(after_path)
        self.assertFalse(after_report.valid)
        self.assertIn(
            "SEMANTIC_EVENT_AFTER_COMPLETION",
            {issue.code for issue in after_report.issues},
        )

        orphan_path = self.root / "completion-without-start.jsonl"
        with LedgerWriter(orphan_path, run_id="completion-without-start") as writer:
            writer.append(_simulation_complete(opportunities=0))
        orphan_report = audit_ledger(orphan_path)
        self.assertFalse(orphan_report.valid)
        self.assertIn(
            "SEMANTIC_COMPLETION_WITHOUT_START",
            {issue.code for issue in orphan_report.issues},
        )

    def test_audit_rejects_cross_record_contract_and_clock_forgery(self) -> None:
        single_tick = _event(0).to_dict()
        single_tick = {
            "event_type": "tick",
            "clock": single_tick["clock"],
            "axis": single_tick["axes"]["main"],
            "severity": "INFO",
            "message": "not atomic",
            "metadata": {},
        }

        changed_order_start = _simulation_start()
        changed_order_start["axes"][0]["quotient_order"] = 5  # type: ignore[index]

        contradictory_completion = _simulation_complete()
        contradictory_axis = contradictory_completion["axes"][0]  # type: ignore[index]
        contradictory_axis.update(  # type: ignore[union-attr]
            {
                "start": 17,
                "target": 19,
                "current_node": 19,
                "visited_nodes": [17, 19],
            }
        )

        outside_tick = _event(0).to_dict()
        outside_tick["axes"]["main"]["node"] = 101  # type: ignore[index]
        outside_tick["axes"]["main"]["is_prime"] = True  # type: ignore[index]

        regressed_tick = _event(1).to_dict()
        regressed_tick["clock"]["monotonic_time_s"] = 0.0  # type: ignore[index]
        regressed_tick["clock"]["slip_s"] = -0.25  # type: ignore[index]

        bad_lattice_tick = _event(1).to_dict()
        bad_lattice_tick["clock"]["lattice_time_s"] = 0.5  # type: ignore[index]
        bad_lattice_tick["clock"]["slip_s"] = -0.24  # type: ignore[index]

        false_phase_tick = _event(0).to_dict()
        false_phase_tick["axes"]["main"]["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=0,
            expected_phase=0.13,
            observed_phase=0.10,
            quotient_order=3,
            tolerance=0.01,
        ).to_dict()

        large_period_start = _simulation_start()
        large_period_start["config"]["lattice_period_s"] = 1_000_000_000_000.0  # type: ignore[index]
        large_period_tick = _event(1).to_dict()
        large_period_tick["clock"]["lattice_time_s"] = 1_000_000_000_000.5  # type: ignore[index]
        large_period_tick["clock"]["monotonic_time_s"] = 1_000_000_000_000.75  # type: ignore[index]
        large_period_tick["clock"]["slip_s"] = 0.25  # type: ignore[index]

        hidden_tick = _event(0).to_dict()
        hidden_tick.pop("event_type")
        hidden_completion = _simulation_complete(opportunities=0)
        hidden_completion["succeeded"] = False
        hidden_axis = hidden_completion["axes"][0]  # type: ignore[index]
        hidden_axis.update(  # type: ignore[union-attr]
            {
                "status": "FAILED",
                "current_node": 11,
                "visited_nodes": [11],
                "error": "route initialization reached its search limit",
            }
        )

        cases = (
            (
                "single-tick-bypass.jsonl",
                (_simulation_start(), single_tick, _simulation_complete(opportunities=0)),
                "SEMANTIC_UNEXPECTED_SIMULATION_EVENT",
            ),
            (
                "axis-contract-drift.jsonl",
                (changed_order_start, _event(0), _event(1), _simulation_complete()),
                "SEMANTIC_AXIS_CONTRACT_CHANGED",
            ),
            (
                "completion-contract-drift.jsonl",
                (_simulation_start(), _event(0), _event(1), contradictory_completion),
                "SEMANTIC_AXIS_CONTRACT_CHANGED",
            ),
            (
                "node-outside-bounds.jsonl",
                (_simulation_start(), outside_tick, _event(1), _simulation_complete()),
                "SEMANTIC_NODE_OUTSIDE_BOUNDS",
            ),
            (
                "monotonic-regression.jsonl",
                (_simulation_start(), _event(0), regressed_tick, _simulation_complete()),
                "SEMANTIC_CLOCK_REGRESSION",
            ),
            (
                "lattice-contract.jsonl",
                (_simulation_start(), _event(0), bad_lattice_tick, _simulation_complete()),
                "SEMANTIC_CLOCK_CONTRACT",
            ),
            (
                "phase-contract.jsonl",
                (_simulation_start(), false_phase_tick, _event(1), _simulation_complete()),
                "SEMANTIC_PHASE_CONTRACT",
            ),
            (
                "large-lattice-drift.jsonl",
                (large_period_start, _event(0), large_period_tick, _simulation_complete()),
                "SEMANTIC_CLOCK_CONTRACT",
            ),
            (
                "hidden-event-type.jsonl",
                (_simulation_start(), hidden_tick, hidden_completion),
                "SEMANTIC_UNEXPECTED_SIMULATION_EVENT",
            ),
        )
        for filename, events, expected_code in cases:
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    for event in events:
                        writer.append(event)
                report = audit_ledger(path)
                self.assertFalse(report.valid)
                self.assertIn(expected_code, {issue.code for issue in report.issues})

    def test_start_receipt_mirrors_engine_limits_and_label_rules(self) -> None:
        oversized = _simulation_start()
        oversized["config"]["max_ticks"] = 10**1_000  # type: ignore[index]

        controlled = _simulation_start()
        controlled["axes"][0]["label"] = "main\nforged"  # type: ignore[index]

        cases = (
            ("oversized-start.jsonl", oversized, "SEMANTIC_START_CONFIG"),
            ("controlled-label.jsonl", controlled, "SEMANTIC_START_AXIS"),
        )
        for filename, start, expected_code in cases:
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    writer.append(start)
                    writer.append(_simulation_complete(opportunities=0))
                report = audit_ledger(path)
                self.assertFalse(report.valid)
                self.assertIn(expected_code, {issue.code for issue in report.issues})

        excess_axes = _simulation_start()
        excess_axes["config"]["max_axes"] = 1  # type: ignore[index]
        excess_axes["axes"].append(  # type: ignore[union-attr]
            {
                "label": "second",
                "start": 17,
                "target": 19,
                "quotient_order": 3,
                "tolerance": 0.01,
            }
        )
        excess_path = self.root / "excess-axes-no-replay.jsonl"
        with LedgerWriter(excess_path, run_id="excess-axes-no-replay") as writer:
            writer.append(excess_axes)
            writer.append(_simulation_complete(opportunities=0))
        with patch.object(
            SimulationEngine,
            "_initialize_axis",
            side_effect=AssertionError("invalid starts must not trigger route replay"),
        ):
            excess_report = audit_ledger(excess_path)
        self.assertFalse(excess_report.valid)
        self.assertIn(
            "SEMANTIC_START_AXES",
            {issue.code for issue in excess_report.issues},
        )

    def test_completion_statuses_are_terminal_and_explain_failures(self) -> None:
        initialization_failure_start = _simulation_start()
        initialization_failure_start["config"]["search_limit"] = 1  # type: ignore[index]
        valid_failure = _simulation_complete(opportunities=0)
        valid_failure["succeeded"] = False
        valid_axis = valid_failure["axes"][0]  # type: ignore[index]
        valid_axis.update(  # type: ignore[union-attr]
            {
                "status": "FAILED",
                "current_node": 11,
                "visited_nodes": [11],
                "error": (
                    "search limit of 1 node expansions was reached "
                    "after exploring 1 nodes"
                ),
            }
        )
        valid_path = self.root / "valid-initialization-failure.jsonl"
        with LedgerWriter(valid_path, run_id="valid-initialization-failure") as writer:
            writer.append(initialization_failure_start)
            writer.append(valid_failure)
        self.assertTrue(audit_ledger(valid_path).valid)

        invented_initialization_failure = json.loads(json.dumps(valid_failure))

        active = json.loads(json.dumps(valid_failure))
        active["axes"][0]["status"] = "ACTIVE"

        failed_at_target = json.loads(json.dumps(valid_failure))
        failed_at_target["axes"][0]["current_node"] = 13
        failed_at_target["axes"][0]["visited_nodes"] = [11, 13]

        unexplained_failure = json.loads(json.dumps(valid_failure))
        unexplained_failure["axes"][0]["error"] = None

        cases = (
            (
                "invented-initialization-failure.jsonl",
                invented_initialization_failure,
                "SEMANTIC_COMPLETION_REPLAY",
            ),
            ("active-completion.jsonl", active, "SEMANTIC_COMPLETION_STATUS"),
            ("failed-at-target.jsonl", failed_at_target, "SEMANTIC_COMPLETION_STATUS"),
            ("unexplained-failure.jsonl", unexplained_failure, "SEMANTIC_COMPLETION_ERROR"),
        )
        for filename, completion, expected_code in cases:
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    writer.append(
                        _simulation_start()
                        if filename == "invented-initialization-failure.jsonl"
                        else initialization_failure_start
                    )
                    writer.append(completion)
                report = audit_ledger(path)
                self.assertFalse(report.valid)
                self.assertIn(expected_code, {issue.code for issue in report.issues})

    def test_audit_replays_lifecycle_and_reroute_receipts(self) -> None:
        premature = _simulation_complete(opportunities=1)
        premature["succeeded"] = False
        premature_axis = premature["axes"][0]  # type: ignore[index]
        premature_axis.update(  # type: ignore[union-attr]
            {
                "status": "FAILED",
                "current_node": 12,
                "visited_nodes": [11, 12],
                "error": "invented early failure",
            }
        )
        premature_path = self.root / "premature-failure.jsonl"
        with LedgerWriter(premature_path, run_id="premature-failure") as writer:
            writer.append(_simulation_start())
            writer.append(_event(0))
            writer.append(premature)
        premature_report = audit_ledger(premature_path)
        self.assertFalse(premature_report.valid)
        self.assertIn(
            "SEMANTIC_COMPLETION_REPLAY",
            {issue.code for issue in premature_report.issues},
        )

        config = EngineConfig(
            lower_bound=1,
            upper_bound=100,
            friction_scale=100,
            search_limit=1_000,
            max_ticks=3,
            max_axes=4,
            max_incidents=3,
            reroute_after_incidents=2,
            lattice_period_s=0.25,
            pace=False,
        )
        spec = AxisSpec(
            label="main",
            start=11,
            target=17,
            quotient_order=3,
            tolerance=0.0,
        )
        result = SimulationEngine(
            config,
            monotonic_clock=lambda: 0.0,
            wall_clock=lambda: datetime(2026, 9, 2, tzinfo=timezone.utc),
        ).run((spec,))
        self.assertGreaterEqual(result.axes[0].reroutes, 1)
        forged_completion = result.summary_dict()
        forged_completion["axes"][0]["reroutes"] = 0  # type: ignore[index]
        reroute_path = self.root / "false-low-reroutes.jsonl"
        with LedgerWriter(reroute_path, run_id="false-low-reroutes") as writer:
            writer.append(
                {
                    "event_type": "simulation_start",
                    "config": config.to_dict(),
                    "axes": [spec.to_dict()],
                    "phase_basis": "normalized bounded-route position",
                    "clock_contract": {
                        "opportunity": "discrete logical index",
                        "lattice": "configured ideal model time",
                        "monotonic": "elapsed execution observation",
                        "utc": "human correlation only",
                    },
                }
            )
            for tick in result.ticks:
                writer.append(tick.to_multi_axis_event())
            writer.append(forged_completion)
        reroute_report = audit_ledger(reroute_path)
        self.assertFalse(reroute_report.valid)
        self.assertIn(
            "SEMANTIC_COMPLETION_REPLAY",
            {issue.code for issue in reroute_report.issues},
        )

        suppressed_tick = result.ticks[0].to_multi_axis_event().to_dict()
        suppressed_tick["max_severity"] = "INFO"
        suppressed_tick["message"] = "fine"
        suppressed_tick["metadata"] = {}
        description_path = self.root / "suppressed-tick-description.jsonl"
        with LedgerWriter(
            description_path, run_id="suppressed-tick-description"
        ) as writer:
            writer.append(
                {
                    "event_type": "simulation_start",
                    "config": config.to_dict(),
                    "axes": [spec.to_dict()],
                    "phase_basis": "normalized bounded-route position",
                    "clock_contract": {
                        "opportunity": "discrete logical index",
                        "lattice": "configured ideal model time",
                        "monotonic": "elapsed execution observation",
                        "utc": "human correlation only",
                    },
                }
            )
            writer.append(suppressed_tick)
            for tick in result.ticks[1:]:
                writer.append(tick.to_multi_axis_event())
            writer.append(result.summary_dict())
        description_report = audit_ledger(description_path)
        self.assertFalse(description_report.valid)
        self.assertIn(
            "SEMANTIC_TICK_DESCRIPTION",
            {issue.code for issue in description_report.issues},
        )

    def test_completion_preserves_start_axis_order(self) -> None:
        config = EngineConfig(
            lower_bound=1,
            upper_bound=100,
            friction_scale=100,
            search_limit=1_000,
            max_ticks=10,
            max_axes=4,
            max_incidents=3,
            reroute_after_incidents=2,
            lattice_period_s=0.25,
            pace=False,
        )
        specs = (
            AxisSpec("zeta", 11, 13, 3, 0.01),
            AxisSpec("alpha", 17, 19, 3, 0.01),
        )
        result = SimulationEngine(
            config,
            monotonic_clock=lambda: 0.0,
            wall_clock=lambda: datetime(2026, 9, 2, tzinfo=timezone.utc),
        ).run(specs)
        completion = result.summary_dict()
        completion["axes"].reverse()  # type: ignore[union-attr]
        path = self.root / "reordered-completion-axes.jsonl"
        with LedgerWriter(path, run_id="reordered-completion-axes") as writer:
            writer.append(
                {
                    "event_type": "simulation_start",
                    "config": config.to_dict(),
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
            for tick in result.ticks:
                writer.append(tick.to_multi_axis_event())
            writer.append(completion)
        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertIn(
            "SEMANTIC_AXIS_ORDER_CHANGED",
            {issue.code for issue in report.issues},
        )

    def test_start_clock_contract_is_exact(self) -> None:
        forged_start = _simulation_start()
        forged_start["clock_contract"] = {
            "opportunity": "wall time",
            "lattice": "configured ideal model time",
            "monotonic": "UTC",
            "utc": "routing input",
            "extra": "forged",
        }
        path = self.root / "forged-clock-contract.jsonl"
        with LedgerWriter(path, run_id="forged-clock-contract") as writer:
            writer.append(forged_start)
            writer.append(_event(0))
            writer.append(_event(1))
            writer.append(_simulation_complete())
        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertIn("SEMANTIC_CLOCK_CONTRACT", {issue.code for issue in report.issues})

    def test_over_limit_ticks_do_not_overflow_audit_replay(self) -> None:
        start = _simulation_start()
        start["config"]["max_ticks"] = 1  # type: ignore[index]
        start["config"]["lattice_period_s"] = 1e308  # type: ignore[index]
        completion = _simulation_complete(opportunities=3)
        path = self.root / "over-limit-replay.jsonl"
        with LedgerWriter(path, run_id="over-limit-replay") as writer:
            writer.append(start)
            writer.append(_event(0))
            writer.append(_event(1))
            writer.append(_event(2))
            writer.append(completion)
        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertIn("SEMANTIC_TICK_LIMIT", {issue.code for issue in report.issues})

    def test_clock_slip_comparison_has_no_large_magnitude_relative_loophole(self) -> None:
        forged = _event(1).to_dict()
        forged["clock"]["monotonic_time_s"] = 1_000_000_000_000_000_000.0  # type: ignore[index]
        forged["clock"]["slip_s"] = 999_999_999_999_500_000.0  # type: ignore[index]
        path = self.root / "large-clock-slip.jsonl"
        with LedgerWriter(path, run_id="large-clock-slip") as writer:
            writer.append(forged)
        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertIn("SEMANTIC_CLOCK_SLIP", {issue.code for issue in report.issues})

    def test_derived_geometry_contract_uses_exact_replay(self) -> None:
        forged_residual = _event(0).to_dict()
        geometry = forged_residual["axes"]["main"]["geometry"]  # type: ignore[index]
        geometry["residual"] = float(geometry["residual"]) + 5e-13  # type: ignore[index]

        drifted_start = _simulation_start()
        drifted_start["axes"][0]["tolerance"] = 0.0  # type: ignore[index]
        drifted_tick = _event(0).to_dict()
        drifted_tick["axes"]["main"]["geometry"]["tolerance"] = 1e-12  # type: ignore[index]

        cases = (
            ("forged-residual.jsonl", (forged_residual,), "SEMANTIC_RESIDUAL"),
            (
                "tiny-tolerance-drift.jsonl",
                (drifted_start, drifted_tick, _event(1), _simulation_complete()),
                "SEMANTIC_AXIS_CONTRACT_CHANGED",
            ),
        )
        for filename, events, expected_code in cases:
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    for event in events:
                        writer.append(event)
                report = audit_ledger(path)
                self.assertFalse(report.valid)
                self.assertIn(expected_code, {issue.code for issue in report.issues})

    def test_malformed_bounded_json_never_escapes_the_auditor(self) -> None:
        closure_array = _event(0).to_dict()
        closure_array["axes"]["main"]["geometry"]["closure_status"] = []  # type: ignore[index]

        severity_object = _event(0).to_dict()
        severity_object["max_severity"] = {}

        completion_arrays = _simulation_complete()
        completion_axis = completion_arrays["axes"][0]  # type: ignore[index]
        completion_axis["status"] = []  # type: ignore[index]
        completion_axis["visited_nodes"] = [[]]  # type: ignore[index]
        completion_axis["breached_nodes"] = [{}]  # type: ignore[index]

        single_tick = _event(0).to_dict()
        malformed_single = {
            "event_type": "tick",
            "clock": single_tick["clock"],
            "axis": single_tick["axes"]["main"],
            "severity": [],
            "message": "malformed",
            "metadata": {},
        }

        for filename, event in (
            ("closure-array.jsonl", closure_array),
            ("severity-object.jsonl", severity_object),
            ("completion-arrays.jsonl", completion_arrays),
            ("single-severity-array.jsonl", malformed_single),
        ):
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    writer.append(event)
                report = audit_ledger(path)
                self.assertIsInstance(report.issues, tuple)
                self.assertFalse(report.valid)

    def test_audit_rejects_illegal_edges_post_anchor_ticks_and_counter_forgery(self) -> None:
        illegal_tick = _event(0).to_dict()
        illegal_axis = illegal_tick["axes"]["main"]  # type: ignore[index]
        illegal_axis["node"] = 97  # type: ignore[index]
        illegal_axis["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=0,
            expected_phase=0.12,
            observed_phase=0.96,
            quotient_order=3,
            tolerance=0.01,
        ).to_dict()
        illegal_completion = _simulation_complete()
        illegal_completion["axes"][0]["visited_nodes"] = [11, 97, 13]  # type: ignore[index]

        anchor_tick = _event(0).to_dict()
        anchor_axis = anchor_tick["axes"]["main"]  # type: ignore[index]
        anchor_axis["node"] = 13  # type: ignore[index]
        anchor_axis["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=0,
            expected_phase=0.12,
            observed_phase=0.12,
            quotient_order=3,
            tolerance=0.01,
        ).to_dict()
        late_completion = _simulation_complete(opportunities=2)

        false_counters = _simulation_complete()
        false_counters["axes"][0]["incidents"] = 3  # type: ignore[index]
        false_counters["axes"][0]["reroutes"] = 99  # type: ignore[index]

        cap_start = _simulation_start()
        cap_start["config"]["max_incidents"] = 1  # type: ignore[index]
        cap_start["config"]["reroute_after_incidents"] = 1  # type: ignore[index]
        cap_completion = _simulation_complete()
        cap_completion["axes"][0]["incidents"] = 1  # type: ignore[index]

        repeated_tick = _event(0).to_dict()
        repeated_axis = repeated_tick["axes"]["main"]  # type: ignore[index]
        repeated_axis["node"] = 11  # type: ignore[index]
        repeated_axis["is_prime"] = True  # type: ignore[index]
        repeated_axis["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=0,
            expected_phase=0.12,
            observed_phase=0.10,
            quotient_order=3,
            tolerance=0.01,
        ).to_dict()
        movement_tick = _event(1).to_dict()
        movement_axis = movement_tick["axes"]["main"]  # type: ignore[index]
        movement_axis["node"] = 12  # type: ignore[index]
        movement_axis["is_prime"] = False  # type: ignore[index]
        movement_axis["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=1,
            expected_phase=0.12,
            observed_phase=0.11,
            quotient_order=3,
            tolerance=0.01,
        ).to_dict()
        movement_completion = _simulation_complete(opportunities=2)
        movement_completion["succeeded"] = False
        movement_result = movement_completion["axes"][0]  # type: ignore[index]
        movement_result.update(  # type: ignore[union-attr]
            {
                "status": "FAILED",
                "current_node": 12,
                "visited_nodes": [11, 12],
                "error": "route ended before the target was reached",
            }
        )

        cap_move_start = _simulation_start()
        cap_move_start["config"]["max_incidents"] = 1  # type: ignore[index]
        cap_move_start["config"]["reroute_after_incidents"] = 1  # type: ignore[index]
        cap_move_start["axes"][0]["tolerance"] = 0.0  # type: ignore[index]
        cap_failure_tick = _event(0).to_dict()
        cap_failure_tick["axes"]["main"]["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=0,
            expected_phase=0.12,
            observed_phase=0.11,
            quotient_order=3,
            tolerance=0.0,
        ).to_dict()
        cap_late_tick = _event(1).to_dict()
        cap_late_tick["axes"]["main"]["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=1,
            expected_phase=0.12,
            observed_phase=0.12,
            quotient_order=3,
            tolerance=0.0,
        ).to_dict()
        cap_move_completion = _simulation_complete(opportunities=2)
        cap_move_completion["axes"][0]["incidents"] = 1  # type: ignore[index]
        cap_move_completion["axes"][0]["breached_nodes"] = [12]  # type: ignore[index]

        unresolved_tick = _event(0).to_dict()
        unresolved_tick["axes"]["main"]["geometry"]["closure_status"] = "UNRESOLVED"  # type: ignore[index]

        missed_incident_start = _simulation_start()
        missed_incident_start["axes"][0]["tolerance"] = 0.0  # type: ignore[index]
        missed_incident_tick = _event(0).to_dict()
        missed_incident_tick["axes"]["main"]["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=0,
            expected_phase=0.12,
            observed_phase=0.11,
            quotient_order=3,
            tolerance=0.0,
        ).to_dict()
        missed_incident_target = _event(1).to_dict()
        missed_incident_target["axes"]["main"]["geometry"] = make_geometry_snapshot(  # type: ignore[index]
            opportunity_index=1,
            expected_phase=0.12,
            observed_phase=0.12,
            quotient_order=3,
            tolerance=0.0,
        ).to_dict()

        cases = (
            (
                "illegal-edge.jsonl",
                (_simulation_start(), illegal_tick, _event(1), illegal_completion),
                "SEMANTIC_ILLEGAL_PATH_EDGE",
            ),
            (
                "tick-after-anchor.jsonl",
                (_simulation_start(), anchor_tick, _event(1), late_completion),
                "SEMANTIC_TICK_AFTER_TERMINAL",
            ),
            (
                "forged-counters.jsonl",
                (_simulation_start(), _event(0), _event(1), false_counters),
                "SEMANTIC_COMPLETION_COUNTERS",
            ),
            (
                "incident-cap-anchor.jsonl",
                (cap_start, _event(0), _event(1), cap_completion),
                "SEMANTIC_COMPLETION_COUNTERS",
            ),
            (
                "movement-after-terminal.jsonl",
                (_simulation_start(), repeated_tick, movement_tick, movement_completion),
                "SEMANTIC_MOVEMENT_AFTER_TERMINAL",
            ),
            (
                "movement-after-incident-cap.jsonl",
                (cap_move_start, cap_failure_tick, cap_late_tick, cap_move_completion),
                "SEMANTIC_MOVEMENT_AFTER_TERMINAL",
            ),
            (
                "unresolved-engine-tick.jsonl",
                (_simulation_start(), unresolved_tick, _event(1), _simulation_complete()),
                "SEMANTIC_SIMULATION_CLOSURE",
            ),
            (
                "missed-incident-summary.jsonl",
                (
                    missed_incident_start,
                    missed_incident_tick,
                    missed_incident_target,
                    _simulation_complete(),
                ),
                "SEMANTIC_COMPLETION_COUNTERS",
            ),
        )
        for filename, events, expected_code in cases:
            with self.subTest(filename=filename):
                path = self.root / filename
                with LedgerWriter(path, run_id=filename) as writer:
                    for event in events:
                        writer.append(event)
                report = audit_ledger(path)
                self.assertFalse(report.valid)
                self.assertIn(expected_code, {issue.code for issue in report.issues})

    def test_writer_rejects_excessive_json_nesting(self) -> None:
        path = self.root / "nested.jsonl"
        value: object = 0
        for _ in range(70):
            value = [value]
        with LedgerWriter(path, run_id="nested-test") as writer:
            with self.assertRaisesRegex(ValueError, "nesting depth"):
                writer.append({"deep": value})

    def test_existing_file_requires_explicit_overwrite(self) -> None:
        path = self.root / "existing.jsonl"
        path.write_text("do not erase", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            LedgerWriter(path, run_id="safe-default")
        self.assertEqual(path.read_text(encoding="utf-8"), "do not erase")

        with LedgerWriter(path, run_id="explicit-reset", overwrite=True):
            pass
        report = audit_ledger(path)
        self.assertTrue(report.valid)
        self.assertEqual(report.event_count, 0)
        self.assertEqual(report.run_id, "explicit-reset")

    def test_audit_detects_content_tampering(self) -> None:
        path = self.root / "tampered.jsonl"
        with LedgerWriter(path, run_id="tamper-test") as writer:
            writer.append({"value": 1})
        lines = path.read_text(encoding="utf-8").splitlines()
        record = json.loads(lines[0])
        record["payload"]["value"] = 99
        lines[0] = canonical_json(record)  # Deliberately retain the old record_hash.
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertTrue(report.tampered)
        self.assertIn("HASH_MISMATCH", {issue.code for issue in report.issues})

    def test_audit_detects_reordering_and_chain_break(self) -> None:
        path = self.root / "reordered.jsonl"
        with LedgerWriter(path, run_id="reorder-test") as writer:
            writer.append({"value": 1})
            writer.append({"value": 2})
        lines = path.read_bytes().splitlines(keepends=True)
        path.write_bytes(lines[1] + lines[0] + lines[2])

        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertTrue(report.tampered)
        codes = {issue.code for issue in report.issues}
        self.assertIn("SEQUENCE_DISCONTINUITY", codes)
        self.assertIn("CHAIN_BREAK", codes)

    def test_audit_detects_clean_tail_truncation_by_missing_seal(self) -> None:
        path = self.root / "unsealed.jsonl"
        writer = LedgerWriter(path, run_id="interrupted")
        writer.append({"value": 1})
        writer.close(seal=False)

        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertTrue(report.truncated)
        self.assertFalse(report.sealed)
        self.assertIn("MISSING_SEAL", {issue.code for issue in report.issues})
        self.assertTrue(audit_ledger(path, require_seal=False).valid)

    def test_audit_detects_partial_invalid_final_line(self) -> None:
        path = self.root / "partial.jsonl"
        writer = LedgerWriter(path, run_id="partial")
        writer.append({"value": 1})
        writer.close(seal=False)
        content = path.read_bytes()
        path.write_bytes(content[:-3])

        report = audit_ledger(path)
        self.assertFalse(report.valid)
        self.assertTrue(report.truncated)
        codes = {issue.code for issue in report.issues}
        self.assertIn("PARTIAL_LINE", codes)
        self.assertIn("INVALID_JSON", codes)

    def test_canonical_json_rejects_non_json_types_and_nonfinite_values(self) -> None:
        with self.assertRaises(TypeError):
            canonical_json({"bad": (1, 2)})
        with self.assertRaises(ValueError):
            canonical_json({"bad": float("inf")})


if __name__ == "__main__":
    unittest.main()
