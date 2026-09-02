# Security and integrity model

Prime Axis Engine has no runtime dependencies and performs no network,
subprocess, dynamic-code, or plugin execution. Its primary attack surfaces are
numeric resource exhaustion, malformed ledgers, filesystem paths, and terminal
output.

## Resource ceilings

- route nodes are positive integers no greater than `10,000,000`;
- route searches expand at most `1,000,000` nodes;
- friction scales are at most `1,000,000`;
- a simulation has at most `100,000` ticks and `256` axes;
- `max_ticks * max_axes` is at most `2,000,000` axis opportunities;
- quotient orders are at most `2**53` for exact float distinction;
- primality is deterministic on the unsigned 64-bit domain;
- divisor counting accepts values no greater than `10**12`;
- JSON nesting is at most 64 levels; and
- each ledger record is at most 4 MiB and is read in bounded chunks.

These are safety limits, not mathematical assertions. Raise them only after
profiling memory and CPU behavior in the intended environment.

## Ledger guarantees

The writer uses exclusive file creation by default. It refuses directories and
symbolic links. Truncation requires `overwrite=True` or CLI `--overwrite`.

The audit checks canonical strict JSON, duplicate keys, finite values, schema,
run identity, sequence continuity, hash continuity, record hashes, final seals,
record counts, partial records, recognized clock/axis/geometry semantics, and
bounded input structure. Recognized simulation runs receive cross-record checks
for start/completion uniqueness and order, contiguous opportunity indices,
stable axis membership and contracts, derived target/node phases, configured
bounds and lattice time, the exact declared clock contract, monotonic clock
ordering, and agreement between tick and completion counts. It lazily reuses
the engine's deterministic initialization and transition functions to replay
each axis. Recorded tick nodes and completion status, path, incidents, reroutes,
breached nodes, error, and axis order must match the replay. Tick severity,
message, and axis-state metadata are also replay-checked. Standalone typed tick
ledgers remain supported, but a `simulation_complete` record is invalid without
a preceding simulation start.

The SHA-256 chain is tamper-evident, not authenticated. An attacker able to
replace the complete ledger can recompute the entire unkeyed chain. For an
adversarial writer or full-file replacement threat, anchor the terminal hash in
trusted storage or sign it externally.

`fsync` requests operating-system durability; it cannot guarantee storage media
behavior after the operating system acknowledges the write.

## Timing and terminal boundary

Elapsed observations use a monotonic clock. UTC is correlation metadata only.
Routing never changes based on execution speed. Axis labels reject control
characters, and ANSI control sequences are emitted only to a TTY, respect
`NO_COLOR`, and restore the cursor through a context manager.

## Scope

The geometry is a deterministic simulation and is not a physical detector,
cryptographic protocol, or proof of a hidden implementation.
