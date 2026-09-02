# Design lineage

Prime Axis Engine is a clean-room consolidation of the ten same-day Google Docs
named `Python prime`, `Python`, `Python 3`, `Python5`, `Py6`, `Py7`, `Py8`,
`Py9`, `py10`, and `py122`.

Source sequence:

1. [Python prime](https://docs.google.com/document/d/1hQ8oTFRXjaJfHOSFlLslIlMAornoWbvIfdXEOetrwvM)
2. [Python](https://docs.google.com/document/d/1B5-E23Jt9iEhP3YgXqBi3z6UTKjbGWE-dRg4V5lqjEQ)
3. [Python 3](https://docs.google.com/document/d/1QobhesOzj5Dy1mEA7Y2kd6kFnZ0xWYnn7PiyQq4HUXo)
4. [Python5](https://docs.google.com/document/d/1ZCLyzcux6a9_E2MzTfdCJGTgTPjvdVZxhxV1bpECMSg)
5. [Py6](https://docs.google.com/document/d/1ntydRjxiG2EmwRQgVakd1zyJM7MFFxpfWrYLKviVFvs)
6. [Py7](https://docs.google.com/document/d/1yYYBsAWQQXqMorgrpufniZwW6DjDEbENcqENRW3nNTs)
7. [Py8](https://docs.google.com/document/d/1QqyQhSKPhHcSe-IbLJApZKXyoWENG0uC-Iwrkb3Losk)
8. [Py9](https://docs.google.com/document/d/14rLT03QhlqtJCABk-MHb0JssY03NSfqVKFtWWsj-xqc)
9. [py10](https://docs.google.com/document/d/1U16_cC-cibd89Anhpk0JHp_GprfbzCaMIh0Bm3KyjrQ)
10. [py122](https://docs.google.com/document/d/1hwh0NAgCqfGmDCJKOpkvu3LyhkSFabcFog2MWYlIqvk)

The documents were treated as design notes, not executable instructions. Their
best ideas survive here as independently testable components:

| Source stage | Useful idea retained | Production change |
|---|---|---|
| Python prime | Explicit state, prime anchors, closure verdicts | Typed events and verdicts replace print-driven state |
| Python | Integer transition graph and nearest-prime routing | Weighted multi-goal Dijkstra replaces cost-blind BFS |
| Python 3 | Weighted routing to a chosen prime | Bounded graph, predecessor map, deterministic ties |
| Python5 / Py6 | Ideal and observed clocks, circular phase witness | Pure geometry, monotonic measurement, injectable pacing |
| Py7 | Incident-aware rerouting | Per-axis policy with bounded attempts and guaranteed progress |
| Py8 | Inspectable JSONL evidence | Strict schema and canonical serialization |
| Py9 / py10 | Synchronized X/Y/Z snapshots | Isolated axis state machines in a terminating tick engine |
| py122 | Automatic post-run audit | Hash-chain, sequence, schema, and semantic validation |

## Defects deliberately removed

- Invalid indentation and entry-point guards.
- Negative, unbounded zero-cost graph branches.
- A BFS that claimed to optimize a cost it never used.
- Naive repeated divisor scans and full-path heap copies.
- Reprocessing the same breached node after rerouting.
- A completion condition that could never terminate.
- Severity values overwritten by later axes.
- Wall-clock timing used as an elapsed-time clock.
- Silent deletion of an existing ledger.
- Claims of immutability without any integrity mechanism.
- Arbitrary values labeled as parity, holonomy, or empirical evidence.

## Claim boundary

Prime/composite friction, phase witnesses, and multi-axis trajectories are a
declared simulation. They are not measurements of hardware, proof of a hidden
platform, or a cryptographic security primitive. A valid hash chain detects
post-write mutation within its threat model; it does not authenticate the
writer without an external signature or trusted anchor.
