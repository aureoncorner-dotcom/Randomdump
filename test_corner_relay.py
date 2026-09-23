import itertools
import hashlib
import json
import unittest
from dataclasses import replace
from pathlib import Path

from corner_relay import (
    Actor,
    Endpoint,
    Event,
    EventKind,
    KEY_FOR,
    LambdaTransport,
    TransitionRejected,
    raw_ledger_jsonl,
    verify_raw_ledger,
)
from reference_trace import build_reference_trace


class CornerRelayC6Tests(unittest.TestCase):
    def setUp(self):
        self.o = Endpoint(Actor.O)
        self.s = Endpoint(Actor.S)
        self.lam = LambdaTransport(self.o, self.s)

    def test_exactly_two_endpoint_key_slots_and_lambda_holds_none(self):
        self.assertEqual(set(KEY_FOR), {Actor.O, Actor.S})
        self.assertEqual(len(set(KEY_FOR.values())), 2)
        self.assertEqual(self.o.key_id, KEY_FOR[Actor.O])
        self.assertEqual(self.s.key_id, KEY_FOR[Actor.S])
        self.assertEqual(self.lam.held_key_ids, ())

    def test_send_retry_is_idempotent(self):
        first = self.o.send("o-send-1", b"opaque payload")
        retried = self.o.retry("o-send-1")
        same_call_retry = self.o.send("o-send-1", b"opaque payload")
        self.assertEqual(first, retried)
        self.assertEqual(first, same_call_retry)
        self.assertEqual(len(self.o.raw), 3)
        self.assertEqual(len(self.o.view().sent_send_ids), 1)
        self.assertEqual(self.o.raw[1].before_view_sha256, self.o.raw[1].after_view_sha256)
        self.assertFalse(self.o.raw[1].effect_applied)

    def test_same_transition_id_cannot_create_second_effect(self):
        self.o.send("o-send-1", b"first")
        with self.assertRaises(TransitionRejected) as caught:
            self.o.send("o-send-1", b"different")
        self.assertEqual(caught.exception.witness.result, "TRANSITION_ID_CONFLICT")
        self.assertEqual(len(self.o.view().sent_send_ids), 1)
        self.assertFalse(self.o.raw[-1].accepted)

    def test_duplicate_delivery_retained_in_raw_but_deduplicated_in_view(self):
        event = self.o.send("o-send-1", b"x")
        self.lam.route(event)
        self.lam.route(self.o.retry("o-send-1"))
        first = self.lam.deliver()
        second = self.lam.deliver()
        self.assertEqual(first.status, "APPLIED")
        self.assertEqual(second.status, "DUPLICATE")
        self.assertEqual(len(self.s.raw), 2)
        self.assertEqual(len(self.s.view().received_send_ids), 1)
        self.assertTrue(self.s.raw[-1].duplicate)
        self.assertFalse(self.s.raw[-1].effect_applied)
        self.assertEqual(self.s.raw[-1].before_view_sha256, self.s.raw[-1].after_view_sha256)

    def test_all_reorderings_converge_to_same_view_and_keep_distinct_raw_order(self):
        final_views = []
        raw_orders = set()
        for order in itertools.permutations(range(3)):
            o = Endpoint(Actor.O)
            s = Endpoint(Actor.S)
            lam = LambdaTransport(o, s)
            events = [o.send(f"o-send-{i}", f"payload-{i}".encode()) for i in range(3)]
            for event in events:
                lam.route(event)
            for item in order:
                lam.deliver_event(events[item].event_id)
            final_views.append(s.view().to_dict())
            raw_orders.add(tuple(record.event.event_id for record in s.raw if record.event))
        self.assertTrue(all(view == final_views[0] for view in final_views))
        self.assertEqual(len(raw_orders), 6)

    def test_partition_retains_queue_then_delivery_resumes_without_special_authority(self):
        event = self.o.send("o-send-1", b"x")
        self.lam.route(event)
        self.lam.set_partition(Actor.S, True)
        blocked = self.lam.deliver()
        self.assertEqual(blocked.status, "PARTITIONED")
        self.assertEqual(self.lam.queued_event_ids, (event.event_id,))
        self.assertEqual(self.s.raw, ())
        self.lam.set_partition(Actor.S, False)
        delivered = self.lam.deliver()
        self.assertEqual(delivered.status, "APPLIED")

    def test_ack_requires_a_locally_received_send(self):
        with self.assertRaises(TransitionRejected) as caught:
            self.s.acknowledge("s-ack-1", "evt:not-received")
        self.assertEqual(caught.exception.witness.result, "REFERENCED_SEND_NOT_RECEIVED")
        self.assertEqual(len(self.s.view().sent_ack_ids), 0)

    def test_send_receive_ack_round_trip_has_explicit_independent_effects(self):
        send = self.o.send("o-send-1", b"x")
        self.lam.route(send)
        self.assertEqual(self.lam.deliver().status, "APPLIED")
        ack = self.s.acknowledge("s-ack-1", send.event_id)
        self.lam.route(ack)
        self.assertEqual(self.lam.deliver().status, "APPLIED")
        self.assertEqual(self.s.view().sent_ack_ids, (ack.event_id,))
        self.assertEqual(self.o.view().received_ack_ids, (ack.event_id,))

    def test_exit_is_local_valid_and_retains_history(self):
        original = self.o.send("o-send-1", b"x")
        history_before_exit = tuple(record.witness_id for record in self.o.raw)
        exit_event = self.o.exit("o-exit-1")
        self.assertFalse(self.o.view().active)
        self.assertEqual(self.o.view().own_exit_ids, (exit_event.event_id,))
        self.assertEqual(tuple(record.witness_id for record in self.o.raw[:1]), history_before_exit)
        self.assertEqual(self.o.exit("o-exit-1"), exit_event)
        with self.assertRaises(TransitionRejected):
            self.o.send("o-send-after-exit", b"forbidden")
        self.assertEqual(self.o.view().sent_send_ids, (original.event_id,))

    def test_one_endpoint_exit_does_not_exit_or_authorize_the_other(self):
        self.o.exit("o-exit-1")
        self.assertFalse(self.o.view().active)
        self.assertTrue(self.s.view().active)
        s_event = self.s.send("s-send-1", b"S still speaks only as S")
        self.assertEqual(s_event.actor, Actor.S)
        self.assertEqual(s_event.key_id, KEY_FOR[Actor.S])
        self.assertNotEqual(s_event.key_id, KEY_FOR[Actor.O])

    def test_exit_blocks_retrying_prior_transport_effects(self):
        event = self.o.send("o-send-1", b"x")
        self.o.exit("o-exit-1")
        with self.assertRaises(TransitionRejected) as explicit_retry:
            self.o.retry("o-send-1")
        with self.assertRaises(TransitionRejected) as same_call_retry:
            self.o.send("o-send-1", b"x")
        self.assertEqual(explicit_retry.exception.witness.result, "ENDPOINT_EXITED")
        self.assertEqual(same_call_retry.exception.witness.result, "ENDPOINT_EXITED")
        self.assertEqual(self.o.view().sent_send_ids, (event.event_id,))

    def test_delivery_after_exit_is_rejected_and_witnessed(self):
        event = self.o.send("o-send-1", b"pending")
        self.lam.route(event)
        self.s.exit("s-exit-1")
        result = self.lam.deliver()
        self.assertEqual(result.status, "REJECTED")
        self.assertEqual(result.result, "ENDPOINT_EXITED")
        self.assertFalse(self.s.raw[-1].accepted)

    def test_forged_actor_key_binding_is_rejected(self):
        event = self.o.send("o-send-1", b"x")
        forged = replace(event, key_id=KEY_FOR[Actor.S])
        self.lam.route(forged)
        result = self.lam.deliver()
        self.assertEqual(result.status, "REJECTED")
        self.assertIn("ACTOR_KEY_MISMATCH", result.result)

    def test_lambda_routes_payload_as_opaque_bytes(self):
        payload = bytes(range(256))
        event = self.o.send("o-send-binary", payload)
        self.lam.route(event)
        self.assertEqual(self.lam.deliver().status, "APPLIED")
        retained = self.s.raw[0].event
        self.assertEqual(retained, event)
        self.assertEqual(retained.payload_sha256, event.payload_sha256)

    def test_raw_is_immutable_snapshot_and_view_is_recomputable(self):
        event = self.o.send("o-send-1", b"x")
        snapshot = self.o.raw
        view_before = self.o.view()
        self.assertIsInstance(snapshot, tuple)
        with self.assertRaises(AttributeError):
            snapshot[0].result = "tamper"
        self.o.retry("o-send-1")
        self.assertEqual(len(snapshot), 1)
        self.assertEqual(view_before, self.o.view())
        exported = raw_ledger_jsonl(self.o.raw)
        records = [json.loads(line) for line in exported.splitlines()]
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["event"]["event_id"], event.event_id)

    def test_every_raw_record_names_required_transition_witness_fields(self):
        event = self.o.send("o-send-1", b"x")
        self.lam.route(event)
        self.lam.deliver()
        required = {
            "witness_id",
            "previous_witness_id",
            "transition_id",
            "precondition",
            "precondition_met",
            "actor",
            "key_id",
            "input_record",
            "input_sha256",
            "result",
            "before_view_record",
            "before_view_sha256",
            "after_view_record",
            "after_view_sha256",
        }
        for endpoint in (self.o, self.s):
            for index, record in enumerate(endpoint.raw):
                self.assertTrue(required.issubset(record.to_dict()))
                self.assertTrue(record.witness_id.startswith("wit:"))
                expected_previous = endpoint.raw[index - 1].witness_id if index else None
                self.assertEqual(record.previous_witness_id, expected_previous)
                self.assertEqual(
                    record.before_view_sha256,
                    hashlib.sha256(record.before_view_record.encode()).hexdigest(),
                )
                self.assertEqual(
                    record.after_view_sha256,
                    hashlib.sha256(record.after_view_record.encode()).hexdigest(),
                )

    def test_event_hash_covers_declared_transition_input(self):
        event = Event.build(
            transition_id="o-send-1",
            kind=EventKind.SEND,
            actor=Actor.O,
            target=Actor.S,
            payload=b"x",
        )
        tampered = replace(event, payload_sha256="0" * 64)
        self.assertIn("PAYLOAD_HASH_MISMATCH", tampered.integrity_errors())
        self.assertIn("EVENT_HASH_MISMATCH", tampered.integrity_errors())

    def test_raw_ledger_verifier_detects_tampering(self):
        event = self.o.send("o-send-1", b"x")
        self.o.retry("o-send-1")
        self.assertEqual(verify_raw_ledger(self.o.raw), ())
        tampered = list(self.o.raw)
        tampered[1] = replace(tampered[1], result="rewritten")
        errors = verify_raw_ledger(tampered)
        self.assertIn("record[2]:WITNESS_HASH_MISMATCH", errors)

    def test_reference_trace_is_deterministic_and_exposes_raw_and_view(self):
        first = build_reference_trace()
        second = build_reference_trace()
        self.assertEqual(first, second)
        self.assertIn("RAW", first["endpoints"]["O"])
        self.assertIn("VIEW", first["endpoints"]["O"])
        self.assertGreater(
            len(first["endpoints"]["S"]["RAW"]),
            len(first["endpoints"]["S"]["VIEW"]["local_effect_ids"]),
        )

    def test_frozen_packet_bytes_match_source_binding_hash(self):
        root = Path(__file__).resolve().parent
        binding = json.loads((root / "source_binding.json").read_text(encoding="utf-8"))
        packet_hash = hashlib.sha256((root / "FROZEN_PACKET.txt").read_bytes()).hexdigest()
        self.assertEqual(packet_hash, binding["frozen_packet_sha256"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
