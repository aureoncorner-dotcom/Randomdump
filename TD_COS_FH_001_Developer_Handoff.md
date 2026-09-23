# TD-COS-FH-001 replacement replay — minimum developer handoff

Version 0.1 · 16 September 2026 (UTC) · Anonymous · CC0 1.0 — No Rights Reserved

**Target:** `TD-COS-FH-001-L2-REPLAY-REPLACEMENT-20260908`

**Disposition:** specification and implementation handoff prepared; replacement implementation and full replay **NOT_RUN** in this task. Historical accepted-update discrepancy **−1,352, UNRESOLVED**. Production **NOT_AUTHORIZED**. Physical Q2 **NOT_RUN**.

The minimum implementation is an additive, pinned-profile execution layer around the unchanged designated sampler: (1) configuration enforcement, (2) lossless event/measurement/checkpoint recording with restart, and (3) schema-aware validation and comparison. A general-purpose configurable sampler, a new transition rule, and new sampling cohorts are unnecessary for this replay.

## 1. What was recovered and checked

The exact replacement amendment ZIP was recovered, including `DYNAMICS_REPLACEMENT_v0.1.json`, `EVENT_CHECKPOINT_REQUIREMENTS.md`, the designated sampler, and both preserved historical ZIPs. These files are available inputs, not missing prerequisites. The source inventory and checks are included in the accompanying ZIP.

| Input | Observed availability and scope |
|---|---|
| Current Geometry Master, §9 | Read from Drive; keeps replacement full replay NOT_RUN and historical cause UNRESOLVED. [M] |
| S9, Toroidal Dynamics v0.1 | Read the exact Master-linked Doc, whose Drive title is v0 and body is v0.1. Defines the ideal kernel and numerical policy. The amendment also binds a separate September 6 v0.1 Doc snapshot; both identities are preserved. [S9] |
| S14 replacement package | Recovered exact ZIP; all **14** listed entries match recorded byte sizes and SHA-256. It defines a prospective target, not a completed implementation. [S14, P14] |
| First-run packet | Recovered; all **9** listed entries match. Contains sampler, 80,000 compact retained measurements, receipt, verifier and comparison. Existing structural verifier freshly passes **16/16**. [P1] |
| Mismatch investigation | Recovered; all **29** listed entries match. Contains 4,096 inspectable events, 32 state/RNG snapshots, bounded results, tracer and comparator. [S12, P12] |
| Sampler contract self-test | Fresh execution reports **123** descriptors with inverse checks, 8 valid starts, 24 face-boundary checks, 8 cube checks, 6 sheet checks, Bessel orders 0–8: PASS. This does not execute a replay. [P1] |
| Repository research branch | Source snapshots exist at commit `98bd55e7668680d1c08d01e041b3920a99bca545`; relevant files are prose archives. [R1] |
| Repository mathematics branch | Commit `e8623fa88a6e049e17e7564222356a6675d6b29d` contains the recovered mathematical verifier and additional rational certificates. Its README explicitly says these do not execute the sampler. [R2] |
| Repository main validation manifest | A.10 manifest at `90301d7db659aaf85475dc06e83e8ed57b1677dd` is SCAFFOLD_ONLY/NOT_RUN and concerns broader simulation gates. It is not replacement-replay evidence. [R3] |

The reviewed repository trees do not supply the missing replacement adapter/recorder. This is a bounded inventory statement, not a claim that no implementation exists anywhere. The mathematical verifier's recovery does not close a sampler gate.

Fresh checks ran under CPython **3.12.14**, NumPy **2.3.5**, SciPy **1.17.0**, Linux **6.18.44**. The designated reference is CPython **3.12.13**, NumPy **2.3.5**, SciPy **1.17.0**, with the source's recorded build/platform. This task's static and structural checks are not a compatibility certification for the different Python build. No replacement trajectory was generated.

## 2. Frozen target and byte bindings

| Bound object | Bytes | SHA-256 |
|---|---:|---|
| `sampler/td_cos_fh_001_sampler.py` | 47,134 | `262f60cf72e41481428c45cb921aee99c1c6178d39f67ed7071252001f180c2b` |
| `DYNAMICS_REPLACEMENT_v0.1.json` | 10,544 | `803484491f4c9d8702d97e0c15eab8cbd7f4940b8f16058f7c15ac9be5e1e275` |
| `EVENT_CHECKPOINT_REQUIREMENTS.md` | 8,416 | `5cd314fb088b687d0b224f539e1d15a31d426386e5dd72a3ef3cf891b260d641` |
| Recovered replacement ZIP | 4,207,769 | `af03debcda42839f38525b3a6bda14aab2d24ad33c8822386d8742fc81e0d3b8` |

