from __future__ import annotations

from datetime import datetime, timezone
import io
import unittest

from prime_axis_engine.engine import (
    AxisSpec,
    AxisStatus,
    ClockRegressionError,
    EngineConfig,
    SimulationEngine,
    default_axis_specs,
)
from prime_axis_engine.model import MultiAxisTickEvent, Severity
from prime_axis_engine.renderer import TerminalRenderer


NOW = datetime(2026, 9, 2, 18, 0, tzinfo=timezone.utc)


class _Ledger:
    def __init__(self) -> None:
        self.events: list[object] = []

    def append(self, event: object, *, timestamp_utc: datetime | None = None) -> dict:
        self.events.append(event)
        return {}


class _TTY(io.StringIO):
    def isatty(self) -> bool:
        return True


class ConfigurationTests(unittest.TestCase):
    def test_axis_specs_are_validated_and_support_arbitrary_labels(self) -> None:
        spec = AxisSpec(" north ", 10, 11, quotient_order=5, tolerance=0.02)
        self.assertEqual(spec.label, "north")
        with self.assertRaises(ValueError):
            AxisSpec("", 10, 11)
        with self.assertRaises(ValueError):
            AxisSpec("bad\nlabel", 10, 11)
        with self.assertRaises(ValueError):
            AxisSpec("A", 10, 12)
        with self.assertRaises(TypeError):
            AxisSpec("A", True, 11)

    def test_config_bounds_axes_and_incidents(self) -> None:
        with self.assertRaises(ValueError):
            EngineConfig(lower_bound=10, upper_bound=9)
        with self.assertRaises(ValueError):
            EngineConfig(max_incidents=2, reroute_after_incidents=3)
        with self.assertRaises(TypeError):
            EngineConfig(pace=1)  # type: ignore[arg-type]
        with self.assertRaisesRegex(ValueError, "tick horizon"):
            EngineConfig(max_ticks=4, max_axes=1, lattice_period_s=1e308)
        with self.assertRaisesRegex(ValueError, r"max_ticks \* max_axes"):
            EngineConfig(max_ticks=100_000, max_axes=256)

        engine = SimulationEngine(
            EngineConfig(max_axes=1),
            monotonic_clock=lambda: 0.0,
            wall_clock=lambda: NOW,
        )
        with self.assertRaisesRegex(ValueError, "must not exceed"):
            engine.run(default_axis_specs()[:2])


class EngineTests(unittest.TestCase):
    def _engine(self, config: EngineConfig | None = None) -> SimulationEngine:
        return SimulationEngine(
            config,
            monotonic_clock=lambda: 10.0,
            wall_clock=lambda: NOW,
        )

    def test_default_run_is_bounded_synchronized_and_reroutes(self) -> None:
        ledger = _Ledger()
        result = self._engine().run(ledger=ledger)

        self.assertTrue(result.succeeded)
        self.assertLess(result.opportunities, result.config.max_ticks)
        self.assertTrue(any(axis.reroutes for axis in result.axes))
        self.assertTrue(all(axis.status is AxisStatus.ANCHORED for axis in result.axes))
        self.assertEqual(len(ledger.events), result.opportunities + 2)
        self.assertIsInstance(ledger.events[0], dict)
        self.assertEqual(ledger.events[0]["event_type"], "simulation_start")  # type: ignore[index]
        self.assertTrue(
            all(
                isinstance(event, MultiAxisTickEvent)
                for event in ledger.events[1:-1]
            )
        )
        self.assertIsInstance(ledger.events[-1], dict)

        for tick in result.ticks:
            typed = tick.to_multi_axis_event()
            self.assertEqual(typed.clock, tick.clock)
            self.assertEqual(set(typed.axes), {"X", "Y", "Z"})
            self.assertEqual(typed.max_severity, tick.max_severity)

    def test_reroute_skips_the_already_processed_breach_node(self) -> None:
        config = EngineConfig(reroute_after_incidents=1, max_incidents=64)
        spec = AxisSpec("custom", 48, 113, tolerance=0.0)
        result = self._engine(config).run([spec])
        axis = result.axes[0]

        self.assertTrue(result.succeeded)
        self.assertGreater(axis.reroutes, 0)
        for breached in axis.breached_nodes:
            self.assertEqual(axis.visited_nodes.count(breached), 1)

    def test_highest_severity_is_order_independent(self) -> None:
        config = EngineConfig(
            upper_bound=20,
            max_incidents=1,
            reroute_after_incidents=1,
        )
        result = self._engine(config).run(
            [
                AxisSpec("critical", 4, 7, tolerance=0.0),
                AxisSpec("anchor", 10, 11, tolerance=0.0),
            ]
        )
        first = result.ticks[0]
        self.assertEqual(first.max_severity, Severity.CRITICAL)
        self.assertEqual(first.to_multi_axis_event().max_severity, Severity.CRITICAL)

    def test_pacing_only_calls_sleeper_and_does_not_change_routes(self) -> None:
        sleeps: list[float] = []
        paced = SimulationEngine(
            EngineConfig(pace=True),
            monotonic_clock=lambda: 2.0,
            wall_clock=lambda: NOW,
            sleeper=sleeps.append,
        ).run([AxisSpec("A", 48, 113)])
        unpaced = self._engine(EngineConfig(pace=False)).run(
            [AxisSpec("A", 48, 113)]
        )

        self.assertEqual(paced.axes[0].visited_nodes, unpaced.axes[0].visited_nodes)
        self.assertEqual(len(sleeps), paced.opportunities - 1)
        self.assertTrue(all(value == paced.config.lattice_period_s for value in sleeps))

    def test_injected_monotonic_clock_must_not_regress(self) -> None:
        values = iter((5.0, 4.0))
        engine = SimulationEngine(
            monotonic_clock=lambda: next(values), wall_clock=lambda: NOW
        )
        with self.assertRaises(ClockRegressionError):
            engine.run([AxisSpec("A", 10, 11)])


class RendererTests(unittest.TestCase):
    def test_non_tty_never_receives_ansi(self) -> None:
        stream = io.StringIO()
        with TerminalRenderer(stream, color=True, live=True):
            pass
        self.assertNotIn("\033[", stream.getvalue())

    def test_tty_cursor_is_restored_on_exception_and_no_color_is_honored(self) -> None:
        stream = _TTY()
        with self.assertRaisesRegex(RuntimeError, "boom"):
            with TerminalRenderer(stream, color=True, live=True, environ={"NO_COLOR": "1"}):
                raise RuntimeError("boom")
        output = stream.getvalue()
        self.assertTrue(output.startswith(TerminalRenderer.HIDE_CURSOR))
        self.assertTrue(output.endswith(TerminalRenderer.SHOW_CURSOR))
        self.assertNotIn(TerminalRenderer.CYAN, output)


if __name__ == "__main__":
    unittest.main()
