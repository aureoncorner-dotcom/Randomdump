"""Generate one deterministic, inspectable RAW-versus-VIEW execution trace."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path

from corner_relay import Actor, Endpoint, LambdaTransport


def _canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _delivery_dict(result) -> dict[str, object]:
    value = asdict(result)
    value["target"] = result.target.value
    return value


def build_reference_trace() -> dict[str, object]:
    o = Endpoint(Actor.O)
    s = Endpoint(Actor.S)
    lam = LambdaTransport(o, s)
    deliveries: list[dict[str, object]] = []

    first = o.send("o-send-001", b"first opaque payload")
    lam.route(first)
    lam.route(o.retry("o-send-001"))
    second = o.send("o-send-002", b"second opaque payload")
    lam.route(second)

    lam.set_partition(Actor.S, True)
    deliveries.append(_delivery_dict(lam.deliver_event(second.event_id)))
    lam.set_partition(Actor.S, False)

    # Deliberately deliver the later SEND first, then the original and its duplicate.
    deliveries.append(_delivery_dict(lam.deliver_event(second.event_id)))
    deliveries.append(_delivery_dict(lam.deliver_event(first.event_id)))
    deliveries.append(_delivery_dict(lam.deliver_event(first.event_id)))

    ack = s.acknowledge("s-ack-001", first.event_id)
    lam.route(ack)
    deliveries.append(_delivery_dict(lam.deliver()))

    s.exit("s-exit-001")
    late = o.send("o-send-003", b"delivery after S exit")
    lam.route(late)
    deliveries.append(_delivery_dict(lam.deliver()))

    trace = {
        "schema": "corner-relay-alpha/reference-trace/v1",
        "artifact_id": "Corner-Relay-alpha-C6-reference-v0.1",
        "schedule": [
            "queue SEND-001",
            "queue idempotent retry SEND-001",
            "queue SEND-002",
            "partition S and attempt SEND-002",
            "unpartition and deliver SEND-002 before SEND-001",
            "deliver SEND-001 and its duplicate",
            "S creates ACK-001 and O receives it",
            "S exits",
            "late delivery to S is rejected and witnessed",
        ],
        "delivery_results": deliveries,
        "endpoints": {
            "O": {
                "RAW": [record.to_dict() for record in o.raw],
                "VIEW": o.view().to_dict(),
            },
            "S": {
                "RAW": [record.to_dict() for record in s.raw],
                "VIEW": s.view().to_dict(),
            },
        },
        "checks": {
            "lambda_held_key_ids": list(lam.held_key_ids),
            "S_raw_record_count": len(s.raw),
            "S_view_effect_count": len(s.view().local_effect_ids),
            "S_active_after_exit": s.view().active,
        },
    }
    return trace


def write_reference_trace(path: Path) -> str:
    trace = build_reference_trace()
    trace_hash = hashlib.sha256(_canonical_json(trace).encode("utf-8")).hexdigest()
    wrapper = {"trace_sha256": trace_hash, "trace": trace}
    path.write_text(json.dumps(wrapper, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return trace_hash


if __name__ == "__main__":
    destination = Path(__file__).resolve().with_name("reference_trace.json")
    print(write_reference_trace(destination))