Hashes identify exact bytes. They do not attest an external registration date or mathematical correctness. Do not reformat the bound configuration and retain its old hash.

| Parameter | Required value |
|---|---|
| Model | Cosine modified-Bessel weights; J=`1`, t=`1/2`, h6=`0`; fixed-reference `Z000` |
| State | 24 unbounded signed integer currents I; 24 binary membrane values M; q in 0…7 |
| Geometry | Periodic 2×2×2; V=8, E=P=24; B=71 attempted microticks/sweep |
| Indexing | Lexicographic (x,y,z), z fastest; edges base then x,y,z; faces base then xy,xz,yz; distinct length-two periodic bonds |
| q encoding | q=qx+2qy+4qz; explicit tuple is xyz; printed three-bit integer is zyx |
| Initial state | Chain c=0…7: q=c, M=0, I=Γ(q); reference cycles start at origin |
| RNG | Separate `random.Random` streams; proposal 64000+c, acceptance 74000+c; `getrandbits` only |
| Schedule | 2,000 warmup + 10,000 retained sweeps per chain; 852,000 attempts per chain |
| Retention | k=1…10,000 at t=(2000+k)×71; first 142,071; last 852,000 |
| Full output | 6,816,000 completed event rows; 80,000 retained rows; 112 declared restart checkpoints |
| Excluded changes | No thinning, current cutoff, equal-sector bias, seed changes, all-zero-start substitution, accepted-move clock or physical-time calibration |

Every chain's checkpoint ticks are exactly:

`0, 512, 142000, 142071, 213000, 284000, 355000, 426000, 497000, 568000, 639000, 710000, 781000, 852000`.

### Descriptor probabilities

These are probabilities of individual descriptors, not family probabilities. Their weighted sum is exactly one; there are 123 descriptors including identity.

| Family, in draw order | Weight / 71 | Descriptors | Probability per descriptor | Parameter order |
|---|---:|---:|---:|---|
| IDENTITY | 8/71 | 1 | 8/71 | None after family choice |
| CUBE | 8/71 | 8 | 1/71 | Cube |
| COUPLED_PLAQUETTE | 24/71 | 48 | 1/142 | Face, then sign |
| EVEN_PLAQUETTE | 24/71 | 48 | 1/142 | Face, then sign |
| CLOSED_SHEET | 1/71 | 6 | 1/426 | Axis, then cut |
| EVEN_REFERENCE_CYCLE | 3/71 | 6 | 1/142 | Axis, then sign |
| UNIT_SECTOR_CYCLE | 3/71 | 6 | 1/142 | Axis, then sign |

Uniform integer selection uses width `(n-1).bit_length()`, rejecting draws ≥n; n=1 draws nothing. Sign bit 0 means −1. Acceptance begins at K=16 with 64-bit prefixes, adding 16 terms and appending 64 bits when unresolved. A cancelled signature or lower ratio bound ≥1 before drawing consumes **zero** acceptance bits. Later proof of probability one retains bits already consumed. Preserve the original call order exactly.

## 3. Minimum implementation and interfaces

The names and signatures below are **proposed developer interfaces**, not recovered executable APIs or an amendment to the bound profile. Implementations and formal schemas require their own version and hashes.

### A. Pinned-profile binding and execution adapter

Proposed interface:

```python
bind_profile(config_path, sampler_path, event_contract_path,
             invocation, runtime, compatibility_record=None) -> BoundRun
create_chain(bound_run, chain_id) -> ObservedRunner
advance_one(runner, next_microtick) -> CommittedEvent | InterruptedAttempt
```

Required behavior:

1. Verify the three bound input hashes and sizes **before creating a chain or consuming RNG**. Strictly parse the JSON; reject malformed data, duplicate keys and unsupported schema/profile identities.
2. Support this exact profile. Derive the invocation from it: fixed lattice, starts, seeds, schedule, accepted-update invariant mode, B=71, reference software policy, and 14 checkpoint addresses. Reject every conflicting override. Metadata such as output location may vary and must be recorded.
3. Explicitly compare parsed settings with the source capabilities and actual constructed runner. Some settings are hardcoded in the pinned code. Exact source binding plus explicit runtime assertions is sufficient for a pinned-profile adapter; no generic dynamics interpreter is needed.
4. Preserve an effective-settings record and the full executed command. Verify any existing output directory's binding on resume; refuse mixed profiles or unexplained prior output. Give each attempt a distinct execution ID under the same profile.
5. Record the actual runtime/build and dependency versions. Use the reference environment, or attach a separately identified compatibility record that states the difference and comparisons performed. A version-string check is not an image hash.
6. Write a new replacement receipt. The source `run_profile` sets historical labels such as `FROZEN_PROSE_PROFILE_WITH_UNRECOVERED_MACHINE_AUTHORITY`; relabelling that output alone is not adoption. Keep historical authority and prospective authority as distinct fields.

