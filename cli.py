"""Command-line interface for routing, simulation, and ledger audit."""

from __future__ import annotations

import argparse
from collections.abc import Mapping
from contextlib import nullcontext
import json
import os
from pathlib import Path
import sys
from typing import Sequence, TextIO

from .engine import (
    AxisSpec,
    EngineConfig,
    EngineError,
    SimulationEngine,
    default_axis_specs,
)
from .ledger import DurabilityPolicy, LedgerWriter, audit_ledger
from .renderer import TerminalRenderer
from .routing import PrimeRoutePlanner, RoutePlanningError, RouteResult


EXIT_OK = 0
EXIT_ERROR = 1
EXIT_AUDIT_FAILED = 3
EXIT_SIMULATION_FAILED = 4
EXIT_INTERRUPTED = 130


def _add_route_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--lower-bound", type=int, default=1)
    parser.add_argument("--upper-bound", type=int, default=250)
    parser.add_argument("--friction-scale", type=int, default=15)
    parser.add_argument("--search-limit", type=int, default=10_000)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="prime-axis-engine",
        description=(
            "Deterministic bounded prime-axis routing and simulation. "
            "The geometry is a declared model, not a physical measurement."
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    route = subparsers.add_parser("route", help="route to a chosen prime target")
    route.add_argument("start", type=int)
    route.add_argument("target", type=int)
    _add_route_options(route)

    nearest = subparsers.add_parser("nearest", help="route to the nearest best prime")
    nearest.add_argument("start", type=int)
    _add_route_options(nearest)

    simulate = subparsers.add_parser(
        "simulate", help="run a synchronized deterministic multi-axis simulation"
    )
    simulate.add_argument(
        "--axis",
        action="append",
        metavar="LABEL:START:TARGET",
        help="repeat for arbitrary axes; defaults to the X/Y/Z demonstration",
    )
    _add_route_options(simulate)
    simulate.add_argument("--quotient-order", type=int, default=3)
    simulate.add_argument("--tolerance", type=float, default=0.01)
    simulate.add_argument("--max-ticks", type=int, default=10_000)
    simulate.add_argument("--max-axes", type=int, default=64)
    simulate.add_argument("--max-incidents", type=int, default=64)
    simulate.add_argument("--reroute-after", type=int, default=3)
    simulate.add_argument("--period", type=float, default=0.2, metavar="SECONDS")
    simulate.add_argument(
        "--pace",
        action="store_true",
        help="sleep between displayed ticks; never changes routing decisions",
    )
    simulate.add_argument("--ledger", type=Path, help="write a new sealed JSONL ledger")
    simulate.add_argument("--run-id", default="prime-axis-run")
    simulate.add_argument(
        "--overwrite",
        action="store_true",
        help="explicitly replace an existing --ledger file",
    )
    simulate.add_argument(
        "--durability",
        choices=[policy.value for policy in DurabilityPolicy],
        default=DurabilityPolicy.FSYNC.value,
    )
    simulate.add_argument("--no-color", action="store_true")
    simulate.add_argument(
        "--include-ticks",
        action="store_true",
        help="with --json, include every tick instead of a bounded summary",
    )

    audit = subparsers.add_parser("audit", help="validate a JSONL ledger")
    audit.add_argument("path", type=Path)
    audit.add_argument(
        "--allow-unsealed",
        action="store_true",
        help="do not fail solely because the final seal is absent",
    )
    audit.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    return parser


def _planner(arguments: argparse.Namespace) -> PrimeRoutePlanner:
    return PrimeRoutePlanner(
        lower_bound=arguments.lower_bound,
        upper_bound=arguments.upper_bound,
        friction_scale=arguments.friction_scale,
        search_limit=arguments.search_limit,
    )


def _route_dict(result: RouteResult) -> dict[str, object]:
    return {
        "mode": result.mode,
        "start": result.start,
        "target": result.target,
        "bounds": {"lower": result.lower_bound, "upper": result.upper_bound},
        "nodes": list(result.nodes),
        "total_friction": result.total_friction,
        "hops": result.hops,
        "explored_nodes": result.explored_nodes,
        "steps": [
            {
                "index": step.index,
                "node": step.node,
                "move": step.move,
                "friction": step.friction,
                "cumulative_friction": step.cumulative_friction,
                "prime": step.prime,
            }
            for step in result.steps
        ],
    }


def _print_route(result: RouteResult, stream: TextIO) -> None:
    stream.write("Route: " + " -> ".join(str(node) for node in result.nodes) + "\n")
    stream.write(
        f"Target {result.target}; hops={result.hops}; "
        f"friction={result.total_friction}; explored={result.explored_nodes}\n"
    )


def _parse_axes(arguments: argparse.Namespace) -> tuple[AxisSpec, ...]:
    if not arguments.axis:
        defaults = default_axis_specs()
        return tuple(
            AxisSpec(
                spec.label,
                spec.start,
                spec.target,
                quotient_order=arguments.quotient_order,
                tolerance=arguments.tolerance,
            )
            for spec in defaults
        )

    specs: list[AxisSpec] = []
    for encoded in arguments.axis:
        try:
            label, start_text, target_text = encoded.rsplit(":", 2)
            start = int(start_text)
            target = int(target_text)
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"invalid --axis {encoded!r}; expected LABEL:START:TARGET"
            ) from exc
        specs.append(
            AxisSpec(
                label,
                start,
                target,
                quotient_order=arguments.quotient_order,
                tolerance=arguments.tolerance,
            )
        )
    return tuple(specs)


