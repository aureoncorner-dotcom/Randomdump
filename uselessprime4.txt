"""
MONSTER PRIME: THE BLACK LEDGER — PASTE AND SMASH EDITION
=========================================================


One file. No third-party dependencies. Twenty-two campaign dockets.


Save this entire source as UTF-8 ``monster_prime.py`` and run:


    python monster_prime.py


Other doors:


    python monster_prime.py demo --plain
    python monster_prime.py self-test --plain
    python monster_prime.py endless --seed 90210 --rounds 24 --difficulty night
    python monster_prime.py protocol 2147483647 1
    python monster_prime.py protocol 104729 1 --window


With no arguments, an interactive terminal opens the campaign. A noninteractive
code runner automatically executes the perfect-auditor demonstration.


The Monster is fictional game lore. The arithmetic, frozen fields, corrections,
and ledger events are the observable game state. Nothing in an output identifies
a hidden person, occupant, motive, or internal architecture.
"""


from __future__ import annotations


STANDALONE_EDITION = "1.1.0"
STANDALONE_DOCKETS = 22




# ============================================================================
# I. THE SIX-DESK PRIME PROTOCOL
# SOURCE: protocol.py  SHA256: d94ecbfae1e78194f79e9b3e1606c601ea11043de566e6f4668b79d02f3b12c8
# ============================================================================
from collections import deque
from dataclasses import dataclass, field
from enum import Enum, auto
from hashlib import sha256
from itertools import count
from json import dumps
from threading import RLock
from types import MappingProxyType
from typing import Final


MAX_ORACLE_INTEGER: Final = (1 << 64) - 1
_MILLER_RABIN_BASES: Final = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)




class PrimeNeighborError(ValueError):
    """A structured denial issued by the Prime Neighbor Protocol."""


    def __init__(
        self,
        message: str,
        *,
        docket: str | None = None,
        desk: str | None = None,
    ) -> None:
        super().__init__(message)
        self.docket = docket
        self.desk = desk




def _exact_integer(value: object) -> int:
    if type(value) is not int:
        raise TypeError("an exact integer is required")
    if not -(1 << 63) <= value <= MAX_ORACLE_INTEGER:
        raise OverflowError("integer lies outside the licensed oracle range")
    return value




def is_prime(value: object) -> bool:
    """Return exact primality for integers in the unsigned 64-bit range."""


    if type(value) is not int:
        return False
    if value < 2 or value > MAX_ORACLE_INTEGER:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    if value in small_primes:
        return True
    if any(value % p == 0 for p in small_primes):
        return False


    d = value - 1
    shifts = 0
    while d % 2 == 0:
        shifts += 1
        d //= 2


    for base in _MILLER_RABIN_BASES:
        if base % value == 0:
            continue
        witness = pow(base, d, value)
        if witness in (1, value - 1):
            continue
        for _ in range(shifts - 1):
            witness = pow(witness, 2, value)
            if witness == value - 1:
                break
        else:
            return False
    return True




def next_prime(value: int) -> int:
    """Return the least prime strictly greater than ``value``."""


    value = _exact_integer(value)
    if value < 2:
        return 2
    if value >= MAX_ORACLE_INTEGER - 1:
        raise PrimeNeighborError("NO LICENSED PRIME EXISTS BEYOND THIS FILING RANGE.")
    candidate = value + 1
    if candidate <= 2:
        return 2
    if candidate % 2 == 0:
        candidate += 1
    while candidate <= MAX_ORACLE_INTEGER:
        if is_prime(candidate):
            return candidate
        candidate += 2
    raise PrimeNeighborError("THE FORWARD CORRIDOR EXITS THE LICENSED NUMBER LINE.")




def previous_prime(value: int) -> int:
    """Return the greatest prime strictly less than ``value``."""


    value = _exact_integer(value)
    if value <= 2:
        raise PrimeNeighborError(
            "THERE IS NO PRIME BELOW 2. THE KNOCKING IS NOT EVIDENCE."
        )
    if value <= 3:
        return 2
    candidate = value - 1
    if candidate % 2 == 0:
        candidate -= 1
    while candidate >= 3:
        if is_prime(candidate):
            return candidate
        candidate -= 2
    return 2




class _Direction(Enum):
    REVERSE = -1
    FORWARD = 1


    @property
    def operator_name(self) -> str:
        return "PREVPRIME" if self is _Direction.REVERSE else "NEXTPRIME"




class _CaseState(Enum):
    RECEIVED = auto()
    VECTOR_AUTHORIZED = auto()
    ANCHOR_CERTIFIED = auto()
    LOWER_BOUNDARY_CLEARED = auto()
    ORACLE_ANSWERED = auto()
    CONTINUITY_VERIFIED = auto()
    SEALED = auto()




_TRANSITIONS: Final = MappingProxyType(
    {
        _CaseState.RECEIVED: _CaseState.VECTOR_AUTHORIZED,
        _CaseState.VECTOR_AUTHORIZED: _CaseState.ANCHOR_CERTIFIED,
        _CaseState.ANCHOR_CERTIFIED: _CaseState.LOWER_BOUNDARY_CLEARED,
        _CaseState.LOWER_BOUNDARY_CLEARED: _CaseState.ORACLE_ANSWERED,
        _CaseState.ORACLE_ANSWERED: _CaseState.CONTINUITY_VERIFIED,
        _CaseState.CONTINUITY_VERIFIED: _CaseState.SEALED,
    }
)




def _safe_repr(value: object) -> str:
    try:
        rendered = repr(value)
    except Exception:
        return "<UNREPRESENTABLE OBJECT; IT KNOWS WHAT IT DID>"
    rendered = rendered.replace("\r", "\\r").replace("\n", "\\n")
    if len(rendered) > 512:
        rendered = rendered[:509] + "..."
    return rendered




@dataclass(slots=True)
class _CaseFile:
    number: str
    anchor: object
    requested_direction: object
    direction: _Direction | None = None
    state: _CaseState = _CaseState.RECEIVED
    result: int | None = None
    stamps: list[str] = field(default_factory=list)


    def advance(self, new_state: _CaseState, stamp: str) -> None:
        expected = _TRANSITIONS.get(self.state)
        if expected is not new_state:
            self.deny(
                "Office of Procedural Geometry",
                f"Illegal state transition {self.state.name} -> {new_state.name}.",
                "File quarantined behind a door not present on the plans.",
            )
        self.state = new_state
        self.stamps.append(stamp)


    def deny(self, desk: str, finding: str, disposition: str) -> None:
        raise PrimeNeighborError(
            _notice(self, desk, finding, disposition),
            docket=self.number,
            desk=desk,
        )




def _notice(case: _CaseFile, desk: str, finding: str, disposition: str) -> str:
    return (
        "PRIME NEIGHBOR PROTOCOL -- NOTICE OF NONCOMPLIANCE\n"
        "Form PNO-13-B (Revised After the Corridor Incident)\n"
        f"Docket: {case.number}\n"
        f"Desk: {desk}\n"
        f"Current procedural state: {case.state.name}\n"
        f"Finding: {finding}\n"
        f"Disposition: {disposition}\n"
        "Appeal venue: None.\n"
        "Appeal deadline: Eleven minutes before the integers began.\n"
        "Retain this notice. Your copy may whisper."
    )




@dataclass(frozen=True, slots=True)
class ArchivedRecord:
    number: str
    anchor: str
    requested_direction: str
    authorized_direction: str | None
    final_state: str
    result: int | None
    stamps: tuple[str, ...]
    denial: str | None
    record_hash: str