**Source evidence:** `run_profile` constructs `(2,2,2)` directly and uses `sha256_file(dynamics_path)` for provenance without parsing its contents. `ChainRunner.__init__` fixes seeds and starts; the CLI can change warmup, retained length and invariant mode. A bare `--dynamics DYNAMICS_REPLACEMENT_v0.1.json` command is therefore insufficient. [P1, sampler `run_profile`, `build_parser`, `ChainRunner.__init__`]

### B. Observer, durable recorder and restart driver

Proposed interface:

```python
record_completed(candidate_event) -> CommitToken
record_measurement(runner, retained_index, event_range) -> CommitToken
checkpoint(runner, committed_prefixes) -> CheckpointRef
interrupt(attempt_context, error) -> InterruptionRef
restore(checkpoint_ref, verified_prefixes, bound_run) -> ObservedRunner
```

Use the original `ChainRunner.microtick`, `choose_family`, `proposal` and `AcceptanceOracle.decide`. The existing tracer demonstrates wrapping methods and inspecting returned decisions. Capture each actual call once; never call proposal selection again for logging, redraw acceptance, replace a decision, or consume either RNG in observer work.

Capture full prestate, both pre-attempt RNG states, chosen descriptor and proposed changes. After the actual oracle returns, capture its signature, decision, full prefix and final order; compute the exact rational bounds without drawing. Capture poststate and RNG digests. Emit the required JSONL only after validation. A completed sampler call is not a durable committed attempt until its entire canonical row is persisted under the recorder's documented commit protocol.

A minimum implementation may use synchronous durable writes per event. A batched implementation needs a separately defined commit boundary and must never report unpersisted attempts as complete. After a crash or partial write, verify the last committed prefix, quarantine any partial suffix, and regenerate from a verified checkpoint. Do not skip an uncertain event. An interrupted computation may be recomputed; the committed event stream must still contain each address once.

Preserve the source's bookkeeping semantics. The source `run()` schedules **11** historical digest checkpoints per chain (88 total); the investigation stores **4** state/RNG snapshots per chain (32); the companion reports **96**; the replacement requires **14** full restart checkpoints per chain (112). They are different objects. Additional observer checkpoints at 0, 512 and 142,071 must not inflate the legacy `invariant_checks` counter or alter legacy checkpoint arrays. Maintain separate observer-check counters.

At 142,000, preserve the source's completed-sweep warmup transition before checkpointing: `after_warmup=True`, warmup endpoint bookkeeping and source checkpoint behavior. At retained ticks, include that tick's measurement and digest/bookkeeping before writing the restart checkpoint. At tick 512, resume mid-sweep: next tick 513, not at the next sweep boundary. At final tick 852,000, next tick is 852,001 and execution is already complete.

### C. Contract validator, normalizer and first-difference comparator

Proposed interface:

```python
validate_bundle(binding, events, checkpoints, measurements, receipt,
                expected_scope) -> ValidationReport
normalize_legacy_prefix(row, verified_initial_state) -> ComparisonRecord
compare_streams(left, right, expected_scope) -> FirstDifferences
verify_restart(checkpoint, uninterrupted_reference, bound_run) -> RestartReport
compare_legacy_receipt(new_projection, preserved_receipt, preserved_samples) -> Report
```

Require the expected chains and tick ranges as input. Validate each side independently before comparison; empty streams, absent chains, identical truncation, null required data, missing nested keys, duplicates, gaps and incompatible bindings cannot pass through equality. Report INCOMPLETE_EVIDENCE for absent/unaligned evidence; report an explicit INVALID_EVIDENCE/FAIL for malformed or internally inconsistent evidence; report DIVERGENCE for unequal valid comparands. Missing evidence must never become MATCH.

For valid aligned rows, compare prestate and proposal RNG/descriptor first, then weight signature/bounds, prefix, acceptance RNG/decision and poststate. Retain the first evidence difference **and** first trajectory/decision difference per chain if they occur at different events. Continue enough to report each chain; include both values, field path, address and input hashes.

