# Prime Axis Engine v1.0

**Union 113 code companion for the Sanskrit orbit/quotient/cocycle upgrade**

Prime Axis Engine turns the ten evolving `PY` Google Docs into one tested,
dependency-free Python application. It combines:

- bounded prime/composite graph routing;
- deterministic weighted Dijkstra search;
- synchronized, isolated X/Y/Z axis state machines;
- an explicit cyclic quotient and return-residual model;
- exact modular cocycle arithmetic;
- finite-domain quotient-descent analysis with counterexamples;
- separate opportunity, lattice, monotonic, and UTC clock fields;
- incident-aware per-axis rerouting;
- canonical hash-chained JSONL evidence; and
- a strict post-run audit for mutation, reordering, and truncation.

The default demonstration anchors X, Y, and Z at primes 113, 139, and 173.
Every graph, geometry, and clock parameter is declared and validated.

## Quick start

Python 3.11 or newer is required. There are no runtime dependencies.

```powershell
cd Prime_Axis_Engine_v1.0
py -m pip install -e .
prime-axis-engine simulate
```

If you prefer not to install it:

```powershell
$env:PYTHONPATH = "src"
py -m prime_axis_engine simulate
```

## Main commands

Find a minimum-friction route to prime 113:

```powershell
prime-axis-engine route 48 113
```

Find the best reachable prime from 48:

```powershell
prime-axis-engine nearest 48
```

Run the default synchronized X/Y/Z model and create a sealed evidence ledger:

```powershell
prime-axis-engine simulate --ledger run.jsonl --run-id union-113-demo
```

Audit the ledger:

```powershell
prime-axis-engine audit run.jsonl
```

Run custom axes:

```powershell
prime-axis-engine simulate `
  --axis X:48:113 `
  --axis Y:72:139 `
  --axis Z:120:173 `
  --upper-bound 250 `
  --quotient-order 3 `
  --tolerance 0.01
```

Add `--json` to `route`, `nearest`, `simulate`, or `audit` for structured
output. Simulation JSON is a bounded summary by default; add `--include-ticks`
when the complete tick history is required. Add `--pace` only when you want a
live timed display; routing itself never depends on wall-clock speed.

An existing ledger is never replaced accidentally. Replacing one requires both
`--ledger PATH` and the explicit `--overwrite` flag.

## Python API

```python
from prime_axis_engine.engine import AxisSpec, EngineConfig, SimulationEngine
from prime_axis_engine.ledger import LedgerWriter, audit_ledger

axes = (
    AxisSpec("X", 48, 113),
    AxisSpec("Y", 72, 139),
    AxisSpec("Z", 120, 173),
)

with LedgerWriter("run.jsonl", run_id="union-113-demo") as ledger:
    result = SimulationEngine(EngineConfig()).run(axes, ledger=ledger)

assert result.succeeded
assert audit_ledger("run.jsonl").valid
```

For a full runnable example, see [`examples/api_demo.py`](examples/api_demo.py).

## What the geometry means

The route geometry normalizes a node and its target inside the configured
finite graph, then compares them in a declared cyclic quotient. It is a
simulation coordinate, not a sensor reading. The cocycle functions operate
exactly in the explicitly selected additive group `Z/mZ`.

`CLOSED`, `FAILED`, and `UNRESOLVED` describe the declared residual test at a
particular opportunity. They do not assert an empirical physical mechanism.

The clock record deliberately keeps four different notions apart:

1. opportunity index;
2. ideal lattice time;
3. elapsed monotonic execution time; and
4. UTC correlation timestamp.

See [`docs/GEOMETRY_CONTRACT.md`](docs/GEOMETRY_CONTRACT.md) for the exact
contract and claim boundary.

## Ledger integrity

Each JSONL record carries a schema version, run ID, sequence number, previous
hash, and its own SHA-256 hash. A final seal receipts the event count and tail.
The audit detects malformed JSON, duplicate keys, non-finite numbers, schema or
run changes, sequence gaps, hash failures, record reordering, partial lines,
missing seals, and mismatched completion counts. For simulation ledgers it also
enforces one start, contiguous zero-based opportunities, a stable axis set, one
terminal completion, and agreement between the tick and completion counts. The
declared bounds, axis contracts and derived phases, lattice clock, monotonic
ordering, and exact four-clock contract are checked across records rather than
in isolation. The auditor also lazily replays the engine's deterministic route
initialization and every axis transition. Tick nodes and final status, path,
incident, reroute, breach, and error receipts must match that replay exactly,
as must axis ordering and each tick's severity, message, and state metadata.

This is tamper-evident evidence, not a digital signature. Anyone who can rewrite
the entire file can also recompute an unkeyed chain. Use an external signed
checkpoint or trusted storage when hostile full-file replacement is in scope.
See [`docs/SECURITY.md`](docs/SECURITY.md) for the full threat model and safety
limits.

## Development checks

```powershell
$env:PYTHONPATH = "src"
py -m unittest discover -s tests -v
py -m compileall -q src
```

The suite covers arithmetic, bounded routing, deterministic ties, geometry,
cocycle composition, synchronized axes, rerouting and termination, CLI exit
codes, ledger durability rules, exact lifecycle replay, and corruption
detection.

## Project map

```text
src/prime_axis_engine/
  number_theory.py   cached primality and divisor counts
  routing.py         bounded deterministic route planner
  model.py           validated immutable evidence records
  geometry.py        quotient, residual, and cocycle primitives
  engine.py          synchronized axis state machines
  ledger.py          canonical JSONL writer and auditor
  renderer.py        TTY-safe optional terminal view
  cli.py             route, nearest, simulate, and audit commands
tests/                dependency-free test suite
docs/                 geometry contract and source lineage
```

The original Google Docs and the synced `sources/` folder were not modified.