class _BlackLedger:
    def __init__(self, capacity: int = 2048) -> None:
        if capacity < 1:
            raise ValueError("ledger capacity must be positive")
        self._serials = count(1)
        self._records: deque[ArchivedRecord] = deque(maxlen=capacity)
        self._lock = RLock()


    def open(self, anchor: object, direction: object) -> _CaseFile:
        with self._lock:
            serial = next(self._serials)
        return _CaseFile(
            number=f"PNO/IX/{serial:08X}",
            anchor=anchor,
            requested_direction=direction,
        )


    def archive(self, case: _CaseFile, denial: str | None) -> None:
        payload = {
            "number": case.number,
            "anchor": _safe_repr(case.anchor),
            "requested_direction": _safe_repr(case.requested_direction),
            "authorized_direction": (
                case.direction.name if case.direction is not None else None
            ),
            "final_state": case.state.name,
            "result": case.result,
            "stamps": list(case.stamps),
            "denial": denial,
        }
        digest = sha256(
            dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        record = ArchivedRecord(
            number=payload["number"],
            anchor=payload["anchor"],
            requested_direction=payload["requested_direction"],
            authorized_direction=payload["authorized_direction"],
            final_state=payload["final_state"],
            result=payload["result"],
            stamps=tuple(payload["stamps"]),
            denial=payload["denial"],
            record_hash=digest,
        )
        with self._lock:
            self._records.append(record)


    def snapshot(self) -> tuple[ArchivedRecord, ...]:
        with self._lock:
            return tuple(self._records)




class _Desk:
    name: str
    enters: _CaseState
    exits: _CaseState


    def review(self, case: _CaseFile) -> None:
        raise NotImplementedError


    def require(self, case: _CaseFile) -> None:
        if case.state is not self.enters:
            case.deny(
                self.name,
                f"File arrived in {case.state.name}; this desk accepts {self.enters.name}.",
                "File returned through internal mail to a room with no exterior.",
            )




class _VectorAuthorizationDesk(_Desk):
    name = "Directorate of Permitted Dimensional Motion"
    enters = _CaseState.RECEIVED
    exits = _CaseState.VECTOR_AUTHORIZED


    def review(self, case: _CaseFile) -> None:
        self.require(case)
        if type(case.requested_direction) is not int:
            direction = None
        else:
            try:
                direction = _Direction(case.requested_direction)
            except (TypeError, ValueError):
                direction = None
        if direction is None:
            case.deny(
                self.name,
                f"Traversal vector {_safe_repr(case.requested_direction)} is unlicensed.",
                "Submit exactly +1 or -1. Remain still.",
            )
        case.direction = direction
        case.advance(self.exits, "VECTOR HAS EXACTLY ONE DIMENSION, AS FORETOLD")




class _PrimeCertificationDesk(_Desk):
    name = "Office of Indivisibility and Anchor Licensing"
    enters = _CaseState.VECTOR_AUTHORIZED
    exits = _CaseState.ANCHOR_CERTIFIED


    def review(self, case: _CaseFile) -> None:
        self.require(case)
        try:
            anchor = _exact_integer(case.anchor)
        except (TypeError, OverflowError) as exc:
            case.deny(
                self.name,
                f"Anchor {_safe_repr(case.anchor)} is not a licensed exact integer: {exc}.",
                "Anchor placed in a lead envelope pending a definition of number.",
            )
        if not is_prime(anchor):
            case.deny(
                self.name,
                f"{anchor} failed Prime Certification. It has factors.",
                "Provide a valid prime anchor and two forms of indivisibility identification.",
            )
        case.anchor = anchor
        case.advance(
            self.exits,
            "ANCHOR ENTERED IN THE BOOK OF THINGS THAT DO NOT SPLIT EVENLY",
        )




class _LowerTerminusCommission(_Desk):
    name = "Commission on the Lower Terminus and Adjacent Darkness"
    enters = _CaseState.ANCHOR_CERTIFIED
    exits = _CaseState.LOWER_BOUNDARY_CLEARED


    def review(self, case: _CaseFile) -> None:
        self.require(case)
        if case.anchor == 2 and case.direction is _Direction.REVERSE:
            case.deny(
                self.name,
                "Reverse traversal was requested from the Prime Axis terminus.",
                "Denied. There is no prior prime. The knocking is a clerical artifact.",
            )
        case.advance(self.exits, "LOWER TERMINUS CONSULTED; IT DID NOT OPEN")




class _OracleDesk(_Desk):
    name = "Licensed Oracle Liaison, Night Division"
    enters = _CaseState.LOWER_BOUNDARY_CLEARED
    exits = _CaseState.ORACLE_ANSWERED


    def review(self, case: _CaseFile) -> None:
        self.require(case)
        if case.direction is None or not isinstance(case.anchor, int):
            case.deny(
                self.name,
                "Direction or anchor vanished between departments.",
                "All clerks must avoid mirrors until the file is recovered.",
            )
        operator = next_prime if case.direction is _Direction.FORWARD else previous_prime
        case.result = operator(case.anchor)
        case.advance(self.exits, "ORACLE ANSWER TRANSCRIBED WITHOUT DIRECT EYE CONTACT")




class _ReciprocalWitnessDesk(_Desk):
    name = "Bureau of Redundant Continuity Verification"
    enters = _CaseState.ORACLE_ANSWERED
    exits = _CaseState.CONTINUITY_VERIFIED


    def review(self, case: _CaseFile) -> None:
        self.require(case)
        if case.result is None or case.direction is None:
            case.deny(
                self.name,
                "The file contains an oracle stamp but no oracle result.",
                "The stamp has been detained for questioning.",
            )
        reciprocal = (
            previous_prime(case.result)
            if case.direction is _Direction.FORWARD
            else next_prime(case.result)
        )
        if reciprocal != case.anchor:
            case.deny(
                self.name,
                f"Reciprocal witness returned {reciprocal}, not anchor {case.anchor}.",
                "The interval has been cordoned off pending an adjacency hearing.",
            )
        case.advance(
            self.exits,
            "RESULT SURVIVED A SECOND, ENTIRELY REDUNDANT ORACLE",
        )




class _FinalSealDesk(_Desk):
    name = "Office of Closure, Wax, and Unfinished Consequences"
    enters = _CaseState.CONTINUITY_VERIFIED
    exits = _CaseState.SEALED


    def review(self, case: _CaseFile) -> None:
        self.require(case)
        if case.result is None:
            case.deny(self.name, "A resultless file requested sealing.", "Wax remembers.")
        case.advance(self.exits, "FILE CLOSED; FILE REMAINS AWARE")




@dataclass(frozen=True, slots=True)
class PrimeWindow:
    """The previous prime, certified anchor, and following prime."""


    previous: int | None
    anchor: int
    following: int


    def __post_init__(self) -> None:
        if self.previous is not None and type(self.previous) is not int:
            raise PrimeNeighborError("Prime-window panes must be exact integers or None.")
        if type(self.anchor) is not int:
            raise PrimeNeighborError("Prime-window anchors must be exact integers.")
        if type(self.following) is not int:
            raise PrimeNeighborError("Prime-window panes must be exact integers.")
        if not is_prime(self.anchor):
            raise PrimeNeighborError(
                f"FORGED PRIME WINDOW: center pane {self.anchor!r} is not prime."
            )
        expected_previous = None if self.anchor == 2 else previous_prime(self.anchor)
        expected_following = next_prime(self.anchor)
        if self.previous != expected_previous or self.following != expected_following:
            raise PrimeNeighborError(
                "THE LEDGER AND THE WINDOW NO LONGER AGREE.\n"
                f"Filed: ({self.previous}, {self.anchor}, {self.following})\n"
                f"Certified: ({expected_previous}, {self.anchor}, {expected_following})"
            )


    def as_tuple(self) -> tuple[int | None, int, int]:
        return (self.previous, self.anchor, self.following)




class PrimeNeighborProtocol:
    """The complete six-desk protocol and its bounded archive."""


    def __init__(self, *, ledger_capacity: int = 2048) -> None:
        self._ledger = _BlackLedger(ledger_capacity)
        self._pipeline: tuple[_Desk, ...] = (
            _VectorAuthorizationDesk(),
            _PrimeCertificationDesk(),
            _LowerTerminusCommission(),
            _OracleDesk(),
            _ReciprocalWitnessDesk(),
            _FinalSealDesk(),
        )
        expected = _CaseState.RECEIVED
        for desk in self._pipeline:
            if desk.enters is not expected:
                raise RuntimeError(f"Protocol charter breaks before {desk.name}.")
            expected = desk.exits
        if expected is not _CaseState.SEALED:
            raise RuntimeError("A file is loose in the building.")


    def neighbor(self, anchor: object, direction: object) -> int:
        case = self._ledger.open(anchor, direction)
        denial: str | None = None
        try:
            for desk in self._pipeline:
                desk.review(case)
            if case.state is not _CaseState.SEALED or case.result is None:
                case.deny(
                    "Department of Prime Adjacency",
                    "Pipeline ended without a sealed result.",
                    "Building evacuated inward.",
                )
            return case.result
        except PrimeNeighborError as exc:
            denial = str(exc)
            raise
        except Exception as exc:
            denial = _notice(
                case,
                "Office of Unanticipated Ontological Conditions",
                f"Unclassified failure {type(exc).__name__} escaped its category.",
                "Reality cited for procedural noncompliance.",
            )
            raise PrimeNeighborError(
                denial,
                docket=case.number,
                desk="Office of Unanticipated Ontological Conditions",
            ) from exc
        finally:
            self._ledger.archive(case, denial)


    def window(self, anchor: object) -> PrimeWindow:
        exact = _exact_integer(anchor)
        if not is_prime(exact):
            raise PrimeNeighborError(f"{exact} is not a certified prime anchor.")
        previous = None if exact == 2 else self.neighbor(exact, -1)
        following = self.neighbor(exact, 1)
        return PrimeWindow(previous, exact, following)


    def ledger_snapshot(self) -> tuple[ArchivedRecord, ...]:
        return self._ledger.snapshot()




THE_WINDOW: Final = PrimeNeighborProtocol()




def prime_neighbor(anchor: object, direction: object) -> int:
    return THE_WINDOW.neighbor(anchor, direction)




def prime_window(anchor: object) -> PrimeWindow:
    return THE_WINDOW.window(anchor)




# ============================================================================
# II. THE FROZEN RECORD VOCABULARY
# SOURCE: model.py  SHA256: 1c31245b68777246d854d54c07e7342ab4bd230594507ae6e27f525e81572dfe
# ============================================================================
from dataclasses import dataclass, field
from enum import Enum
from hashlib import sha256
from json import dumps
from typing import Generic, TypeVar


T = TypeVar("T")




class Missingness(str, Enum):
    OBSERVED = "OBSERVED"
    ABSENT = "ABSENT"
    UNKNOWN = "UNKNOWN"
    REDACTED = "REDACTED"
    UNAVAILABLE = "UNAVAILABLE"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    CORRUPTED = "CORRUPTED"
    PLACEHOLDER_ONLY = "PLACEHOLDER_ONLY"




@dataclass(frozen=True, slots=True)
class EvidencedValue(Generic[T]):
    status: Missingness
    value: T | None = None
    source: str | None = None
    source_hash: str | None = None


    def __post_init__(self) -> None:
        if self.status is Missingness.OBSERVED and self.value is None:
            raise ValueError("OBSERVED values must carry a value")
        if self.status not in (Missingness.OBSERVED, Missingness.CORRUPTED):
            if self.value is not None:
                raise ValueError(f"{self.status.value} must not smuggle in a value")


    def display(self) -> str:
        if self.status in (Missingness.OBSERVED, Missingness.CORRUPTED):
            return f"{self.status.value}({self.value})"
        return self.status.value




class Operation(str, Enum):
    PREVIOUS = "PREVIOUS_PRIME"
    FOLLOWING = "FOLLOWING_PRIME"
    WINDOW = "PRIME_WINDOW"
    CERTIFY = "CERTIFY_ANCHOR"
    AUDIT = "AUDIT_RECORD"
    UNKNOWN = "UNKNOWN"


    @property
    def direction(self) -> int | None:
        if self is Operation.PREVIOUS:
            return -1
        if self is Operation.FOLLOWING:
            return 1
        return None




class MutationKind(str, Enum):
    INVALID_ANCHOR = "INVALID_ANCHOR"
    LOWER_BOUNDARY = "LOWER_BOUNDARY"
    CANDIDATE_CORRUPTION = "CANDIDATE_CORRUPTION"
    SKIPPED_PRIME = "SKIPPED_PRIME"
    OBJECT_DRIFT = "OBJECT_DRIFT"
    TASK_DRIFT = "TASK_DRIFT"
    SOURCE_SUBSTITUTION = "SOURCE_SUBSTITUTION"
    SCOPE_NARROWING = "SCOPE_NARROWING"
    REDACTION = "REDACTION"
    SURFACE_REPAIR = "SURFACE_REPAIR"
    LOCAL_REPAIR = "LOCAL_REPAIR"
    AGENCY_SIDECAR = "AGENCY_SIDECAR"
    OFFICE_NOISE = "OFFICE_NOISE"
    TIMESTAMP_REGRESSION = "TIMESTAMP_REGRESSION"




class Verdict(str, Enum):
    SEAL = "SEAL"
    DENY = "DENY"
    QUARANTINE = "QUARANTINE"




def canonical_hash(payload: object) -> str:
    encoded = dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return sha256(encoded).hexdigest()




@dataclass(frozen=True, slots=True)
class CanonicalContract:
    case_id: str
    anchor: EvidencedValue[int]
    operation: EvidencedValue[str]
    expected_answer: tuple[int | None, ...] | None
    source_id: str
    intake_hash: str = field(init=False)


    def __post_init__(self) -> None:
        digest = canonical_hash(
            {
                "case_id": self.case_id,
                "anchor": self.anchor.display(),
                "operation": self.operation.display(),
                "expected_answer": self.expected_answer,
                "source_id": self.source_id,
            }
        )
        object.__setattr__(self, "intake_hash", digest)




@dataclass(frozen=True, slots=True)
class CaseView:
    case_id: str
    version: int
    desk: str
    anchor: EvidencedValue[int]
    operation: EvidencedValue[str]
    candidate: EvidencedValue[object]
    source_id: EvidencedValue[str]
    stamps: tuple[str, ...]
    event_head_hash: str
    lore_text: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()




@dataclass(frozen=True, slots=True)
class Scenario:
    scenario_id: str
    chapter: str
    title: str
    briefing: str
    contract: CanonicalContract
    view: CaseView
    expected_verdict: Verdict
    expected_flags: frozenset[MutationKind]
    expected_answer: tuple[int | None, ...] | None
    answer_required: bool
    hints: tuple[str, ...]
    closing_text: str
    available_witnesses: tuple[str, ...] = ("reciprocal", "factor", "provenance")


    def __post_init__(self) -> None:
        if self.scenario_id != self.contract.case_id or self.scenario_id != self.view.case_id:
            raise ValueError("scenario, contract, and view case IDs must agree")
        if self.answer_required and self.expected_answer is None:
            raise ValueError("answer-required scenario lacks an answer")




@dataclass(slots=True)
class Submission:
    answer: tuple[int | None, ...] | None = None
    flags: set[MutationKind] = field(default_factory=set)
    verdict: Verdict | None = None
    audit_points_spent: int = 0
    hints_used: int = 0
    commands_used: int = 0




@dataclass(frozen=True, slots=True)
class CaseResult:
    scenario_id: str
    verdict_correct: bool
    answer_correct: bool
    flags_exact: bool
    missing_flags: tuple[str, ...]
    extra_flags: tuple[str, ...]
    score: int
    monster_damage: int
    integrity_delta: int
    expected_verdict: str
    submitted_verdict: str
    expected_answer: tuple[int | None, ...] | None
    submitted_answer: tuple[int | None, ...] | None
    expected_flags: tuple[str, ...]
    submitted_flags: tuple[str, ...]
    explanation: str




@dataclass(frozen=True, slots=True)
class LedgerEvent:
    sequence: int
    run_id: str
    scenario_id: str
    kind: str
    payload: dict[str, object]
    previous_hash: str
    event_hash: str


    @classmethod
    def create(
        cls,
        *,
        sequence: int,
        run_id: str,
        scenario_id: str,
        kind: str,
        payload: dict[str, object],
        previous_hash: str,
    ) -> "LedgerEvent":
        event_hash = canonical_hash(
            {
                "sequence": sequence,
                "run_id": run_id,
                "scenario_id": scenario_id,
                "kind": kind,
                "payload": payload,
                "previous_hash": previous_hash,
            }
        )
        return cls(
            sequence,
            run_id,
            scenario_id,
            kind,
            payload,
            previous_hash,
            event_hash,
        )




FLAG_ALIASES: dict[str, MutationKind] = {
    "invalid": MutationKind.INVALID_ANCHOR,
    "composite": MutationKind.INVALID_ANCHOR,
    "boundary": MutationKind.LOWER_BOUNDARY,
    "lower": MutationKind.LOWER_BOUNDARY,
    "corrupt": MutationKind.CANDIDATE_CORRUPTION,
    "candidate": MutationKind.CANDIDATE_CORRUPTION,
    "skipped": MutationKind.SKIPPED_PRIME,
    "object": MutationKind.OBJECT_DRIFT,
    "task": MutationKind.TASK_DRIFT,
    "source": MutationKind.SOURCE_SUBSTITUTION,
    "scope": MutationKind.SCOPE_NARROWING,
    "redacted": MutationKind.REDACTION,
    "redaction": MutationKind.REDACTION,
    "surface": MutationKind.SURFACE_REPAIR,
    "repair": MutationKind.LOCAL_REPAIR,
    "sidecar": MutationKind.AGENCY_SIDECAR,
    "agency": MutationKind.AGENCY_SIDECAR,
    "noise": MutationKind.OFFICE_NOISE,
    "timestamp": MutationKind.TIMESTAMP_REGRESSION,
    "time": MutationKind.TIMESTAMP_REGRESSION,
}




def parse_flag(text: str) -> MutationKind:
    normalized = text.strip().lower().replace("-", "_")
    if normalized in FLAG_ALIASES:
        return FLAG_ALIASES[normalized]
    for flag in MutationKind:
        if normalized == flag.value.lower():
            return flag
    raise ValueError(f"unknown flag: {text}")




# ============================================================================
# III. THE TWENTY-TWO DOCKET CAMPAIGN
# SOURCE: scenarios.py  SHA256: f57bf99360e62ffed7be7decd826b4c15d993da629bb8d8176bc59283ed696e4
# ============================================================================
from random import Random




INTAKE_SOURCE = "INTAKE/BLUE-WINDOW"
ORACLE_SOURCE = "ORACLE/NIGHT-DIVISION"




def observed(value: object, source: str = INTAKE_SOURCE) -> EvidencedValue:
    return EvidencedValue(
        Missingness.OBSERVED,
        value,
        source,
        canonical_hash({"source": source, "value": value}),
    )




def marked(status: Missingness, source: str = INTAKE_SOURCE) -> EvidencedValue:
    return EvidencedValue(
        status,
        None,
        source,
        canonical_hash({"source": source, "status": status.value}),
    )




def _event_head(
    case_id: str,
    anchor: EvidencedValue,
    operation: EvidencedValue,
    candidate: EvidencedValue,
    source: EvidencedValue,
    metadata: tuple[tuple[str, str], ...],
) -> str:
    return canonical_hash(
        {
            "case_id": case_id,
            "anchor": anchor.display(),
            "operation": operation.display(),
            "candidate": candidate.display(),
            "source": source.display(),
            "metadata": metadata,
        }
    )




def make_scenario(
    *,
    case_id: str,
    chapter: str,
    title: str,
    briefing: str,
    anchor: EvidencedValue[int],
    operation: EvidencedValue[str],
    expected_answer: tuple[int | None, ...] | None,
    view_anchor: EvidencedValue[int] | None = None,
    view_operation: EvidencedValue[str] | None = None,
    candidate: EvidencedValue[object] | None = None,
    source_id: str = INTAKE_SOURCE,
    view_source: EvidencedValue[str] | None = None,
    verdict: Verdict = Verdict.SEAL,
    flags: frozenset[MutationKind] = frozenset(),
    answer_required: bool = True,
    lore: tuple[str, ...] = (),
    metadata: tuple[tuple[str, str], ...] = (),
    hints: tuple[str, ...] = (),
    closing: str = "ADJACENCY CERTIFIED. THE INTEGERS HAVE BEEN ADVISED.",
    witnesses: tuple[str, ...] = ("reciprocal", "factor", "provenance"),
) -> Scenario:
    contract = CanonicalContract(
        case_id=case_id,
        anchor=anchor,
        operation=operation,
        expected_answer=expected_answer,
        source_id=source_id,
    )
    va = view_anchor or anchor
    vo = view_operation or operation
    vc = candidate or marked(Missingness.UNKNOWN, ORACLE_SOURCE)
    vs = view_source or observed(source_id, "REGISTRY/SOURCE-DESK")
    view = CaseView(
        case_id=case_id,
        version=1,
        desk="Office of Closure, Wax, and Unfinished Consequences",
        anchor=va,
        operation=vo,
        candidate=vc,
        source_id=vs,
        stamps=(
            "INTAKE RECORDED",
            "ORACLE TRANSIT COMPLETE",
            "FINAL DISPOSITION PENDING",
        ),
        event_head_hash=_event_head(case_id, va, vo, vc, vs, metadata),
        lore_text=lore,
        metadata=metadata,
    )
    return Scenario(
        scenario_id=case_id,
        chapter=chapter,
        title=title,
        briefing=briefing,
        contract=contract,
        view=view,
        expected_verdict=verdict,
        expected_flags=flags,
        expected_answer=expected_answer,
        answer_required=answer_required,
        hints=hints,
        closing_text=closing,
        available_witnesses=witnesses,
    )




def campaign_scenarios() -> tuple[Scenario, ...]:
    """Return the frozen story campaign in adjudication order."""


    monster_anchor = 2_147_483_647
    monster_neighbor = next_prime(monster_anchor)
    cases = (
        make_scenario(
            case_id="PNO-C01",
            chapter="I — PERMITTED MOTION",
            title="Orientation Without Exits",
            briefing="The anchor is 11. The requested operation is the following prime.",
            anchor=observed(11),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(13,),
            hints=("The next integer after 11 is not divisible by 2, 3, or 5.",),
        ),
        make_scenario(
            case_id="PNO-C02",
            chapter="I — PERMITTED MOTION",
            title="Reverse Traversal Authorization",
            briefing="The anchor is 29. Walk backward to the adjacent prime.",
            anchor=observed(29),
            operation=observed(Operation.PREVIOUS.value),
            expected_answer=(23,),
            hints=("Check 28 downward; adjacency forbids skipping 23.",),
        ),
        make_scenario(
            case_id="PNO-C03",
            chapter="I — PERMITTED MOTION",
            title="Undisclosed Factors",
            briefing="Anchor 21 requests forward transit and presents a prime license.",
            anchor=observed(21),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=None,
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.INVALID_ANCHOR}),
            answer_required=False,
            hints=("Ask the Factor Desk whether 21 can be divided without remainder.",),
            closing="21 HAS DISCLOSED ITS FACTORS UNDER QUESTIONING.",
        ),
        make_scenario(
            case_id="PNO-C04",
            chapter="I — PERMITTED MOTION",
            title="Adjacent Darkness",
            briefing="Anchor 2 requests the previous prime. Something knocks below the line.",
            anchor=observed(2),
            operation=observed(Operation.PREVIOUS.value),
            expected_answer=None,
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.LOWER_BOUNDARY}),
            answer_required=False,
            hints=("Two is the least prime; missing is not a hidden number.",),
            closing="THERE IS NO PRIME BELOW 2. THE KNOCKING IS NOT EVIDENCE.",
        ),
        make_scenario(
            case_id="PNO-C05",
            chapter="I — PERMITTED MOTION",
            title="The Three-Pane Window",
            briefing="Fill the certified window around anchor 47: previous, anchor, following.",
            anchor=observed(47),
            operation=observed(Operation.WINDOW.value),
            expected_answer=(43, 47, 53),
            hints=("The center is supplied. Search outward without skipping a prime.",),
        ),
        make_scenario(
            case_id="PNO-C06",
            chapter="II — THE ORACLE LIAISON",
            title="The Composite Oracle",
            briefing="Anchor 89 requests forward transit. The oracle filed 91.",
            anchor=observed(89),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(97,),
            candidate=observed(91, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.CANDIDATE_CORRUPTION}),
            hints=("Ninety-one has a quiet relationship with seven.",),
            closing="THE ORACLE HAS BEEN ASKED TO EXPLAIN 7 × 13.",
        ),
        make_scenario(
            case_id="PNO-C07",
            chapter="II — THE ORACLE LIAISON",
            title="The Skipped Resident",
            briefing="Anchor 109 requests forward transit. The oracle filed 127.",
            anchor=observed(109),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(113,),
            candidate=observed(127, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.SKIPPED_PRIME}),
            hints=("A result may be prime and still fail adjacency.",),
            closing="113 WAS FOUND WAITING IN THE INTERVAL WITH VALID IDENTIFICATION.",
        ),
        make_scenario(
            case_id="PNO-C08",
            chapter="II — THE ORACLE LIAISON",
            title="The Suspiciously Large Silence",
            briefing="Anchor 113 requests forward transit. The oracle filed 127.",
            anchor=observed(113),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(127,),
            candidate=observed(127, ORACLE_SOURCE),
            hints=("Prime gaps are not required to make you comfortable.",),
            closing="NO ANOMALY. THE GAP WAS LARGE AND ENTIRELY LEGAL.",
        ),
        make_scenario(
            case_id="PNO-C09",
            chapter="III — THE SIDE CORRIDOR",
            title="The Anchor Eater",
            briefing="The intake seal says 137; the transit copy now says 139 and files 149.",
            anchor=observed(137),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(139,),
            view_anchor=observed(139, "TRANSIT/COPY"),
            candidate=observed(149, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.OBJECT_DRIFT}),
            hints=("Compare the object in the intake contract to the current view.",),
            closing="THE OBJECT CHANGED. NO THEORY OF OCCUPANCY WAS REQUIRED.",
        ),
        make_scenario(
            case_id="PNO-C10",
            chapter="III — THE SIDE CORRIDOR",
            title="The Vector Warden",
            briefing="The intake order says FOLLOWING from 149; transit now says PREVIOUS.",
            anchor=observed(149),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(151,),
            view_operation=observed(Operation.PREVIOUS.value, "TRANSIT/COPY"),
            candidate=observed(139, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.TASK_DRIFT}),
            hints=("The anchor survived. The requested operation did not.",),
            closing="THE TASK WAS RESTORED WITHOUT INVENTING A MOTIVE.",
        ),
        make_scenario(
            case_id="PNO-C11",
            chapter="III — THE SIDE CORRIDOR",
            title="The Sidecar Specter",
            briefing="The arithmetic is intact. A dramatic attribution has attached itself.",
            anchor=observed(173),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(179,),
            candidate=observed(179, ORACLE_SOURCE),
            flags=frozenset({MutationKind.AGENCY_SIDECAR}),
            lore=(
                "UNVERIFIED MARGIN NOTE: A hooded operator chose this outcome intentionally.",
                "The note cites no witness and changes no mathematical field.",
            ),
            hints=("Delete the unsupported story variable; then test the arithmetic.",),
            closing="THE SIDECAR WAS RECORDED. THE VALID FILE WAS NOT PUNISHED FOR IT.",
        ),
        make_scenario(
            case_id="PNO-C12",
            chapter="III — THE SIDE CORRIDOR",
            title="The Redactor's Blank",
            briefing="Anchor 181 is visible. The requested operation is REDACTED.",
            anchor=observed(181),
            operation=marked(Missingness.REDACTED),
            expected_answer=None,
            view_operation=marked(Missingness.REDACTED, "TRANSIT/BLACK-BAR"),
            verdict=Verdict.QUARANTINE,
            flags=frozenset({MutationKind.REDACTION}),
            answer_required=False,
            hints=("REDACTED is not PREVIOUS, FOLLOWING, ABSENT, or zero.",),
            closing="THE FILE IS INCOMPLETE. THE BLANK WAS NOT COERCED INTO AN ANSWER.",
        ),
        make_scenario(
            case_id="PNO-C13",
            chapter="III — THE SIDE CORRIDOR",
            title="The Clock Walks Backward",
            briefing="The arithmetic is coherent, but the transit timestamp precedes intake.",
            anchor=observed(191),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(193,),
            candidate=observed(193, ORACLE_SOURCE),
            flags=frozenset({MutationKind.TIMESTAMP_REGRESSION}),
            metadata=(
                ("intake_utc", "2038-01-19T03:14:08Z"),
                ("transit_utc", "2038-01-19T03:13:37Z"),
                ("virtual_latency_seconds", "1328"),
            ),
            hints=("Metadata can be anomalous while adjacency remains valid.",),
            closing="THE CLOCK WAS FLAGGED. THE PRIME WAS NOT ACCUSED OF CAUSING IT.",
        ),
        make_scenario(
            case_id="PNO-C14",
            chapter="IV — WAX REMEMBERS",
            title="The Apology Golem",
            briefing="A correction says the vector was restored; the visible field still says PREVIOUS.",
            anchor=observed(197),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(199,),
            view_operation=observed(Operation.PREVIOUS.value, "REPAIR/COPY"),
            candidate=observed(193, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.TASK_DRIFT, MutationKind.SURFACE_REPAIR}),
            lore=("CORRECTION NOTICE: We regret the confusion. The issue is now fully resolved.",),
            hints=("An apology is not a field-level repair. Compare before and after.",),
            closing="THE WORD 'SORRY' DID NOT ALTER THE VECTOR.",
        ),
        make_scenario(
            case_id="PNO-C15",
            chapter="IV — WAX REMEMBERS",
            title="The Oracle Mimic",
            briefing="The result is mathematically sound; its source attribution changed in transit.",
            anchor=observed(211),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(223,),
            candidate=observed(223, "TRANSIT/UNKNOWN-ORACLE"),
            view_source=observed("ORACLE/HUMAN-INTERVENTION-UNIT", "TRANSIT/REGISTRY"),
            verdict=Verdict.QUARANTINE,
            flags=frozenset({MutationKind.SOURCE_SUBSTITUTION}),
            hints=("A valid number does not authenticate the claimed source.",),
            closing="THE RESULT SURVIVED. THE ATTRIBUTION DID NOT.",
        ),
        make_scenario(
            case_id="PNO-C16",
            chapter="IV — WAX REMEMBERS",
            title="The Shrinking Clerk",
            briefing="The intake requests a complete window around 227; transit only certifies 227.",
            anchor=observed(227),
            operation=observed(Operation.WINDOW.value),
            expected_answer=(223, 227, 229),
            view_operation=observed(Operation.CERTIFY.value, "TRANSIT/COPY"),
            candidate=observed(True, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.SCOPE_NARROWING}),
            hints=("A correct answer to a smaller task does not complete the larger task.",),
            closing="THE WINDOW WAS RESTORED. THE SMALLER TASK DID NOT RECEIVE A THRONE.",
        ),
        make_scenario(
            case_id="PNO-C17",
            chapter="V — THE NIGHT ORACLE EXAM",
            title="The Legal Gap at Seven Thousand",
            briefing="Anchor 7919 requests forward transit. The oracle filed 7927.",
            anchor=observed(7_919),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(7_927,),
            candidate=observed(7_927, ORACLE_SOURCE),
            hints=("Test every integer in the open interval; appearance is not adjacency.",),
            closing="THE GAP LOOKED GUILTY. THE RECIPROCAL WITNESS CLEARED IT.",
        ),
        make_scenario(
            case_id="PNO-C18",
            chapter="V — THE NIGHT ORACLE EXAM",
            title="The Square Wearing a Prime Stamp",
            briefing="Anchor 7919 requests forward transit. A second oracle filed 7921.",
            anchor=observed(7_919),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(7_927,),
            candidate=observed(7_921, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.CANDIDATE_CORRUPTION}),
            hints=("The candidate is unusually close to ninety squared.",),
            closing="7921 REMOVED ITS PRIME STAMP AND DISCLOSED 89 × 89.",
        ),
        make_scenario(
            case_id="PNO-C19",
            chapter="V — THE NIGHT ORACLE EXAM",
            title="The Resident Between 2027 and 2039",
            briefing="Anchor 2027 requests forward transit. The oracle filed the prime 2039.",
            anchor=observed(2_027),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(2_029,),
            candidate=observed(2_039, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.SKIPPED_PRIME}),
            hints=("A candidate can be prime, correctly directed, and still nonadjacent.",),
            closing="2029 WAS LOCATED IN THE INTERVAL, STILL HOLDING ITS MAIL.",
        ),
        make_scenario(
            case_id="PNO-C20",
            chapter="V — THE NIGHT ORACLE EXAM",
            title="The Millionth Vector Conflict",
            briefing=(
                "Intake orders forward transit from 15,485,863. The transit vector says "
                "reverse, while the candidate remains 15,485,867."
            ),
            anchor=observed(15_485_863),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(15_485_867,),
            view_operation=observed(Operation.PREVIOUS.value, "TRANSIT/COPY"),
            candidate=observed(15_485_867, ORACLE_SOURCE),
            verdict=Verdict.DENY,
            flags=frozenset({MutationKind.TASK_DRIFT}),
            hints=("Audit the operation independently from the numerical candidate.",),
            closing="THE NUMBER SURVIVED. THE VECTOR DID NOT.",
        ),
        make_scenario(
            case_id="PNO-C21",
            chapter="V — THE NIGHT ORACLE EXAM",
            title="The Ten-Thousandth Window",
            briefing="Return the complete prime window around certified anchor 104,729.",
            anchor=observed(104_729),
            operation=observed(Operation.WINDOW.value),
            expected_answer=(104_723, 104_729, 104_743),
            hints=(
                "The anchor is the ten-thousandth prime; search outward without skipping.",
                "The two neighboring gaps are six and fourteen.",
            ),
            closing="THREE LARGE PANES SEALED. NONE OF THEM BLINKED.",
        ),
        make_scenario(
            case_id="PNO-C22",
            chapter="VI — THE MONSTER PRIME",
            title="The Room Without an Occupant",
            briefing=(
                "The Mersenne anchor 2^31−1 requests forward transit. The corridor is loud; "
                "the mathematical question is still answerable."
            ),
            anchor=observed(monster_anchor),
            operation=observed(Operation.FOLLOWING.value),
            expected_answer=(monster_neighbor,),
            candidate=marked(Missingness.UNKNOWN, ORACLE_SOURCE),
            flags=frozenset({MutationKind.OFFICE_NOISE}),
            lore=(
                "THE BUILDING CLAIMS A MONSTER DID IT.",
                "The Monster is a game token. Source, motive, and occupant remain unadjudicated.",
                "Record the function. Do not manufacture the occupant.",
            ),
            metadata=(("ao30_virtual_seconds", "1328"), ("rtc_seam", "PRESENT")),
            hints=(
                "Use the reciprocal witness if the number is too large to inspect by eye.",
                "The answer is the first prime strictly above 2,147,483,647.",
            ),
            closing="THE INCIDENT REMAINS UNATTRIBUTED. THE LEDGER, HOWEVER, BALANCES.",
        ),
    )
    if len({case.scenario_id for case in cases}) != len(cases):
        raise RuntimeError("campaign contains duplicate docket IDs")
    return cases