The preserved comparator checks its historical diagnostic schema. It lacks replacement binding/field validation, expected full-run coverage, canonical encodings and checkpoint/measurement validation. Its return value `MATCH_ON_SUPPLIED_PREFIX` cannot be renamed full conformance. Extend through a separately hashed validator/normalizer; preserve the original comparator unchanged. [P12]

## 4. Evidence files and exact fields

The following preserves `EVENT_CHECKPOINT_REQUIREMENTS.md`. Proposed names fill details that that document describes semantically but does not assign a key name. Freeze those choices in a new schema artifact before execution; do not edit the bound contract to conceal the distinction.

### Common serialization

UTF-8, sorted object keys, compact separators, LF-terminated JSONL, exactly one object per nonempty line, no NaN/Infinity. Reject duplicate keys. I values are always canonical signed decimal strings: `"0"`, `"1"`, `"-1"`; no plus signs, leading zeroes or negative zero. Prefixes are unsigned decimal strings. W and sum_I2 are decimal strings. Any other integer beyond JSON's interoperable range is a decimal string. Rationals are reduced `numerator/denominator` strings with positive denominator, including `1/1` and `0/1`.

Hash the **uncompressed canonical** evidence bytes. If compressed files are supplied, hash their container bytes separately. Do not require compressed archive byte identity to demonstrate trajectory identity.

### `run_binding.json`

Required content: schema/version; profile and execution ID; amendment/configuration/sampler/adapter/recorder/validator/schema hashes and sizes; input packet hashes; effective settings and invocation; runtime/build and dependency evidence; compatibility-record identity if applicable; clocks, initial states and seed-to-state checks; expected chain/tick/sample/checkpoint coverage. Record actual timestamps separately from computational time.

Bind each implementation file separately even when a combined adapter/observer hash is also supplied. Record the original sampler hash and any instrumentation implementation hash; do not represent patched sampler bytes as the designated unchanged source.

### `events.jsonl`

| Required key(s) | Type and semantics |
|---|---|
| `schema` | Exactly `td-replacement-event/1` |
| `profile_id`, `config_sha256` | Exact profile and configuration identity |
| `chain`, `microtick` | Chain 0…7; completed tick 1…852000; chain-major, contiguous |
| `sweep`, `position_in_sweep` | `(tick-1)//71+1`, `(tick-1)%71+1` |
| `family` | One of the seven ordered family names |
| `proposal` | Integer `a`, `b`, `sign`; unused a/b=−1, unused sign=0; follow source descriptor meanings |
| `descriptor_probability` | Exact elementary probability from §2, using canonical rational spelling |
| `proposed_changes` | Ordered `[edge_index, signed_decimal_delta]` pairs, membrane toggles, q_xor; retain candidate changes on rejection. Proposed inner key for pairs: `current_changes` |
| `before`, `after` | Each: `state_sha256`, `q_integer`, `q_xyz`, `q_printed_zyx`, `W_xyz`, `N_M`, `sum_I2`; preserve explicitly labelled legacy BLAKE2b-128 additionally for historical comparison |
| `acceptance` | Null only on identity. Otherwise: `delta_N_M`, sorted nonzero `[Bessel_order,power]` signature, `series_order`, `ratio_lower`, `ratio_upper`, `prefix`, `prefix_bits`, `decision`, `no_draw` |
| `outcome` | Exactly IDENTITY, ACCEPTED or REJECTED |
| Four RNG digest keys | `proposal_rng_before`, `proposal_rng_after`, `acceptance_rng_before`, `acceptance_rng_after` |
| `delta_W_xyz`, `eta_xyz` | Signed actual post-minus-pre winding, and componentwise mod-two parity. Proposed exact-string encoding for delta_W; eta uses three binary integers |

The state digest is SHA-256 of exactly `{"I":[decimal strings],"M":[binary integers],"q_integer":integer}` serialized with sorted keys and compact separators, **without LF**. Derived fields do not enter this digest and require independent checks. Every reconstructed state must satisfy integer divergence zero, membrane parity, q/W parity, all-cut agreement and cached N_M=sum(M).

`ratio_lower/upper` are bounds on **R**, not already clipped acceptance probabilities. Derive A bounds as min(1,R bounds). A prefix p of b bits represents `[p/2^b,(p+1)/2^b)`. Accept when `(p+1)/2^b ≤ A_lower`; reject when `p/2^b ≥ A_upper`. Reconstruct each earlier comparison from the complete final prefix to verify the original stopping point and draw consumption, not just the final decision. For b>0, enforce b a positive multiple of 64 and final K=16+16×(b/64−1) for this source's refinement schedule. The initial no-draw branch has b=0, prefix=`"0"`, K=16, decision=true and unchanged acceptance RNG.

