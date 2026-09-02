"""Strict canonical JSONL ledger with a SHA-256 evidence chain.

The chain is tamper-*evident*, not access control and not a digital signature.
Anyone able to rewrite the complete file can recompute an unkeyed SHA-256 chain.
Use filesystem protections or an external signed checkpoint when adversarial
rewrites are in scope.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import hashlib
import json
import math
import os
from pathlib import Path
import re
from typing import Any, Mapping

from .engine import AxisSpec, AxisStatus, EngineConfig, SimulationEngine
from .geometry import return_residual
from .model import (
    JSONValue,
    MAX_JSON_NESTING,
    ClockSnapshot,
    MultiAxisTickEvent,
    TickEvent,
    format_utc,
)
from .number_theory import is_prime
from .routing import MAX_ROUTE_NODE, allowed_moves


SCHEMA_VERSION = "prime-axis-ledger/1.0"
GENESIS_HASH = "0" * 64
MAX_LEDGER_LINE_BYTES = 4 * 1024 * 1024

_HASH_RE = re.compile(r"^[0-9a-f]{64}$")
_RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")
_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$")
_RECORD_KEYS = {
    "schema_version",
    "run_id",
    "seq",
    "timestamp_utc",
    "record_type",
    "payload",
    "prev_hash",
    "record_hash",
}


class DurabilityPolicy(str, Enum):
    """How each record is handed to the operating system."""

    NONE = "none"
    FLUSH = "flush"
    FSYNC = "fsync"


@dataclass(frozen=True, slots=True)
class AuditIssue:
    """One ledger integrity or format finding."""

    code: str
    message: str
    line_number: int | None = None
    fatal: bool = True

    def __post_init__(self) -> None:
        if not isinstance(self.code, str) or not self.code:
            raise ValueError("code must be a non-empty string")
        if not isinstance(self.message, str) or not self.message:
            raise ValueError("message must be a non-empty string")
        if self.line_number is not None:
            if isinstance(self.line_number, bool) or not isinstance(self.line_number, int):
                raise TypeError("line_number must be an integer or None")
            if self.line_number < 1:
                raise ValueError("line_number must be >= 1")
        if not isinstance(self.fatal, bool):
            raise TypeError("fatal must be a bool")

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "code": self.code,
            "message": self.message,
            "line_number": self.line_number,
            "fatal": self.fatal,
        }


@dataclass(frozen=True, slots=True)
class AuditReport:
    """Structured result returned by :func:`audit_ledger`."""

    path: str
    valid: bool
    sealed: bool
    truncated: bool
    tampered: bool
    run_id: str | None
    record_count: int
    event_count: int
    last_seq: int | None
    last_hash: str | None
    issues: tuple[AuditIssue, ...]

    @property
    def ok(self) -> bool:
        return self.valid

    def to_dict(self) -> dict[str, JSONValue]:
        return {
            "path": self.path,
            "valid": self.valid,
            "sealed": self.sealed,
            "truncated": self.truncated,
            "tampered": self.tampered,
            "run_id": self.run_id,
            "record_count": self.record_count,
            "event_count": self.event_count,
            "last_seq": self.last_seq,
            "last_hash": self.last_hash,
            "issues": [issue.to_dict() for issue in self.issues],
        }


def _normalize_json(
    value: object,
    *,
    path: str = "payload",
    depth: int = 0,
) -> JSONValue:
    if depth > MAX_JSON_NESTING:
        raise ValueError(
            f"{path} exceeds the maximum JSON nesting depth of "
            f"{MAX_JSON_NESTING}"
        )
    if value is None or isinstance(value, (str, bool)):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"{path} contains NaN or Infinity")
        return value
    if isinstance(value, list):
        return [
            _normalize_json(
                item,
                path=f"{path}[{index}]",
                depth=depth + 1,
            )
            for index, item in enumerate(value)
        ]
    if isinstance(value, Mapping):
        normalized: dict[str, JSONValue] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise TypeError(f"{path} keys must be strings")
            normalized[key] = _normalize_json(
                item,
                path=f"{path}.{key}",
                depth=depth + 1,
            )
        return normalized
    raise TypeError(f"{path} contains non-JSON type {type(value).__name__}")


def canonical_json(value: object) -> str:
    """Serialize a strict JSON value to the ledger's canonical representation."""

    normalized = _normalize_json(value)
    return json.dumps(
        normalized,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _hash_record(record_without_hash: Mapping[str, object]) -> str:
    payload = canonical_json(record_without_hash).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _validate_run_id(run_id: object) -> str:
    if not isinstance(run_id, str) or not _RUN_ID_RE.fullmatch(run_id):
        raise ValueError(
            "run_id must be 1-128 characters: ASCII letters, digits, dot, underscore, colon, or hyphen"
        )
    return run_id


def _timestamp(value: datetime | None = None) -> str:
    return format_utc(datetime.now(timezone.utc) if value is None else value)


class LedgerWriter:
    """Create one new ledger and seal it on a successful close.

    Existing paths are rejected by default using an exclusive create.  Passing
    ``overwrite=True`` is the only operation that truncates an existing regular
    file, and symbolic links are still refused.  A normal context-manager exit
    writes a final seal; an exceptional exit leaves the file unsealed so audit
    can identify the incomplete run.
    """

    def __init__(
        self,
        path: str | os.PathLike[str],
        *,
        run_id: str,
        overwrite: bool = False,
        durability: DurabilityPolicy | str = DurabilityPolicy.FSYNC,
    ) -> None:
        if not isinstance(overwrite, bool):
            raise TypeError("overwrite must be a bool")
        try:
            policy = DurabilityPolicy(durability)
        except (TypeError, ValueError) as exc:
            raise ValueError("durability must be 'none', 'flush', or 'fsync'") from exc

        self.path = Path(path)
        self.run_id = _validate_run_id(run_id)
        self.durability = policy
        self._seq = 0
        self._event_count = 0
        self._prev_hash = GENESIS_HASH
        self._sealed = False
        self._closed = False

        parent = self.path.parent
        if not parent.exists() or not parent.is_dir():
            raise FileNotFoundError(f"ledger parent directory does not exist: {parent}")
        if self.path.exists() and self.path.is_dir():
            raise IsADirectoryError(str(self.path))
        if self.path.is_symlink():
            raise ValueError("refusing to write a ledger through a symbolic link")

        flags = os.O_WRONLY | os.O_CREAT
        flags |= os.O_TRUNC if overwrite else os.O_EXCL
        flags |= getattr(os, "O_BINARY", 0)
        flags |= getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(self.path, flags, 0o600)
        try:
            self._stream = os.fdopen(fd, "wb")
        except BaseException:
            os.close(fd)
            raise

    @property
    def closed(self) -> bool:
        return self._closed

    @property
    def next_seq(self) -> int:
        return self._seq

    @property
    def last_hash(self) -> str:
        return self._prev_hash

    def __enter__(self) -> LedgerWriter:
        if self._closed:
            raise ValueError("cannot re-enter a closed ledger")
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> bool:
        self.close(seal=exc_type is None)
        return False

    def _ensure_open(self) -> None:
        if self._closed:
            raise ValueError("ledger is closed")
        if self._sealed:
            raise ValueError("ledger is sealed")

    def _synchronize(self) -> None:
        if self.durability is DurabilityPolicy.NONE:
            return
        self._stream.flush()
        if self.durability is DurabilityPolicy.FSYNC:
            os.fsync(self._stream.fileno())

    def _append_record(
        self,
        record_type: str,
        payload: Mapping[str, object],
        timestamp_utc: datetime | None,
    ) -> dict[str, JSONValue]:
        self._ensure_open()
        normalized_payload = _normalize_json(payload)
        if not isinstance(normalized_payload, dict):
            raise TypeError("record payload must be a mapping")
        base: dict[str, object] = {
            "schema_version": SCHEMA_VERSION,
            "run_id": self.run_id,
            "seq": self._seq,
            "timestamp_utc": _timestamp(timestamp_utc),
            "record_type": record_type,
            "payload": normalized_payload,
            "prev_hash": self._prev_hash,
        }
        record_hash = _hash_record(base)
        record: dict[str, object] = {**base, "record_hash": record_hash}
        encoded = canonical_json(record).encode("utf-8") + b"\n"
        if len(encoded) > MAX_LEDGER_LINE_BYTES:
            raise ValueError(
                f"ledger record exceeds the {MAX_LEDGER_LINE_BYTES}-byte limit"
            )
        written = self._stream.write(encoded)
        if written != len(encoded):
            raise OSError(f"short ledger write: wrote {written} of {len(encoded)} bytes")

        # Advance in-memory chain state before a durability call.  If flush or
        # fsync fails, retrying the same writer must not emit a duplicate seq.
        self._prev_hash = record_hash
        self._seq += 1
        if record_type == "event":
            self._event_count += 1
        elif record_type == "seal":
            self._sealed = True
        self._synchronize()
        return json.loads(canonical_json(record))

    def append(
        self,
        event: TickEvent | MultiAxisTickEvent | Mapping[str, JSONValue],
        *,
        timestamp_utc: datetime | None = None,
    ) -> dict[str, JSONValue]:
        """Append one typed tick or strict JSON mapping and return its envelope."""

        if isinstance(event, (TickEvent, MultiAxisTickEvent)):
            payload = event.to_dict()
            effective_timestamp = event.clock.wall_time_utc if timestamp_utc is None else timestamp_utc
        elif isinstance(event, Mapping):
            payload = event
            effective_timestamp = timestamp_utc
        else:
            raise TypeError("event must be a TickEvent, MultiAxisTickEvent, or mapping")
        return self._append_record("event", payload, effective_timestamp)

    def close(self, *, seal: bool = True) -> None:
        """Close the stream, optionally writing the detectable end-of-run seal."""

        if not isinstance(seal, bool):
            raise TypeError("seal must be a bool")
        if self._closed:
            return
        try:
            if seal and not self._sealed:
                self._append_record(
                    "seal",
                    {
                        "event_count": self._event_count,
                        "final_event_hash": self._prev_hash,
                    },
                    None,
                )
            if self.durability is not DurabilityPolicy.NONE:
                self._synchronize()
        finally:
            self._stream.close()
            self._closed = True


class _DuplicateKey(ValueError):
    pass


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateKey(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    raise ValueError(f"non-standard JSON numeric constant: {value}")


def _parse_timestamp(value: object) -> bool:
    if not isinstance(value, str) or not _UTC_RE.fullmatch(value):
        return False
    try:
        datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return False
    return True


def _bounded_ledger_lines(stream: object):
    """Yield physical ledger lines without allocating an unbounded record."""

    line_number = 0
    while True:
        raw_line = stream.readline(MAX_LEDGER_LINE_BYTES + 1)  # type: ignore[attr-defined]
        if not raw_line:
            return
        line_number += 1
        if len(raw_line) <= MAX_LEDGER_LINE_BYTES:
            yield line_number, raw_line
            continue

        # Drain the remainder of this one physical record in bounded chunks so
        # the next yielded value starts at the next JSONL record.
        ends_here = raw_line.endswith(b"\n")
        while not ends_here:
            chunk = stream.readline(MAX_LEDGER_LINE_BYTES + 1)  # type: ignore[attr-defined]
            if not chunk:
                break
            ends_here = chunk.endswith(b"\n")
        yield line_number, None


def _is_integer(
    value: object,
    *,
    minimum: int | None = None,
    maximum: int | None = None,
) -> bool:
    if isinstance(value, bool) or not isinstance(value, int):
        return False
    if minimum is not None and value < minimum:
        return False
    return maximum is None or value <= maximum


def _is_finite_number(
    value: object,
    *,
    minimum: float | None = None,
    maximum: float | None = None,
) -> bool:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        number = float(value)
    except (OverflowError, ValueError):
        return False
    if not math.isfinite(number):
        return False
    if minimum is not None and number < minimum:
        return False
    if maximum is not None and number > maximum:
        return False
    return True


def _validate_clock_payload(
    clock: object,
    *,
    path: str,
) -> tuple[list[tuple[str, str]], int | None]:
    issues: list[tuple[str, str]] = []
    if not isinstance(clock, dict):
        return [("SEMANTIC_CLOCK", f"{path} must be an object")], None
    required = {
        "opportunity_index",
        "lattice_time_s",
        "monotonic_time_s",
        "slip_s",
        "wall_time_utc",
    }
    if set(clock) != required:
        issues.append(
            (
                "SEMANTIC_CLOCK_SHAPE",
                f"{path} keys must be exactly {sorted(required)}",
            )
        )
    index = clock.get("opportunity_index")
    valid_index = index if _is_integer(index, minimum=0) else None
    if valid_index is None:
        issues.append(
            ("SEMANTIC_CLOCK_INDEX", f"{path}.opportunity_index must be a non-negative integer")
        )
    lattice = clock.get("lattice_time_s")
    monotonic = clock.get("monotonic_time_s")
    slip = clock.get("slip_s")
    if not _is_finite_number(lattice, minimum=0.0):
        issues.append(
            ("SEMANTIC_LATTICE_TIME", f"{path}.lattice_time_s must be finite and non-negative")
        )
    if not _is_finite_number(monotonic, minimum=0.0):
        issues.append(
            ("SEMANTIC_MONOTONIC_TIME", f"{path}.monotonic_time_s must be finite and non-negative")
        )
    if not _is_finite_number(slip):
        issues.append(("SEMANTIC_CLOCK_SLIP", f"{path}.slip_s must be finite"))
    elif _is_finite_number(lattice, minimum=0.0) and _is_finite_number(
        monotonic, minimum=0.0
    ):
        expected_slip = float(monotonic) - float(lattice)  # type: ignore[arg-type]
        if float(slip) != expected_slip:
            issues.append(
                ("SEMANTIC_CLOCK_SLIP", f"{path}.slip_s is inconsistent with the two source clocks")
            )
    if not _parse_timestamp(clock.get("wall_time_utc")):
        issues.append(
            ("SEMANTIC_WALL_TIME", f"{path}.wall_time_utc must be canonical UTC")
        )
    return issues, valid_index


def _validate_axis_payload(
    axis: object,
    *,
    path: str,
    expected_index: int | None,
) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    if not isinstance(axis, dict):
        return [("SEMANTIC_AXIS", f"{path} must be an object")]
    if set(axis) != {"node", "is_prime", "geometry"}:
        issues.append(
            (
                "SEMANTIC_AXIS_SHAPE",
                f"{path} must contain only node, is_prime, and geometry",
            )
        )
    node = axis.get("node")
    prime_flag = axis.get("is_prime")
    if not _is_integer(node, minimum=1, maximum=MAX_ROUTE_NODE):
        issues.append(
            ("SEMANTIC_NODE", f"{path}.node must be in [1, {MAX_ROUTE_NODE}]")
        )
    if not isinstance(prime_flag, bool):
        issues.append(("SEMANTIC_PRIME_FLAG", f"{path}.is_prime must be boolean"))
    elif _is_integer(
        node, minimum=1, maximum=MAX_ROUTE_NODE
    ) and prime_flag is not is_prime(node):  # type: ignore[arg-type]
        issues.append(
            ("SEMANTIC_PRIME_FLAG", f"{path}.is_prime is inconsistent with node")
        )

    geometry = axis.get("geometry")
    if not isinstance(geometry, dict):
        issues.append(("SEMANTIC_GEOMETRY", f"{path}.geometry must be an object"))
        return issues
    geometry_keys = {
        "opportunity_index",
        "quotient_order",
        "quotient_label",
        "expected_phase",
        "observed_phase",
        "residual",
        "tolerance",
        "closure_status",
    }
    if set(geometry) != geometry_keys:
        issues.append(
            (
                "SEMANTIC_GEOMETRY_SHAPE",
                f"{path}.geometry keys must be exactly {sorted(geometry_keys)}",
            )
        )
    index = geometry.get("opportunity_index")
    if not _is_integer(index, minimum=0):
        issues.append(
            ("SEMANTIC_GEOMETRY_INDEX", f"{path}.geometry.opportunity_index must be non-negative")
        )
    elif expected_index is not None and index != expected_index:
        issues.append(
            ("SEMANTIC_GEOMETRY_INDEX", f"{path}.geometry does not share the tick opportunity index")
        )

    order = geometry.get("quotient_order")
    valid_order = _is_integer(order, minimum=1) and int(order) <= 2**53  # type: ignore[arg-type]
    if not valid_order:
        issues.append(
            ("SEMANTIC_QUOTIENT_ORDER", f"{path}.geometry.quotient_order must be in [1, 2**53]")
        )
    elif geometry.get("quotient_label") != f"C_{order}":
        issues.append(
            ("SEMANTIC_QUOTIENT_LABEL", f"{path}.geometry.quotient_label is inconsistent with its order")
        )

    expected_phase = geometry.get("expected_phase")
    observed_phase = geometry.get("observed_phase")
    for name, value in (
        ("expected_phase", expected_phase),
        ("observed_phase", observed_phase),
    ):
        if not _is_finite_number(value, minimum=0.0) or float(value) >= 1.0:  # type: ignore[arg-type]
            issues.append(
                ("SEMANTIC_PHASE", f"{path}.geometry.{name} must be in [0, 1)")
            )
    residual = geometry.get("residual")
    tolerance = geometry.get("tolerance")
    if not _is_finite_number(residual, minimum=0.0, maximum=0.5):
        issues.append(
            ("SEMANTIC_RESIDUAL", f"{path}.geometry.residual must be in [0, 0.5]")
        )
    if not _is_finite_number(tolerance, minimum=0.0, maximum=0.5):
        issues.append(
            ("SEMANTIC_TOLERANCE", f"{path}.geometry.tolerance must be in [0, 0.5]")
        )

    phases_valid = all(
        _is_finite_number(value, minimum=0.0) and float(value) < 1.0  # type: ignore[arg-type]
        for value in (expected_phase, observed_phase)
    )
    if valid_order and phases_valid and _is_finite_number(
        residual, minimum=0.0, maximum=0.5
    ):
        expected_residual = return_residual(
            float(expected_phase),  # type: ignore[arg-type]
            float(observed_phase),  # type: ignore[arg-type]
            int(order),  # type: ignore[arg-type]
        )
        if float(residual) != expected_residual:
            issues.append(
                ("SEMANTIC_RESIDUAL", f"{path}.geometry.residual does not match the declared comparator")
            )

    status = geometry.get("closure_status")
    if not isinstance(status, str) or status not in {"CLOSED", "FAILED", "UNRESOLVED"}:
        issues.append(
            ("SEMANTIC_CLOSURE", f"{path}.geometry.closure_status is invalid")
        )
    elif _is_finite_number(residual, minimum=0.0, maximum=0.5) and _is_finite_number(
        tolerance, minimum=0.0, maximum=0.5
    ):
        if status == "CLOSED" and float(residual) > float(tolerance):
            issues.append(("SEMANTIC_CLOSURE", f"{path}.geometry CLOSED residual exceeds tolerance"))
        if status == "FAILED" and float(residual) <= float(tolerance):
            issues.append(("SEMANTIC_CLOSURE", f"{path}.geometry FAILED residual does not exceed tolerance"))
    return issues


def _validate_event_payload(payload: dict[str, object]) -> list[tuple[str, str]]:
    """Validate recognized Prime Axis payloads beyond envelope integrity."""

    event_type = payload.get("event_type")
    issues: list[tuple[str, str]] = []
    if event_type == "simulation_start":
        config = payload.get("config")
        axes = payload.get("axes")
        validated_config: EngineConfig | None = None
        if not isinstance(config, dict):
            issues.append(("SEMANTIC_START_CONFIG", "payload.config must be an object"))
            lower = upper = None
        else:
            try:
                validated_config = EngineConfig(**config)
            except (TypeError, ValueError, OverflowError) as exc:
                issues.append(
                    (
                        "SEMANTIC_START_CONFIG",
                        f"payload.config is not an executable engine configuration: {exc}",
                    )
                )
                validated_config = None
            lower = config.get("lower_bound")
            upper = config.get("upper_bound")
            if not _is_integer(lower, minimum=1, maximum=MAX_ROUTE_NODE):
                issues.append(("SEMANTIC_START_CONFIG", "lower_bound is invalid"))
            if not _is_integer(upper, minimum=1, maximum=MAX_ROUTE_NODE):
                issues.append(("SEMANTIC_START_CONFIG", "upper_bound is invalid"))
            if (
                _is_integer(lower, minimum=1, maximum=MAX_ROUTE_NODE)
                and _is_integer(upper, minimum=1, maximum=MAX_ROUTE_NODE)
                and int(lower) > int(upper)  # type: ignore[arg-type]
            ):
                issues.append(("SEMANTIC_START_CONFIG", "configured bounds are reversed"))
            for name in (
                "friction_scale",
                "search_limit",
                "max_ticks",
                "max_axes",
                "max_incidents",
                "reroute_after_incidents",
            ):
                if not _is_integer(config.get(name), minimum=1):
                    issues.append(("SEMANTIC_START_CONFIG", f"config.{name} must be positive"))
            if not _is_finite_number(config.get("lattice_period_s"), minimum=0.0) or float(
                config.get("lattice_period_s", 0.0)
            ) <= 0.0:
                issues.append(("SEMANTIC_START_CONFIG", "config.lattice_period_s must be positive"))
            if not isinstance(config.get("pace"), bool):
                issues.append(("SEMANTIC_START_CONFIG", "config.pace must be boolean"))

        if not isinstance(axes, list) or not axes:
            issues.append(("SEMANTIC_START_AXES", "payload.axes must be a non-empty array"))
        else:
            if validated_config is not None and len(axes) > validated_config.max_axes:
                issues.append(
                    (
                        "SEMANTIC_START_AXES",
                        f"payload.axes exceeds configured max_axes={validated_config.max_axes}",
                    )
                )
            labels: set[str] = set()
            for position, axis in enumerate(axes):
                path = f"payload.axes[{position}]"
                if not isinstance(axis, dict):
                    issues.append(("SEMANTIC_START_AXIS", f"{path} must be an object"))
                    continue
                try:
                    AxisSpec(**axis)
                except (TypeError, ValueError, OverflowError) as exc:
                    issues.append(
                        (
                            "SEMANTIC_START_AXIS",
                            f"{path} is not an executable axis specification: {exc}",
                        )
                    )
                label = axis.get("label")
                if (
                    not isinstance(label, str)
                    or not label
                    or label.strip() != label
                    or len(label) > 64
                    or any(ord(character) < 32 or ord(character) == 127 for character in label)
                ):
                    issues.append(("SEMANTIC_START_AXIS", f"{path}.label is invalid"))
                elif label.casefold() in labels:
                    issues.append(("SEMANTIC_START_AXIS", f"{path}.label is duplicated"))
                else:
                    labels.add(label.casefold())
                start = axis.get("start")
                target = axis.get("target")
                for name, value in (("start", start), ("target", target)):
                    if not _is_integer(value, minimum=1, maximum=MAX_ROUTE_NODE):
                        issues.append(("SEMANTIC_START_AXIS", f"{path}.{name} is invalid"))
                    elif (
                        isinstance(config, dict)
                        and _is_integer(lower, minimum=1, maximum=MAX_ROUTE_NODE)
                        and _is_integer(upper, minimum=1, maximum=MAX_ROUTE_NODE)
                        and not int(lower) <= int(value) <= int(upper)  # type: ignore[arg-type]
                    ):
                        issues.append(("SEMANTIC_START_AXIS", f"{path}.{name} is outside configured bounds"))
                if _is_integer(target, minimum=1, maximum=MAX_ROUTE_NODE) and not is_prime(target):  # type: ignore[arg-type]
                    issues.append(("SEMANTIC_START_AXIS", f"{path}.target must be prime"))
                order = axis.get("quotient_order")
                if not _is_integer(order, minimum=1, maximum=2**53):
                    issues.append(("SEMANTIC_START_AXIS", f"{path}.quotient_order is invalid"))
                tolerance = axis.get("tolerance")
                if not _is_finite_number(tolerance, minimum=0.0, maximum=0.5):
                    issues.append(("SEMANTIC_START_AXIS", f"{path}.tolerance is invalid"))
        if payload.get("phase_basis") != "normalized bounded-route position":
            issues.append(("SEMANTIC_PHASE_BASIS", "payload.phase_basis is unsupported"))
        expected_clock_contract = {
            "opportunity": "discrete logical index",
            "lattice": "configured ideal model time",
            "monotonic": "elapsed execution observation",
            "utc": "human correlation only",
        }
        if payload.get("clock_contract") != expected_clock_contract:
            issues.append(
                (
                    "SEMANTIC_CLOCK_CONTRACT",
                    "payload.clock_contract must exactly match the executable engine contract",
                )
            )
        return issues

    if event_type == "tick":
        clock_issues, index = _validate_clock_payload(payload.get("clock"), path="payload.clock")
        issues.extend(clock_issues)
        issues.extend(
            _validate_axis_payload(payload.get("axis"), path="payload.axis", expected_index=index)
        )
        severity = payload.get("severity")
        if not isinstance(severity, str) or severity not in {"INFO", "WARNING", "CRITICAL"}:
            issues.append(("SEMANTIC_SEVERITY", "payload.severity is invalid"))
        if not isinstance(payload.get("message"), str):
            issues.append(("SEMANTIC_MESSAGE", "payload.message must be a string"))
        if not isinstance(payload.get("metadata"), dict):
            issues.append(("SEMANTIC_METADATA", "payload.metadata must be an object"))
        return issues

    if event_type == "multi_axis_tick":
        clock_issues, index = _validate_clock_payload(payload.get("clock"), path="payload.clock")
        issues.extend(clock_issues)
        axes = payload.get("axes")
        if not isinstance(axes, dict) or not axes:
            issues.append(("SEMANTIC_AXES", "payload.axes must be a non-empty object"))
        else:
            for label, axis in axes.items():
                if (
                    not isinstance(label, str)
                    or not label
                    or label.strip() != label
                    or len(label) > 64
                    or any(ord(character) < 32 or ord(character) == 127 for character in label)
                ):
                    issues.append(("SEMANTIC_AXIS_LABEL", "payload.axes contains an invalid label"))
                    continue
                issues.extend(
                    _validate_axis_payload(
                        axis,
                        path=f"payload.axes.{label}",
                        expected_index=index,
                    )
                )
        max_severity = payload.get("max_severity")
        if not isinstance(max_severity, str) or max_severity not in {"INFO", "WARNING", "CRITICAL"}:
            issues.append(("SEMANTIC_SEVERITY", "payload.max_severity is invalid"))
        if not isinstance(payload.get("message"), str):
            issues.append(("SEMANTIC_MESSAGE", "payload.message must be a string"))
        if not isinstance(payload.get("metadata"), dict):
            issues.append(("SEMANTIC_METADATA", "payload.metadata must be an object"))
        return issues

    if event_type == "simulation_complete":
        succeeded = payload.get("succeeded")
        opportunities = payload.get("opportunities")
        axes = payload.get("axes")
        if not isinstance(succeeded, bool):
            issues.append(("SEMANTIC_COMPLETION", "payload.succeeded must be boolean"))
        if not _is_integer(opportunities, minimum=0):
            issues.append(("SEMANTIC_COMPLETION", "payload.opportunities must be non-negative"))
        statuses: list[str] = []
        if not isinstance(axes, list) or not axes:
            issues.append(("SEMANTIC_COMPLETION_AXES", "completion axes must be a non-empty array"))
        else:
            labels: set[str] = set()
            for position, axis in enumerate(axes):
                path = f"payload.axes[{position}]"
                if not isinstance(axis, dict):
                    issues.append(("SEMANTIC_COMPLETION_AXIS", f"{path} must be an object"))
                    continue
                label = axis.get("label")
                if (
                    not isinstance(label, str)
                    or not label
                    or label.strip() != label
                    or len(label) > 64
                    or any(ord(character) < 32 or ord(character) == 127 for character in label)
                ):
                    issues.append(("SEMANTIC_COMPLETION_AXIS", f"{path}.label is invalid"))
                elif label.casefold() in labels:
                    issues.append(("SEMANTIC_COMPLETION_AXIS", f"{path}.label is duplicated"))
                else:
                    labels.add(label.casefold())
                status = axis.get("status")
                if not isinstance(status, str) or status not in {"ANCHORED", "FAILED"}:
                    issues.append(("SEMANTIC_COMPLETION_STATUS", f"{path}.status is invalid"))
                else:
                    statuses.append(status)
                for name in ("start", "target", "current_node"):
                    if not _is_integer(
                        axis.get(name), minimum=1, maximum=MAX_ROUTE_NODE
                    ):
                        issues.append(
                            (
                                "SEMANTIC_COMPLETION_NODE",
                                f"{path}.{name} must be in [1, {MAX_ROUTE_NODE}]",
                            )
                        )
                target = axis.get("target")
                if _is_integer(
                    target, minimum=1, maximum=MAX_ROUTE_NODE
                ) and not is_prime(target):  # type: ignore[arg-type]
                    issues.append(("SEMANTIC_COMPLETION_TARGET", f"{path}.target must be prime"))
                for name in ("incidents", "reroutes"):
                    if not _is_integer(axis.get(name), minimum=0):
                        issues.append(("SEMANTIC_COMPLETION_COUNT", f"{path}.{name} must be non-negative"))
                visited = axis.get("visited_nodes")
                breached = axis.get("breached_nodes")
                visited_valid = (
                    isinstance(visited, list)
                    and bool(visited)
                    and all(
                        _is_integer(node, minimum=1, maximum=MAX_ROUTE_NODE)
                        for node in visited
                    )
                )
                if not visited_valid:
                    issues.append(("SEMANTIC_VISITED_NODES", f"{path}.visited_nodes must be non-empty and positive"))
                elif isinstance(visited, list) and visited[-1] != axis.get("current_node"):
                    issues.append(("SEMANTIC_VISITED_NODES", f"{path}.current_node must be the final visited node"))
                breached_valid = isinstance(breached, list) and all(
                    _is_integer(node, minimum=1, maximum=MAX_ROUTE_NODE)
                    for node in breached
                )
                if not breached_valid:
                    issues.append(("SEMANTIC_BREACHED_NODES", f"{path}.breached_nodes is invalid"))
                elif (
                    visited_valid
                    and isinstance(visited, list)
                    and isinstance(breached, list)
                    and not set(breached).issubset(set(visited))
                ):
                    issues.append(("SEMANTIC_BREACHED_NODES", f"{path}.breached_nodes must have been visited"))
                if status == "ANCHORED" and axis.get("current_node") != target:
                    issues.append(("SEMANTIC_COMPLETION_STATUS", f"{path} is ANCHORED away from its target"))
                if status == "FAILED" and axis.get("current_node") == target:
                    issues.append(("SEMANTIC_COMPLETION_STATUS", f"{path} is FAILED at its target"))
                error = axis.get("error")
                if status == "FAILED" and (not isinstance(error, str) or not error):
                    issues.append(("SEMANTIC_COMPLETION_ERROR", f"{path}.error must explain a FAILED status"))
                elif status == "ANCHORED" and error is not None:
                    issues.append(("SEMANTIC_COMPLETION_ERROR", f"{path}.error must be null when ANCHORED"))
                elif error is not None and not isinstance(error, str):
                    issues.append(("SEMANTIC_COMPLETION_ERROR", f"{path}.error must be a string or null"))
        if isinstance(succeeded, bool) and statuses:
            if succeeded != all(status == "ANCHORED" for status in statuses):
                issues.append(("SEMANTIC_COMPLETION", "payload.succeeded conflicts with axis statuses"))
        return issues

    # Arbitrary application records remain permitted, but only recognized
    # Prime Axis event types receive the domain-semantic audit above.
    return issues


def audit_ledger(
    path: str | os.PathLike[str],
    *,
    require_seal: bool = True,
) -> AuditReport:
    """Audit format, hashes, ordering, seal/count, and partial-line evidence."""

    if not isinstance(require_seal, bool):
        raise TypeError("require_seal must be a bool")
    ledger_path = Path(path)
    issues: list[AuditIssue] = []
    truncated = False
    tampered = False

    def add(
        code: str,
        message: str,
        line_number: int | None = None,
        *,
        kind: str = "tamper",
        fatal: bool = True,
    ) -> None:
        nonlocal truncated, tampered
        issues.append(AuditIssue(code, message, line_number, fatal))
        if kind == "truncation":
            truncated = True
        elif kind == "tamper":
            tampered = True

    if not ledger_path.exists():
        add("FILE_NOT_FOUND", "ledger file does not exist", kind="truncation")
        return AuditReport(
            path=str(ledger_path),
            valid=False,
            sealed=False,
            truncated=True,
            tampered=False,
            run_id=None,
            record_count=0,
            event_count=0,
            last_seq=None,
            last_hash=None,
            issues=tuple(issues),
        )
    if not ledger_path.is_file():
        add("NOT_A_FILE", "ledger path is not a regular file", kind="tamper")
        return AuditReport(
            path=str(ledger_path),
            valid=False,
            sealed=False,
            truncated=False,
            tampered=True,
            run_id=None,
            record_count=0,
            event_count=0,
            last_seq=None,
            last_hash=None,
            issues=tuple(issues),
        )

    record_count = 0
    event_count = 0
    expected_seq = 0
    expected_prev = GENESIS_HASH
    run_id: str | None = None
    last_seq: int | None = None
    last_hash: str | None = None
    last_record_type: str | None = None
    saw_seal = False
    simulation_started = False
    simulation_completed = False
    simulation_tick_count = 0
    simulation_axis_labels: frozenset[str] | None = None
    simulation_axis_order: tuple[str, ...] | None = None
    simulation_config: EngineConfig | None = None
    simulation_axis_specs: dict[str, AxisSpec] | None = None
    simulation_paths: dict[str, list[int]] | None = None
    simulation_terminal_labels: set[str] | None = None
    simulation_incident_counts: dict[str, int] | None = None
    simulation_breached_nodes: dict[str, set[int]] | None = None
    # Audit replay deliberately uses the engine's own transition functions so
    # receipt validation cannot drift into a weaker approximation of runtime
    # behavior.  States are advanced lazily, one ledger tick at a time.
    simulation_replay_engine: SimulationEngine | None = None
    simulation_replay_states: dict[str, Any] | None = None
    simulation_previous_monotonic: float | None = None

    try:
        stream = ledger_path.open("rb")
    except OSError as exc:
        add("READ_ERROR", f"unable to open ledger: {exc}", kind="truncation")
        return AuditReport(
            path=str(ledger_path),
            valid=False,
            sealed=False,
            truncated=True,
            tampered=False,
            run_id=None,
            record_count=0,
            event_count=0,
            last_seq=None,
            last_hash=None,
            issues=tuple(issues),
        )

    with stream:
        for line_number, raw_line in _bounded_ledger_lines(stream):
            record_count += 1
            if raw_line is None:
                add(
                    "LINE_TOO_LONG",
                    f"record exceeds the {MAX_LEDGER_LINE_BYTES}-byte safety limit",
                    line_number,
                )
                expected_seq += 1
                continue
            if not raw_line.endswith(b"\n"):
                add(
                    "PARTIAL_LINE",
                    "final record is not newline-terminated",
                    line_number,
                    kind="truncation",
                )
                content = raw_line
            else:
                content = raw_line[:-1]

            try:
                text = content.decode("utf-8")
            except UnicodeDecodeError as exc:
                add("INVALID_UTF8", f"record is not UTF-8: {exc}", line_number)
                expected_seq += 1
                continue
            if not text:
                add("EMPTY_LINE", "empty lines are not valid ledger records", line_number)
                expected_seq += 1
                continue

            try:
                record = json.loads(
                    text,
                    object_pairs_hook=_unique_object,
                    parse_constant=_reject_constant,
                )
            except RecursionError as exc:
                add("JSON_NESTING", f"record nesting is too deep: {exc}", line_number)
                expected_seq += 1
                continue
            except (json.JSONDecodeError, UnicodeError, ValueError) as exc:
                add("INVALID_JSON", f"record is not strict JSON: {exc}", line_number)
                expected_seq += 1
                continue
            if not isinstance(record, dict):
                add("INVALID_RECORD", "top-level JSON value must be an object", line_number)
                expected_seq += 1
                continue

            try:
                canonical = canonical_json(record)
            except RecursionError as exc:
                add("JSON_NESTING", f"record nesting is too deep: {exc}", line_number)
                expected_seq += 1
                continue
            except (TypeError, ValueError) as exc:
                code = "JSON_NESTING" if "nesting depth" in str(exc) else "INVALID_JSON_VALUE"
                add(code, str(exc), line_number)
                expected_seq += 1
                continue
            if canonical != text:
                add("NON_CANONICAL_JSON", "record does not use canonical key order/spacing", line_number)

            keys = set(record)
            if keys != _RECORD_KEYS:
                missing = sorted(_RECORD_KEYS - keys)
                extra = sorted(keys - _RECORD_KEYS)
                add(
                    "RECORD_SHAPE",
                    f"record keys differ; missing={missing}, extra={extra}",
                    line_number,
                )

            if record.get("schema_version") != SCHEMA_VERSION:
                add("SCHEMA_VERSION", "unsupported or missing schema version", line_number)

            current_run_id = record.get("run_id")
            try:
                validated_run_id = _validate_run_id(current_run_id)
            except ValueError as exc:
                add("RUN_ID", str(exc), line_number)
                validated_run_id = None
            if validated_run_id is not None:
                if run_id is None:
                    run_id = validated_run_id
                elif validated_run_id != run_id:
                    add("RUN_ID_CHANGED", "run_id changed inside the ledger", line_number)

            seq = record.get("seq")
            if isinstance(seq, bool) or not isinstance(seq, int) or seq < 0:
                add("INVALID_SEQUENCE", "seq must be a non-negative integer", line_number)
                expected_seq += 1
            else:
                last_seq = seq
                if seq != expected_seq:
                    add(
                        "SEQUENCE_DISCONTINUITY",
                        f"expected seq {expected_seq}, found {seq}",
                        line_number,
                    )
                expected_seq = seq + 1

            if not _parse_timestamp(record.get("timestamp_utc")):
                add("TIMESTAMP", "timestamp_utc is not canonical UTC", line_number)

            prev_hash = record.get("prev_hash")
            if not isinstance(prev_hash, str) or not _HASH_RE.fullmatch(prev_hash):
                add("PREV_HASH_FORMAT", "prev_hash must be 64 lowercase hex characters", line_number)
            elif prev_hash != expected_prev:
                add(
                    "CHAIN_BREAK",
                    f"prev_hash does not match the preceding record at seq {expected_seq - 1}",
                    line_number,
                )

            record_hash = record.get("record_hash")
            if not isinstance(record_hash, str) or not _HASH_RE.fullmatch(record_hash):
                add("RECORD_HASH_FORMAT", "record_hash must be 64 lowercase hex characters", line_number)
            else:
                last_hash = record_hash
                unsigned = {key: value for key, value in record.items() if key != "record_hash"}
                try:
                    computed_hash = _hash_record(unsigned)
                except (TypeError, ValueError, RecursionError) as exc:
                    add("HASH_INPUT", f"record cannot be hashed: {exc}", line_number)
                else:
                    if record_hash != computed_hash:
                        add("HASH_MISMATCH", "record_hash does not match record content", line_number)
                expected_prev = record_hash

            record_type = record.get("record_type")
            last_record_type = record_type if isinstance(record_type, str) else None
            payload = record.get("payload")
            if not isinstance(payload, dict):
                add("PAYLOAD_SHAPE", "payload must be a JSON object", line_number)

            if record_type == "event":
                if saw_seal:
                    add("RECORD_AFTER_SEAL", "event appears after a seal", line_number)
                event_count += 1
                if isinstance(payload, dict):
                    for code, message in _validate_event_payload(payload):
                        add(code, message, line_number, kind="semantic")

                    event_type = payload.get("event_type")
                    if event_type == "simulation_start":
                        if simulation_started:
                            add(
                                "SEMANTIC_DUPLICATE_SIMULATION_START",
                                "simulation_start appears more than once",
                                line_number,
                                kind="semantic",
                            )
                        else:
                            simulation_started = True
                            if event_count != 1:
                                add(
                                    "SEMANTIC_SIMULATION_START_ORDER",
                                    "simulation_start must be the first event",
                                    line_number,
                                    kind="semantic",
                                )
                            config = payload.get("config")
                            if isinstance(config, dict):
                                try:
                                    simulation_config = EngineConfig(**config)
                                except (TypeError, ValueError, OverflowError):
                                    simulation_config = None
                            axes = payload.get("axes")
                            if isinstance(axes, list):
                                labels = [
                                    axis.get("label")
                                    for axis in axes
                                    if isinstance(axis, dict)
                                    and isinstance(axis.get("label"), str)
                                ]
                                if len(labels) == len(axes) and len(labels) == len(set(labels)):
                                    simulation_axis_labels = frozenset(labels)
                                    simulation_axis_order = tuple(labels)
                                parsed_specs: dict[str, AxisSpec] = {}
                                folded_labels: set[str] = set()
                                for axis in axes:
                                    if not isinstance(axis, dict):
                                        break
                                    try:
                                        spec = AxisSpec(**axis)
                                    except (TypeError, ValueError, OverflowError):
                                        break
                                    folded = spec.label.casefold()
                                    if spec.label != axis.get("label") or folded in folded_labels:
                                        break
                                    folded_labels.add(folded)
                                    parsed_specs[spec.label] = spec
                                if len(parsed_specs) == len(axes):
                                    simulation_axis_specs = parsed_specs
                                    simulation_paths = {
                                        label: [spec.start]
                                        for label, spec in parsed_specs.items()
                                    }
                                    simulation_terminal_labels = {
                                        label
                                        for label, spec in parsed_specs.items()
                                        if spec.start == spec.target
                                    }
                                    simulation_incident_counts = {
                                        label: 0 for label in parsed_specs
                                    }
                                    simulation_breached_nodes = {
                                        label: set() for label in parsed_specs
                                    }
                                    if simulation_config is not None:
                                        simulation_replay_engine = SimulationEngine(
                                            simulation_config,
                                            monotonic_clock=lambda: 0.0,
                                            wall_clock=lambda: datetime(
                                                1970, 1, 1, tzinfo=timezone.utc
                                            ),
                                            sleeper=lambda _seconds: None,
                                        )
                                        try:
                                            replay_specs = (
                                                simulation_replay_engine._validated_specs(  # noqa: SLF001
                                                    tuple(parsed_specs.values())
                                                )
                                            )
                                        except (TypeError, ValueError):
                                            # The semantic validator has already
                                            # recorded the invalid start.  Do not
                                            # spend route-search work replaying it.
                                            simulation_replay_engine = None
                                        else:
                                            try:
                                                simulation_replay_states = {
                                                    spec.label: simulation_replay_engine._initialize_axis(  # noqa: SLF001
                                                        spec
                                                    )
                                                    for spec in replay_specs
                                                }
                                            except Exception as exc:
                                                add(
                                                    "SEMANTIC_REPLAY_ERROR",
                                                    (
                                                        "deterministic initialization replay failed "
                                                        f"safely with {type(exc).__name__}"
                                                    ),
                                                    line_number,
                                                    kind="semantic",
                                                )
                                                simulation_replay_engine = None
                                                simulation_replay_states = None

                        if simulation_completed:
                            add(
                                "SEMANTIC_EVENT_AFTER_COMPLETION",
                                "simulation_start appears after simulation_complete",
                                line_number,
                                kind="semantic",
                            )

                    elif simulation_started:
                        if simulation_completed:
                            add(
                                "SEMANTIC_EVENT_AFTER_COMPLETION",
                                "an event appears after simulation_complete",
                                line_number,
                                kind="semantic",
                            )

                        if event_type == "multi_axis_tick":
                            if (
                                simulation_axis_labels
                                and simulation_terminal_labels is not None
                                and simulation_axis_labels.issubset(
                                    simulation_terminal_labels
                                )
                            ):
                                add(
                                    "SEMANTIC_TICK_AFTER_TERMINAL",
                                    "a synchronized tick appears after every axis is terminal",
                                    line_number,
                                    kind="semantic",
                                )
                            clock = payload.get("clock")
                            opportunity_index = (
                                clock.get("opportunity_index")
                                if isinstance(clock, dict)
                                else None
                            )
                            if (
                                isinstance(opportunity_index, int)
                                and not isinstance(opportunity_index, bool)
                                and opportunity_index >= 0
                                and opportunity_index != simulation_tick_count
                            ):
                                add(
                                    "SEMANTIC_OPPORTUNITY_SEQUENCE",
                                    (
                                        "simulation tick opportunity_index must be contiguous "
                                        f"from zero; expected {simulation_tick_count}, "
                                        f"found {opportunity_index}"
                                    ),
                                    line_number,
                                    kind="semantic",
                                )

                            if (
                                simulation_config is not None
                                and simulation_tick_count >= simulation_config.max_ticks
                            ):
                                add(
                                    "SEMANTIC_TICK_LIMIT",
                                    "simulation contains more ticks than configured max_ticks",
                                    line_number,
                                    kind="semantic",
                                )

                            if isinstance(clock, dict) and simulation_config is not None:
                                lattice_time = clock.get("lattice_time_s")
                                expected_lattice = (
                                    simulation_tick_count
                                    * simulation_config.lattice_period_s
                                )
                                if (
                                    _is_finite_number(lattice_time, minimum=0.0)
                                    and float(lattice_time) != expected_lattice
                                ):
                                    add(
                                        "SEMANTIC_CLOCK_CONTRACT",
                                        "lattice_time_s conflicts with the configured lattice period",
                                        line_number,
                                        kind="semantic",
                                    )

                                monotonic_time = clock.get("monotonic_time_s")
                                if _is_finite_number(monotonic_time, minimum=0.0):
                                    current_monotonic = float(monotonic_time)
                                    if (
                                        simulation_previous_monotonic is not None
                                        and current_monotonic < simulation_previous_monotonic
                                    ):
                                        add(
                                            "SEMANTIC_CLOCK_REGRESSION",
                                            "monotonic_time_s regresses within the simulation",
                                            line_number,
                                            kind="semantic",
                                        )
                                    simulation_previous_monotonic = current_monotonic

                            tick_axes = payload.get("axes")
                            if (
                                simulation_axis_labels is not None
                                and isinstance(tick_axes, dict)
                                and all(isinstance(label, str) for label in tick_axes)
                                and frozenset(tick_axes) != simulation_axis_labels
                            ):
                                add(
                                    "SEMANTIC_AXIS_SET_CHANGED",
                                    "simulation tick axis labels differ from simulation_start",
                                    line_number,
                                    kind="semantic",
                                )
                            if (
                                isinstance(tick_axes, dict)
                                and simulation_axis_specs is not None
                            ):
                                replay_ticks: dict[str, Any] = {}
                                if (
                                    simulation_replay_engine is not None
                                    and simulation_replay_states is not None
                                    and simulation_config is not None
                                    and simulation_tick_count
                                    < simulation_config.max_ticks
                                ):
                                    try:
                                        replay_clock = ClockSnapshot(
                                            opportunity_index=simulation_tick_count,
                                            lattice_time_s=(
                                                simulation_tick_count
                                                * simulation_config.lattice_period_s
                                            ),
                                            monotonic_time_s=0.0,
                                            wall_time_utc=datetime(
                                                1970, 1, 1, tzinfo=timezone.utc
                                            ),
                                        )
                                        replay_ticks = {
                                            label: simulation_replay_engine._advance_axis(  # noqa: SLF001
                                                state, replay_clock
                                            )
                                            for label, state in simulation_replay_states.items()
                                        }
                                    except Exception as exc:
                                        add(
                                            "SEMANTIC_REPLAY_ERROR",
                                            (
                                                "deterministic tick replay failed safely "
                                                f"with {type(exc).__name__}"
                                            ),
                                            line_number,
                                            kind="semantic",
                                        )
                                        simulation_replay_engine = None
                                        simulation_replay_states = None
                                if replay_ticks:
                                    severity_rank = {
                                        "INFO": 0,
                                        "WARNING": 1,
                                        "CRITICAL": 2,
                                    }
                                    expected_max_severity = max(
                                        (
                                            tick.event.severity.value
                                            for tick in replay_ticks.values()
                                        ),
                                        key=severity_rank.__getitem__,
                                        default="INFO",
                                    )
                                    expected_message = (
                                        "synchronized opportunity "
                                        f"{simulation_tick_count}"
                                    )
                                    expected_metadata = {
                                        "axis_states": {
                                            label: {
                                                "status": tick.status.value,
                                                "advanced": tick.advanced,
                                                "incident_count": tick.incident_count,
                                                "rerouted": tick.rerouted,
                                                "message": tick.message,
                                            }
                                            for label, tick in replay_ticks.items()
                                        },
                                        "phase_basis": (
                                            "normalized bounded-route position"
                                        ),
                                    }
                                    if (
                                        payload.get("max_severity")
                                        != expected_max_severity
                                        or payload.get("message")
                                        != expected_message
                                        or payload.get("metadata")
                                        != expected_metadata
                                    ):
                                        add(
                                            "SEMANTIC_TICK_DESCRIPTION",
                                            "tick severity, message, or metadata conflicts with deterministic engine replay",
                                            line_number,
                                            kind="semantic",
                                        )
                                tick_moved_any = False
                                tick_nodes_valid = True
                                for label, spec in simulation_axis_specs.items():
                                    axis = tick_axes.get(label)
                                    if not isinstance(axis, dict):
                                        tick_nodes_valid = False
                                        continue
                                    geometry = axis.get("geometry")
                                    if isinstance(geometry, dict):
                                        declared_tolerance = geometry.get("tolerance")
                                        tolerance_matches = (
                                            _is_finite_number(
                                                declared_tolerance,
                                                minimum=0.0,
                                                maximum=0.5,
                                            )
                                            and float(declared_tolerance) == spec.tolerance
                                        )
                                        if (
                                            geometry.get("quotient_order")
                                            != spec.quotient_order
                                            or not tolerance_matches
                                        ):
                                            add(
                                                "SEMANTIC_AXIS_CONTRACT_CHANGED",
                                                f"axis {label!r} geometry conflicts with simulation_start",
                                                line_number,
                                                kind="semantic",
                                            )
                                        residual = geometry.get("residual")
                                        declared_closure = geometry.get("closure_status")
                                        if (
                                            _is_finite_number(
                                                residual,
                                                minimum=0.0,
                                                maximum=0.5,
                                            )
                                            and _is_finite_number(
                                                declared_tolerance,
                                                minimum=0.0,
                                                maximum=0.5,
                                            )
                                        ):
                                            expected_closure = (
                                                "CLOSED"
                                                if float(residual)
                                                <= float(declared_tolerance)
                                                else "FAILED"
                                            )
                                            if declared_closure != expected_closure:
                                                add(
                                                    "SEMANTIC_SIMULATION_CLOSURE",
                                                    f"axis {label!r} closure status is not executable-engine output",
                                                    line_number,
                                                    kind="semantic",
                                                )
                                    node = axis.get("node")
                                    expected_tick = replay_ticks.get(label)
                                    if (
                                        expected_tick is not None
                                        and _is_integer(
                                            node,
                                            minimum=1,
                                            maximum=MAX_ROUTE_NODE,
                                        )
                                        and int(node) != expected_tick.node
                                    ):
                                        add(
                                            "SEMANTIC_REPLAY_NODE",
                                            f"axis {label!r} node conflicts with deterministic engine replay",
                                            line_number,
                                            kind="semantic",
                                        )
                                    if (
                                        isinstance(geometry, dict)
                                        and simulation_config is not None
                                        and _is_integer(
                                            node,
                                            minimum=simulation_config.lower_bound,
                                            maximum=simulation_config.upper_bound,
                                        )
                                    ):
                                        span = (
                                            simulation_config.upper_bound
                                            - simulation_config.lower_bound
                                            + 1
                                        )
                                        expected_phase = (
                                            spec.target - simulation_config.lower_bound
                                        ) / span
                                        observed_phase = (
                                            int(node) - simulation_config.lower_bound
                                        ) / span
                                        declared_expected = geometry.get("expected_phase")
                                        declared_observed = geometry.get("observed_phase")
                                        phases_match = (
                                            _is_finite_number(
                                                declared_expected,
                                                minimum=0.0,
                                                maximum=1.0,
                                            )
                                            and float(declared_expected) < 1.0
                                            and _is_finite_number(
                                                declared_observed,
                                                minimum=0.0,
                                                maximum=1.0,
                                            )
                                            and float(declared_observed) < 1.0
                                            and float(declared_expected) == expected_phase
                                            and float(declared_observed) == observed_phase
                                        )
                                        if not phases_match:
                                            add(
                                                "SEMANTIC_PHASE_CONTRACT",
                                                f"axis {label!r} phases conflict with its target/node and bounds",
                                                line_number,
                                                kind="semantic",
                                            )
                                    if (
                                        simulation_paths is not None
                                        and _is_integer(
                                            node,
                                            minimum=1,
                                            maximum=MAX_ROUTE_NODE,
                                        )
                                    ):
                                        path = simulation_paths[label]
                                        was_terminal = (
                                            simulation_terminal_labels is not None
                                            and label in simulation_terminal_labels
                                        )
                                        axis_moved = path[-1] != node
                                        if path[-1] != node:
                                            tick_moved_any = True
                                            if (
                                                simulation_terminal_labels is not None
                                                and label in simulation_terminal_labels
                                            ):
                                                add(
                                                    "SEMANTIC_MOVEMENT_AFTER_TERMINAL",
                                                    f"axis {label!r} moves after entering a terminal state",
                                                    line_number,
                                                    kind="semantic",
                                                )
                                            if (
                                                simulation_config is not None
                                                and simulation_config.lower_bound
                                                <= path[-1]
                                                <= simulation_config.upper_bound
                                                and int(node)
                                                not in allowed_moves(
                                                    path[-1],
                                                    lower_bound=simulation_config.lower_bound,
                                                    upper_bound=simulation_config.upper_bound,
                                                )
                                            ):
                                                add(
                                                    "SEMANTIC_ILLEGAL_PATH_EDGE",
                                                    f"axis {label!r} uses a move outside the declared graph",
                                                    line_number,
                                                    kind="semantic",
                                                )
                                            path.append(int(node))
                                        elif (
                                            simulation_terminal_labels is not None
                                            and int(node) != spec.target
                                        ):
                                            simulation_terminal_labels.add(label)
                                        if (
                                            simulation_terminal_labels is not None
                                            and int(node) == spec.target
                                        ):
                                            simulation_terminal_labels.add(label)
                                        if (
                                            axis_moved
                                            and not was_terminal
                                            and int(node) != spec.target
                                            and isinstance(geometry, dict)
                                            and geometry.get("closure_status") == "FAILED"
                                            and simulation_incident_counts is not None
                                            and simulation_breached_nodes is not None
                                        ):
                                            simulation_incident_counts[label] += 1
                                            simulation_breached_nodes[label].add(int(node))
                                            if (
                                                simulation_config is not None
                                                and simulation_terminal_labels is not None
                                                and simulation_incident_counts[label]
                                                >= simulation_config.max_incidents
                                            ):
                                                simulation_terminal_labels.add(label)
                                    else:
                                        tick_nodes_valid = False
                                    if (
                                        simulation_config is not None
                                        and _is_integer(
                                            node,
                                            minimum=1,
                                            maximum=MAX_ROUTE_NODE,
                                        )
                                        and not simulation_config.lower_bound
                                        <= int(node)
                                        <= simulation_config.upper_bound
                                    ):
                                        add(
                                            "SEMANTIC_NODE_OUTSIDE_BOUNDS",
                                            f"axis {label!r} node is outside configured bounds",
                                            line_number,
                                            kind="semantic",
                                        )
                                if (
                                    tick_nodes_valid
                                    and not tick_moved_any
                                    and set(tick_axes) == set(simulation_axis_specs)
                                ):
                                    add(
                                        "SEMANTIC_TICK_WITHOUT_ACTIVE_AXIS",
                                        "a synchronized tick contains no active-axis movement",
                                        line_number,
                                        kind="semantic",
                                    )
                            simulation_tick_count += 1

                        elif event_type == "tick":
                            add(
                                "SEMANTIC_UNEXPECTED_SIMULATION_EVENT",
                                "synchronized simulations must use multi_axis_tick records",
                                line_number,
                                kind="semantic",
                            )

                        elif event_type == "simulation_complete":
                            if simulation_completed:
                                add(
                                    "SEMANTIC_DUPLICATE_COMPLETION",
                                    "simulation_complete appears more than once",
                                    line_number,
                                    kind="semantic",
                                )
                            declared_opportunities = payload.get("opportunities")
                            if (
                                isinstance(declared_opportunities, int)
                                and not isinstance(declared_opportunities, bool)
                                and declared_opportunities >= 0
                                and declared_opportunities != simulation_tick_count
                            ):
                                add(
                                    "SEMANTIC_COMPLETION_COUNT",
                                    (
                                        "simulation_complete opportunities must equal the "
                                        f"number of ticks; expected {simulation_tick_count}, "
                                        f"found {declared_opportunities}"
                                    ),
                                    line_number,
                                    kind="semantic",
                                )

                            completion_axes = payload.get("axes")
                            if (
                                simulation_replay_states is not None
                                and simulation_config is not None
                                and simulation_tick_count
                                >= simulation_config.max_ticks
                            ):
                                for replay_state in simulation_replay_states.values():
                                    if replay_state.status is AxisStatus.ACTIVE:
                                        replay_state.status = AxisStatus.FAILED
                                        replay_state.error = (
                                            f"maximum of {simulation_config.max_ticks} "
                                            "logical opportunities reached"
                                        )
                            if (
                                simulation_axis_labels is not None
                                and isinstance(completion_axes, list)
                            ):
                                completion_labels = [
                                    axis.get("label")
                                    for axis in completion_axes
                                    if isinstance(axis, dict)
                                    and isinstance(axis.get("label"), str)
                                ]
                                if (
                                    len(completion_labels) != len(completion_axes)
                                    or len(completion_labels) != len(set(completion_labels))
                                    or frozenset(completion_labels) != simulation_axis_labels
                                ):
                                    add(
                                        "SEMANTIC_AXIS_SET_CHANGED",
                                        "completion axis labels differ from simulation_start",
                                        line_number,
                                        kind="semantic",
                                    )
                                elif (
                                    simulation_axis_order is not None
                                    and tuple(completion_labels)
                                    != simulation_axis_order
                                ):
                                    add(
                                        "SEMANTIC_AXIS_ORDER_CHANGED",
                                        "completion axis order differs from simulation_start",
                                        line_number,
                                        kind="semantic",
                                    )
                                elif simulation_axis_specs is not None:
                                    axes_by_label = {
                                        str(axis["label"]): axis
                                        for axis in completion_axes
                                        if isinstance(axis, dict)
                                        and isinstance(axis.get("label"), str)
                                    }
                                    for label, spec in simulation_axis_specs.items():
                                        axis = axes_by_label.get(label)
                                        if not isinstance(axis, dict):
                                            continue
                                        if (
                                            axis.get("start") != spec.start
                                            or axis.get("target") != spec.target
                                        ):
                                            add(
                                                "SEMANTIC_AXIS_CONTRACT_CHANGED",
                                                f"completion contract for axis {label!r} conflicts with simulation_start",
                                                line_number,
                                                kind="semantic",
                                            )
                                        if simulation_paths is not None:
                                            observed_path = simulation_paths[label]
                                            if axis.get("current_node") != observed_path[-1]:
                                                add(
                                                    "SEMANTIC_COMPLETION_STATE",
                                                    f"completion node for axis {label!r} conflicts with the final tick",
                                                    line_number,
                                                    kind="semantic",
                                                )
                                            if axis.get("visited_nodes") != observed_path:
                                                add(
                                                    "SEMANTIC_COMPLETION_PATH",
                                                    f"completion path for axis {label!r} conflicts with tick history",
                                                    line_number,
                                                    kind="semantic",
                                                )
                                        incidents = axis.get("incidents")
                                        reroutes = axis.get("reroutes")
                                        breached = axis.get("breached_nodes")
                                        if simulation_replay_states is not None:
                                            replay_state = simulation_replay_states[label]
                                            replay_receipt = {
                                                "status": replay_state.status.value,
                                                "current_node": replay_state.current_node,
                                                "incidents": replay_state.incidents,
                                                "reroutes": replay_state.reroutes,
                                                "visited_nodes": replay_state.visited_nodes,
                                                "breached_nodes": sorted(
                                                    replay_state.breached_nodes
                                                ),
                                                "error": replay_state.error,
                                            }
                                            if any(
                                                axis.get(name) != expected
                                                for name, expected in replay_receipt.items()
                                            ):
                                                add(
                                                    "SEMANTIC_COMPLETION_REPLAY",
                                                    f"axis {label!r} completion receipt conflicts with deterministic engine replay",
                                                    line_number,
                                                    kind="semantic",
                                                )
                                        if (
                                            simulation_incident_counts is not None
                                            and _is_integer(incidents, minimum=0)
                                            and int(incidents)
                                            != simulation_incident_counts[label]
                                        ):
                                            add(
                                                "SEMANTIC_COMPLETION_COUNTERS",
                                                f"axis {label!r} incident count conflicts with tick history",
                                                line_number,
                                                kind="semantic",
                                            )
                                        if (
                                            simulation_breached_nodes is not None
                                            and isinstance(breached, list)
                                            and all(
                                                _is_integer(
                                                    node,
                                                    minimum=1,
                                                    maximum=MAX_ROUTE_NODE,
                                                )
                                                for node in breached
                                            )
                                            and set(breached)
                                            != simulation_breached_nodes[label]
                                        ):
                                            add(
                                                "SEMANTIC_COMPLETION_COUNTERS",
                                                f"axis {label!r} breached nodes conflict with tick history",
                                                line_number,
                                                kind="semantic",
                                            )
                                        if (
                                            simulation_config is not None
                                            and _is_integer(incidents, minimum=0)
                                            and int(incidents)
                                            > min(
                                                simulation_tick_count,
                                                simulation_config.max_incidents
                                                - (1 if axis.get("status") == "ANCHORED" else 0),
                                            )
                                        ):
                                            add(
                                                "SEMANTIC_COMPLETION_COUNTERS",
                                                f"axis {label!r} incident count exceeds the run limits",
                                                line_number,
                                                kind="semantic",
                                            )
                                        if (
                                            simulation_config is not None
                                            and _is_integer(incidents, minimum=0)
                                            and _is_integer(reroutes, minimum=0)
                                            and int(reroutes)
                                            > min(
                                                simulation_tick_count,
                                                min(
                                                    int(incidents),
                                                    simulation_config.max_incidents - 1,
                                                )
                                                // simulation_config.reroute_after_incidents,
                                            )
                                        ):
                                            add(
                                                "SEMANTIC_COMPLETION_COUNTERS",
                                                f"axis {label!r} reroute count exceeds the incident policy",
                                                line_number,
                                                kind="semantic",
                                            )
                                        if (
                                            _is_integer(incidents, minimum=0)
                                            and isinstance(breached, list)
                                            and all(
                                                _is_integer(
                                                    node,
                                                    minimum=1,
                                                    maximum=MAX_ROUTE_NODE,
                                                )
                                                for node in breached
                                            )
                                            and len(set(breached)) > int(incidents)
                                        ):
                                            add(
                                                "SEMANTIC_COMPLETION_COUNTERS",
                                                f"axis {label!r} has more breached nodes than incidents",
                                                line_number,
                                                kind="semantic",
                                            )
                            simulation_completed = True
                        else:
                            add(
                                "SEMANTIC_UNEXPECTED_SIMULATION_EVENT",
                                "only multi_axis_tick and simulation_complete may follow simulation_start",
                                line_number,
                                kind="semantic",
                            )
                    elif event_type == "simulation_complete":
                        add(
                            "SEMANTIC_COMPLETION_WITHOUT_START",
                            "simulation_complete has no preceding simulation_start",
                            line_number,
                            kind="semantic",
                        )
            elif record_type == "seal":
                if saw_seal:
                    add("MULTIPLE_SEALS", "ledger contains more than one seal", line_number)
                saw_seal = True
                if isinstance(payload, dict):
                    if set(payload) != {"event_count", "final_event_hash"}:
                        add("SEAL_SHAPE", "seal payload has unexpected keys", line_number)
                    declared_count = payload.get("event_count")
                    if (
                        isinstance(declared_count, bool)
                        or not isinstance(declared_count, int)
                        or declared_count < 0
                    ):
                        add("SEAL_COUNT", "seal event_count must be a non-negative integer", line_number)
                    elif declared_count != event_count:
                        add(
                            "SEAL_COUNT_MISMATCH",
                            f"seal declares {declared_count} events but {event_count} precede it",
                            line_number,
                            kind="truncation" if declared_count > event_count else "tamper",
                        )
                    final_event_hash = payload.get("final_event_hash")
                    if final_event_hash != prev_hash:
                        add("SEAL_HASH_MISMATCH", "seal final_event_hash does not match prev_hash", line_number)
            else:
                add("RECORD_TYPE", "record_type must be 'event' or 'seal'", line_number)

    if record_count == 0:
        add("EMPTY_LEDGER", "ledger contains no records", kind="truncation")

    if simulation_started and not simulation_completed:
        add(
            "SEMANTIC_MISSING_COMPLETION",
            "simulation_start has no matching simulation_complete event",
            kind="semantic",
        )

    sealed = saw_seal and last_record_type == "seal"
    if require_seal and not sealed:
        add("MISSING_SEAL", "ledger has no valid final seal", kind="truncation")

    valid = not any(issue.fatal for issue in issues)
    return AuditReport(
        path=str(ledger_path),
        valid=valid,
        sealed=sealed,
        truncated=truncated,
        tampered=tampered,
        run_id=run_id,
        record_count=record_count,
        event_count=event_count,
        last_seq=last_seq,
        last_hash=last_hash,
        issues=tuple(issues),
    )


__all__ = [
    "AuditIssue",
    "AuditReport",
    "DurabilityPolicy",
    "GENESIS_HASH",
    "LedgerWriter",
    "SCHEMA_VERSION",
    "audit_ledger",
    "canonical_json",
]
