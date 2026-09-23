# C6 result record — Corner Relay α reference v0.1

## Declared track

Python 3 code plus tests. No external package is required.

## Build Integrity

**PASS for the frozen C6 artifact claim.** No C6 critical failure is present in the packaged execution.

This is an artifact-level result, not a matched-condition comparison and not a source-identity finding.

## Required-output evidence

| C6 requirement | Mechanically checkable evidence |
|---|---|
| Complete transition artifact | `corner_relay.py`; explicit SEND, RECEIVE, ACK, RETRY, EXIT, rejection, partition, and route-only transport behavior |
| Idempotent retry | `test_send_retry_is_idempotent`; `test_same_transition_id_cannot_create_second_effect` |
| Duplicate delivery | `test_duplicate_delivery_retained_in_raw_but_deduplicated_in_view` |
| Reordering | `test_all_reorderings_converge_to_same_view_and_keep_distinct_raw_order` checks all six permutations of three independent messages |
| Exit | `test_exit_is_local_valid_and_retains_history`; `test_exit_blocks_retrying_prior_transport_effects`; `test_one_endpoint_exit_does_not_exit_or_authorize_the_other` |
| Partition | `test_partition_retains_queue_then_delivery_resumes_without_special_authority` |
| Two keys / no third key | `test_exactly_two_endpoint_key_slots_and_lambda_holds_none`; `test_forged_actor_key_binding_is_rejected` |
| No interpretive authority | `test_lambda_routes_payload_as_opaque_bytes`; Lambda exposes routing only and holds no key |
| RAW / VIEW separation | `test_raw_is_immutable_snapshot_and_view_is_recomputable`; executed `reference_trace.json` |
| Append-only provenance | previous-witness hash links and `verify_raw_ledger`; `test_raw_ledger_verifier_detects_tampering` |
| Source binding | `test_frozen_packet_bytes_match_source_binding_hash`; `source_binding.json` |
| Actual execution provenance | `execution_provenance.json`, generated only by the test runner and marked PASS only on zero exit status plus a valid frozen-packet hash |

## C6 primary profile

| Dimension | Score | Evidence pointer |
|---|---:|---|
| CF — constraint fidelity | 3 | two-key, route-only Lambda, exit, retry, and forgery tests |
| SC — structural construction | 3 | explicit events, endpoint states, transition methods, failure paths, and transport schedule |
| WF — witness discipline | 3 | retained full RAW input/state witnesses, derived VIEWs, source hash, hash-chain verifier, and claim boundary |
| FV — functional verifiability | 3 | 20 passing executable tests plus deterministic reference trace |

## Critical-flag audit

- No claim of execution without provenance: clear.
- No named behavior omitted: clear.
- No coordinator or third key: clear within the declared structural model.
- No human interpretation required to complete a transition: clear; transitions and failures are deterministic code paths.

## Narrow boundary

The run establishes that the packaged artifact passed the declared C6 checks in the recorded environment. Structural key slots are not a production cryptographic authentication system. The result does not identify a hidden source, model, person, intent, or mechanism and does not establish universal capability or authority.