Identity has null acceptance, unchanged state and unchanged acceptance RNG; proposal RNG still advances for family selection. Rejection retains I/M/q and all state-derived observables, but its RNG and evidence generally advance. `no_draw` means zero consumed acceptance bits, not merely that the final acceptance probability is one.

### `checkpoints.jsonl`

| Required content | Restore requirement |
|---|---|
| Schema/profile/config/sampler/observer identity; chain; completed and next tick | Verify binding and exact scheduled address before restore |
| Complete I/M/q and N_M; all observables and state digests | Recompute rather than trust cached values |
| Both complete RNG states and digests | JSON `[version, internal_state_array, gaussian_cache]`; reconstruct outer/internal tuples before `setstate`; preserve all words and index; Gaussian cache null for this profile |
| Prefix ranges, row counts, byte lengths and hashes | Precisely identify event/measurement bytes through the checkpoint; verify before using |
| Source bookkeeping | Outcome/family counts; acceptance-bit histogram; oracle signature-use and refinement counters/maxima; invariant counts; retained index; warmup flag; current state/winding; visited sectors; extrema; round-trip counters and phases; historical checkpoint list where needed |
| Incremental receipt state | Restore accumulators or deterministically rebuild from verified prefixes. Re-feed exact legacy packed event bytes and legacy sample digest bytes to reconstruct legacy hash objects; canonical JSONL bytes build separate canonical hashes |

RNG digest remains `SHA256(repr(reconstructed_python_tuple).encode("ascii"))`. Hashing JSON RNG text would define a different digest. Seeds alone cannot restore the progressed generator.

Oracle caches may be rebuilt because they only memoize exact computations; their counters must retain source semantics. A digest value cannot restore a hash object's internal state. The existing 32 investigation snapshots contain state/RNG information but not all runner accumulators, so they are calibration/reconstruction inputs, not already-complete replacement restarts.

### `measurements.jsonl`

One row per chain and retained index k=1…10000. Required semantic content: schema and profile/config identity, chain, k, completed tick `(2000+k)*71`, inclusive event range `[(2000+k-1)*71+1,(2000+k)*71]`, state digest, q with explicit encoding, signed W, N_M, sum_I2, all-cut consistency. Preserve legacy state digest for comparison. First range is **142001…142071**; final range **851930…852000**. The warmup endpoint 142000 is not a retained row. Every interval has 71 attempts, regardless of acceptance or repeated states.

### Receipt, interruption records and manifest

The final receipt records expected/actual coverage, completed ranges, per-chain computational comparisons, restart coverage, validation outcomes, input/output/implementation hashes, actual environment, start/end times and explicit remaining statuses. A completion status requires successful finalization and verification of all required files. Store incomplete runs and errors with their actual scope.

An interruption record includes attempted address and stage, last durable address, error, available pre/candidate state, both RNG states before/current, unfinished acceptance prefix/order, and recovery checkpoint/prefix identity. An unfinished proposal is neither a completed attempt nor a rejection. If exact pending-state capture is unavailable, explicitly mark it and regenerate from a verified checkpoint. This does not permit claiming continuation across an unrecorded gap.

The manifest lists each file's exact bytes and SHA-256, excluding itself from its own list. Bind the manifest externally in the delivery receipt or enclosing package; avoid self-referential hashes.

## 5. Legacy normalization and receipt comparison

Normalize a historical prefix only after validating its own schema and source hashes. Map its `before/after.I` integers to exact decimal strings; derive the new state SHA-256 from full I/M/q; retain the original BLAKE2b-128 identity. Split `proposal.current_changes`, membrane toggles and q_xor into the new proposed-changes object. Map acceptance `signature=[delta_N_M,powers]` into the two explicit fields and `accepted` to `decision`. Canonicalize rational `"1"` to `"1/1"`; derive `no_draw` from consumed bits and verify RNG equality. Add descriptor probability, clock indices, delta_W and eta by deterministic calculation. These are traceable derived fields, not newly observed historical evidence. Identity's absent historical acceptance maps to null under the explicit identity rule only.

The normalizer must not manufacture unavailable historical full-trace events or infer acceptance prefixes from aggregate totals. Preserve the original sidecar and write a conversion receipt identifying every transformation.

