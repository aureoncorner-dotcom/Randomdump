"""Deterministic Corner Relay alpha C6 reference transition artifact.

The artifact models two independently owned endpoint key slots (O and S), a
route-only Lambda transport, append-only RAW witness records, and derived
VIEWs.  Key identifiers are structural capability labels, not a production
cryptographic authentication scheme; see README.md for the claim boundary.
"""

from __future__ import annotations

import base64
import hashlib
import json
from dataclasses import asdict, dataclass, replace
from enum import Enum
from types import MappingProxyType
from typing import Iterable, Mapping, NoReturn, Optional, Sequence


ARTIFACT_ID = "Corner-Relay-alpha-C6-reference-v0.1"


class Actor(str, Enum):
    O = "O"
    S = "S"


class EventKind(str, Enum):
    SEND = "SEND"
    ACK = "ACK"
    EXIT = "EXIT"


# Exactly two key slots exist. LambdaTransport never receives either slot.
KEY_FOR: Mapping[Actor, str] = MappingProxyType(
    {Actor.O: "corner-relay:key:O", Actor.S: "corner-relay:key:S"}
)


def peer(actor: Actor) -> Actor:
    return Actor.S if actor is Actor.O else Actor.O


def _canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Event:
    """A declared endpoint event transported without semantic interpretation."""

    event_id: str
    transition_id: str
    kind: EventKind
    actor: Actor
    key_id: str
    target: Actor
    payload_b64: str
    payload_sha256: str
    ref_event_id: Optional[str] = None
    schema: str = "corner-relay-alpha/event/v1"

    @classmethod
    def build(
        cls,
        *,
        transition_id: str,
        kind: EventKind,
        actor: Actor,
        target: Actor,
        payload: bytes = b"",
        ref_event_id: Optional[str] = None,
    ) -> "Event":
        if not transition_id:
            raise ValueError("transition_id must be non-empty")
        body = {
            "schema": "corner-relay-alpha/event/v1",
            "transition_id": transition_id,
            "kind": kind.value,
            "actor": actor.value,
            "key_id": KEY_FOR[actor],
            "target": target.value,
            "payload_b64": base64.b64encode(payload).decode("ascii"),
            "payload_sha256": hashlib.sha256(payload).hexdigest(),
            "ref_event_id": ref_event_id,
        }
        event_id = "evt:" + _sha256_text(_canonical_json(body))
        return cls(
            event_id=event_id,
            transition_id=transition_id,
            kind=kind,
            actor=actor,
            key_id=KEY_FOR[actor],
            target=target,
            payload_b64=body["payload_b64"],
            payload_sha256=body["payload_sha256"],
            ref_event_id=ref_event_id,
        )

    def body_dict(self) -> dict[str, object]:
        return {
            "schema": self.schema,
            "transition_id": self.transition_id,
            "kind": self.kind.value,
            "actor": self.actor.value,
            "key_id": self.key_id,
            "target": self.target.value,
            "payload_b64": self.payload_b64,
            "payload_sha256": self.payload_sha256,
            "ref_event_id": self.ref_event_id,
        }

    def to_dict(self) -> dict[str, object]:
        return {"event_id": self.event_id, **self.body_dict()}

    def canonical_record(self) -> str:
        return _canonical_json(self.to_dict())

    def integrity_errors(self) -> tuple[str, ...]:
        errors: list[str] = []
        if self.actor not in KEY_FOR or self.key_id != KEY_FOR[self.actor]:
            errors.append("ACTOR_KEY_MISMATCH")
        try:
            payload = base64.b64decode(self.payload_b64, validate=True)
        except Exception:
            errors.append("INVALID_PAYLOAD_BASE64")
        else:
            if hashlib.sha256(payload).hexdigest() != self.payload_sha256:
                errors.append("PAYLOAD_HASH_MISMATCH")
        expected_event_id = "evt:" + _sha256_text(_canonical_json(self.body_dict()))
        if self.event_id != expected_event_id:
            errors.append("EVENT_HASH_MISMATCH")
        if self.actor == self.target and self.kind is not EventKind.EXIT:
            errors.append("SELF_ROUTED_NON_EXIT")
        if self.kind is EventKind.SEND and self.ref_event_id is not None:
            errors.append("SEND_HAS_REFERENCE")
        if self.kind is EventKind.ACK and not self.ref_event_id:
            errors.append("ACK_MISSING_REFERENCE")
        if self.kind is EventKind.EXIT and self.target is not self.actor:
            errors.append("EXIT_TARGET_MISMATCH")
        return tuple(errors)


