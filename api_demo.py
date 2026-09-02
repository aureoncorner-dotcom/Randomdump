"""Small end-to-end Prime Axis Engine API example."""

from __future__ import annotations

from pathlib import Path

from prime_axis_engine.engine import AxisSpec, EngineConfig, SimulationEngine
from prime_axis_engine.ledger import LedgerWriter, audit_ledger


def main() -> None:
    output = Path("union-113-demo.jsonl")
    axes = (
        AxisSpec("X", 48, 113),
        AxisSpec("Y", 72, 139),
        AxisSpec("Z", 120, 173),
    )
    config = EngineConfig(upper_bound=250, max_ticks=500)

    with LedgerWriter(output, run_id="union-113-demo") as ledger:
        result = SimulationEngine(config).run(axes, ledger=ledger)

    report = audit_ledger(output)
    print(f"anchored={result.succeeded} opportunities={result.opportunities}")
    print(f"ledger_valid={report.valid} records={report.record_count}")


if __name__ == "__main__":
    main()