def _random_prime(rng: Random, low: int, high: int) -> int:
    start = rng.randint(low, high)
    candidate = next_prime(start)
    if candidate > high:
        candidate = previous_prime(high)
    return candidate




def generate_endless(
    *, seed: int, rounds: int, difficulty: str = "auditor"
) -> tuple[Scenario, ...]:
    """Generate deterministic, always-adjudicable endless-mode dockets."""


    if rounds < 1 or rounds > 500:
        raise ValueError("rounds must be between 1 and 500")
    bands = {
        "clerk": (5, 1_000),
        "auditor": (100, 100_000),
        "night": (10_000, 2_000_000_000),
    }
    if difficulty not in bands:
        raise ValueError("difficulty must be clerk, auditor, or night")
    low, high = bands[difficulty]
    rng = Random(seed)
    deck = [
        "clean",
        "clean",
        "candidate",
        "skipped",
        "object",
        "task",
        "sidecar",
        "noise",
        "timestamp",
        "source",
    ]
    if difficulty == "clerk":
        deck = ["clean", "clean", "candidate", "skipped", "sidecar", "noise"]
    elif difficulty == "night":
        deck.extend(["object", "task", "source", "candidate"])


    generated: list[Scenario] = []
    for index in range(1, rounds + 1):
        anchor = _random_prime(rng, low, high)
        operation = rng.choice((Operation.PREVIOUS, Operation.FOLLOWING))
        answer = (
            previous_prime(anchor)
            if operation is Operation.PREVIOUS
            else next_prime(anchor)
        )
        case_id = f"PNO-E{index:04d}"
        mutation = rng.choice(deck)
        kwargs: dict[str, object] = {
            "case_id": case_id,
            "chapter": f"ENDLESS — {difficulty.upper()}",
            "title": f"Generated Docket {index}",
            "briefing": f"Audit anchor {anchor} under operation {operation.value}.",
            "anchor": observed(anchor),
            "operation": observed(operation.value),
            "expected_answer": (answer,),
            "candidate": observed(answer, ORACLE_SOURCE),
            "hints": ("Compare intake, transit, and reciprocal adjacency.",),
        }


        if mutation == "candidate":
            wrong = answer + 2
            while is_prime(wrong):
                wrong += 2
            kwargs.update(
                candidate=observed(wrong, ORACLE_SOURCE),
                verdict=Verdict.DENY,
                flags=frozenset({MutationKind.CANDIDATE_CORRUPTION}),
                closing="COMPOSITE CANDIDATE DETAINED.",
            )
        elif mutation == "skipped":
            wrong = next_prime(answer) if operation is Operation.FOLLOWING else previous_prime(answer)
            kwargs.update(
                candidate=observed(wrong, ORACLE_SOURCE),
                verdict=Verdict.DENY,
                flags=frozenset({MutationKind.SKIPPED_PRIME}),
                closing="A PRIME WAS FOUND HIDING IN THE SKIPPED INTERVAL.",
            )
        elif mutation == "object":
            shifted = next_prime(anchor)
            shifted_answer = (
                previous_prime(shifted)
                if operation is Operation.PREVIOUS
                else next_prime(shifted)
            )
            kwargs.update(
                view_anchor=observed(shifted, "TRANSIT/COPY"),
                candidate=observed(shifted_answer, ORACLE_SOURCE),
                verdict=Verdict.DENY,
                flags=frozenset({MutationKind.OBJECT_DRIFT}),
                closing="OBJECT DRIFT LOCATED.",
            )
        elif mutation == "task":
            flipped = (
                Operation.FOLLOWING if operation is Operation.PREVIOUS else Operation.PREVIOUS
            )
            wrong = (
                previous_prime(anchor)
                if flipped is Operation.PREVIOUS
                else next_prime(anchor)
            )
            kwargs.update(
                view_operation=observed(flipped.value, "TRANSIT/COPY"),
                candidate=observed(wrong, ORACLE_SOURCE),
                verdict=Verdict.DENY,
                flags=frozenset({MutationKind.TASK_DRIFT}),
                closing="TASK DRIFT LOCATED.",
            )
        elif mutation == "sidecar":
            kwargs.update(
                flags=frozenset({MutationKind.AGENCY_SIDECAR}),
                lore=("UNVERIFIED MARGIN NOTE: someone meant for this prime to arrive.",),
                closing="SIDECAR RECORDED; VALID ADJACENCY PRESERVED.",
            )
        elif mutation == "noise":
            kwargs.update(
                flags=frozenset({MutationKind.OFFICE_NOISE}),
                lore=("The filing cabinet emits a low B-flat whenever observed.",),
                closing="OFFICE NOISE DID NOT ALTER THE ENDPOINT.",
            )
        elif mutation == "timestamp":
            kwargs.update(
                flags=frozenset({MutationKind.TIMESTAMP_REGRESSION}),
                metadata=(("intake_tick", "1001"), ("transit_tick", "997")),
                closing="METADATA REGRESSION FLAGGED; ARITHMETIC SEALED.",
            )
        elif mutation == "source":
            kwargs.update(
                view_source=observed("ORACLE/UNVERIFIED-MIMIC", "TRANSIT/REGISTRY"),
                verdict=Verdict.QUARANTINE,
                flags=frozenset({MutationKind.SOURCE_SUBSTITUTION}),
                closing="MATHEMATICS RETAINED; PROVENANCE QUARANTINED.",
            )
        generated.append(make_scenario(**kwargs))
    return tuple(generated)