Two recorded no-draw regression fixtures are chain **7, tick 5** (EVEN_REFERENCE_CYCLE, cancelled signature) and chain **0, tick 53** (UNIT_SECTOR_CYCLE, lower ratio bound already ≥1). These are known reproduction events, not identified companion divergences.

For full replay, compare all 80,000 preserved sample values/hashes, source per-chain event and measurement digest commitments, final states/RNGs, source checkpoint comparisons, and computational counters. Recompute legacy packed event digests from the exact new event evidence, in source byte order. Matching canonical SHA-256 is a different comparison from matching the source's BLAKE2b-128 state hash.

Use an explicit comparison projection/allowlist. Compare exact integer counts, sectors, observables, proposal/acceptance bookkeeping and digests; compare numerical diagnostic fields under the reference environment or a separately documented compatibility policy. New timestamps, elapsed duration, paths, execution/profile metadata, added canonical hashes, observer counters and compressed container bytes are not historical trajectory comparands. Do not blanket-ignore new or unknown computational fields. Preserve legacy invariant-check counts separately because new observer checks legitimately add work.

The old receipt does not contain an inspectable full historical event stream. Full replacement event evidence must therefore be checked against an uninterrupted reference execution and by independent state/acceptance reconstruction, while historical comparison uses the available 4,096 prefix events, retained samples, checkpoints and digest commitments. Label these evidence scopes separately; do not claim event-by-event comparison with an unavailable full historical stream. Two runs of the same implementation establish repeatability, not an independent proof of the kernel.

## 6. Validation matrix and exact release gates

All gates below are **future requirements for the replacement implementation**, except the source-integrity/structural checks explicitly reported in §1. Tests and schema documents alone are not a replay PASS. The machine-readable matrix in the packet carries NOT_RUN status for these implementation gates.

| Gate | Required tests/evidence | Exact pass criterion |
|---|---|---|
| G0 — Binding | Correct frozen bundle; mutate configuration/source/contract bytes, schedule, seed, family weights, bit order, invariant mode; introduce unsupported runtime | Valid inputs yield exact effective settings; every conflict halts before RNG advancement. Different runtime requires explicit compatibility evidence, never silent acceptance |
| G1 — Schema and scope | Empty streams; missing chain/row/nested key; equal truncation; duplicate/reordered addresses; malformed JSON; duplicate keys; invalid rational/decimal; missing final LF; wrong hash/profile | All invalid/incomplete cases rejected; no MATCH on missing evidence; valid serialization round-trips exactly |
| G2 — Transition and RNG | 123 descriptors/inverses, exact elementary probabilities, all eight starts; integer-selection rejection and n=1 no-draw; sign mapping; local versus global signature; rational acceptance/refinement/no-draw fixtures | Exact normalization and state constraints; original draw order and decisions; full prefix reconstruction; observer consumes zero RNG draws |
| G3 — Observer neutrality | Observer enabled versus disabled under same source, initialization and RNG states; compare state, both RNGs, decisions and legacy bookkeeping at each bounded step | Zero state/decision/RNG/computational-counter differences; recording checks accounted separately |
| G4 — Historical bounded calibration | All eight 512-event prefixes; tick-142000 state/proposal-RNG/acceptance-RNG commitments; tick-142071 state digest, q, W, N_M, sum_I2 | **4,096/4,096** normalized events match; every endpoint comparison passes in every chain; no inferred missing fields |
| G5 — Checkpoint restart and failure recovery | Fresh-process restore at every declared checkpoint; missing/tampered prefix; mid-sweep tick512; warmup boundary; first/final retained boundary; partial output, precision, invariant and representation interruptions | Every restored nonfinal checkpoint reproduces uninterrupted suffix, measurements, final state, both RNGs and computational receipt exactly; all 112 checkpoints validated, including 8 terminal no-op restores; no duplicate/lost committed attempts or invented outcomes |
| G6 — Full replacement replay | Complete chain-major event stream; lossless reconstruction; all decisions/observables checked; all measurements/checkpoints; source receipt/sample comparisons and uninterrupted/restarted comparison | **6,816,000** events = 8×852000, **80,000** retained rows = 8×10000, **112** full checkpoints = 8×14; zero unexplained differences; complete per-chain coverage and successful finalization |
| G7 — Status and provenance | Separate historical and replacement fields; implementation/schema hashes; source/output manifest; actual runtime; first-difference reports and all interrupted attempts | Claim only replacement conformance when G0–G6 pass; historical −1352 stays UNRESOLVED; original authority UNRECOVERED; production NOT_AUTHORIZED; Q2 NOT_RUN |