def _write_json(value: object, stream: TextIO) -> None:
    json.dump(value, stream, ensure_ascii=False, allow_nan=False, sort_keys=True)
    stream.write("\n")


def _run_simulation(
    arguments: argparse.Namespace,
    *,
    stdout: TextIO,
    environ: Mapping[str, str],
) -> int:
    if arguments.overwrite and arguments.ledger is None:
        raise ValueError("--overwrite requires --ledger")
    if arguments.include_ticks and not arguments.json:
        raise ValueError("--include-ticks requires --json")

    specs = _parse_axes(arguments)
    config = EngineConfig(
        lower_bound=arguments.lower_bound,
        upper_bound=arguments.upper_bound,
        friction_scale=arguments.friction_scale,
        search_limit=arguments.search_limit,
        max_ticks=arguments.max_ticks,
        max_axes=arguments.max_axes,
        max_incidents=arguments.max_incidents,
        reroute_after_incidents=arguments.reroute_after,
        lattice_period_s=arguments.period,
        pace=arguments.pace,
    )
    engine = SimulationEngine(config)

    ledger_context = (
        LedgerWriter(
            arguments.ledger,
            run_id=arguments.run_id,
            overwrite=arguments.overwrite,
            durability=arguments.durability,
        )
        if arguments.ledger is not None
        else nullcontext(None)
    )
    renderer = None if arguments.json else TerminalRenderer(
        stdout,
        color=False if arguments.no_color else None,
        live=arguments.pace,
        environ=environ,
    )
    renderer_context = renderer if renderer is not None else nullcontext(None)

    with ledger_context as ledger, renderer_context:
        result = engine.run(specs, ledger=ledger, renderer=renderer)

    if arguments.json:
        output = result.to_dict() if arguments.include_ticks else result.summary_dict()
        output["config"] = result.config.to_dict()
        if arguments.ledger is not None:
            output["ledger"] = str(arguments.ledger)
        _write_json(output, stdout)
    elif arguments.ledger is not None:
        stdout.write(f"Ledger sealed at {arguments.ledger}\n")

    return EXIT_OK if result.succeeded else EXIT_SIMULATION_FAILED


def _run_audit(arguments: argparse.Namespace, *, stdout: TextIO) -> int:
    report = audit_ledger(arguments.path, require_seal=not arguments.allow_unsealed)
    if arguments.json:
        _write_json(report.to_dict(), stdout)
    else:
        status = "valid" if report.valid else "invalid"
        stdout.write(
            f"Ledger {status}: records={report.record_count}, "
            f"events={report.event_count}, sealed={report.sealed}\n"
        )
        for issue in report.issues:
            location = f" line {issue.line_number}" if issue.line_number else ""
            stdout.write(f"- {issue.code}{location}: {issue.message}\n")
    return EXIT_OK if report.valid else EXIT_AUDIT_FAILED


def main(
    argv: Sequence[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    environ: Mapping[str, str] | None = None,
) -> int:
    """Run the CLI and return a process exit code."""

    output = stdout or sys.stdout
    error_output = stderr or sys.stderr
    environment = os.environ if environ is None else environ
    parser = build_parser()
    arguments = parser.parse_args(argv)

    try:
        if arguments.command == "route":
            result = _planner(arguments).route_to_prime(
                arguments.start, arguments.target
            )
            if arguments.json:
                _write_json(_route_dict(result), output)
            else:
                _print_route(result, output)
            return EXIT_OK
        if arguments.command == "nearest":
            result = _planner(arguments).route_to_nearest_prime(arguments.start)
            if arguments.json:
                _write_json(_route_dict(result), output)
            else:
                _print_route(result, output)
            return EXIT_OK
        if arguments.command == "simulate":
            return _run_simulation(arguments, stdout=output, environ=environment)
        if arguments.command == "audit":
            return _run_audit(arguments, stdout=output)
        raise AssertionError(f"unhandled command: {arguments.command}")
    except KeyboardInterrupt:
        error_output.write("interrupted\n")
        return EXIT_INTERRUPTED
    except FileExistsError as exc:
        location = exc.filename or getattr(arguments, "ledger", None) or "ledger"
        message = f"ledger already exists: {location}; pass --overwrite to replace it"
        if getattr(arguments, "json", False):
            _write_json({"error": message, "error_type": type(exc).__name__}, error_output)
        else:
            error_output.write(f"error: {message}\n")
        return EXIT_ERROR
    except (EngineError, RoutePlanningError, OSError, TypeError, ValueError) as exc:
        if getattr(arguments, "json", False):
            _write_json({"error": str(exc), "error_type": type(exc).__name__}, error_output)
        else:
            error_output.write(f"error: {exc}\n")
        return EXIT_ERROR


__all__ = [
    "EXIT_AUDIT_FAILED",
    "EXIT_ERROR",
    "EXIT_INTERRUPTED",
    "EXIT_OK",
    "EXIT_SIMULATION_FAILED",
    "build_parser",
    "main",
]