@dataclass(frozen=True)
class WitnessRecord:
    """One retained RAW invocation or delivery record."""

    record_no: int
    witness_id: str
    previous_witness_id: Optional[str]
    transition_id: str
    action: str
    actor: Actor
    key_id: str
    input_record: str
    input_sha256: str
    precondition: str
    precondition_met: bool
    accepted: bool
    effect_applied: bool
    duplicate: bool
    result: str
    before_view_record: str
    before_view_sha256: str
    after_view_record: str
    after_view_sha256: str
    event: Optional[Event]
    schema: str = "corner-relay-alpha/raw-witness/v1"

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["actor"] = self.actor.value
        value["event"] = self.event.to_dict() if self.event else None
        return value


@dataclass(frozen=True)
class EndpointView:
    """A deterministic summary derived from RAW; never a replacement for RAW."""

    actor: Actor
    active: bool
    sent_send_ids: tuple[str, ...]
    received_send_ids: tuple[str, ...]
    sent_ack_ids: tuple[str, ...]
    received_ack_ids: tuple[str, ...]
    own_exit_ids: tuple[str, ...]
    local_effect_ids: tuple[str, ...]
    transition_bindings: tuple[tuple[str, str], ...]
    schema: str = "corner-relay-alpha/view/v1"

    def to_dict(self) -> dict[str, object]:
        return {
            "schema": self.schema,
            "actor": self.actor.value,
            "active": self.active,
            "sent_send_ids": list(self.sent_send_ids),
            "received_send_ids": list(self.received_send_ids),
            "sent_ack_ids": list(self.sent_ack_ids),
            "received_ack_ids": list(self.received_ack_ids),
            "own_exit_ids": list(self.own_exit_ids),
            "local_effect_ids": list(self.local_effect_ids),
            "transition_bindings": [list(item) for item in self.transition_bindings],
        }


class TransitionRejected(RuntimeError):
    def __init__(self, witness: WitnessRecord):
        super().__init__(witness.result)
        self.witness = witness