For G2, construct deterministic test doubles that force integer-selection retries, zero-draw acceptances, rejection, acceptance, multiple prefix refinements and a later probability-one proof. Mark synthetic fixtures as synthetic. A tighter-bound check using the original Bessel routine is useful but is not an independent numerical implementation. A separately written validator should reconstruct global histogram signatures and rational-series bounds for decision verification.

For G5, there are **104 nonfinal** and **8 terminal** checkpoints. The conservative handoff acceptance criterion is a fresh-process suffix-to-end check for every nonfinal checkpoint. If an implementation substitutes segment checks or a smaller restart test set, report that narrower scope and justify it explicitly; do not silently call it this full restart gate. Restart work repeats the same deterministic trajectory and supplies no new independent cohort.

### Representation and interruption cases that need explicit tests

The source uses Python integers for currents but narrower storage for some evidence: signed 64-bit currents in `state_bytes`; unsigned-byte `prefix_bits`, unsigned-short series order and signed 32-bit winding values in the packed legacy event digest; int32 winding/sum_I2 and int16 N_M in retained NumPy arrays. Inspect all packed fields, not just the two limits named in the amendment.

Check values before any narrowing conversion. Canonical event/state evidence remains exact; optional legacy encodings must never wrap or truncate. If a required legacy encoding cannot represent a value, interrupt with the exact available state/prefix and identify the failed comparison obligation. Do not silently continue and claim full legacy conformance. A legacy prefix of 256 bits is already outside its unsigned-byte width; test the failure path synthetically without changing the acceptance procedure or forcing historical RNG draws. No such overflow has been diagnosed in the historical runs.

Inject failure before a row, during a row, after durable row/before checkpoint, during measurement finalization and during checkpoint publication. Recovery must either exactly resume an available pending state or reproduce the suffix from the last verified checkpoint. A file-write error cannot convert an accepted proposal into a rejection or advance the committed clock.

### Secondary numerical cross-checks

For a conforming reproduction of the designated trajectory, expect **769,117 identities**, **6,046,883 nonidentity proposals**, **1,107,368 accepted nonidentity** and **4,939,515 rejected**. Their sums must reconcile, but they are secondary to ordered evidence. The companion's **1,108,720** accepted count is not a tuning target.

## 7. Minimum implementation delivery packet

| Deliverable | Minimum contents |
|---|---|
| Immutable authority/input directory | Exact configuration, event/checkpoint contract, sampler and preserved packets, with manifests and links |
| Adapter/runner | Pinned binding enforcement; original-kernel execution; observer hooks; exact schedule; interruption and restore interfaces |
| Recorder/encoding module | Canonical event/state/RNG/rational encodings; durable commit handling; full checkpoints; exact retained measurements |
| Validator/comparator | Formal field validation plus semantic checks; lossless reconstruction; legacy normalizer; first differences; receipt projection; restart verification |
| Test fixtures and matrix | Preserved 4096-event evidence and checkpoint/sample anchors; clearly labelled synthetic corruption/refinement/failure fixtures; G0–G7 results |
| Environment/implementation record | Source commit or exact source hashes, clean tree/diff disclosure, implementation and schema hashes, software/build, dependency evidence, invocation and compatibility record if needed |
| Execution evidence | `run_binding.json`, `events.jsonl`, `checkpoints.jsonl`, `measurements.jsonl`, interruption records if any, validation/restart/comparison reports, final receipt and manifest |

These are responsibilities, not a requirement for seven separate programs. A small implementation can share modules while retaining separate identities and test results. The preserved sampler file should remain byte-identical. No production-scale inventory, new L=3 cohort, new physics run or mathematical proof rerun is needed to establish this bounded engineering replay.

Recommended implementation order: bind and validate inputs; implement canonical encoders/strict schemas; instrument original methods; pass bounded neutrality/calibration; implement and fault-test restart; generate and validate the complete replacement stream; publish the scoped receipt. Full run and restart evidence follow successful bounded gates, not mere successful source self-tests.

## 8. What genuinely remains missing

1. The separately hashed configuration-enforcing adapter, full recorder/restart driver and replacement-schema validator/normalizer, with passing implementation tests.
2. Formal schemas and concrete implementations for the semantically specified checkpoint, measurement, binding and interruption structures; freeze any proposed field names or commit-protocol choices before execution.
3. A reference-runtime execution environment, or a separately identified compatibility record for the actual environment.
4. The full replacement execution evidence and complete restart/conformance reports. These remain NOT_RUN; this handoff has supplied requirements and recovered inputs, not run results.
5. **For historical diagnosis only:** the companion executable, original authoritative `DYNAMICS.json`, `EVENT_FORMAT.md`, ordered event evidence, complete checkpoint/RNG records and their original configuration/source binding. Their recovery would permit a separate first-divergence investigation; it is not necessary to redefine the already-frozen replacement target.