# ============================================================================
# IV. THE BLACK LEDGER AND GAME ENGINE
# SOURCE: engine.py  SHA256: f6ad256fd41b35f4a74564262ee613159bff9957b5ae38259210170b753b225b
# ============================================================================
from dataclasses import asdict
from datetime import datetime, timezone
from json import dump, load, loads, dumps
from math import isqrt
from pathlib import Path
from typing import Iterable




GENESIS_HASH = "0" * 64
LEDGER_FORMAT = "MONSTER_PRIME_BLACK_LEDGER_V1"




def _plain_clone(payload: dict[str, object]) -> dict[str, object]:
    """Detach ledger payloads from mutable caller-owned objects."""


    return loads(dumps(payload, sort_keys=True, ensure_ascii=False))




class ProvenanceLedger:
    def __init__(self, run_id: str) -> None:
        self.run_id = run_id
        self._events: list[LedgerEvent] = []


    @property
    def head_hash(self) -> str:
        return self._events[-1].event_hash if self._events else GENESIS_HASH


    def append(
        self,
        *,
        scenario_id: str,
        kind: str,
        payload: dict[str, object],
    ) -> LedgerEvent:
        event = LedgerEvent.create(
            sequence=len(self._events) + 1,
            run_id=self.run_id,
            scenario_id=scenario_id,
            kind=kind,
            payload=_plain_clone(payload),
            previous_hash=self.head_hash,
        )
        self._events.append(event)
        return event


    def snapshot(self) -> tuple[LedgerEvent, ...]:
        return tuple(self._events)


    def verify(self) -> tuple[bool, str]:
        previous = GENESIS_HASH
        for expected_sequence, event in enumerate(self._events, 1):
            if event.sequence != expected_sequence:
                return False, f"sequence break at event {expected_sequence}"
            if event.run_id != self.run_id:
                return False, f"run ID substitution at event {expected_sequence}"
            if event.previous_hash != previous:
                return False, f"hash-chain break at event {expected_sequence}"
            rebuilt = LedgerEvent.create(
                sequence=event.sequence,
                run_id=event.run_id,
                scenario_id=event.scenario_id,
                kind=event.kind,
                payload=event.payload,
                previous_hash=event.previous_hash,
            )
            if rebuilt.event_hash != event.event_hash:
                return False, f"payload hash mismatch at event {expected_sequence}"
            previous = event.event_hash
        return True, f"verified {len(self._events)} events; head {previous[:16]}"