class Endpoint:
    """One independent endpoint with one fixed key slot and a local RAW ledger."""

    def __init__(self, actor: Actor):
        self.actor = actor
        self._key_id = KEY_FOR[actor]
        self._raw: list[WitnessRecord] = []

    @property
    def key_id(self) -> str:
        return self._key_id

    @property
    def raw(self) -> tuple[WitnessRecord, ...]:
        """An immutable snapshot of the retained append-only source ledger."""

        return tuple(self._raw)

    def _derive_view(self, records: Sequence[WitnessRecord]) -> EndpointView:
        sent_send: dict[str, Event] = {}
        received_send: dict[str, Event] = {}
        sent_ack: dict[str, Event] = {}
        received_ack: dict[str, Event] = {}
        exits: dict[str, Event] = {}
        effects: dict[str, Event] = {}
        bindings: dict[str, str] = {}

        for record in records:
            event = record.event
            if not record.accepted or event is None:
                continue
            effects.setdefault(event.event_id, event)
            if event.actor is self.actor:
                bindings.setdefault(event.transition_id, event.event_id)
            if event.kind is EventKind.SEND:
                if event.actor is self.actor:
                    sent_send.setdefault(event.event_id, event)
                elif event.target is self.actor:
                    received_send.setdefault(event.event_id, event)
            elif event.kind is EventKind.ACK:
                if event.actor is self.actor:
                    sent_ack.setdefault(event.event_id, event)
                elif event.target is self.actor:
                    received_ack.setdefault(event.event_id, event)
            elif event.kind is EventKind.EXIT and event.actor is self.actor:
                exits.setdefault(event.event_id, event)

        return EndpointView(
            actor=self.actor,
            active=not exits,
            sent_send_ids=tuple(sorted(sent_send)),
            received_send_ids=tuple(sorted(received_send)),
            sent_ack_ids=tuple(sorted(sent_ack)),
            received_ack_ids=tuple(sorted(received_ack)),
            own_exit_ids=tuple(sorted(exits)),
            local_effect_ids=tuple(sorted(effects)),
            transition_bindings=tuple(sorted(bindings.items())),
        )

    def view(self) -> EndpointView:
        return self._derive_view(self._raw)

    @staticmethod
    def _view_sha256(view: EndpointView) -> str:
        return _sha256_text(_canonical_json(view.to_dict()))

    def _append_witness(
        self,
        *,
        transition_id: str,
        action: str,
        input_record: str,
        precondition: str,
        precondition_met: bool,
        accepted: bool,
        effect_applied: bool,
        duplicate: bool,
        result: str,
        event: Optional[Event],
    ) -> WitnessRecord:
        before = self.view()
        before_record = _canonical_json(before.to_dict())
        provisional = WitnessRecord(
            record_no=len(self._raw) + 1,
            witness_id="",
            previous_witness_id=(self._raw[-1].witness_id if self._raw else None),
            transition_id=transition_id,
            action=action,
            actor=self.actor,
            key_id=self._key_id,
            input_record=input_record,
            input_sha256=_sha256_text(input_record),
            precondition=precondition,
            precondition_met=precondition_met,
            accepted=accepted,
            effect_applied=effect_applied,
            duplicate=duplicate,
            result=result,
            before_view_record=before_record,
            before_view_sha256=_sha256_text(before_record),
            after_view_record="",
            after_view_sha256="",
            event=event,
        )
        after = self._derive_view([*self._raw, provisional])
        after_record = _canonical_json(after.to_dict())
        provisional = replace(
            provisional,
            after_view_record=after_record,
            after_view_sha256=_sha256_text(after_record),
        )
        witness_body = provisional.to_dict()
        witness_body["witness_id"] = ""
        witness = replace(
            provisional,
            witness_id="wit:" + _sha256_text(_canonical_json(witness_body)),
        )
        self._raw.append(witness)
        return witness

    def _reject(
        self,
        *,
        transition_id: str,
        action: str,
        input_record: str,
        precondition: str,
        result: str,
        event: Optional[Event] = None,
    ) -> NoReturn:
        witness = self._append_witness(
            transition_id=transition_id,
            action=action,
            input_record=input_record,
            precondition=precondition,
            precondition_met=False,
            accepted=False,
            effect_applied=False,
            duplicate=False,
            result=result,
            event=event,
        )
        raise TransitionRejected(witness)

    def _own_event_for_transition(self, transition_id: str) -> Optional[Event]:
        for witness in self._raw:
            event = witness.event
            if (
                witness.accepted
                and event is not None
                and event.actor is self.actor
                and event.transition_id == transition_id
            ):
                return event
        return None

    def _received_send(self, event_id: str) -> Optional[Event]:
        for witness in self._raw:
            event = witness.event
            if (
                witness.accepted
                and event is not None
                and event.event_id == event_id
                and event.kind is EventKind.SEND
                and event.target is self.actor
                and event.actor is not self.actor
            ):
                return event
        return None

    def _sent_send(self, event_id: str) -> Optional[Event]:
        for witness in self._raw:
            event = witness.event
            if (
                witness.accepted
                and event is not None
                and event.event_id == event_id
                and event.kind is EventKind.SEND
                and event.actor is self.actor
            ):
                return event
        return None

    def send(self, transition_id: str, payload: bytes, target: Optional[Actor] = None) -> Event:
        target = peer(self.actor) if target is None else target
        event = Event.build(
            transition_id=transition_id,
            kind=EventKind.SEND,
            actor=self.actor,
            target=target,
            payload=payload,
        )
        existing = self._own_event_for_transition(transition_id)
        if existing is not None:
            if existing == event:
                if not self.view().active:
                    self._reject(
                        transition_id=transition_id,
                        action="SEND_RETRY",
                        input_record=event.canonical_record(),
                        precondition="endpoint remains active for transport retry",
                        result="ENDPOINT_EXITED",
                        event=existing,
                    )
                self._append_witness(
                    transition_id=transition_id,
                    action="SEND_RETRY",
                    input_record=event.canonical_record(),
                    precondition="transition identifier is bound to the exact prior event",
                    precondition_met=True,
                    accepted=True,
                    effect_applied=False,
                    duplicate=True,
                    result="IDEMPOTENT_RETRY_RETURNED_EXISTING_EFFECT",
                    event=existing,
                )
                return existing
            self._reject(
                transition_id=transition_id,
                action="SEND",
                input_record=event.canonical_record(),
                precondition="transition identifier is unused or bound to the exact prior event",
                result="TRANSITION_ID_CONFLICT",
                event=event,
            )
        if target is self.actor:
            self._reject(
                transition_id=transition_id,
                action="SEND",
                input_record=event.canonical_record(),
                precondition="target is the other declared endpoint",
                result="SELF_SEND_FORBIDDEN",
                event=event,
            )
        if not self.view().active:
            self._reject(
                transition_id=transition_id,
                action="SEND",
                input_record=event.canonical_record(),
                precondition="endpoint is active",
                result="ENDPOINT_EXITED",
                event=event,
            )
        self._append_witness(
            transition_id=transition_id,
            action="SEND",
            input_record=event.canonical_record(),
            precondition="endpoint is active and transition identifier is unused",
            precondition_met=True,
            accepted=True,
            effect_applied=True,
            duplicate=False,
            result="SEND_EFFECT_CREATED",
            event=event,
        )
        return event

    def retry(self, transition_id: str) -> Event:
        existing = self._own_event_for_transition(transition_id)
        input_record = _canonical_json({"transition_id": transition_id})
        if existing is None:
            self._reject(
                transition_id=transition_id,
                action="RETRY",
                input_record=input_record,
                precondition="transition identifier names an existing local effect",
                result="UNKNOWN_TRANSITION",
            )
        if not self.view().active and existing.kind is not EventKind.EXIT:
            self._reject(
                transition_id=transition_id,
                action="RETRY",
                input_record=input_record,
                precondition="endpoint remains active or retry is the existing EXIT",
                result="ENDPOINT_EXITED",
                event=existing,
            )
        self._append_witness(
            transition_id=transition_id,
            action="RETRY",
            input_record=existing.canonical_record(),
            precondition="transition identifier names an existing local effect",
            precondition_met=True,
            accepted=True,
            effect_applied=False,
            duplicate=True,
            result="IDEMPOTENT_RETRY_RETURNED_EXISTING_EFFECT",
            event=existing,
        )
        return existing

    def acknowledge(self, transition_id: str, received_send_event_id: str) -> Event:
        received = self._received_send(received_send_event_id)
        input_record = _canonical_json(
            {"transition_id": transition_id, "received_send_event_id": received_send_event_id}
        )
        if received is None:
            self._reject(
                transition_id=transition_id,
                action="ACK",
                input_record=input_record,
                precondition="referenced SEND is present in local accepted RAW",
                result="REFERENCED_SEND_NOT_RECEIVED",
            )
        event = Event.build(
            transition_id=transition_id,
            kind=EventKind.ACK,
            actor=self.actor,
            target=received.actor,
            ref_event_id=received.event_id,
        )
        existing = self._own_event_for_transition(transition_id)
        if existing is not None:
            if existing == event:
                if not self.view().active:
                    self._reject(
                        transition_id=transition_id,
                        action="ACK_RETRY",
                        input_record=event.canonical_record(),
                        precondition="endpoint remains active for transport retry",
                        result="ENDPOINT_EXITED",
                        event=existing,
                    )
                self._append_witness(
                    transition_id=transition_id,
                    action="ACK_RETRY",
                    input_record=event.canonical_record(),
                    precondition="transition identifier is bound to the exact prior ACK",
                    precondition_met=True,
                    accepted=True,
                    effect_applied=False,
                    duplicate=True,
                    result="IDEMPOTENT_RETRY_RETURNED_EXISTING_EFFECT",
                    event=existing,
                )
                return existing
            self._reject(
                transition_id=transition_id,
                action="ACK",
                input_record=event.canonical_record(),
                precondition="transition identifier is unused or bound to the exact prior ACK",
                result="TRANSITION_ID_CONFLICT",
                event=event,
            )
        if not self.view().active:
            self._reject(
                transition_id=transition_id,
                action="ACK",
                input_record=event.canonical_record(),
                precondition="endpoint is active",
                result="ENDPOINT_EXITED",
                event=event,
            )
        self._append_witness(
            transition_id=transition_id,
            action="ACK",
            input_record=event.canonical_record(),
            precondition="endpoint is active and referenced SEND is locally received",
            precondition_met=True,
            accepted=True,
            effect_applied=True,
            duplicate=False,
            result="ACK_EFFECT_CREATED",
            event=event,
        )
        return event

    def exit(self, transition_id: str) -> Event:
        event = Event.build(
            transition_id=transition_id,
            kind=EventKind.EXIT,
            actor=self.actor,
            target=self.actor,
        )
        existing = self._own_event_for_transition(transition_id)
        if existing is not None:
            if existing == event:
                self._append_witness(
                    transition_id=transition_id,
                    action="EXIT_RETRY",
                    input_record=event.canonical_record(),
                    precondition="transition identifier is bound to the exact prior EXIT",
                    precondition_met=True,
                    accepted=True,
                    effect_applied=False,
                    duplicate=True,
                    result="IDEMPOTENT_RETRY_RETURNED_EXISTING_EXIT",
                    event=existing,
                )
                return existing
            self._reject(
                transition_id=transition_id,
                action="EXIT",
                input_record=event.canonical_record(),
                precondition="transition identifier is unused or bound to the exact prior EXIT",
                result="TRANSITION_ID_CONFLICT",
                event=event,
            )
        if not self.view().active:
            self._reject(
                transition_id=transition_id,
                action="EXIT",
                input_record=event.canonical_record(),
                precondition="endpoint is active",
                result="ENDPOINT_ALREADY_EXITED",
                event=event,
            )
        self._append_witness(
            transition_id=transition_id,
            action="EXIT",
            input_record=event.canonical_record(),
            precondition="endpoint is active and transition identifier is unused",
            precondition_met=True,
            accepted=True,
            effect_applied=True,
            duplicate=False,
            result="EXIT_EFFECT_CREATED_HISTORY_RETAINED",
            event=event,
        )
        return event

    def receive(self, event: Event) -> WitnessRecord:
        input_record = event.canonical_record()
        errors = event.integrity_errors()
        if errors:
            self._reject(
                transition_id=event.transition_id,
                action="RECEIVE",
                input_record=input_record,
                precondition="event integrity, actor/key binding, and event schema are valid",
                result="INVALID_EVENT:" + ",".join(errors),
                event=event,
            )
        if event.target is not self.actor or event.actor is self.actor:
            self._reject(
                transition_id=event.transition_id,
                action="RECEIVE",
                input_record=input_record,
                precondition="declared target is this endpoint and actor is the peer endpoint",
                result="ROUTE_OR_ACTOR_MISMATCH",
                event=event,
            )
        if event.kind not in (EventKind.SEND, EventKind.ACK):
            self._reject(
                transition_id=event.transition_id,
                action="RECEIVE",
                input_record=input_record,
                precondition="transported event is SEND or ACK",
                result="NON_TRANSPORT_EVENT",
                event=event,
            )
        if not self.view().active:
            self._reject(
                transition_id=event.transition_id,
                action="RECEIVE",
                input_record=input_record,
                precondition="endpoint is active",
                result="ENDPOINT_EXITED",
                event=event,
            )
        if event.kind is EventKind.ACK and self._sent_send(event.ref_event_id or "") is None:
            self._reject(
                transition_id=event.transition_id,
                action="RECEIVE_ACK",
                input_record=input_record,
                precondition="ACK references a SEND created by this endpoint",
                result="ACK_REFERENCE_NOT_LOCAL_SEND",
                event=event,
            )
        duplicate = event.event_id in self.view().local_effect_ids
        return self._append_witness(
            transition_id=event.transition_id,
            action="RECEIVE_" + event.kind.value,
            input_record=input_record,
            precondition="endpoint active; target, actor/key binding, integrity, and reference valid",
            precondition_met=True,
            accepted=True,
            effect_applied=not duplicate,
            duplicate=duplicate,
            result=("DUPLICATE_DELIVERY_RETAINED_NO_NEW_EFFECT" if duplicate else "DELIVERY_EFFECT_CREATED"),
            event=event,
        )