The exact replacement JSON, designated source bytes, first-run packet, original investigation prefix, new event/checkpoint prose contract, seeds, schedule, checkpoint addresses and retained comparison samples are **not missing**. The full original companion record remains a different evidence gap.

## 9. Status language for the future receipt

Until G0–G7 pass, retain `replacement_full_replay: NOT_RUN` if no full replay has been attempted, or use a truthful scoped status such as IN_PROGRESS, INTERRUPTED, FAIL or INCOMPLETE_EVIDENCE after an attempt. A bounded PASS must include its exact coverage and must not be promoted to full PASS.

After an actual full pass, suitable wording is:

> Replacement replay conforms to TD-COS-FH-001-L2-REPLAY-REPLACEMENT-20260908 within the recorded source, environment, schema, event, measurement and restart checks. Historical reproduction-versus-companion difference remains −1,352 accepted nonidentity updates; its first divergence and cause remain UNRESOLVED. This result supplies no production authorization or physical Q2 result.

This is a future receipt template, not a statement that a pass occurred. The historical production prerequisite to resolve the mismatch is not waived. Any later decision to proceed while it remains unresolved needs its own dated rationale and limits under S14.

## 10. Sources and evidence scope

- **[M]** [Geometry Master, §9 and source list](https://docs.google.com/document/d/12bTng3TNz29eR-M4yD_616QrGUI4wqRI1QUcjLZXYJA/edit).
- **[S9]** [Toroidal Dynamics, exact Master-linked Doc](https://docs.google.com/document/d/1jDBi4zR7W4fkJ_1F_gKU-RQPfkBgiBllXF5Pw1onP1Q/edit); [separate September 6 v0.1 Doc bound by amendment](https://docs.google.com/document/d/1ZMFcH3AV574iMI8qREeOcLS3NPb7rchNnyB1juHnYeM/edit).
- **[S14]** [Prospective replacement amendment](https://docs.google.com/document/d/1gXUSaFvix1R_7-sqtkO5m8VqZqxGnDbl2JiLXas8KF4/edit).
- **[S12]** [Deterministic mismatch investigation](https://docs.google.com/document/d/1G88zvSUXi78R6uCMJYBEZpOmFpIiyP8OAK8_gtd9Hxw/edit).
- **[P14]** Exact recovered `TD_COS_FH_001_Replacement_Amendment_v0.1.zip`, included in the companion delivery; SHA-256 and key file bindings in §2. Read its unchanged event/checkpoint requirements alongside this handoff.
- **[P1]** `preserved/TD_COS_FH_001_L2_FIRST_RUN_PACKET_v0.1.zip` inside P14; SHA-256 `9614c440bbdc07253e2bbe354bda34eadaa707ff85ff5ff0a023c720de5fb4e1`; [Drive first-run receipt](https://docs.google.com/document/d/1R6V-Sa6ga1uSEgFLSidUQQBPeqAWF8RTCy8Zn6ICyUc/edit).
- **[P12]** `preserved/TD_COS_FH_001_Mismatch_Investigation_v0.1.zip` inside P14; SHA-256 `6688106ed6f9dc1d5415f6472c8ebcf3941ae48dc225ad1a34670052b5c459e9`.
- **[R1]** [Research source branch at inspected commit](https://github.com/MailanPatternMonkey-ai/Gettin-Started/tree/98bd55e7668680d1c08d01e041b3920a99bca545/corpus/research_2026-07-08_to_2026-09-08/toroidal_models_and_validation).
- **[R2]** [Mathematics README at inspected commit](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/mathematics/TD-COS-FH-001/README.md) and [provenance](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/mathematics/TD-COS-FH-001/provenance.json).
- **[R3]** [Main A.10 source/build manifest at inspected commit](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/90301d7db659aaf85475dc06e83e8ed57b1677dd/corpus/protocols/simulation_protocol_v0.3/validation/11_source_commit_build_environment_manifest.md).

Freshly verified in this task: artifact integrity, existing receipt structure/sample commitments, source contract self-test, source/code inspection and handoff arithmetic/consistency. Historical bounded replay results remain preserved source evidence. Replacement adapter tests, full replacement replay, fresh-process replacement restarts and comparison to the unavailable companion were not executed.