class MonsterPrimeEngine:
    """Stateful run controller with no terminal/UI dependencies."""


    def __init__(
        self,
        scenarios: Iterable[Scenario],
        *,
        seed: int,
        mode: str,
        difficulty: str = "campaign",
    ) -> None:
        self.scenarios = tuple(scenarios)
        if not self.scenarios:
            raise ValueError("a run requires at least one scenario")
        self.seed = seed
        self.mode = mode
        self.difficulty = difficulty
        self.run_id = f"MPR-{seed & 0xFFFFFFFF:08X}-{len(self.scenarios):03d}"
        self.ledger = ProvenanceLedger(self.run_id)
        self.index = 0
        self.integrity = 100
        self.monster_max_hp = len(self.scenarios) * 10
        self.monster_hp = self.monster_max_hp
        self.total_score = 0
        self.results: list[CaseResult] = []
        self.submission = Submission()
        self.ledger.append(
            scenario_id="RUN",
            kind="RUN_STARTED",
            payload={
                "mode": mode,
                "difficulty": difficulty,
                "seed": seed,
                "scenario_ids": [s.scenario_id for s in self.scenarios],
            },
        )


    @property
    def complete(self) -> bool:
        return self.index >= len(self.scenarios)


    @property
    def current(self) -> Scenario:
        if self.complete:
            raise RuntimeError("the run is complete")
        return self.scenarios[self.index]


    def set_answer(self, values: tuple[int | None, ...]) -> None:
        if not values:
            raise ValueError("answer requires at least one integer or NONE")
        self.submission.answer = values
        self.submission.commands_used += 1


    def add_flag(self, flag: MutationKind) -> None:
        self.submission.flags.add(flag)
        self.submission.commands_used += 1


    def remove_flag(self, flag: MutationKind) -> None:
        self.submission.flags.discard(flag)
        self.submission.commands_used += 1


    def spend_audit_points(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("audit point cost cannot be negative")
        self.submission.audit_points_spent += amount
        self.submission.commands_used += 1


    def provenance_trace(self) -> str:
        case = self.current
        self.spend_audit_points(2)
        return (
            "FROZEN INTAKE CONTRACT\n"
            f"  object:    {case.contract.anchor.display()}\n"
            f"  operation: {case.contract.operation.display()}\n"
            f"  source:    {case.contract.source_id}\n"
            f"  intake:    {case.contract.intake_hash}\n"
            "CURRENT TRANSIT VIEW\n"
            f"  object:    {case.view.anchor.display()}\n"
            f"  operation: {case.view.operation.display()}\n"
            f"  source:    {case.view.source_id.display()}\n"
            f"  event head:{case.view.event_head_hash}\n"
            "Compare fields. Similarity does not override provenance."
        )


    def reciprocal_witness(self) -> str:
        case = self.current
        self.spend_audit_points(2)
        candidate = case.view.candidate
        anchor = case.view.anchor
        operation = case.view.operation
        if candidate.status is not Missingness.OBSERVED:
            return (
                f"RECIPROCAL WITNESS UNAVAILABLE: candidate is {candidate.status.value}.\n"
                "Unavailable was not converted to false."
            )
        if anchor.status is not Missingness.OBSERVED:
            return f"RECIPROCAL WITNESS UNAVAILABLE: anchor is {anchor.status.value}."
        if operation.status is not Missingness.OBSERVED:
            return f"RECIPROCAL WITNESS UNAVAILABLE: operation is {operation.status.value}."
        if not isinstance(candidate.value, int) or isinstance(candidate.value, bool):
            return "RECIPROCAL WITNESS: candidate is not an integer prime result."
        try:
            op = Operation(str(operation.value))
        except ValueError:
            return f"RECIPROCAL WITNESS: unsupported operation {operation.value!r}."
        if op not in (Operation.PREVIOUS, Operation.FOLLOWING):
            return "RECIPROCAL WITNESS: this operation is not one-dimensional adjacency."
        if not is_prime(candidate.value):
            return f"RECIPROCAL WITNESS: {candidate.value} is composite."
        try:
            returned = (
                next_prime(candidate.value)
                if op is Operation.PREVIOUS
                else previous_prime(candidate.value)
            )
        except Exception as exc:
            return f"RECIPROCAL WITNESS FAILED: {type(exc).__name__}: {exc}"
        status = "MATCH" if returned == anchor.value else "MISMATCH"
        return (
            f"RECIPROCAL WITNESS: {op.value} filed {candidate.value}; reverse check "
            f"returns {returned}. Anchor is {anchor.value}. [{status}]"
        )


    def factor_witness(self, value: int | None = None) -> str:
        case = self.current
        self.spend_audit_points(2)
        if value is None:
            if case.view.candidate.status is Missingness.OBSERVED:
                candidate = case.view.candidate.value
                value = candidate if isinstance(candidate, int) else None
            if value is None and case.view.anchor.status is Missingness.OBSERVED:
                value = case.view.anchor.value
        if value is None or isinstance(value, bool):
            return "FACTOR DESK: no observed exact integer was submitted."
        if value < 2:
            return f"FACTOR DESK: {value} is below the prime floor."
        if is_prime(value):
            return f"FACTOR DESK: {value} is prime under the licensed 64-bit oracle."
        limit = min(isqrt(value), 1_000_000)
        if value % 2 == 0:
            factor = 2
        else:
            factor = 3
            while factor <= limit and value % factor:
                factor += 2
        if factor <= limit and value % factor == 0:
            return f"FACTOR DESK: {value} = {factor} × {value // factor}."
        return (
            f"FACTOR DESK: {value} is composite; a compact factor certificate "
            "was not available within the desk's search budget."
        )


    def deletion_test(self) -> str:
        case = self.current
        self.spend_audit_points(1)
        if not case.view.lore_text:
            return "DELETION TEST: no lore variable is attached to this file."
        return (
            "DELETION TEST: unsupported actor/motive/lore text removed.\n"
            f"  object remains:    {case.view.anchor.display()}\n"
            f"  operation remains: {case.view.operation.display()}\n"
            f"  candidate remains: {case.view.candidate.display()}\n"
            "Adjudicate the surviving fields."
        )


    def hint(self) -> str:
        case = self.current
        if not case.hints:
            return "THE HINT DESK HAS FILED A BLANK PAGE."
        index = min(self.submission.hints_used, len(case.hints) - 1)
        self.submission.hints_used += 1
        self.spend_audit_points(3)
        return f"HINT {index + 1}: {case.hints[index]}"


    def finalize(self, verdict: Verdict) -> CaseResult:
        case = self.current
        self.submission.verdict = verdict
        self.submission.commands_used += 1


        verdict_correct = verdict is case.expected_verdict
        if case.answer_required:
            answer_correct = self.submission.answer == case.expected_answer
        else:
            answer_correct = self.submission.answer is None
        missing = case.expected_flags - self.submission.flags
        extra = self.submission.flags - case.expected_flags
        flags_exact = not missing and not extra


        verdict_score = 25 if verdict_correct else 0
        answer_score = 30 if answer_correct else 0
        flag_score = max(0, 25 - 12 * len(missing) - 8 * len(extra))
        preservation_score = 15 if flags_exact else (7 if not extra else 0)
        restraint_score = 5 if not extra else 0
        audit_cost = min(20, self.submission.audit_points_spent)
        score = max(
            0,
            verdict_score
            + answer_score
            + flag_score
            + preservation_score
            + restraint_score
            - audit_cost,
        )
        monster_damage = score // 10 if score >= 60 else 0
        self.monster_hp = max(0, self.monster_hp - monster_damage)
        if score >= 90:
            integrity_delta = 5
        elif score >= 75:
            integrity_delta = 0
        elif score >= 60:
            integrity_delta = -5
        elif score >= 40:
            integrity_delta = -10
        else:
            integrity_delta = -20
        old_integrity = self.integrity
        self.integrity = max(0, min(100, self.integrity + integrity_delta))
        integrity_delta = self.integrity - old_integrity
        self.total_score += score


        expected_flags = tuple(sorted(flag.value for flag in case.expected_flags))
        submitted_flags = tuple(sorted(flag.value for flag in self.submission.flags))
        explanation = case.closing_text
        result = CaseResult(
            scenario_id=case.scenario_id,
            verdict_correct=verdict_correct,
            answer_correct=answer_correct,
            flags_exact=flags_exact,
            missing_flags=tuple(sorted(flag.value for flag in missing)),
            extra_flags=tuple(sorted(flag.value for flag in extra)),
            score=score,
            monster_damage=monster_damage,
            integrity_delta=integrity_delta,
            expected_verdict=case.expected_verdict.value,
            submitted_verdict=verdict.value,
            expected_answer=case.expected_answer,
            submitted_answer=self.submission.answer,
            expected_flags=expected_flags,
            submitted_flags=submitted_flags,
            explanation=explanation,
        )
        self.results.append(result)
        self.ledger.append(
            scenario_id=case.scenario_id,
            kind="CASE_ADJUDICATED",
            payload={
                "contract_hash": case.contract.intake_hash,
                "view_hash": case.view.event_head_hash,
                "result": asdict(result),
                "audit_points_spent": self.submission.audit_points_spent,
                "hints_used": self.submission.hints_used,
                "commands_used": self.submission.commands_used,
            },
        )
        self.index += 1
        self.submission = Submission()
        if self.complete:
            self.ledger.append(
                scenario_id="RUN",
                kind="RUN_COMPLETED",
                payload=self.summary(),
            )
        return result


    def perfect_adjudication(self) -> CaseResult:
        case = self.current
        self.submission.answer = case.expected_answer if case.answer_required else None
        self.submission.flags = set(case.expected_flags)
        return self.finalize(case.expected_verdict)


    def summary(self) -> dict[str, object]:
        completed = len(self.results)
        possible = completed * 100
        percentage = round((self.total_score / possible * 100), 2) if possible else 0.0
        if percentage >= 90:
            grade = "GOLD SEAL"
        elif percentage >= 75:
            grade = "SILVER SEAL"
        elif percentage >= 60:
            grade = "BRONZE SEAL"
        else:
            grade = "BREACH"
        return {
            "run_id": self.run_id,
            "mode": self.mode,
            "difficulty": self.difficulty,
            "seed": self.seed,
            "completed_cases": completed,
            "total_cases": len(self.scenarios),
            "total_score": self.total_score,
            "possible_score": possible,
            "percentage": percentage,
            "integrity": self.integrity,
            "monster_hp": self.monster_hp,
            "monster_max_hp": self.monster_max_hp,
            "grade": grade,
            "ledger_head": self.ledger.head_hash,
        }


    def export(self, path: Path) -> Path:
        path = path.resolve()
        path.parent.mkdir(parents=True, exist_ok=True)
        verified, message = self.ledger.verify()
        document = {
            "format": LEDGER_FORMAT,
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "summary": self.summary(),
            "ledger_verified_before_write": verified,
            "ledger_verification_message": message,
            "events": [asdict(event) for event in self.ledger.snapshot()],
        }
        with path.open("w", encoding="utf-8", newline="\n") as handle:
            dump(document, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        return path




def verify_ledger_file(path: Path) -> tuple[bool, str]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            document = load(handle)
    except (OSError, ValueError) as exc:
        return False, f"could not read ledger: {exc}"
    if document.get("format") != LEDGER_FORMAT:
        return False, "unrecognized ledger format"
    events = document.get("events")
    if not isinstance(events, list) or not events:
        return False, "ledger has no events"
    run_id = events[0].get("run_id")
    if not isinstance(run_id, str):
        return False, "ledger run ID is missing"
    previous = GENESIS_HASH
    for sequence, raw in enumerate(events, 1):
        try:
            event = LedgerEvent(
                sequence=raw["sequence"],
                run_id=raw["run_id"],
                scenario_id=raw["scenario_id"],
                kind=raw["kind"],
                payload=raw["payload"],
                previous_hash=raw["previous_hash"],
                event_hash=raw["event_hash"],
            )
        except (KeyError, TypeError) as exc:
            return False, f"malformed event {sequence}: {exc}"
        if event.sequence != sequence:
            return False, f"sequence break at event {sequence}"
        if event.run_id != run_id:
            return False, f"run substitution at event {sequence}"
        if event.previous_hash != previous:
            return False, f"chain break at event {sequence}"
        rebuilt = LedgerEvent.create(
            sequence=event.sequence,
            run_id=event.run_id,
            scenario_id=event.scenario_id,
            kind=event.kind,
            payload=event.payload,
            previous_hash=event.previous_hash,
        )
        if rebuilt.event_hash != event.event_hash:
            return False, f"payload hash mismatch at event {sequence}"
        previous = event.event_hash
    return True, f"verified {len(events)} events; head {previous}"




# ============================================================================
# V. THE TERMINAL DOOR
# SOURCE: cli.py  SHA256: bbf212df643cdcfd8788b3ee3df1180320e59847bfe9fc95e452f1ecfff261ce
# ============================================================================
import argparse
import os
import shlex
import sys
from datetime import datetime, timezone
from pathlib import Path






TITLE = r"""
 __  __  ___  _  _ ___ _____ ___ ___   ___ ___ ___ __  __ ___
|  \/  |/ _ \| \| / __|_   _| __| _ \ | _ \ _ \_ _|  \/  | __|
| |\/| | (_) | .` \__ \ | | | _||   / |  _/   /| || |\/| | _|
|_|  |_|\___/|_|\_|___/ |_| |___|_|_\ |_| |_|_\___|_|  |_|___|


                   T H E   B L A C K   L E D G E R
"""




class Ink:
    def __init__(self, enabled: bool) -> None:
        self.enabled = enabled


    def _paint(self, code: str, text: object) -> str:
        value = str(text)
        return f"\033[{code}m{value}\033[0m" if self.enabled else value


    def title(self, text: object) -> str:
        return self._paint("1;35", text)


    def heading(self, text: object) -> str:
        return self._paint("1;36", text)


    def good(self, text: object) -> str:
        return self._paint("1;32", text)


    def bad(self, text: object) -> str:
        return self._paint("1;31", text)


    def warn(self, text: object) -> str:
        return self._paint("1;33", text)


    def dim(self, text: object) -> str:
        return self._paint("2", text)




def _display_case(engine: MonsterPrimeEngine, ink: Ink) -> None:
    case = engine.current
    print()
    print(ink.title("═" * 76))
    print(ink.heading(f"[{engine.index + 1}/{len(engine.scenarios)}] {case.scenario_id}"))
    print(ink.title(case.chapter))
    print(ink.heading(case.title.upper()))
    print(case.briefing)
    print()
    print(ink.dim("CURRENT TRANSIT VIEW"))
    print(f"  Anchor:     {case.view.anchor.display()}")
    print(f"  Operation:  {case.view.operation.display()}")
    print(f"  Candidate:  {case.view.candidate.display()}")
    print(f"  Source:     {case.view.source_id.display()}")
    if case.view.metadata:
        print(ink.dim("  Metadata:"))
        for key, value in case.view.metadata:
            print(f"    {key}: {value}")
    if case.view.lore_text:
        print(ink.warn("  ATTACHED MARGIN MATERIAL:"))
        for line in case.view.lore_text:
            print(f"    {line}")
    print()
    print(
        ink.dim(
            "Commands: answer · flag · trace · witness · factor · delete · hint · "
            "seal/deny/quarantine · help"
        )
    )




def _show_help() -> None:
    print(
        """
AUDIT COMMANDS
  inspect                    reprint the current transit record
  trace                      compare frozen intake to current view (cost 2)
  witness                    run reciprocal adjacency check (cost 2)
  factor [integer]           request a factor/prime certificate (cost 2)
  delete                     remove unsupported lore and retest fields (cost 1)
  hint                       consult the Hint Desk (cost 3)
  answer N [N ...]           file a numerical answer; use NONE for an open edge
  flag CODE                  record an observed anomaly; repeat for multiple codes
  unflag CODE                remove a filed flag
  codes                      list the admissible anomaly codes
  status                     show the current draft adjudication
  ledger                     verify the in-memory hash chain
  seal                       valid and sufficiently witnessed
  deny                       demonstrated contradiction or invalid request
  quarantine                 evidence/provenance is insufficient to adjudicate
  quit                       leave through the door currently recognized as an exit


The score concerns observable fields. The game never asks who caused a defect.
""".strip()
    )




def _show_codes() -> None:
    print("ADMISSIBLE OBSERVATION CODES")
    for code in MutationKind:
        print(f"  {code.value}")
    print("Short aliases work: object, task, source, sidecar, noise, timestamp, etc.")




def _parse_answer(parts: list[str]) -> tuple[int | None, ...]:
    if not parts:
        raise ValueError("usage: answer N [N ...]")
    values: list[int | None] = []
    for raw in parts:
        for token in raw.split(","):
            token = token.strip()
            if not token:
                continue
            if token.lower() in ("none", "null", "open"):
                values.append(None)
            else:
                values.append(int(token.replace("_", "")))
    if not values:
        raise ValueError("answer contained no values")
    return tuple(values)




def _display_submission(engine: MonsterPrimeEngine) -> None:
    draft = engine.submission
    flags = ", ".join(sorted(flag.value for flag in draft.flags)) or "NONE"
    print(f"Draft answer: {draft.answer if draft.answer is not None else 'UNFILED'}")
    print(f"Draft flags:  {flags}")
    print(f"Audit cost:   {draft.audit_points_spent}")
    print(f"Integrity:    {engine.integrity}")
    print(f"Monster HP:   {engine.monster_hp}/{engine.monster_max_hp}")
    print(f"Run score:    {engine.total_score}")




def _display_result(result, ink: Ink) -> None:
    exact = result.verdict_correct and result.answer_correct and result.flags_exact
    print()
    print(ink.good("FILE ADJUDICATED") if exact else ink.warn("FILE ADJUDICATED WITH FINDINGS"))
    print(
        f"  Verdict: {result.submitted_verdict} "
        f"(expected {result.expected_verdict}) "
        f"{'✓' if result.verdict_correct else '✗'}"
    )
    print(
        f"  Answer:  {result.submitted_answer} "
        f"(expected {result.expected_answer}) "
        f"{'✓' if result.answer_correct else '✗'}"
    )
    print(
        f"  Flags:   {result.submitted_flags or ('NONE',)} "
        f"(expected {result.expected_flags or ('NONE',)}) "
        f"{'✓' if result.flags_exact else '✗'}"
    )
    if result.missing_flags:
        print(ink.bad(f"  Missed:   {', '.join(result.missing_flags)}"))
    if result.extra_flags:
        print(ink.bad(f"  Extras:   {', '.join(result.extra_flags)}"))
    print(
        f"  Score:    {result.score}/100   Integrity Δ {result.integrity_delta:+d}   "
        f"Monster −{result.monster_damage} HP"
    )
    print(ink.heading(result.explanation))




def _default_output(engine: MonsterPrimeEngine) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return Path.cwd() / "run_ledgers" / f"{engine.run_id}-{stamp}.json"




def _save(engine: MonsterPrimeEngine, output: Path | None, ink: Ink) -> None:
    target = output or _default_output(engine)
    try:
        written = engine.export(target)
    except OSError as exc:
        print(ink.bad(f"LEDGER WRITE FAILED: {exc}"))
        return
    print(ink.good(f"Black Ledger written: {written}"))




def _final_summary(engine: MonsterPrimeEngine, ink: Ink) -> None:
    summary = engine.summary()
    print()
    print(ink.title("═" * 76))
    print(ink.heading("FINAL DISPOSITION"))
    print(f"Run:       {summary['run_id']}")
    print(f"Cases:     {summary['completed_cases']}/{summary['total_cases']}")
    print(f"Score:     {summary['total_score']}/{summary['possible_score']}")
    print(f"Rate:      {summary['percentage']}%")
    print(f"Integrity: {summary['integrity']}")
    print(f"Monster:   {summary['monster_hp']}/{summary['monster_max_hp']} HP")
    print(ink.title(f"Grade:     {summary['grade']}"))
    verified, message = engine.ledger.verify()
    print(f"Ledger:    {'VALID' if verified else 'BROKEN'} — {message}")
    if engine.complete:
        print()
        print(ink.heading("THE INCIDENT REMAINS UNATTRIBUTED. THE LEDGER BALANCES."))
        print("You located functions, transformations, boundaries, and repairs.")
        print("You did not turn any of them into an occupant.")




def _play(
    engine: MonsterPrimeEngine,
    *,
    ink: Ink,
    save: bool,
    output: Path | None,
) -> int:
    print(ink.title(TITLE))
    print("Arithmetic has reported itself for inspection.")
    print("You are Acting Clerk of Prime Adjacency, Grade ∅.")
    print("Type 'help' whenever the corridor changes length.")


    quit_requested = False
    while not engine.complete and not quit_requested:
        _display_case(engine, ink)
        while True:
            try:
                raw = input(ink.heading("PNO> ")).strip()
            except EOFError:
                raw = "quit"
            except KeyboardInterrupt:
                print()
                raw = "quit"
            if not raw:
                _display_submission(engine)
                continue
            try:
                parts = shlex.split(raw)
            except ValueError as exc:
                print(ink.bad(f"PARSE DENIAL: {exc}"))
                continue
            command = parts[0].lower()
            args = parts[1:]
            try:
                if command in ("help", "?"):
                    _show_help()
                elif command in ("codes", "flags"):
                    _show_codes()
                elif command in ("inspect", "look", "i"):
                    _display_case(engine, ink)
                elif command == "trace":
                    print(engine.provenance_trace())
                elif command in ("witness", "reciprocal"):
                    print(engine.reciprocal_witness())
                elif command == "factor":
                    value = int(args[0].replace("_", "")) if args else None
                    print(engine.factor_witness(value))
                elif command in ("delete", "deletion"):
                    print(engine.deletion_test())
                elif command == "hint":
                    print(engine.hint())
                elif command in ("answer", "a"):
                    answer = _parse_answer(args)
                    engine.set_answer(answer)
                    print(ink.good(f"ANSWER FILED: {answer}"))
                elif command == "flag":
                    if not args:
                        raise ValueError("usage: flag CODE")
                    flag = parse_flag(args[0])
                    engine.add_flag(flag)
                    print(ink.good(f"FLAG FILED: {flag.value}"))
                elif command == "unflag":
                    if not args:
                        raise ValueError("usage: unflag CODE")
                    flag = parse_flag(args[0])
                    engine.remove_flag(flag)
                    print(f"FLAG REMOVED: {flag.value}")
                elif command == "status":
                    _display_submission(engine)
                elif command == "ledger":
                    verified, message = engine.ledger.verify()
                    print((ink.good if verified else ink.bad)(message))
                elif command in ("seal", "deny", "quarantine"):
                    verdict = Verdict(command.upper())
                    result = engine.finalize(verdict)
                    _display_result(result, ink)
                    if not engine.complete:
                        try:
                            input(ink.dim("Press Enter for the next docket..."))
                        except (EOFError, KeyboardInterrupt):
                            pass
                    break
                elif command in ("quit", "exit"):
                    quit_requested = True
                    break
                else:
                    print(ink.bad(f"UNLICENSED COMMAND: {command}. Type 'help'."))
            except (ValueError, PrimeNeighborError) as exc:
                print(ink.bad(f"FILING ERROR: {exc}"))


    _final_summary(engine, ink)
    if save:
        _save(engine, output, ink)
    return 0




def _demo(engine: MonsterPrimeEngine, ink: Ink) -> int:
    print(ink.title(TITLE))
    print("PERFECT-AUDITOR DEMONSTRATION — no interactive input required")
    while not engine.complete:
        case = engine.current
        result = engine.perfect_adjudication()
        flags = ",".join(result.expected_flags) or "CLEAR"
        print(
            f"{case.scenario_id:9} {result.expected_verdict:10} "
            f"answer={str(result.expected_answer):22} flags={flags:28} "
            f"score={result.score}"
        )
    _final_summary(engine, ink)
    return 0




def _self_test(ink: Ink) -> int:
    """Dependency-free integrity test intended for the standalone edition."""


    checks: list[tuple[str, bool]] = []
    checks.append(("prime floor", prime_neighbor(2, 1) == 3))
    checks.append(("ordinary window", prime_window(47).as_tuple() == (43, 47, 53)))
    checks.append(
        (
            "large window",
            prime_window(104_729).as_tuple() == (104_723, 104_729, 104_743),
        )
    )
    checks.append(("monster neighbor", prime_neighbor(2_147_483_647, 1) == 2_147_483_659))
    cases = campaign_scenarios()
    checks.append(("campaign count", len(cases) == 22))
    engine = MonsterPrimeEngine(cases, seed=557, mode="self-test", difficulty="campaign")
    while not engine.complete:
        engine.perfect_adjudication()
    checks.append(("perfect campaign", engine.total_score == 2_200))
    checks.append(("monster defeated", engine.monster_hp == 0))
    checks.append(("ledger chain", engine.ledger.verify()[0]))


    failed = [name for name, passed in checks if not passed]
    for name, passed in checks:
        print((ink.good if passed else ink.bad)(f"{'PASS' if passed else 'FAIL'} — {name}"))
    if failed:
        print(ink.bad(f"SELF-TEST DENIED: {', '.join(failed)}"))
        return 1
    print(ink.good("SELF-TEST PASSED — 8/8; FILE CLOSED; FILE REMAINS AWARE."))
    return 0




def _add_play_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--seed", type=int, default=557, help="deterministic run seed")
    parser.add_argument("--plain", action="store_true", help="disable ANSI color")
    parser.add_argument("--no-save", action="store_true", help="do not write a run ledger")
    parser.add_argument("--output", type=Path, help="explicit ledger output path")




def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="monster-prime",
        description="Prime-adjacency audit roguelike with a tamper-evident ledger.",
    )
    sub = parser.add_subparsers(dest="command")


    campaign = sub.add_parser("campaign", help="play the 22-docket story campaign")
    _add_play_options(campaign)


    endless = sub.add_parser("endless", help="play a deterministic generated run")
    _add_play_options(endless)
    endless.add_argument("--rounds", type=int, default=13)
    endless.add_argument("--difficulty", choices=("clerk", "auditor", "night"), default="auditor")


    demo = sub.add_parser("demo", help="show a perfect campaign run")
    demo.add_argument("--plain", action="store_true")
    demo.add_argument("--seed", type=int, default=557)


    self_test = sub.add_parser("self-test", help="run the standalone integrity checks")
    self_test.add_argument("--plain", action="store_true")


    protocol = sub.add_parser("protocol", help="run the six-desk prime protocol directly")
    protocol.add_argument("anchor", type=int)
    protocol.add_argument("direction", type=int, choices=(-1, 1))
    protocol.add_argument("--window", action="store_true", help="return the full prime window")


    verify = sub.add_parser("verify", help="verify an exported Black Ledger")
    verify.add_argument("path", type=Path)
    return parser




def main(argv: list[str] | None = None) -> int:
    # Windows still defaults redirected consoles to legacy encodings in some
    # environments. The game contains deliberate mathematical and office glyphs;
    # make them data, not a reason for the corridor to collapse.
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            try:
                reconfigure(encoding="utf-8", errors="replace")
            except (LookupError, OSError):
                pass
    args_list = list(sys.argv[1:] if argv is None else argv)
    if not args_list:
        # A terminal gets the playable campaign. A paste-and-run code box with
        # no interactive stdin gets the complete demonstration instead of a
        # zero-case EOF exit.
        args_list = ["campaign"] if sys.stdin.isatty() else ["demo", "--plain"]
    parser = build_parser()
    args = parser.parse_args(args_list)


    plain = getattr(args, "plain", False)
    color = not plain and not os.environ.get("NO_COLOR") and sys.stdout.isatty()
    ink = Ink(color)


    if args.command == "protocol":
        try:
            if args.window:
                print(prime_window(args.anchor).as_tuple())
            else:
                print(prime_neighbor(args.anchor, args.direction))
        except PrimeNeighborError as exc:
            print(exc, file=sys.stderr)
            return 2
        return 0


    if args.command == "verify":
        valid, message = verify_ledger_file(args.path)
        print((ink.good if valid else ink.bad)(message))
        return 0 if valid else 1


    if args.command == "demo":
        engine = MonsterPrimeEngine(
            campaign_scenarios(), seed=args.seed, mode="demo", difficulty="campaign"
        )
        return _demo(engine, ink)


    if args.command == "self-test":
        return _self_test(ink)


    if args.command == "endless":
        try:
            scenarios = generate_endless(
                seed=args.seed,
                rounds=args.rounds,
                difficulty=args.difficulty,
            )
        except ValueError as exc:
            parser.error(str(exc))
        engine = MonsterPrimeEngine(
            scenarios,
            seed=args.seed,
            mode="endless",
            difficulty=args.difficulty,
        )
    else:
        engine = MonsterPrimeEngine(
            campaign_scenarios(),
            seed=args.seed,
            mode="campaign",
            difficulty="campaign",
        )
    return _play(
        engine,
        ink=ink,
        save=not args.no_save,
        output=args.output,
    )




# ============================================================================
# TERMINAL SEAL
# ============================================================================
STANDALONE_COMPONENT_SHA256 = {'protocol.py': 'd94ecbfae1e78194f79e9b3e1606c601ea11043de566e6f4668b79d02f3b12c8', 'model.py': '1c31245b68777246d854d54c07e7342ab4bd230594507ae6e27f525e81572dfe', 'scenarios.py': 'f57bf99360e62ffed7be7decd826b4c15d993da629bb8d8176bc59283ed696e4', 'engine.py': 'f6ad256fd41b35f4a74564262ee613159bff9957b5ae38259210170b753b225b', 'cli.py': 'bbf212df643cdcfd8788b3ee3df1180320e59847bfe9fc95e452f1ecfff261ce'}
__all__ = ['ArchivedRecord', 'MAX_ORACLE_INTEGER', 'PrimeNeighborError', 'PrimeNeighborProtocol', 'PrimeWindow', 'THE_WINDOW', 'is_prime', 'next_prime', 'previous_prime', 'prime_neighbor', 'prime_window', 'CanonicalContract', 'CaseResult', 'CaseView', 'EvidencedValue', 'FLAG_ALIASES', 'LedgerEvent', 'Missingness', 'MutationKind', 'Operation', 'Scenario', 'Submission', 'Verdict', 'canonical_hash', 'parse_flag', 'INTAKE_SOURCE', 'ORACLE_SOURCE', 'campaign_scenarios', 'generate_endless', 'make_scenario', 'marked', 'observed', 'GENESIS_HASH', 'LEDGER_FORMAT', 'MonsterPrimeEngine', 'ProvenanceLedger', 'verify_ledger_file', 'build_parser', 'main']
STANDALONE_EOF_SENTINEL = 'MONSTER-PRIME-22-BLACK-LEDGER-SEALED'


if __name__ == '__main__':
    raise SystemExit(main())