@dataclass(frozen=True)
class DeliveryResult:
    status: str
    event_id: str
    target: Actor
    witness_id: Optional[str]
    result: str


class LambdaTransport:
    """Lambda routes declared envelopes; it holds no key and decides no meaning."""

    held_key_ids: tuple[str, ...] = ()

    def __init__(self, o: Endpoint, s: Endpoint):
        if {o.actor, s.actor} != {Actor.O, Actor.S}:
            raise ValueError("Lambda requires exactly endpoints O and S")
        self._endpoints = {o.actor: o, s.actor: s}
        self._queue: list[Event] = []
        self._partitioned: set[Actor] = set()

    @property
    def queued_event_ids(self) -> tuple[str, ...]:
        return tuple(event.event_id for event in self._queue)

    def route(self, event: Event) -> None:
        """Queue exactly the event's declared route without reading its payload."""

        self._queue.append(event)

    def set_partition(self, target: Actor, blocked: bool) -> None:
        if blocked:
            self._partitioned.add(target)
        else:
            self._partitioned.discard(target)

    def deliver(self, index: int = 0, *, retain_copy: bool = False) -> DeliveryResult:
        event = self._queue[index]
        if event.target in self._partitioned:
            return DeliveryResult(
                status="PARTITIONED",
                event_id=event.event_id,
                target=event.target,
                witness_id=None,
                result="QUEUE_RETAINED_NO_ENDPOINT_TRANSITION",
            )
        if not retain_copy:
            self._queue.pop(index)
        try:
            witness = self._endpoints[event.target].receive(event)
        except TransitionRejected as rejected:
            witness = rejected.witness
            return DeliveryResult(
                status="REJECTED",
                event_id=event.event_id,
                target=event.target,
                witness_id=witness.witness_id,
                result=witness.result,
            )
        return DeliveryResult(
            status="APPLIED" if witness.effect_applied else "DUPLICATE",
            event_id=event.event_id,
            target=event.target,
            witness_id=witness.witness_id,
            result=witness.result,
        )

    def deliver_event(self, event_id: str, *, retain_copy: bool = False) -> DeliveryResult:
        for index, event in enumerate(self._queue):
            if event.event_id == event_id:
                return self.deliver(index, retain_copy=retain_copy)
        raise KeyError(event_id)


