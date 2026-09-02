from __future__ import annotations

import io
import json
from pathlib import Path
import tempfile
import unittest

from prime_axis_engine.cli import (
    EXIT_AUDIT_FAILED,
    EXIT_ERROR,
    EXIT_OK,
    EXIT_SIMULATION_FAILED,
    main,
)


class CLITests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self._temporary_directory.name)

    def tearDown(self) -> None:
        self._temporary_directory.cleanup()

    def _run(self, arguments: list[str]) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        code = main(arguments, stdout=stdout, stderr=stderr, environ={"NO_COLOR": "1"})
        return code, stdout.getvalue(), stderr.getvalue()

    def test_route_and_nearest_json(self) -> None:
        code, output, error = self._run(["route", "4", "7", "--upper-bound", "20", "--json"])
        self.assertEqual(code, EXIT_OK)
        self.assertEqual(error, "")
        route = json.loads(output)
        self.assertEqual(route["nodes"], [4, 8, 7])

        code, output, _ = self._run(["nearest", "4", "--upper-bound", "10", "--json"])
        self.assertEqual(code, EXIT_OK)
        self.assertEqual(json.loads(output)["target"], 5)

    def test_invalid_route_has_nonzero_exit_and_json_error(self) -> None:
        code, output, error = self._run(["route", "4", "9", "--json"])
        self.assertEqual(code, EXIT_ERROR)
        self.assertEqual(output, "")
        self.assertIn("target must be prime", json.loads(error)["error"])

    def test_simulate_writes_sealed_ledger_and_audit_passes(self) -> None:
        ledger = self.root / "run.jsonl"
        code, output, error = self._run(
            [
                "simulate",
                "--axis",
                "north:10:11",
                "--ledger",
                str(ledger),
                "--durability",
                "none",
                "--json",
            ]
        )
        self.assertEqual(code, EXIT_OK)
        self.assertEqual(error, "")
        result = json.loads(output)
        self.assertTrue(result["succeeded"])
        self.assertEqual(result["axes"][0]["label"], "north")
        self.assertEqual(result["ledger"], str(ledger))
        self.assertNotIn("ticks", result)

        code, output, error = self._run(["audit", str(ledger), "--json"])
        self.assertEqual(code, EXIT_OK)
        self.assertEqual(error, "")
        report = json.loads(output)
        self.assertTrue(report["valid"])
        self.assertTrue(report["sealed"])
        # One configuration receipt, one synchronized tick, and one completion.
        self.assertEqual(report["event_count"], 3)

    def test_existing_ledger_requires_explicit_overwrite(self) -> None:
        ledger = self.root / "existing.jsonl"
        ledger.write_text("keep me", encoding="utf-8")
        base = [
            "simulate",
            "--axis",
            "A:10:11",
            "--ledger",
            str(ledger),
            "--durability",
            "none",
        ]

        code, _, error = self._run(base)
        self.assertEqual(code, EXIT_ERROR)
        self.assertIn("already exists", error)
        self.assertEqual(ledger.read_text(encoding="utf-8"), "keep me")

        code, output, error = self._run(base + ["--overwrite"])
        self.assertEqual(code, EXIT_OK)
        self.assertEqual(error, "")
        self.assertIn("Ledger sealed", output)

    def test_failed_simulation_and_bad_audit_have_distinct_nonzero_codes(self) -> None:
        code, output, error = self._run(
            [
                "simulate",
                "--axis",
                "A:4:7",
                "--upper-bound",
                "20",
                "--tolerance",
                "0",
                "--max-incidents",
                "1",
                "--reroute-after",
                "1",
                "--json",
            ]
        )
        self.assertEqual(code, EXIT_SIMULATION_FAILED)
        self.assertEqual(error, "")
        self.assertFalse(json.loads(output)["succeeded"])

        bad = self.root / "bad.jsonl"
        bad.write_text("not-json\n", encoding="utf-8")
        code, output, error = self._run(["audit", str(bad), "--json"])
        self.assertEqual(code, EXIT_AUDIT_FAILED)
        self.assertEqual(error, "")
        self.assertFalse(json.loads(output)["valid"])

    def test_overwrite_without_ledger_is_rejected(self) -> None:
        code, _, error = self._run(["simulate", "--overwrite"])
        self.assertEqual(code, EXIT_ERROR)
        self.assertIn("requires --ledger", error)

    def test_tick_history_is_explicitly_opt_in_for_json(self) -> None:
        code, _, error = self._run(["simulate", "--include-ticks"])
        self.assertEqual(code, EXIT_ERROR)
        self.assertIn("requires --json", error)

        code, output, error = self._run(
            [
                "simulate",
                "--axis",
                "A:10:11",
                "--json",
                "--include-ticks",
            ]
        )
        self.assertEqual(code, EXIT_OK)
        self.assertEqual(error, "")
        self.assertEqual(len(json.loads(output)["ticks"]), 1)


if __name__ == "__main__":
    unittest.main()