def raw_ledger_jsonl(records: Iterable[WitnessRecord]) -> str:
    """Lossless line-oriented export of retained RAW witness records."""

    return "\n".join(_canonical_json(record.to_dict()) for record in records) + "\n"


def verify_raw_ledger(records: Sequence[WitnessRecord]) -> tuple[str, ...]:
    """Mechanically verify RAW ordering, links, record hashes, and state continuity."""

    errors: list[str] = []
    previous: Optional[WitnessRecord] = None
    for index, record in enumerate(records, start=1):
        prefix = f"record[{index}]"
        if record.record_no != index:
            errors.append(f"{prefix}:RECORD_NUMBER_MISMATCH")
        expected_previous = previous.witness_id if previous else None
        if record.previous_witness_id != expected_previous:
            errors.append(f"{prefix}:PREVIOUS_WITNESS_MISMATCH")
        if _sha256_text(record.input_record) != record.input_sha256:
            errors.append(f"{prefix}:INPUT_HASH_MISMATCH")
        if _sha256_text(record.before_view_record) != record.before_view_sha256:
            errors.append(f"{prefix}:BEFORE_VIEW_HASH_MISMATCH")
        if _sha256_text(record.after_view_record) != record.after_view_sha256:
            errors.append(f"{prefix}:AFTER_VIEW_HASH_MISMATCH")
        if previous and previous.after_view_record != record.before_view_record:
            errors.append(f"{prefix}:VIEW_CONTINUITY_MISMATCH")
        witness_body = record.to_dict()
        witness_body["witness_id"] = ""
        expected_witness_id = "wit:" + _sha256_text(_canonical_json(witness_body))
        if record.witness_id != expected_witness_id:
            errors.append(f"{prefix}:WITNESS_HASH_MISMATCH")
        previous = record
    return tuple(errors)
