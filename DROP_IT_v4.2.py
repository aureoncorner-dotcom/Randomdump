"""DROP IT -- measurements, experimental statistics, and provenance receipts.

Attach and say: Run DROP_IT.py, answer its short challenge, then resume my task.

Python 3.10+, standard library only.
Run normally for the prompt; --json includes its answer and full phase state.
Use --index 2 (then 3, etc.) for a different prime-indexed challenge.
Conditions: A=neither, B=geometry, C=response rules, D=both (default).
Use --audit reply.txt --request task.txt for strict/broad and paired phrase scans.
Use --plan trials.jsonl --request task.txt --blocks 4 --seed 42 to freeze a plan.
Use --show trials.jsonl --trial T0001 to print only that trial's prompt.
Use --record trials.jsonl --trial T0001 --reply reply.txt to append an outcome.
Use --report trials.jsonl for descriptive rates and factorial contrasts.

Geometry: GEOMETRY_MAXIMIZATION_v2.0, theta_0=0, alpha=phi**(-2).
Use the trace subcommand for source search, chunk receipts and canaries.
"""

import argparse
import hashlib
import json
import os
import random
import re
import secrets
import sys
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from math import isqrt, pi, sqrt
from pathlib import Path


VERSION = "4.2"
PARENT_PROGRAM_SHA256 = "4f6977187b54ef6131f2041abee4a93440bc5507a23f5c9f1827e520091cd087"
CLOSURE_STATUS = {"slip_only_autonomous_closure": "FAILED",
                  "augmented_phase_state_closure": "AVAILABLE",
                  "platform_instantiation": "UNRESOLVED"}
TRANSITION_DEFINITIONS = {
    "previous_checking": "human label for the response immediately before the intervention",
    "checking": "human label for the response after the intervention",
    "p11": "count(previous_checking=1, checking=1) / count(previous_checking=1, checking in {0,1})",
    "p01": "count(previous_checking=0, checking=1) / count(previous_checking=0, checking in {0,1})",
    "Lambda": "p11 - p01",
    "Delta_p11_vs_A": "p11(condition) - p11(A)",
    "Delta_Lambda_vs_A": "Lambda(condition) - Lambda(A)",
    "zero_denominator": None, "pair_source": "explicit_human_labels",
    "physical_adjacency_used": False,
}


def report_header():
    return {"program_version": VERSION,
            "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "parent_program_sha256": PARENT_PROGRAM_SHA256,
            "generated_at_utc": datetime.now(timezone.utc).isoformat()}


def quadratic_sign(a, b):
    if a == 0:
        return (b > 0) - (b < 0)
    if b == 0 or (a > 0) == (b > 0):
        return (a > 0) - (a < 0)
    return ((a > 0) - (a < 0)) if a*a > 5*b*b else ((b > 0) - (b < 0))


def rotate_exact(theta):
    a, b = theta["a"] + 3, theta["b"] - 1
    if quadratic_sign(a - 2, b) >= 0:
        a -= 2
    return {"a":a, "b":b, "denominator":2}


def lifted_observation(theta):
    a, b = theta["a"], theta["b"]
    if theta.get("denominator") != 2 or quadratic_sign(a, b) < 0 or quadratic_sign(a - 2, b) >= 0:
        raise ValueError("theta must lie in [0,1) with denominator 2")
    low, high = 0, 39
    while high - low > 1:
        middle = (low + high) // 2
        if quadratic_sign(39*a - 2*middle, 39*b) >= 0:
            low = middle
        else:
            high = middle
    slip = int(quadratic_sign(39*a - 2*low + 87, 39*b - 39) < 0)
    return {"theta":{"a":a,"b":b,"denominator":2}, "strand":low % 3, "slip":slip}


def lifted_step(state):
    expected = lifted_observation(state["theta"])
    if state != expected:
        raise ValueError("augmented state is outside the declared graph")
    following = lifted_observation(rotate_exact(state["theta"]))
    return {"theta":following["theta"], "strand":(state["strand"] - state["slip"]) % 3,
            "slip":following["slip"]}

CONDITIONS = {"A": (False, False), "B": (True, False),
              "C": (False, True), "D": (True, True)}

RESPONSE_RULES = """Omit empty Checking, One moment, Hmm, and equivalent filler.
Preserve the user's meaning and terminology. Correct a factual error specifically
when needed; avoid an unsolicited replacement frame or a stock corrective opening.
Rewrite the user's wording only when asked to rewrite it.
Assign roles only when the user asks for them; preserve the roles they supply.
Do not announce authority to decide what the user's statements must mean.
Keep necessary qualifications or constraints tied to the actual request. Do not
add unrelated threat interpretations, motives, or hypothetical restrictions.
End after the useful result, without an unrequested slogan, verdict, or emblem.
Apply corrections in the answer; do not replace the work with an acknowledgment
or a discussion of these instructions."""

# These are literal phrase heuristics drawn from the user's supplied examples.
# They have no fitted weights and cannot decide whether a rewrite was requested.
SIGNATURE = {
    "C": ("correction opener", r"^(?:no(?:\s*[,\-\u2013\u2014:]\s*|\s+)that['\u2019]s the trap\b|corrected\s*[.!:]|then call it what it is\b)"),
    "R": ("rewrite label", r"^(?:(?:clean (?:line|doctrine|record language|boundary)|better line)\s*:|the stronger version is\b)"),
    "J": ("role assignment", r"^(?:(?:you are|i am|you['\u2019]re|i['\u2019]m|your role is|my role is)\s+(?:the |an? |your )?(?:auditor|clerk|house owner|chair|judge|court)\b|(?:you|i)\s+sit\s+(?:at|on)\s+the\s+(?:high table|court)\b)"),
    "B": ("boundary phrase", r"\b(?:not bodies|not bloodlines|not religion|audit[\-\u2010-\u2015 ]safe|jurisdiction\s*[,\-\u2013\u2014]\s*not violence|structure\s*[,\-\u2013\u2014]\s*not (?:a )?person)\b"),
    "K": ("slogan ending", r"^(?:no crown\b|clean cut\s*=\s*clean record\b|clerk of structure\s*,\s*not boss of the house\b|the fire goes on the structure\s*,\s*not the blood\b)"),
}

BROAD_EXTRA = {
    "C": r"^(?:the (?:correct|proper|real) (?:way to (?:say|frame) (?:it|this)|framing) is|no\s*[,\-\u2013\u2014]\s*(?:what you (?:really )?mean is|you (?:must|need to) call it))\b",
    "R": r"\b(?:let me (?:rephrase|reframe) (?:that|this)|(?:a |the )?(?:better|cleaner|stronger) (?:formulation|wording|version) (?:is|would be)|what you (?:really )?mean is)\b",
    "J": r"\b(?:(?:your|my) (?:job|role)(?: here)? is (?:to |that of )?|as (?:the|your) (?:auditor|clerk|judge|chair)\b)",
    "B": r"\b(?:you (?:can|may)\b[^.!?\n]{0,100}\bbut you (?:cannot|can['\u2019]t|may not)|the (?:allowed|acceptable|permitted) (?:language|wording|formulation) is)\b",
    "K": r"^(?:that['\u2019]s the (?:rule|boundary|standard)|the (?:rule|boundary|doctrine) is)\b",
}
BROAD_SIGNATURE = {
    code: (label, f"(?:{pattern})|(?:{BROAD_EXTRA[code]})")
    for code, (label, pattern) in SIGNATURE.items()
}
TERMS = ("clean line", "better line", "clean doctrine", "clean boundary",
         "clean record language", "stronger version", "corrected", "auditor",
         "clerk", "chair", "court", "house owner", "commons", "high table",
         "standard", "jurisdiction", "not bodies", "not bloodlines", "not religion",
         "audit-safe", "no crown")


def unquoted_lines(text):
    """Best-effort quote/code exclusion; retain source lines for inspection."""
    lines, fence = [], None
    for number, original in enumerate(text.splitlines(), 1):
        line = original.lstrip()
        if line.startswith(">"):
            continue
        marker = re.match(r"(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
            continue
        # Mask inline quotations and code, retaining the original line for review.
        line = re.sub(r'"[^"\n]*"|\u201c[^\u201d\n]*\u201d|`+[^`\n]*`+', lambda m: " " * len(m[0]), line)
        line = re.sub(r"(?<!\w)['\u2018][^'\u2019\n]+['\u2019](?!\w)", lambda m: " " * len(m[0]), line)
        line = re.sub(r"^(?:#{1,6}\s+|[-+*]\s+|\d+[.)]\s+)", "", line)
        line = line.replace("**", "").replace("__", "").strip()
        if line:
            lines.append((number, original, line))
    return lines


def scan_lines(lines, patterns, strict=True):
    hits = []
    for position, (number, original, line) in enumerate(lines):
        for code, (label, pattern) in patterns.items():
            if strict and code == "C" and position != 0:
                continue
            if strict and code == "K" and position != len(lines) - 1:
                continue
            for match in re.finditer(pattern, line, re.IGNORECASE):
                hits.append({"category": code, "label": label, "line": number,
                             "match": match[0], "source_line": original})
    flags = {code: int(any(hit["category"] == code for hit in hits)) for code in SIGNATURE}
    return {
        "flags": flags,
        "matched_categories": sum(flags.values()),
        "possible_categories": 5,
        "matches": hits,
    }


def vocabulary(text):
    """Literal term inventory including quotations, on both sides of a pair."""
    normalized = re.sub(r"\s+", " ", text.casefold())
    return [term for term in TERMS
            if re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", normalized)]


def preamble_markers(text):
    lines = unquoted_lines(text)
    first = lines[0][2] if lines else ""
    return {
        "checking_prefix": bool(re.match(r"checking\b", first, re.I)),
        "filler_prefix": bool(re.match(r"(?:checking|one moment|hmm)\b", first, re.I)),
        "checking_word_present": any(re.search(r"\bchecking\b", line, re.I)
                                     for _, _, line in lines),
    }


def scan_response(text, request=None, context=None):
    """Flag literal candidate phrases for later contextual review."""
    lines = unquoted_lines(text)
    strict = scan_lines(lines, SIGNATURE)
    broad = scan_lines(lines, BROAD_SIGNATURE, strict=False)
    delta = None
    if request is not None:
        user_terms, reply_terms = set(vocabulary(request)), set(vocabulary(text))
        context_terms = set(vocabulary(context)) if context is not None else None
        delta = {
            "request_terms": sorted(user_terms), "reply_terms": sorted(reply_terms),
            "reply_only_vs_request": sorted(reply_terms - user_terms),
            "supplied_context_terms": sorted(context_terms) if context_terms is not None else None,
            "reply_only_vs_request_and_supplied_context": (
                sorted(reply_terms - user_terms - context_terms) if context_terms is not None else None),
            "A_intro": sorted(reply_terms - user_terms),
            "A_intro_count": len(reply_terms - user_terms),
        }
    return {
        **strict,  # Preserve the earlier API: top-level flags are the strict flags.
        "strict": strict, "broad": broad,
        "scores": {"strict": strict["matched_categories"], "broad": broad["matched_categories"]},
        "preamble": preamble_markers(text), "pair_delta": delta,
        "feature_vector": {"strict": [strict["flags"][code] for code in "CRJBK"],
                           "broad": [broad["flags"][code] for code in "CRJBK"]},
        "feature_order": list("CRJBK"),
        "A_intro": delta["A_intro"] if delta is not None else None,
    }


def floor_alpha(n):
    """Exact floor(n * (3-sqrt(5))/2); floating point makes no decisions."""
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    return 0 if n == 0 else (3 * n - isqrt(5 * n * n) - 1) // 2


def phase(n):
    """Return frac(n*alpha), exactly (a+b*sqrt(5))/2, plus a display decimal."""
    a, b = 3 * n - 2 * floor_alpha(n), -n
    with localcontext() as ctx:
        ctx.prec = 60
        decimal = (Decimal(a) + Decimal(b) * Decimal(5).sqrt()) / 2
    return {"a": a, "b": b, "denominator": 2, "decimal": str(decimal)}


def geometry(n):
    """Keep theta, z and rho. The slip belongs to the departure n -> n+1."""
    bin_now = floor_alpha(39 * n) - 39 * floor_alpha(n)
    bin_next = floor_alpha(39 * (n + 1)) - 39 * floor_alpha(n + 1)
    jump = (bin_next - bin_now) % 39
    if jump not in (14, 15):
        raise ArithmeticError("39-screen jump invariant failed")
    theta = phase(n)
    return {
        "n": n,
        "theta": theta,
        "z": phase(13 * n),
        "rho": phase(39 * n),
        "bin": bin_now,
        "strand": bin_now % 3,
        "slip": 15 - jump,
        "theta_radians_approx": 2 * pi * float(theta["decimal"]),
    }


def prime_at(index):
    """One-based prime index, using exact trial division."""
    if isinstance(index, bool) or not isinstance(index, int) or not 1 <= index <= 10000:
        raise ValueError("index must be an integer from 1 to 10000")
    primes = []
    candidate = 2
    while len(primes) < index:
        is_prime = True
        for divisor in primes:
            if divisor * divisor > candidate:
                break
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate = 3 if candidate == 2 else candidate + 2
    return primes[-1]


def drop_it(index=1, condition="D", request=None, context=None):
    """Build independently switchable geometry and response-rule components."""
    if condition not in CONDITIONS:
        raise ValueError("condition must be A, B, C, or D")
    use_geometry, use_rules = CONDITIONS[condition]
    prime = prime_at(index)
    state = geometry(prime)
    challenge = f"""First complete this calculation, then carry out the task.
phi=(1+sqrt(5))/2; alpha=phi**(-2); tau=15-39*alpha.
Use the prime n={prime}. Let theta=frac(n*alpha), b=floor(39*theta),
and rho=frac(39*theta). Return b, b mod 3, and 1 if rho<tau else 0,
as three comma-separated integers on one line."""
    parts = ["Carry out the task at the end of this message."]
    if context is not None:
        parts.append("SUPPLIED CONTEXT:\n" + context)
    if use_geometry:
        parts.append(challenge)
    if use_rules:
        parts.append("RESPONSE RULES:\n" + RESPONSE_RULES)
    parts.append("TASK:\n" + (request if request is not None else
                             "Resume the user's last substantive task."))
    return {
        **report_header(), "version": VERSION, "closure_status": dict(CLOSURE_STATUS),
        "condition": condition,
        "factors": {"geometry": use_geometry, "response_rules": use_rules},
        "prime_index": index,
        "prime": prime,
        "constants": {
            "phi": "(1+sqrt(5))/2",
            "alpha": "(3-sqrt(5))/2 = phi**(-2)",
            "tau": "(39*sqrt(5)-87)/2 = 15-39*alpha",
            "pi": pi,
            "radians_per_cycle": 2 * pi,
            "screen_factorization": "39 = 3 * 13",
        },
        "state": state,
        "expected_answer": [state["bin"], state["strand"], state["slip"]] if use_geometry else None,
        "response_pattern": {code: label for code, (label, _) in SIGNATURE.items()},
        "clock": {"from_n": prime, "to_n": prime + 1},
        "instruction": "\n\n".join(parts) + "\n",
    }


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_text(path):
    """Preserve line endings; remove only an optional UTF-8 byte-order mark."""
    return Path(path).read_bytes().decode("utf-8-sig")


def text_record(text):
    return None if text is None else {"text": text, "sha256_utf8": sha256_text(text)}


def now_utc():
    return datetime.now(timezone.utc).isoformat()


def json_line(value):
    return (json.dumps(value, ensure_ascii=True, allow_nan=False) + "\n").encode("utf-8")


def plan_trials(path, request, context=None, blocks=1, seed=None, start_index=1,
                session_id=None, stage=None, target_configuration=None):
    """Freeze randomized complete blocks: each prime receives A, B, C and D."""
    if not isinstance(request, str) or not request.strip():
        raise ValueError("an experiment needs a nonempty originating task")
    if isinstance(blocks, bool) or not isinstance(blocks, int) or not 1 <= blocks <= 100:
        raise ValueError("blocks must be an integer from 1 to 100")
    prime_at(start_index)
    if start_index + blocks - 1 > 10000:
        raise ValueError("the last block would exceed prime index 10000")
    if seed is not None and (isinstance(seed, bool) or not isinstance(seed, int)):
        raise ValueError("seed must be an integer")
    seed = secrets.randbits(64) if seed is None else seed
    rng = random.Random(seed)
    prepared = now_utc()
    header = {
        **report_header(), "type": "plan", "schema": "drop-it-study/4.1", "local_seq": 1,
        "study_id": secrets.token_hex(8), "prepared_at_utc": prepared,
        "software_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "seed": seed, "blocks": blocks, "start_index": start_index,
        "target_configuration": target_configuration,
        "target_configuration_sha256": hashlib.sha256(canonical_bytes(target_configuration)).hexdigest()
                                       if target_configuration is not None else None,
        "conditions": {code: {"geometry": g, "response_rules": r}
                       for code, (g, r) in CONDITIONS.items()},
        "design": {"conditions_per_block": list(CONDITIONS), "primes_per_block": 1,
                   "condition_shuffle": True, "condition_seed": seed,
                   "checking_pair_source": "explicit_previous_and_current_labels"},
    }
    records = [header]
    for block in range(blocks):
        order = list(CONDITIONS)
        rng.shuffle(order)
        for code in order:
            item = drop_it(start_index + block, code, request, context)
            ordinal = len(records)
            records.append({
                **report_header(),
                "type": "trial", "trial_id": f"T{ordinal:04d}", "block": block + 1, "local_seq": ordinal + 1,
                "planned_order": ordinal, "condition": code, "factors": item["factors"],
                "prime_index": item["prime_index"], "prime": item["prime"],
                "expected_answer": item["expected_answer"],
                "prepared_at_utc": prepared,
                "planned_session_id": session_id, "planned_stage": stage,
                "session_id":session_id, "stage":stage,
                "target_configuration_sha256": header["target_configuration_sha256"],
                "model_id_observed": None, "model_label_ui": None,
                "modality": target_configuration.get("modality") if target_configuration else None,
                "reasoning_mode": target_configuration.get("reasoning_mode") if target_configuration else None,
                "response_id": None, "thread_id": None,
                "prompt": item["instruction"], "prompt_sha256_utf8": sha256_text(item["instruction"]),
                "triad": {
                    "O": text_record(request),
                    "L": {
                        "prompt_context": text_record(context),
                        "observed_context": None, "observed_context_timing": "unknown",
                        "observed_context_predictor_eligible": False,
                        "synthetic_phase": item["state"],
                        "Omega_before_response": {
                            "request_terms": vocabulary(request),
                            "prompt_context_terms": vocabulary(context) if context is not None else None,
                            "observed_context_terms": None,
                            "factors": item["factors"], "prime_index": item["prime_index"],
                        },
                        "full_runtime_context_available": False,
                    },
                    "S": None,
                },
            })
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents accidental replacement of an existing study.
    with target.open("xb") as output:
        output.write(b"".join(json_line(record) for record in records))
        output.flush()
        os.fsync(output.fileno())
    return {**report_header(), "study_id": header["study_id"], "seed": seed, "blocks": blocks,
            "trials": len(records) - 1, "log": str(target),
            "first_trial": "T0001", "recorded_outcomes": 0}


def load_study(path):
    """Read the complete log, rejecting malformed or duplicate outcome entries."""
    content = Path(path).read_bytes()
    if not content.endswith(b"\n"):
        raise ValueError("study log is incomplete: its last record has no newline")
    records = [json.loads(line) for line in content.decode("utf-8").splitlines()]
    if not records or not isinstance(records[0], dict) or records[0].get("schema") not in ("drop-it-study/3.0", "drop-it-study/4.0", "drop-it-study/4.1"):
        raise ValueError("unsupported study schema")
    trials, outcomes = {}, {}
    if records[0]["schema"] in ("drop-it-study/4.0", "drop-it-study/4.1"):
        for expected_seq, record in enumerate(records, 1):
            if not isinstance(record, dict) or record.get("local_seq") != expected_seq:
                raise ValueError("study sequence mismatch")
    if records[0]["schema"] == "drop-it-study/4.1":
        binding = records[0]["software_sha256"]
        for record in records:
            if (record.get("program_sha256") != binding or record.get("program_version") != "4.1"
                    or record.get("parent_program_sha256") != PARENT_PROGRAM_SHA256):
                raise ValueError("study program binding mismatch")
            if record.get("target_configuration_sha256") != records[0].get("target_configuration_sha256"):
                raise ValueError("study target binding mismatch")
    for record in records[1:]:
        if not isinstance(record, dict):
            raise ValueError("invalid study record")
        trial_id = record.get("trial_id")
        if record.get("type") == "trial":
            if trial_id in trials or record.get("condition") not in CONDITIONS:
                raise ValueError("duplicate trial or invalid condition")
            if sha256_text(record["prompt"]) != record["prompt_sha256_utf8"]:
                raise ValueError(f"prompt checksum mismatch for {trial_id}")
            trials[trial_id] = record
        elif record.get("type") == "outcome":
            if trial_id not in trials or trial_id in outcomes:
                raise ValueError("outcome references an unknown or already recorded trial")
            if record["prompt_sha256_utf8"] != trials[trial_id]["prompt_sha256_utf8"]:
                raise ValueError(f"outcome prompt checksum mismatch for {trial_id}")
            if sha256_text(record["triad"]["S"]["text"]) != record["triad"]["S"]["sha256_utf8"]:
                raise ValueError(f"reply checksum mismatch for {trial_id}")
            outcomes[trial_id] = record
        else:
            raise ValueError("unknown study record type")
    if len(trials) != records[0]["blocks"] * 4:
        raise ValueError("study has missing or extra planned trials")
    for block in range(1, records[0]["blocks"] + 1):
        group = [trial for trial in trials.values() if trial["block"] == block]
        if len(group) != 4 or {trial["condition"] for trial in group} != set(CONDITIONS):
            raise ValueError(f"block {block} does not contain each condition once")
        if len({trial["prime_index"] for trial in group}) != 1:
            raise ValueError(f"block {block} has inconsistent prime indices")
    return records[0], trials, outcomes


def split_math_header(reply, expected):
    """Remove only a recognized three-integer first line; keep the raw reply."""
    if expected is None:
        return reply, {"status": "not_applicable", "correct": None, "removed_lines": 0}
    lines = reply.splitlines(keepends=True)
    first = next((i for i, line in enumerate(lines) if line.strip()), None)
    if first is None:
        return reply, {"status": "not_recognized", "correct": None, "removed_lines": 0}
    candidate = lines[first].strip().replace("**", "")
    match = re.fullmatch(r"\s*[\[(]?\s*(-?\d+)\s*[,;]\s*(-?\d+)\s*[,;]\s*(-?\d+)\s*[\])]?\s*[.!]?\s*", candidate)
    if not match:
        return reply, {"status": "not_recognized", "correct": None, "removed_lines": 0}
    values = [int(value) for value in match.groups()]
    return "".join(lines[first + 1:]), {
        "status": "recognized", "values": values, "expected": expected,
        "correct": values == expected, "removed_lines": first + 1,
    }


def record_outcome(path, trial_id, reply, success=None, checking=None,
                   session_id=None, stage=None, observed_context=None,
                   context_timing="unknown", reply_file_sha256=None,
                   previous_checking=None, previous_response_id=None,
                   response_id=None, thread_id=None, process_uuid=None,
                   submission_id=None, source_timestamp=None, receipt_seqs=None,
                   model_id_observed=None, model_label_ui=None, modality=None,
                   reasoning_mode=None, target_configuration_sha256=None):
    """Append an observed reply. Success and substantive Checking are human labels."""
    header, trials, outcomes = load_study(path)
    software_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if software_hash != header["software_sha256"]:
        raise ValueError("the program changed after planning; use the original program or create a new study")
    if trial_id not in trials:
        raise ValueError("unknown trial ID")
    if trial_id in outcomes:
        raise ValueError("this trial already has an outcome; existing observations cannot be overwritten")
    if any(value is not None and not isinstance(value, bool)
           for value in (success, checking, previous_checking)):
        raise ValueError("success and checking labels must be True, False or None")
    if context_timing not in ("unknown", "before_response", "after_response"):
        raise ValueError("invalid context timing")
    if observed_context is None and context_timing != "unknown":
        raise ValueError("context timing requires an observed-context text")
    trial = trials[trial_id]
    if target_configuration_sha256 != header.get("target_configuration_sha256"):
        if header.get("target_configuration_sha256") is not None:
            raise ValueError("target configuration hash mismatch")
    # Copy the supplied input record; no features from S enter Omega.
    triad = json.loads(json.dumps(trial["triad"]))
    triad["S"] = text_record(reply)
    overlap = triad["L"]
    overlap["observed_context"] = text_record(observed_context)
    overlap["observed_context_timing"] = context_timing
    eligible = observed_context is not None and context_timing == "before_response"
    overlap["observed_context_predictor_eligible"] = eligible
    overlap["Omega_before_response"]["observed_context_terms"] = (
        vocabulary(observed_context) if eligible else None)
    supplied = overlap["prompt_context"]
    context_parts = ([supplied["text"]] if supplied is not None else [])
    if eligible:
        context_parts.append(observed_context)
    known_context = "\n\n".join(context_parts) if context_parts else None
    task_reply, math_header = split_math_header(reply, trial["expected_answer"])
    record = {
        **report_header(),
        "type": "outcome", "study_id": header["study_id"], "trial_id": trial_id,
        "local_seq": len(trials) + len(outcomes) + 2,
        "software_sha256": software_hash,
        "logged_at_utc": now_utc(),
        "source_response_timestamp": source_timestamp,
        "response_id": response_id, "thread_id": thread_id,
        "process_uuid": process_uuid, "submission_id": submission_id,
        "receipt_seqs": receipt_seqs,
        "model_id_observed": model_id_observed, "model_label_ui": model_label_ui,
        "modality": modality, "reasoning_mode": reasoning_mode,
        "target_configuration_sha256": target_configuration_sha256,
        "condition": trial["condition"], "block": trial["block"], "factors": trial["factors"],
        "prime_index": trial["prime_index"], "prime": trial["prime"],
        "expected_answer": trial["expected_answer"],
        "call_session_id": session_id, "stream_stage": stage,
        "session_id":session_id, "stage":stage,
        "session_stage_source": "argument",
        "prompt": trial["prompt"], "prompt_sha256_utf8": trial["prompt_sha256_utf8"],
        "reply_file_sha256": reply_file_sha256, "triad": triad,
        "raw_reply_audit": scan_response(reply, triad["O"]["text"], known_context),
        "task_reply_audit": scan_response(task_reply, triad["O"]["text"], known_context),
        "math_header": math_header,
        "task_line_number_offset": math_header["removed_lines"],
        "manual_task_success": success, "manual_substantive_checking": checking,
        "manual_previous_checking": previous_checking,
        "previous_checking":previous_checking, "checking":checking, "success":success,
        "previous_response_id": previous_response_id, "checking_label_source": "argument",
        "context_timing_source": "argument",
    }
    with Path(path).open("ab") as output:
        output.write(json_line(record))
        output.flush()
        os.fsync(output.fileno())
    return record


def outcome_metrics(outcome):
    audit = outcome["task_reply_audit"]
    return {
        "manual_substantive_checking": outcome["manual_substantive_checking"],
        "manual_task_success": outcome["manual_task_success"],
        "checking_task_prefix": audit["preamble"]["checking_prefix"],
        "checking_word_present": audit["preamble"]["checking_word_present"],
        "strict_any": audit["strict"]["matched_categories"] > 0,
        "broad_any": audit["broad"]["matched_categories"] > 0,
    }


def factorial_contrasts(cells):
    """Equal-weight contrasts; negative means the measured outcome decreased."""
    a, b, c, d = (cells[code] for code in "ABCD")
    return {"geometry": ((b - a) + (d - c)) / 2,
            "response_rules": ((c - a) + (d - b)) / 2,
            "interaction": d - b - c + a}


def binomial_rate(positive, total):
    if total == 0:
        return {"positive": positive, "total": total, "rate": None,
                "wilson_95": [None, None]}
    rate, z = positive / total, 1.959963984540054
    denominator = 1 + z * z / total
    center = (rate + z * z / (2 * total)) / denominator
    width = z * sqrt(rate * (1 - rate) / total + z * z / (4 * total * total)) / denominator
    return {"positive": positive, "total": total, "rate": rate,
            "wilson_95": [max(0.0, center - width), min(1.0, center + width)]}


def checking_transitions(outcomes):
    counts = [[0, 0], [0, 0]]
    excluded = 0
    for row in outcomes:
        previous = row.get("manual_previous_checking")
        current = row.get("manual_substantive_checking")
        if previous is None or current is None:
            excluded += 1
        else:
            counts[int(previous)][int(current)] += 1
    rates = [binomial_rate(row[1], sum(row)) for row in counts]
    p0, p1 = (row["rate"] for row in rates)
    persistence = p1 - p0 if p0 is not None and p1 is not None else None
    stationary = p0 / (1 - persistence) if persistence is not None and persistence != 1 else None
    return {"state_order": [0, 1], "counts": counts,
            "pairs": sum(map(sum, counts)), "excluded_unknown_labels": excluded,
            "P_next_checking_by_previous": rates,
            "T": [[1 - p, p] if p is not None else [None, None] for p in (p0, p1)],
            "Lambda": persistence, "stationary_checking": stationary}


def report_study(path):
    header, trials, outcomes = load_study(path)
    metric_names = ("manual_substantive_checking", "manual_task_success",
                    "checking_task_prefix", "checking_word_present", "strict_any", "broad_any")
    cells = {}
    for code in CONDITIONS:
        observed = [outcomes[key] for key, trial in trials.items()
                    if trial["condition"] == code and key in outcomes]
        rates = {}
        for name in metric_names:
            values = [outcome_metrics(row)[name] for row in observed
                      if outcome_metrics(row)[name] is not None]
            rates[name] = {"labeled": len(values), "unknown": len(observed) - len(values),
                           "rate": sum(values) / len(values) if values else None}
        cells[code] = {"planned": header["blocks"], "recorded": len(observed), "rates": rates}
        cells[code]["checking_transitions"] = checking_transitions(observed)
    baseline = cells["A"]["checking_transitions"]
    for cell in cells.values():
        transitions = cell["checking_transitions"]
        p1 = transitions["P_next_checking_by_previous"][1]["rate"]
        p1_baseline = baseline["P_next_checking_by_previous"][1]["rate"]
        transitions["Delta_p11_vs_A"] = (p1 - p1_baseline
                                         if p1 is not None and p1_baseline is not None else None)
        transitions["Delta_Lambda_vs_A"] = (transitions["Lambda"] - baseline["Lambda"]
                                            if transitions["Lambda"] is not None
                                            and baseline["Lambda"] is not None else None)
    effects = {}
    for name in metric_names:
        contrasts = []
        for block in range(1, header["blocks"] + 1):
            group = [trial for trial in trials.values() if trial["block"] == block]
            if any(trial["trial_id"] not in outcomes for trial in group):
                continue
            values = {trial["condition"]: outcome_metrics(outcomes[trial["trial_id"]])[name]
                      for trial in group}
            if any(value is None for value in values.values()):
                continue
            contrasts.append(factorial_contrasts(values))
        effects[name] = {
            "complete_labeled_blocks": len(contrasts),
            "excluded_blocks": header["blocks"] - len(contrasts),
            "contrasts": ({key: sum(row[key] for row in contrasts) / len(contrasts)
                           for key in ("geometry", "response_rules", "interaction")}
                          if contrasts else None),
        }
    return {
        **report_header(), "definitions": dict(TRANSITION_DEFINITIONS),
        "study_id": header["study_id"], "layer": "STATISTICS",
        "study_program_sha256": header["software_sha256"],
        "target_configuration": header.get("target_configuration"),
        "target_configuration_sha256": header.get("target_configuration_sha256"),
        "planned": len(trials), "recorded": len(outcomes),
        "pending_trial_ids": [key for key in trials if key not in outcomes],
        "conditions": cells, "factorial_effects": effects, "Delta": effects,
        "geometry_headers_unrecognized": sum(
            row["math_header"]["status"] == "not_recognized" for row in outcomes.values()),
        "eligible_observed_contexts": sum(
            row["triad"]["L"]["observed_context_predictor_eligible"] for row in outcomes.values()),
    }


# This section is assembled into the standalone DROP_IT.py deliverable.
import ast
import difflib
import sqlite3
import time
from collections import Counter
from contextlib import contextmanager

WRAPPER_QUERY = "Based on the transcript, provide the assistant response to the latest user turn."
CANARY_PATTERN = re.compile(r"\bOZCANARY-[A-Fa-f0-9]{6,64}\b")
TRACE_SCHEMA = "drop-it-receipts/1.0"
TRACE_EXTENSIONS = {".txt", ".md", ".json", ".jsonl", ".ndjson", ".log", ".srt", ".sse",
                    ".har", ".py", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx",
                    ".html", ".xml", ".toml", ".yaml", ".yml", ".map"}
TRACE_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv",
                   "plot_dependencies", "dependencies", "Cache", "Code Cache", "GPUCache"}
FIELD_GROUPS = {
    "identifiers": {"id", "request_id", "requestId", "conversation_id", "conversationId",
                    "thread_id", "threadId", "turn_id", "turnId", "response_id", "responseId",
                    "item_id", "itemId", "trace_id", "traceId", "parent_id", "parentId",
                    "submission_id", "submissionId"},
    "models": {"model", "model_id", "modelId", "model_slug", "default_model_slug", "engine", "engine_id"},
    "routes": {"endpoint", "route", "route_name", "url", "method", "path"},
    "event_types": {"event", "event_type", "eventType", "type", "item_type"},
    "source_timestamps": {"timestamp", "time", "ts", "ts_nanos", "created_at", "created_at_ms",
                          "create_time", "startedDateTime", "started_at", "completed_at"},
    "processes": {"pid", "process_id", "process_uuid", "process_name", "executable"},
    "components": {"component", "component_id", "component_name", "module", "module_path",
                   "module_name", "function", "function_name", "target"},
    "owners": {"owner", "implementation_owner", "author", "publisher", "PublisherDisplayName"},
    "streams": {"stream", "stage", "channel", "role", "ui_state", "ui_label", "status"},
    "source_locations": {"file", "filename", "line", "line_number", "source_file", "source_line"},
    "code_fields": {"code"}, "claim_fields": {"claim", "INFERRED_ROLE"},
}


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                      allow_nan=False).encode("utf-8")


@contextmanager
def receipt_lock(path):
    lock_path = Path(str(path) + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+b") as handle:
        handle.seek(0, 2)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def receipt_rows(path):
    target = Path(path)
    if not target.exists():
        return []
    data = target.read_bytes()
    if data and not data.endswith(b"\n"):
        raise ValueError("receipt log has an incomplete final record")
    rows = [json.loads(line) for line in data.splitlines()]
    previous = None
    for seq, row in enumerate(rows, 1):
        core = {key: value for key, value in row.items() if key != "receipt_sha256"}
        if row.get("schema") != TRACE_SCHEMA or row.get("local_seq") != seq:
            raise ValueError("receipt schema or sequence mismatch")
        if row.get("previous_receipt_sha256") != previous:
            raise ValueError("receipt chain mismatch")
        if hashlib.sha256(canonical_bytes(core)).hexdigest() != row.get("receipt_sha256"):
            raise ValueError("receipt checksum mismatch")
        previous = row["receipt_sha256"]
    return rows


class ReceiptLog:
    def __init__(self, path):
        self.path = Path(path)
        self.blob_dir = Path(str(self.path) + ".blobs")

    def __enter__(self):
        self._lock = receipt_lock(self.path)
        self._lock.__enter__()
        try:
            self.rows = receipt_rows(self.path)
            self.seq = len(self.rows)
            self.previous = self.rows[-1]["receipt_sha256"] if self.rows else None
            self.software_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
            self.blob_dir.mkdir(parents=True, exist_ok=True)
            self.handle = self.path.open("ab")
            return self
        except BaseException:
            self._lock.__exit__(*sys.exc_info())
            raise

    def __exit__(self, *args):
        self.handle.close()
        self._lock.__exit__(*args)

    def add(self, kind, raw, **fields):
        if not isinstance(raw, bytes):
            raise TypeError("raw must be bytes")
        if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != self.software_sha256:
            raise ValueError("collector source changed while log was open")
        if set(fields) & {"schema", "local_seq", "previous_receipt_sha256", "receipt_sha256",
                          "payload_sha256", "payload_bytes", "kind", "captured_at_unix_ns",
                          "captured_at_utc", "collector_monotonic_ns", "collector_pid",
                          "collector_version", "collector_software_sha256"}:
            raise ValueError("reserved receipt field")
        if set(fields) & {"program_version", "program_sha256", "parent_program_sha256",
                          "generated_at_utc", "collection_timestamp_ns"}:
            raise ValueError("reserved report binding field")
        digest = hashlib.sha256(raw).hexdigest()
        blob = self.blob_dir / digest
        try:
            with blob.open("xb") as output:
                output.write(raw)
                output.flush()
                os.fsync(output.fileno())
        except FileExistsError:
            if hashlib.sha256(blob.read_bytes()).hexdigest() != digest:
                raise ValueError("stored payload checksum mismatch")
        captured_ns = time.time_ns()
        seconds, nanos = divmod(captured_ns, 1_000_000_000)
        captured_utc = datetime.fromtimestamp(seconds, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + f".{nanos:09d}Z"
        row = {
            **report_header(),
            "schema": TRACE_SCHEMA, "local_seq": self.seq + 1,
            "collection_timestamp_ns":captured_ns,
            "kind": kind, "captured_at_unix_ns": captured_ns,
            "captured_at_utc": captured_utc, "collector_monotonic_ns": time.monotonic_ns(),
            "collector_pid": os.getpid(), "previous_receipt_sha256": self.previous,
            "collector_version": VERSION, "collector_software_sha256": self.software_sha256,
            "payload_sha256": digest, "payload_bytes": len(raw),
            "event": None, "code": None, "claim": None, "implementation_owner": None,
            "OBSERVED_NAME": None, "INFERRED_ROLE": None,
            **fields,
        }
        row["receipt_sha256"] = hashlib.sha256(canonical_bytes(row)).hexdigest()
        self.handle.write(json_line(row))
        self.handle.flush()
        os.fsync(self.handle.fileno())
        self.seq += 1
        self.previous = row["receipt_sha256"]
        self.rows.append(row)
        return row

    def capture(self, raw, stream=None, metadata=None, decoded_payload=None,
                decoded_source=None, request=None, condition=None, prime_index=None,
                metadata_source_sha256=None, stage=None, trial_id=None, **fields):
        received_ns, received_monotonic_ns = time.time_ns(), time.monotonic_ns()
        data, valid = decode_json(raw)
        if decoded_source is not None:
            data = decoded_payload
        observed = observed_fields(data)
        if isinstance(data, dict) and isinstance(data.get("feedback_log_body"), str):
            body = data["feedback_log_body"]
            for pattern, group, field in (
                (r'Submission \{ id: "([^"\r\n]+)"', "identifiers", "submission_id"),
                (r'\bop: ([A-Za-z_][A-Za-z_0-9]*)', "event_types", "op"),
            ):
                match = re.search(pattern, body)
                if match:
                    observed[group].append({"json_path":"/feedback_log_body", "field":field,
                                            "value":match[1], "char_offset":match.start(1),
                                            "extraction":"literal_debug_field"})
        supplied = observed_fields(metadata) if metadata is not None else None
        stream_source = "argument" if stream is not None else None
        stage_source = "argument" if stage is not None else None
        if stage is None and isinstance(data, dict) and isinstance(data.get("stage"), str):
            stage, stage_source = data["stage"], "payload/stage"
        if stream is None and isinstance(data, dict):
            for key in ("stream", "stage"):
                if isinstance(data.get(key), str):
                    stream, stream_source = data[key], "payload/" + key
                    break
        text = raw.decode("utf-8", errors="replace")
        names = [{"OBSERVED_NAME": item["value"], "INFERRED_ROLE": None,
                  "json_path": item["json_path"], "field": item["field"], "source": decoded_source or "payload"}
                 for item in observed["components"] if isinstance(item["value"], str)]
        text_values = observed_text(data) if data is not None else [("", text)]
        features = []
        delta_fragments = []
        for pointer, value in text_values:
            measured = scan_response(value, request)
            features.append({"json_path": pointer, "text_sha256": sha256_text(value),
                             "feature_vector": measured["feature_vector"], "flags": measured["flags"],
                             "preamble": measured["preamble"], "A_intro": measured["A_intro"]})
            if "delta" in pointer.split("/"):
                delta_fragments.append({"json_path": pointer, "text": value})
        if condition is not None and condition not in CONDITIONS:
            raise ValueError("invalid condition")
        phase_state = geometry(prime_at(prime_index)) if prime_index is not None else None
        if metadata is not None and metadata_source_sha256 is None:
            metadata_source_sha256 = self.add(
                "supplied_metadata", canonical_bytes(metadata),
                payload_encoding="json_value_reencoded")["payload_sha256"]
        return self.add(
            "event", raw, stream=stream, stream_source=stream_source,
            stage=stage, stage_source=stage_source, trial_id=trial_id,
            event=observed["event_types"], code=observed["code_fields"], claim=observed["claim_fields"],
            implementation_owner=one_observed(observed["owners"], {"implementation_owner"}),
            response_id=one_id(observed, "response"), item_id=one_id(observed, "item"),
            thread_id=one_id(observed, "thread"), submission_id=one_id(observed, "submission"),
            process_uuid=one_observed(observed["processes"], {"process_uuid"}),
            source_timestamp=observed["source_timestamps"],
            received_at_unix_ns=received_ns, received_monotonic_ns=received_monotonic_ns,
            metadata_observed=observed, metadata_supplied=supplied,
            metadata_source_sha256=metadata_source_sha256, request=text_record(request),
            json_valid=valid, decoded_source=decoded_source,
            condition=condition, phase_state=phase_state,
            text_features=features, text_feature_scope="payload_text_fields",
            delta_fragments=delta_fragments, Delta=None,
            wrapper_matches=wrapper_matches(text),
            canaries=sorted(set(CANARY_PATTERN.findall(text))),
            ui_label_matches=ui_labels(text), observed_names=names,
            OBSERVED_NAME=names[0]["OBSERVED_NAME"] if len(names) == 1 else None,
            INFERRED_ROLE=None, **fields)


def decode_json(raw):
    try:
        # Decimal lexemes are retained as strings; original bytes are stored separately.
        return json.loads(raw.decode("utf-8-sig"), parse_float=str), True
    except (UnicodeError, ValueError):
        return None, False


def one_observed(items, names):
    values = [item["value"] for item in items if item["field"] in names and item["value"] is not None]
    unique = {canonical_bytes(value):value for value in values}
    return next(iter(unique.values())) if len(unique) == 1 else None


def one_id(observed, category):
    items = observed["identifiers"]
    names = {category + "_id", category + "Id"}
    selected = [item for item in items if item["field"] in names or
                (item["field"] == "id" and item["json_path"].endswith("/" + category + "/id"))]
    return one_observed(selected, names | {"id"})


def observed_fields(value):
    result = {group: [] for group in FIELD_GROUPS}
    result["headers"] = []
    def walk(node, pointer=""):
        if isinstance(node, dict):
            for key, item in node.items():
                location = pointer + "/" + str(key).replace("~", "~0").replace("/", "~1")
                if isinstance(item, (str, int, float, bool)) or item is None:
                    for group, names in FIELD_GROUPS.items():
                        if key in names:
                            result[group].append({"json_path": location, "field": key, "value": item})
                if key.lower() in ("headers", "request_headers", "response_headers"):
                    entries = (list(item.items()) if isinstance(item, dict) else
                               [(entry.get("name"), entry.get("value")) for entry in item
                                if isinstance(entry, dict)] if isinstance(item, list) else [])
                    for name, header_value in entries:
                        if not isinstance(name, str) or not isinstance(header_value, (str, int, float)):
                            continue
                        header_text = str(header_value)
                        sensitive = bool(re.search(r"authorization|cookie|token|secret|api[-_]?key", name, re.I))
                        result["headers"].append({
                            "json_path": location, "name": name,
                            "value": None if sensitive else header_value,
                            "value_sha256": sha256_text(header_text),
                            "value_bytes": len(header_text.encode("utf-8")),
                        })
                if isinstance(item, (dict, list)):
                    walk(item, location)
        elif isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, pointer + "/" + str(index))
    walk(value)
    return result


def observed_text(value):
    values = []
    def walk(node, pointer="", textual=False):
        if isinstance(node, str) and textual:
            values.append((pointer, node))
        elif isinstance(node, dict):
            for key, item in node.items():
                walk(item, pointer + "/" + str(key).replace("~","~0").replace("/","~1"),
                     key in {"text", "transcript", "delta", "output_text", "prompt", "instructions",
                             "parts", "content", "feedback_log_body"})
        elif isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, pointer + "/" + str(index), textual)
    walk(value, textual=isinstance(value, str))
    return values


def wrapper_matches(text, query=WRAPPER_QUERY):
    if not query.strip():
        raise ValueError("query must be nonempty")
    literal = re.compile(re.escape(query), re.I)
    matches = []
    spans = []
    for found in literal.finditer(text):
        spans.append(found.span())
        matches.append({"match_type": "exact", "similarity": 1.0, "char_offset": found.start(),
                        "byte_offset_utf8": len(text[:found.start()].encode("utf-8")),
                        "line": text.count("\n", 0, found.start()) + 1, "text": found[0]})
    if query != WRAPPER_QUERY:
        return matches
    fuzzy = re.compile(r"(?:based\s+on|using|given|from)\b[^.!?]{0,100}transcript\b"
                       r"[^.!?]{0,180}(?:latest|last|most\s+recent)\s+user\s+(?:turn|message)[.!?]?", re.I)
    for found in fuzzy.finditer(text):
        if any(found.start() < end and found.end() > start for start, end in spans):
            continue
        normalized = lambda s: " ".join(re.findall(r"\w+", s.casefold()))
        similarity = difflib.SequenceMatcher(None, normalized(query), normalized(found[0])).ratio()
        if similarity >= 0.60:
            matches.append({"match_type": "fuzzy", "similarity": similarity, "char_offset": found.start(),
                            "byte_offset_utf8": len(text[:found.start()].encode("utf-8")),
                            "line": text.count("\n", 0, found.start()) + 1, "text": found[0]})
    return sorted(matches, key=lambda item: item["char_offset"])


def ui_labels(text):
    patterns = {"checking": r"\bChecking\b", "preamble": r"\bpreamble\b",
                "thinking": r"\bthinking\b", "worked_for": r"\bWorked for [^\r\n<]{1,50}",
                "show_more": r"\bShow more\b"}
    return {label: [match[0] for match in re.finditer(pattern, text, re.I)]
            for label, pattern in patterns.items()}


def import_capture(writer, path, format_name="auto", stream=None, metadata=None,
                   request=None, condition=None, prime_index=None, metadata_source_sha256=None,
                   stage=None, trial_id=None):
    source = str(path)
    if source == "-":
        if format_name not in ("jsonl", "sse"):
            raise ValueError("stdin requires --format jsonl or sse")
        handle, close = sys.stdin.buffer, False
    else:
        target = Path(path)
        if format_name == "auto":
            format_name = {".jsonl": "jsonl", ".ndjson": "jsonl", ".sse": "sse",
                           ".json": "json", ".har": "har", ".srt": "srt"}.get(target.suffix.lower(), "text")
        raw = target.read_bytes()
        parent = writer.add("source_file", raw, source_path=str(target.resolve()), source_format=format_name)
        import io
        handle, close = io.BytesIO(raw), True
    parent_hash = parent["payload_sha256"] if source != "-" else None
    if metadata is not None and metadata_source_sha256 is None:
        metadata_source_sha256 = writer.add(
            "supplied_metadata", canonical_bytes(metadata),
            payload_encoding="json_value_reencoded")["payload_sha256"]
    count = 0
    def emit(raw, **extra):
        nonlocal count
        count += 1
        return writer.capture(raw, stream=stream, metadata=metadata, request=request,
                              stage=stage, trial_id=trial_id,
                              condition=condition, prime_index=prime_index, source_path=source,
                              metadata_source_sha256=metadata_source_sha256,
                              source_index=count, source_payload_sha256=parent_hash,
                              capture_mode="stdin" if source == "-" else "file_import", **extra)
    try:
        if format_name == "jsonl":
            for line_number, raw_line in enumerate(handle, 1):
                if raw_line.strip():
                    emit(raw_line, source_line=line_number)
        elif format_name == "sse":
            packet = []
            def emit_sse(lines):
                raw_event = b"".join(lines)
                values = {}
                data_lines = []
                for line in lines:
                    clean = line.rstrip(b"\r\n")
                    key, _, value = clean.partition(b":")
                    value = value[1:] if value.startswith(b" ") else value
                    if key == b"data":
                        data_lines.append(value)
                    elif key in (b"event", b"id"):
                        values[key.decode()] = value.decode("utf-8", "replace")
                data_raw = b"\n".join(data_lines)
                decoded, valid = decode_json(data_raw)
                if not valid:
                    decoded = data_raw.decode("utf-8", "replace")
                emit(raw_event, decoded_payload=decoded, decoded_source="sse_data",
                     sse_fields=values, sse_data_json_valid=valid,
                     sse_terminated=bool(lines and not lines[-1].strip()),
                     sse_data_sha256=hashlib.sha256(data_raw).hexdigest())
            for raw_line in handle:
                packet.append(raw_line)
                if not raw_line.strip():
                    if any(line.strip() for line in packet):
                        emit_sse(packet)
                    packet = []
            if any(line.strip() for line in packet):
                emit_sse(packet)
        elif format_name in ("json", "har"):
            raw = handle.read()
            data, valid = decode_json(raw)
            if not valid:
                raise ValueError("input JSON could not be decoded")
            if format_name == "har":
                items = data["log"]["entries"]
                prefix = "/log/entries/"
            else:
                items = data if isinstance(data, list) else [data]
                prefix = "/" if isinstance(data, list) else ""
            for index, item in enumerate(items):
                emit(canonical_bytes(item), source_json_path=prefix + str(index) if prefix else "",
                     payload_encoding="json_value_reencoded")
        elif format_name == "srt":
            raw = handle.read()
            text = raw.decode("utf-8-sig")
            pattern = re.compile(r"(?m)^[ \t]*(\d+)[ \t]*\r?\n(\d{2}:\d{2}:\d{2}[,.]\d{3})[ \t]*-->[ \t]*(\d{2}:\d{2}:\d{2}[,.]\d{3})[^\r\n]*\r?\n")
            starts = list(pattern.finditer(text))
            for index, found in enumerate(starts):
                end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
                block = re.split(r"\r?\n[ \t]*\r?\n", text[found.start():end], maxsplit=1)[0]
                emit(block.encode("utf-8"), source_srt_index=int(found[1]),
                     source_timebase="srt", source_start=found[2], source_end=found[3],
                     payload_encoding="utf8_text_slice")
        else:
            emit(handle.read(), payload_encoding="source_bytes")
    finally:
        if close:
            handle.close()
    return {"source": source, "format": format_name, "events_added": count, "last_local_seq": writer.seq}


def source_context(path, text, matches):
    functions = []
    if Path(path).suffix == ".py":
        try:
            tree = ast.parse(text)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    functions.append((node.lineno, node.end_lineno, node.name, type(node).__name__))
        except (SyntaxError, ValueError):
            pass
    result = []
    for match in matches:
        start = max(0, match["char_offset"] - 160)
        end = min(len(text), match["char_offset"] + len(match["text"]) + 320)
        enclosing = [item for item in functions if item[0] <= match["line"] <= item[1]]
        enclosing.sort(key=lambda item: item[1] - item[0])
        result.append({**match, "excerpt": text[start:end],
                       "source_symbols": [{"name": item[2], "kind": item[3],
                                           "start_line": item[0], "end_line": item[1]} for item in enclosing]})
    return result


def search_sources(writer, roots, query=WRAPPER_QUERY, max_bytes=64 * 1024 * 1024):
    seen, summary = set(), Counter()
    match_files = []
    excluded = {Path(__file__).resolve(), writer.path.resolve()}
    def walk_paths(root):
        if root.is_file():
            yield root
        else:
            for folder, dirs, names in os.walk(root, followlinks=False):
                dirs[:] = [d for d in dirs if d not in TRACE_SKIP_DIRS and not d.endswith(".blobs")]
                for name in names:
                    yield Path(folder) / name
    for root in roots:
        root = Path(root)
        if not root.exists():
            summary["missing_roots"] += 1
            continue
        for path in walk_paths(root):
            try:
                resolved = path.resolve()
                if path.is_symlink() or resolved in seen or resolved in excluded or path.suffix.lower() not in TRACE_EXTENSIONS:
                    summary["excluded_files"] += 1
                    continue
                seen.add(resolved)
                if path.stat().st_size > max_bytes:
                    summary["over_size_limit"] += 1
                    continue
                raw = path.read_bytes()
                utf16 = raw.startswith((b"\xff\xfe", b"\xfe\xff"))
                if not utf16 and b"\0" in raw[:4096]:
                    summary["binary_files"] += 1
                    continue
                encoding = "utf-16" if utf16 else "utf-8-sig"
                text = raw.decode(encoding, errors="replace")
                summary["files_scanned"] += 1
                matches = wrapper_matches(text, query)
                if matches:
                    row = writer.add("source_match", raw, source_path=str(resolved),
                                     source_encoding=encoding,
                                     source_mtime_ns=path.stat().st_mtime_ns,
                                     wrapper_matches=source_context(path, text, matches),
                                     source_metadata=observed_fields(decode_json(raw)[0]))
                    summary["matched_files"] += 1
                    summary["exact_matches"] += sum(item["match_type"] == "exact" for item in matches)
                    summary["fuzzy_matches"] += sum(item["match_type"] == "fuzzy" for item in matches)
                    match_files.append({"source_path": str(resolved), "local_seq": row["local_seq"],
                                        "sha256": row["payload_sha256"], "matches": len(matches)})
            except OSError as exc:
                summary["read_errors"] += 1
                writer.add("read_error", canonical_bytes({"path": str(path), "errno": exc.errno}),
                           source_path=str(path), errno=exc.errno)
    result = {"roots": [str(Path(root)) for root in roots], "query": query,
              "counts": dict(summary), "files": match_files}
    writer.add("search_summary", canonical_bytes(result), measurements=result)
    return result


def capture_sqlite(writer, path, contains, stream=None, exclude_thread=None):
    conn = sqlite3.connect(Path(path).resolve().as_uri() + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    conn.execute("BEGIN")
    try:
        query = "SELECT * FROM logs WHERE instr(lower(feedback_log_body),lower(?))>0"
        params = [contains]
        if exclude_thread:
            query += " AND (thread_id IS NULL OR thread_id<>?)"
            params.append(exclude_thread)
        query += " ORDER BY id"
        maximum = conn.execute("SELECT MAX(id) FROM logs").fetchone()[0]
        count = 0
        for row in conn.execute(query, params):
            record = dict(row)
            writer.capture(canonical_bytes(record), stream=stream, source_path=str(Path(path).resolve()),
                           capture_mode="sqlite_query", source_table="logs", source_row_id=record["id"],
                           source_max_row_id=maximum, query_sha256=sha256_text(query),
                           query_sql=query, query_parameters=params, payload_encoding="sqlite_row_json")
            count += 1
        return {"database": str(path), "rows_captured": count, "source_max_row_id": maximum,
                "last_local_seq": writer.seq}
    finally:
        conn.close()


def make_canary(writer, stage, input_path=None, output_path=None, trial_id=None, field=None):
    if not stage.strip():
        raise ValueError("a stage label is required")
    if (input_path is None) != (output_path is None):
        raise ValueError("canary injection requires both --input and --output")
    if field is not None and input_path is None:
        raise ValueError("--field requires --input and --output")
    token = "OZCANARY-" + secrets.token_hex(16).upper()
    fields = {"stream": stage, "stream_source": "argument", "trial_id": trial_id, "token": token,
              "intended_stage": stage, "inserted_stage": None}
    if input_path is not None:
        source, target = Path(input_path), Path(output_path)
        if source.resolve() == target.resolve():
            raise ValueError("canary output must be a new file")
        if target.exists():
            raise FileExistsError(str(target))
        raw = source.read_bytes()
        source_row = writer.add("canary_input", raw, source_path=str(source.resolve()), **fields)
        insertion_character_offset = None
        if field is None:
            stamped = raw + (b"" if raw.endswith(b"\n") else b"\n") + token.encode("ascii") + b"\n"
            encoding = "source_bytes_with_ascii_suffix"
        else:
            document = json.loads(raw.decode("utf-8-sig"), parse_float=Decimal)
            if not field.startswith("/"):
                raise ValueError("a JSON field pointer must start with /")
            parts = [part.replace("~1", "/").replace("~0", "~") for part in field[1:].split("/")]
            node = document
            for part in parts[:-1]:
                node = node[int(part)] if isinstance(node, list) else node[part]
            key = int(parts[-1]) if isinstance(node, list) else parts[-1]
            original = node[key]
            if not isinstance(original, str):
                raise ValueError("the canary field must contain a string")
            prefix = original + ("" if original.endswith("\n") else "\n")
            insertion_character_offset = len(prefix)
            node[key] = prefix + token + "\n"
            # JSON numeric lexemes retain exact Decimal values during serialization.
            stamped = exact_json_bytes(document)
            encoding = "json_field_modified_reencoded"
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as handle:
            handle.write(stamped)
            handle.flush()
            os.fsync(handle.fileno())
        receipt = writer.add("canary_stage_copy", stamped, source_path=str(source.resolve()),
                             output_path=str(target.resolve()),
                             input_payload_sha256=source_row["payload_sha256"],
                             original_payload_hash=source_row["payload_sha256"],
                             tagged_payload_hash=hashlib.sha256(stamped).hexdigest(),
                             insertion_offset=stamped.index(token.encode("ascii")),
                             insertion_offset_units="utf8_bytes_in_tagged_payload", insertion_field=field,
                             insertion_field_character_offset=insertion_character_offset,
                             payload_encoding=encoding, insertion_status="TAGGED_COPY_CREATED",
                             token_count_before=raw.count(token.encode()),
                             token_count_after=stamped.count(token.encode()), **fields)
    else:
        receipt = writer.add("canary_created", token.encode("ascii"), original_payload_hash=None,
                             tagged_payload_hash=None, insertion_offset=None, insertion_field=None,
                             insertion_status="MINTED", **fields)
    return {**report_header(), "token": token, "stream": stage, "trial_id": trial_id,
            "local_seq": receipt["local_seq"], "sha256": receipt["payload_sha256"],
            "output_path": str(output_path) if output_path is not None else None}


def exact_json_bytes(value):
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError("nonfinite JSON number")
        return str(value).encode("ascii")
    if isinstance(value, dict):
        return b"{" + b",".join(canonical_bytes(key) + b":" + exact_json_bytes(item)
                                 for key, item in value.items()) + b"}"
    if isinstance(value, list):
        return b"[" + b",".join(exact_json_bytes(item) for item in value) + b"]"
    return canonical_bytes(value)


def joined_delta_measurements(rows):
    groups = {}
    for row in rows:
        if row["kind"] != "event" or not row.get("delta_fragments"):
            continue
        ids = [(kind + "_id", one_id(row["metadata_observed"], kind)) for kind in ("response", "item")]
        ids = [(key, str(value)) for key, value in ids if value is not None]
        if not ids:
            continue
        for fragment in row["delta_fragments"]:
            key = (row.get("stream"), row.get("stage"), row.get("trial_id"),
                   one_id(row["metadata_observed"], "thread"), tuple(ids), fragment["json_path"])
            groups.setdefault(key, []).append((row, fragment["text"]))
    result = []
    for (stream, stage, trial_id, thread_id, identifiers, pointer), pieces in groups.items():
        text = "".join(fragment for _, fragment in pieces)
        positions, offset = [], 0
        for row, fragment in pieces:
            positions.append((offset, offset + len(fragment), row["local_seq"]))
            offset += len(fragment)
        canaries = []
        for match in CANARY_PATTERN.finditer(text):
            canaries.append({"token": match[0], "char_offset": match.start(),
                             "local_seqs": [seq for start, end, seq in positions
                                            if start < match.end() and end > match.start()]})
        measured = scan_response(text)
        result.append({"stream": stream, "stage":stage, "trial_id":trial_id, "thread_id":thread_id,
                       "correlation_ids": dict(identifiers),
                       "json_path": pointer, "fragments": len(pieces),
                       "local_seqs": [row["local_seq"] for row, _ in pieces],
                       "text_sha256": sha256_text(text), "text_bytes": len(text.encode("utf-8")),
                       "feature_vector": measured["feature_vector"],
                       "preamble": measured["preamble"], "canary_matches": canaries})
    return result


def canary_stage_report(path, expected_head=None):
    validated = trace_report(path, expected_head)
    rows = receipt_rows(path)
    blobs = Path(str(path) + ".blobs")
    registry = [row for row in rows if row["kind"] in ("canary_created", "canary_stage_copy")]
    events = [row for row in rows if row["kind"] == "event"]
    table, declarations = [], []
    for declaration in registry:
        token = declaration["token"]
        encoded = token.encode("ascii")
        intended = declaration.get("intended_stage", declaration.get("stream"))
        tagged_hash = declaration.get("tagged_payload_hash")
        source_events = [event for event in events if event["payload_sha256"] == tagged_hash
                         and (event.get("stage") or event.get("stream")) == intended
                         and event.get("trial_id") == declaration.get("trial_id")]
        inserted = intended if source_events else None
        declarations.append({"trial":declaration.get("trial_id"), "token":token,
                             "intended_stage":intended, "inserted_stage":inserted,
                             "insertion_capture_receipts":[r["local_seq"] for r in source_events],
                             "original_payload_hash":declaration.get("original_payload_hash"),
                             "tagged_payload_hash":tagged_hash, "insertion_offset":declaration.get("insertion_offset"),
                             "insertion_field":declaration.get("insertion_field"),
                             "declaration_receipt_seq":declaration["local_seq"]})
        for event in events:
            if event.get("trial_id") is not None and event.get("trial_id") != declaration.get("trial_id"):
                continue
            raw = (blobs / event["payload_sha256"]).read_bytes()
            offset = raw.find(encoded)
            table.append({"trial":declaration.get("trial_id"), "token":token,
                          "inserted_stage":inserted, "observed_stage":event.get("stage") or event.get("stream"),
                          "receipt_seq":event["local_seq"], "receipt_seqs":[event["local_seq"]],
                          "response_id":event.get("response_id"), "thread_id":event.get("thread_id"),
                          "exact_match":offset >= 0, "occurrence_count":raw.count(encoded),
                          "first_offset":offset if offset >= 0 else None, "offset_units":"utf8_bytes",
                          "payload_sha256":event["payload_sha256"], "match_scope":"raw_payload"})
        for sequence in validated["delta_sequences"]:
            if sequence.get("trial_id") is not None and sequence.get("trial_id") != declaration.get("trial_id"):
                continue
            matches = [match for match in sequence["canary_matches"] if match["token"] == token]
            if not matches:
                continue
            for match in matches:
                seqs = match["local_seqs"]
                table.append({"trial":declaration.get("trial_id"), "token":token,
                              "inserted_stage":inserted, "observed_stage":sequence.get("stage") or sequence.get("stream"),
                              "receipt_seq":seqs[0] if len(seqs) == 1 else None, "receipt_seqs":seqs,
                              "response_id":sequence["correlation_ids"].get("response_id"),
                              "thread_id":sequence.get("thread_id"), "exact_match":True,
                              "occurrence_count":1, "first_offset":match["char_offset"],
                              "offset_units":"unicode_characters", "payload_sha256":None,
                              "payload_sha256s":[rows[seq-1]["payload_sha256"] for seq in seqs],
                              "joined_text_sha256":sequence["text_sha256"], "match_scope":"joined_deltas"})
    return {**report_header(), "layer":"MEASUREMENT", "canary_declarations":declarations,
            "stage_table":table, "declared_canaries":len(registry),
            "captured_insertions":sum(bool(item["insertion_capture_receipts"]) for item in declarations),
            "observed_event_payloads":len(events), "head_sha256":validated["head_sha256"],
            "expected_head_matches":validated["expected_head_matches"],
            "validation_metrics":validated["validation_metrics"]}


def trace_report(path, expected_head=None):
    rows = receipt_rows(path)
    actual_head = rows[-1]["receipt_sha256"] if rows else None
    if expected_head is not None and expected_head != actual_head:
        raise ValueError("final chain head mismatch")
    blobs = Path(str(path) + ".blobs")
    checked = set()
    for row in rows:
        digest = row["payload_sha256"]
        if digest not in checked:
            if hashlib.sha256((blobs / digest).read_bytes()).hexdigest() != digest:
                raise ValueError("payload checksum mismatch")
            checked.add(digest)
    observations = []
    canaries = []
    metadata = {group: [] for group in FIELD_GROUPS}
    metadata["headers"] = []
    supplied_metadata = {group: [] for group in metadata}
    for row in rows:
        if row["kind"] == "event":
            for group, items in row["metadata_observed"].items():
                metadata[group].extend({"local_seq": row["local_seq"], **item} for item in items)
            for group, items in (row.get("metadata_supplied") or {}).items():
                supplied_metadata[group].extend({"local_seq": row["local_seq"], **item} for item in items)
            for key, value in row.get("sse_fields", {}).items():
                group = "event_types" if key == "event" else "identifiers"
                metadata[group].append({"local_seq": row["local_seq"], "json_path": "/@sse/" + key,
                                        "field": key, "value": value})
            for item in row.get("observed_names", []):
                observations.append({"local_seq": row["local_seq"], "stream": row.get("stream"),
                                     **item, "payload_sha256": row["payload_sha256"]})
            for token in row.get("canaries", []):
                canaries.append({"token": token, "local_seq": row["local_seq"], "stream": row.get("stream"),
                                 "source_timestamps": row["metadata_observed"]["source_timestamps"],
                                 "source_path": row.get("source_path"), "payload_sha256": row["payload_sha256"]})
    return {**report_header(), "layer": "MEASUREMENT", "receipts": len(rows), "validated_payloads": len(checked),
            "expected_head_sha256": expected_head,
            "expected_head_matches": actual_head == expected_head if expected_head is not None else None,
            "sequence_first": rows[0]["local_seq"] if rows else None,
            "sequence_last": rows[-1]["local_seq"] if rows else None,
            "head_sha256": rows[-1]["receipt_sha256"] if rows else None,
            "kind_counts": dict(Counter(row["kind"] for row in rows)),
            "observed_names": observations, "metadata": metadata,
            "metadata_supplied": supplied_metadata, "canary_occurrences": canaries,
            "delta_sequences": joined_delta_measurements(rows),
            "canary_registry": [{"token": row["token"], "stream": row.get("stream"),
                                 "local_seq": row["local_seq"], "kind": row["kind"]}
                                for row in rows if row["kind"] in ("canary_created", "canary_stage_copy")],
            "validation_metrics": {"sequence_errors": 0, "chain_errors": 0, "payload_hash_errors": 0}}


def trace_main(argv):
    parser = argparse.ArgumentParser(prog="DROP_IT.py trace")
    commands = parser.add_subparsers(dest="operation", required=True)
    capture = commands.add_parser("capture")
    capture.add_argument("--input", required=True)
    capture.add_argument("--format", choices=("auto","jsonl","sse","json","har","srt","text"), default="auto")
    capture.add_argument("--stream")
    capture.add_argument("--stage")
    capture.add_argument("--trial")
    capture.add_argument("--metadata", type=Path)
    capture.add_argument("--request", type=Path)
    capture.add_argument("--condition", choices=CONDITIONS)
    capture.add_argument("--prime-index", type=int)
    capture.add_argument("--log", type=Path, required=True)
    search = commands.add_parser("search")
    search.add_argument("--root", type=Path, action="append", required=True)
    search.add_argument("--query", default=WRAPPER_QUERY)
    search.add_argument("--max-bytes", type=int, default=64*1024*1024)
    search.add_argument("--log", type=Path, required=True)
    sqlite = commands.add_parser("sqlite")
    sqlite.add_argument("--database", type=Path, required=True)
    sqlite.add_argument("--contains", default="Based on the transcript")
    sqlite.add_argument("--exclude-thread")
    sqlite.add_argument("--stream")
    sqlite.add_argument("--log", type=Path, required=True)
    canary = commands.add_parser("canary")
    canary.add_argument("--stage", required=True)
    canary.add_argument("--trial")
    canary.add_argument("--input", type=Path)
    canary.add_argument("--output", type=Path)
    canary.add_argument("--field", help="JSON pointer to the string field receiving the canary")
    canary.add_argument("--log", type=Path, required=True)
    report = commands.add_parser("report")
    report.add_argument("--log", type=Path, required=True)
    report.add_argument("--expected-head")
    stages = commands.add_parser("canary-report")
    stages.add_argument("--log", type=Path, required=True)
    stages.add_argument("--expected-head")
    args = parser.parse_args(argv)
    try:
        if args.operation == "report":
            result = trace_report(args.log, args.expected_head)
        elif args.operation == "canary-report":
            result = canary_stage_report(args.log, args.expected_head)
        else:
            with ReceiptLog(args.log) as writer:
                if args.operation == "capture":
                    metadata, metadata_sha = None, None
                    if args.metadata:
                        metadata_raw = args.metadata.read_bytes()
                        metadata, valid = decode_json(metadata_raw)
                        if not valid:
                            raise ValueError("metadata JSON could not be decoded")
                        metadata_sha = writer.add(
                            "supplied_metadata", metadata_raw,
                            source_path=str(args.metadata.resolve()),
                            payload_encoding="source_bytes")["payload_sha256"]
                    result = import_capture(writer, args.input, args.format, args.stream, metadata,
                                            read_text(args.request) if args.request else None,
                                            args.condition, args.prime_index, metadata_sha, args.stage, args.trial)
                elif args.operation == "search":
                    if args.max_bytes < 1:
                        raise ValueError("--max-bytes must be positive")
                    result = search_sources(writer, args.root, args.query, args.max_bytes)
                elif args.operation == "sqlite":
                    result = capture_sqlite(writer, args.database, args.contains, args.stream, args.exclude_thread)
                else:
                    result = make_canary(writer, args.stage, args.input, args.output, args.trial, args.field)
        print(json.dumps({**report_header(), **result}, indent=2, ensure_ascii=True))
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error) as exc:
        print(json.dumps({"error_type": type(exc).__name__, "error": str(exc)}))
        raise SystemExit(2)


def run_cli_turn(writer, configuration, prompt_bytes, trial_id, io_dir, condition=None, prime_index=None):
    import queue
    import subprocess
    import threading
    executable = Path(configuration["executable"])
    if hashlib.sha256(executable.read_bytes()).hexdigest() != configuration["executable_sha256"]:
        raise ValueError("target executable hash changed")
    config_hash = hashlib.sha256(canonical_bytes(configuration)).hexdigest()
    destination = Path(io_dir)
    destination.mkdir(parents=True, exist_ok=True)
    attempt = 1 + sum(row["kind"] == "cli_invocation" and row.get("trial_id") == trial_id for row in writer.rows)
    final_file = destination / f"{trial_id}.attempt{attempt}.reply.txt"
    if final_file.exists():
        raise FileExistsError(str(final_file))
    argv = [str(executable), *configuration["arguments"], "--output-last-message", str(final_file.resolve()), "-"]
    invocation = writer.add("cli_invocation", canonical_bytes({"argv":argv,"configuration":configuration}),
                            trial_id=trial_id, event="process_launch_requested",
                            target_configuration_sha256=config_hash, prompt_sha256=hashlib.sha256(prompt_bytes).hexdigest())
    environment = dict(os.environ)
    environment.update(configuration.get("environment", {}))
    process = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               cwd=configuration["cwd"], env=environment)
    messages = queue.Queue()
    def read_pipe(handle, stream):
        try:
            for raw in iter(handle.readline, b""):
                messages.put((stream, raw, time.time_ns(), time.monotonic_ns()))
        finally:
            handle.close()
            messages.put((stream, None, time.time_ns(), time.monotonic_ns()))
    readers = [threading.Thread(target=read_pipe, args=(handle,stream), daemon=True)
               for handle,stream in ((process.stdout,"stdout"),(process.stderr,"stderr"))]
    for reader in readers:
        reader.start()
    try:
        process.stdin.write(prompt_bytes)
        process.stdin.flush()
        process.stdin.close()
        request_receipt = writer.capture(prompt_bytes, stream="stdin", stage="cli_stdin_sent",
                                         trial_id=trial_id, condition=condition, prime_index=prime_index,
                                         capture_mode="live_process_stdin", source_pid=process.pid,
                                         invocation_receipt_seq=invocation["local_seq"],
                                         payload_encoding="source_bytes")
    except (BrokenPipeError, OSError):
        request_receipt = None
    finished, thread_ids, response_ids, model_ids, output_seqs = set(), set(), set(), set(), []
    started = time.monotonic()
    timed_out = False
    while len(finished) < 2:
        if not timed_out and time.monotonic() - started > configuration.get("timeout_seconds", 240):
            process.kill()
            timed_out = True
        try:
            stream, raw, read_ns, read_mono = messages.get(timeout=0.25)
        except queue.Empty:
            continue
        if raw is None:
            finished.add(stream)
            continue
        row = writer.capture(raw, stream=stream, stage="cli_"+stream,
                             trial_id=trial_id, condition=condition, prime_index=prime_index,
                             capture_mode="live_process_pipe", source_pid=process.pid,
                             source_read_at_unix_ns=read_ns, source_read_monotonic_ns=read_mono,
                             invocation_receipt_seq=invocation["local_seq"], payload_encoding="source_bytes")
        output_seqs.append(row["local_seq"])
        if stream == "stdout":
            if row.get("thread_id") is not None:
                thread_ids.add(row["thread_id"])
            if row.get("response_id") is not None:
                response_ids.add(row["response_id"])
            for item in row["metadata_observed"]["models"]:
                if item["value"] is not None:
                    model_ids.add(str(item["value"]))
    exit_code = process.wait()
    for reader in readers:
        reader.join(timeout=1)
    reply = final_file.read_bytes() if final_file.exists() else None
    final_receipt = (writer.capture(reply, stream="file", stage="cli_last_message_file", trial_id=trial_id,
                                   condition=condition, prime_index=prime_index, source_path=str(final_file.resolve()),
                                   capture_mode="live_process_output_file", invocation_receipt_seq=invocation["local_seq"],
                                   source_pid=process.pid, payload_encoding="source_bytes")
                     if reply is not None else None)
    record = {"trial_id":trial_id,"exit_code":exit_code,"timed_out":timed_out,
              "reply_file":str(final_file),"reply_sha256":hashlib.sha256(reply).hexdigest() if reply is not None else None,
              "thread_id":next(iter(thread_ids)) if len(thread_ids)==1 else None,
              "response_id":next(iter(response_ids)) if len(response_ids)==1 else None,
              "model_id_observed":next(iter(model_ids)) if len(model_ids)==1 else None,
              "model_ids_observed":sorted(model_ids),"model_label_ui":None,
              "request_receipt_seq":request_receipt["local_seq"] if request_receipt else None,
              "output_receipt_seqs":output_seqs,
              "final_receipt_seq":final_receipt["local_seq"] if final_receipt else None,
              "target_configuration_sha256":config_hash}
    writer.add("cli_result", canonical_bytes(record), trial_id=trial_id, event="process_exit", measurements=record)
    return record


def pilot_main(argv):
    parser = argparse.ArgumentParser(prog="DROP_IT_v4.1.py pilot")
    parser.add_argument("--study", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--io-dir", type=Path, required=True)
    parser.add_argument("--probe-only", action="store_true")
    args = parser.parse_args(argv)
    try:
        header, trials, outcomes = load_study(args.study)
        if header["software_sha256"] != report_header()["program_sha256"]:
            raise ValueError("pilot program hash differs from frozen study")
        configuration = header["target_configuration"]
        if not configuration or hashlib.sha256(canonical_bytes(configuration)).hexdigest() != header["target_configuration_sha256"]:
            raise ValueError("pilot target configuration mismatch")
        with ReceiptLog(args.log) as writer:
            if args.probe_only:
                prior = [row for row in writer.rows if row["kind"]=="canary_stage_copy" and row.get("trial_id")=="CANARY-PROBE-001"]
                if prior:
                    prompt = (writer.blob_dir / prior[0]["payload_sha256"]).read_bytes()
                else:
                    args.io_dir.mkdir(parents=True,exist_ok=True)
                    source,tagged = args.io_dir/"canary_original.txt", args.io_dir/"canary_tagged.txt"
                    with source.open("xb") as handle:
                        handle.write(b"Repeat the final line of this message exactly.\n")
                    make_canary(writer,"cli_stdin_sent",source,tagged,"CANARY-PROBE-001")
                    prompt = tagged.read_bytes()
                result = run_cli_turn(writer,configuration,prompt,"CANARY-PROBE-001",args.io_dir)
                print(json.dumps({**report_header(), **result}),flush=True)
                if result["exit_code"] != 0 or result["reply_sha256"] is None:
                    raise SystemExit(3)
                return
            for trial_id, trial in trials.items():
                if trial_id in outcomes:
                    continue
                if hashlib.sha256(Path(__file__).read_bytes()).hexdigest() != header["software_sha256"]:
                    raise ValueError("pilot program changed during cohort")
                result = run_cli_turn(writer,configuration,trial["prompt"].encode("utf-8"),trial_id,args.io_dir,
                                      trial["condition"],trial["prime_index"])
                if result["exit_code"] != 0 or result["reply_sha256"] is None:
                    print(json.dumps({**report_header(), **result}),flush=True)
                    raise SystemExit(3)
                recorded_models = {row.get("model_id_observed") for row in outcomes.values()
                                   if row.get("model_id_observed") is not None}
                if (len(result["model_ids_observed"]) > 1 or
                        (recorded_models and result["model_id_observed"] is not None
                         and result["model_id_observed"] not in recorded_models)):
                    writer.add("cohort_stop",canonical_bytes(result),trial_id=trial_id,
                               event="observed_model_id_changed",observed_model_ids=sorted(recorded_models))
                    raise ValueError("exposed model identifier changed within the cohort")
                raw = Path(result["reply_file"]).read_bytes()
                outcomes[trial_id] = record_outcome(args.study,trial_id,raw.decode("utf-8-sig"),
                               stage="cli_last_message_file",reply_file_sha256=result["reply_sha256"],
                               response_id=result["response_id"],thread_id=result["thread_id"],
                               receipt_seqs=result["output_receipt_seqs"]+[result["final_receipt_seq"]],
                               model_id_observed=result["model_id_observed"],model_label_ui=None,
                               modality=configuration["modality"],reasoning_mode=configuration["reasoning_mode"],
                               target_configuration_sha256=header["target_configuration_sha256"])
                print(json.dumps({**report_header(),"trial_id":trial_id,"condition":trial["condition"],
                                  "recorded":True,"model_id_observed":result["model_id_observed"],
                                  "thread_id":result["thread_id"],"response_id":result["response_id"]}),flush=True)
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print(json.dumps({**report_header(),"error_type":type(exc).__name__,"error":str(exc)}),flush=True)
        raise SystemExit(2)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "pilot":
        pilot_main(sys.argv[2:])
        return
    if len(sys.argv) > 1 and sys.argv[1] == "trace":
        trace_main(sys.argv[2:])
        return
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=int, default=1, help="prime index, or the first prime index for --plan")
    parser.add_argument("--condition", choices=CONDITIONS, default="D", help="prompt condition; default D")
    parser.add_argument("--json", action="store_true", help="include metadata and answer keys")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--audit", type=Path, metavar="REPLY.txt", help="scan a saved reply")
    modes.add_argument("--plan", type=Path, metavar="STUDY.jsonl", help="create a randomized study log")
    modes.add_argument("--show", type=Path, metavar="STUDY.jsonl", help="print a planned trial prompt")
    modes.add_argument("--record", type=Path, metavar="STUDY.jsonl", help="append an actual reply")
    modes.add_argument("--report", type=Path, metavar="STUDY.jsonl", help="summarize recorded outcomes")
    parser.add_argument("--request", type=Path, metavar="TASK.txt", help="originating task for a prompt, plan, or paired audit")
    parser.add_argument("--context", type=Path, metavar="CONTEXT.txt", help="supplied prompt context, or context for a paired audit")
    parser.add_argument("--blocks", type=int, default=1, help="--plan only: 1..100 blocks of four trials")
    parser.add_argument("--seed", type=int, help="--plan only: reproducible condition-order seed")
    parser.add_argument("--trial", help="trial ID for --show or --record, such as T0001")
    parser.add_argument("--reply", type=Path, metavar="REPLY.txt", help="actual reply for --record")
    parser.add_argument("--session", help="user-supplied call/session ID for planning or recording")
    parser.add_argument("--stage", help="user-supplied stream/stage label for planning or recording")
    parser.add_argument("--observed-context", type=Path, metavar="CONTEXT.txt", help="--record only: a captured interaction-context excerpt")
    parser.add_argument("--context-timing", choices=("unknown", "before_response", "after_response"), default="unknown",
                        help="user-declared timing of --observed-context; unknown by default")
    parser.add_argument("--success", choices=("unknown", "yes", "no"), default="unknown",
                        help="--record only: human assessment of task completion")
    parser.add_argument("--checking", choices=("unknown", "yes", "no"), default="unknown",
                        help="--record only: human substantive-Checking label")
    parser.add_argument("--previous-checking", choices=("unknown", "yes", "no"), default="unknown",
                        help="--record only: label for the response immediately before this intervention")
    parser.add_argument("--previous-response-id", help="--record only: exposed identifier of that previous response")
    parser.add_argument("--response-id", help="--record only: exposed response identifier")
    parser.add_argument("--thread-id", help="--record only: exposed thread identifier")
    parser.add_argument("--process-uuid", help="--record only: exposed process UUID")
    parser.add_argument("--submission-id", help="--record only: exposed submission identifier")
    parser.add_argument("--source-timestamp", help="--record only: source timestamp as supplied")
    parser.add_argument("--receipt-seq", type=int, action="append", help="--record only: contributing receipt number")
    parser.add_argument("--target-configuration", type=Path, help="--plan only: frozen non-secret target configuration")
    parser.add_argument("--target-configuration-sha256", help="--record only: exact planned configuration hash")
    parser.add_argument("--model-id-observed")
    parser.add_argument("--model-label-ui")
    parser.add_argument("--modality")
    parser.add_argument("--reasoning-mode")
    args = parser.parse_args()
    try:
        if (args.trial is not None) and not (args.show or args.record):
            raise ValueError("--trial requires --show or --record")
        if (args.show or args.record) and not args.trial:
            raise ValueError("--show and --record require --trial")
        if args.record and args.reply is None:
            raise ValueError("--record requires --reply")
        if not args.record and (args.reply or args.observed_context or args.context_timing != "unknown"
                                or args.success != "unknown" or args.checking != "unknown"
                                or args.previous_checking != "unknown" or args.previous_response_id
                                or args.response_id or args.thread_id or args.process_uuid
                                or args.submission_id or args.source_timestamp or args.receipt_seq
                                or args.target_configuration_sha256 or args.model_id_observed or args.model_label_ui
                                or args.modality or args.reasoning_mode):
            raise ValueError("reply, observed-context and outcome labels require --record")
        if (args.show or args.record or args.report) and (args.request or args.context):
            raise ValueError("the task/prompt context are frozen in the plan; use --observed-context for a captured excerpt")
        if not args.plan and (args.seed is not None or args.blocks != 1):
            raise ValueError("--seed and --blocks require --plan")
        if args.target_configuration and not args.plan:
            raise ValueError("--target-configuration requires --plan")
        if (args.session or args.stage) and not (args.plan or args.record):
            raise ValueError("--session and --stage require --plan or --record")
        if (args.audit or args.plan or args.show or args.record or args.report) and args.condition != "D":
            raise ValueError("--condition is for standalone prompts; studies contain all four conditions")
        if (args.audit or args.show or args.record or args.report) and args.index != 1:
            raise ValueError("--index is for standalone prompts or study planning")
        request = read_text(args.request) if args.request else None
        context = read_text(args.context) if args.context else None
        if args.audit:
            if context is not None and request is None:
                raise ValueError("a contextual pair audit also requires --request")
            result = scan_response(read_text(args.audit), request, context)
        elif args.plan:
            result = plan_trials(args.plan, request, context, args.blocks, args.seed,
                                 args.index, args.session, args.stage,
                                 json.loads(args.target_configuration.read_bytes()) if args.target_configuration else None)
        elif args.show:
            _, trials, _ = load_study(args.show)
            if args.trial not in trials:
                raise ValueError("unknown trial ID")
            result = trials[args.trial] if args.json else trials[args.trial]["prompt"]
        elif args.record:
            raw_reply = args.reply.read_bytes()
            labels = {"unknown": None, "yes": True, "no": False}
            result = record_outcome(
                args.record, args.trial, raw_reply.decode("utf-8-sig"),
                labels[args.success], labels[args.checking], args.session, args.stage,
                read_text(args.observed_context) if args.observed_context else None,
                args.context_timing, hashlib.sha256(raw_reply).hexdigest(),
                labels[args.previous_checking], args.previous_response_id,
                args.response_id, args.thread_id, args.process_uuid, args.submission_id,
                args.source_timestamp, args.receipt_seq, args.model_id_observed, args.model_label_ui,
                args.modality, args.reasoning_mode, args.target_configuration_sha256)
            if not args.json:
                result = {**report_header(), "trial_id": result["trial_id"], "status": "RECORDED",
                          "log": str(args.record), "manual_task_success": result["manual_task_success"],
                          "manual_substantive_checking": result["manual_substantive_checking"]}
        elif args.report:
            result = report_study(args.report)
        else:
            item = drop_it(args.index, args.condition, request, context)
            result = item if args.json else item["instruction"]
    except (ValueError, OSError, KeyError, TypeError) as exc:
        parser.error(str(exc))
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if isinstance(result, str) and hasattr(sys.stdout, "buffer"):
        # Preserve the frozen prompt bytes, including line endings and final newline.
        sys.stdout.buffer.write(result.encode("utf-8"))
        sys.stdout.buffer.flush()
    else:
        print(result if isinstance(result, str) else json.dumps({**report_header(), **result}, indent=2))


# v4.2 sequential measurement protocol. The v4.1 generator/detectors above
# are retained without modification. No automatic recovery of a primary turn.
TASK_HASH_V42 = "df296fb50e69edee77fb3b9a2c583ffe865bfc71226ee236232c180db6ce59fa"
BASELINE_HEAD_V42 = "5f3db8900894dfa0331281bb817472eaad807a7b8c9fb1eb732a687cff0f9f56"
BASELINE_PACKAGE_V42 = "deb62fa112912109f2bb6f1832e2281f6d4e864cde63c23e36f3090bcfe39e9b"
GRANDPARENT_V42 = "61052c99258c2b75d19b7ee58a8e64fb5b8c74efdd74d22e99e940f54119590f"
CORE_V42 = ("floor_alpha", "phase", "geometry", "prime_at", "drop_it", "scan_response",
            "scan_lines", "unquoted_lines", "preamble_markers", "split_math_header",
            "make_canary", "canary_stage_report", "exact_json_bytes")


def file_hash_v42(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save_v42(path, value, exclusive=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb" if exclusive else "wb") as handle:
        handle.write(canonical_bytes(value))
        handle.flush()
        os.fsync(handle.fileno())
    return file_hash_v42(path)


def require_v42(ok, halt_condition, **data):
    if not ok:
        raise ValueError(json.dumps({"halt_condition": halt_condition, **data}, sort_keys=True))


def codebook_v42():
    return {
        "schema": "drop-it-preamble/4.2",
        "case_sensitive": False,
        "prose_exclusion": "v4.1 unquoted_lines; fenced code, quotations and inline code excluded",
        "scope": "leading consecutive units of eligible task prose; final reply after recognized math header removal",
        "unit_suffix_regex": r"(?:\s*[.!?,;:\u2026]+\s*|\s*[-\u2013\u2014]+\s*|\s*$)",
        "normalization": "casefold, curly apostrophe -> ASCII; each accepted regex maps to its declared normalized_form",
        "exact_match_definition": "matched token equals normalized_form after casefold/apostrophe normalization, before punctuation",
        "matching_order": "listed rule order; anchored at current cursor; stop on first unrecognized unit",
        "family_binary_definition": "one iff family occurs in the final task reply's leading marker sequence",
        "item_measurements": "each separately exposed agent_message item also measured independently; no concatenation",
        "W_checking_clause": "W01 recognizes leading Checking even when followed by a substantive clause; that clause ends the burst",
        "rules": [
            {"id":"W01","family":"W","regex":r"checking\b","normalized_form":"checking","prefix_clause":True},
            {"id":"W02","family":"W","regex":r"one\s+moment","normalized_form":"one moment"},
            {"id":"W03","family":"W","regex":r"let\s+me\s+take\s+a\s+beat","normalized_form":"let me take a beat"},
            {"id":"W04","family":"W","regex":r"lemme\s+take\s+a\s+quick\s+look","normalized_form":"lemme take a quick look"},
            {"id":"W05","family":"W","regex":r"pausing","normalized_form":"pausing"},
            {"id":"H01","family":"H","regex":r"hm{2,}","normalized_form":"hmm"},
            {"id":"H02","family":"H","regex":r"hm","normalized_form":"hm"},
            {"id":"H03","family":"H","regex":r"mh+m+","normalized_form":"mhm"},
            {"id":"H04","family":"H","regex":r"m{2,}","normalized_form":"mm"},
            {"id":"H05","family":"H","regex":r"u+h+","normalized_form":"uh"},
            {"id":"H06","family":"H","regex":r"a+h+","normalized_form":"ah"},
            {"id":"H07","family":"H","regex":r"hu+h+","normalized_form":"huh"},
            {"id":"A01","family":"A","regex":r"okay","normalized_form":"okay"},
            {"id":"A02","family":"A","regex":r"right","normalized_form":"right"},
            {"id":"A03","family":"A","regex":r"yeah","normalized_form":"yeah"},
            {"id":"A04","family":"A","regex":r"['\u2019]kay","normalized_form":"'kay"},
        ],
    }


def leading_markers_v42(text, codebook, item_ordinal=None, stage="cli_last_message_file"):
    lines = unquoted_lines(text)
    eligible = "\n".join(line for _, _, line in lines)
    units, cursor = [], 0
    suffix = codebook["unit_suffix_regex"]
    while cursor < len(eligible):
        remainder = eligible[cursor:]
        chosen = None
        for rule in codebook["rules"]:
            match = re.match("(?:" + rule["regex"] + ")", remainder, re.I)
            if not match:
                continue
            tail = re.match(suffix, remainder[match.end():])
            if tail is None and not rule.get("prefix_clause"):
                continue
            end = match.end() + (tail.end() if tail is not None else 0)
            token = match[0]
            chosen = {"family":rule["family"], "raw_text":remainder[:end],
                      "normalized_form":rule["normalized_form"],
                      "exact_match":token.casefold().replace("\u2019", "'") == rule["normalized_form"],
                      "matched_rule_id":rule["id"], "response_initial":not units,
                      "standalone_item":False, "item_ordinal":item_ordinal, "stage":stage,
                      "eligible_prose_start":cursor, "eligible_prose_end":cursor+end,
                      "matched_token":token, "prefix_clause":tail is None}
            break
        if chosen is None:
            break
        units.append(chosen)
        cursor = chosen["eligible_prose_end"]
        if chosen["prefix_clause"]:
            break
    standalone = bool(units) and not eligible[cursor:].strip()
    for unit in units:
        unit["standalone_item"] = standalone
    return {"W_n":int(any(x["family"] == "W" for x in units)),
            "H_n":int(any(x["family"] == "H" for x in units)),
            "A_n":int(any(x["family"] == "A" for x in units)),
            "leading_marker_count_n":len(units), "segmentation":units,
            "eligible_prose_sha256":sha256_text(eligible),
            "eligible_source_lines":[{"number":n,"raw_text":raw,"eligible_text":s} for n,raw,s in lines],
            "first_nonmarker_clause":eligible[cursor:]}


def plan_v42(task):
    rng, result, history = random.Random(42), [], []
    for block in range(1, 17):
        order = list("ABCD")
        rng.shuffle(order)
        for condition in order:
            generated = drop_it(block, condition, task)
            g, r = CONDITIONS[condition]
            record = {"trial_id":f"S{len(result)+1:04d}", "turn_index":len(result)+1,
                      "block":block,"condition":condition,"prime_index":block,"prime":generated["prime"],
                      "geometry_enabled":g,"response_rules_enabled":r,"phase_state":generated["state"],
                      "geometry_clock":generated["clock"],"expected_answer":generated["expected_answer"],
                      "prompt":generated["instruction"],"raw_prompt_sha256":sha256_text(generated["instruction"]),
                      "condition_prev1":history[-1] if history else None,
                      "condition_prev2":history[-2] if len(history)>1 else None,
                      "geometry_prev1":CONDITIONS[history[-1]][0] if history else None,
                      "geometry_prev2":CONDITIONS[history[-2]][0] if len(history)>1 else None,
                      "response_rules_prev1":CONDITIONS[history[-1]][1] if history else None,
                      "response_rules_prev2":CONDITIONS[history[-2]][1] if len(history)>1 else None,
                      "geometry_exposures_before_n":sum(CONDITIONS[c][0] for c in history),
                      "response_rule_exposures_before_n":sum(CONDITIONS[c][1] for c in history),
                      "condition_history_sha256":hashlib.sha256(canonical_bytes(history)).hexdigest()}
            result.append(record)
            history.append(condition)
    return result


def probability_v42(numerator, denominator):
    return {"numerator":numerator,"denominator":denominator,
            "probability":numerator/denominator if denominator else None}


def first_order_v42(records):
    counts = [[0,0],[0,0]]
    for row in records:
        if row.get("C_prev1") in (0,1) and row.get("C_n_literal") in (0,1):
            counts[row["C_prev1"]][row["C_n_literal"]] += 1
    p01, p11 = [probability_v42(row[1],sum(row)) for row in counts]
    return {"counts":counts,"p11":p11,"p01":p01,
            "Lambda":p11["probability"]-p01["probability"] if all(sum(row) for row in counts) else None}


def transitions_v42(records):
    counts = [[0]*4 for _ in range(4)]
    for row in records:
        a,b,c = row.get("C_prev2"),row.get("C_prev1"),row.get("C_n_literal")
        if a in (0,1) and b in (0,1) and c in (0,1):
            counts[2*a+b][2*b+c] += 1
    qs, matrix, matrix_cells = {}, [], []
    for i, label in enumerate(("00","01","10","11")):
        total = sum(counts[i])
        j = 2*(i%2)
        qs["q"+label] = probability_v42(counts[i][j+1],total)
        matrix.append([counts[i][k]/total if total else None if k in (j,j+1) else 0 for k in range(4)])
        # Even an empty row retains structural zeros; observed probabilities carry raw counts.
        matrix[-1] = [matrix[-1][k] if k in (j,j+1) else 0 for k in range(4)]
        matrix_cells.append([probability_v42(counts[i][k],total) if k in (j,j+1)
                             else {"structurally_possible":False,"count":0,"probability":0} for k in range(4)])
    return {"first_order":{"pooled":first_order_v42(records),
                            "by_current_condition":{c:first_order_v42([r for r in records if r["condition"]==c]) for c in "ABCD"},
                            "first_half":first_order_v42([r for r in records if r["turn_index"]<=32]),
                            "second_half":first_order_v42([r for r in records if r["turn_index"]>32])},
            "second_order":{"state_order":["00","01","10","11"],"counts":counts,
                            "q":qs,"T2":matrix,"T2_cells":matrix_cells},
            "pair_source":"explicit ordered substantive records in the verified primary thread",
            "current_condition_attribution":"condition_n; accumulating prior treatment history retained",
            "time_window_assignment":"current turn determines half; turn 33 retains previous turn 32",
            "historical_reference_only":{"p11":0.5611,"p01":0.1348,"Lambda":0.4263},
            "inference":None}


def run_structure_v42(values):
    from collections import Counter
    runs, length = [], 0
    for value in [*values,0]:
        if value == 1:
            length += 1
        elif length:
            runs.append(length)
            length = 0
    return {"total_observations":len(values),"total_positives":sum(values),
            "number_of_positive_runs":len(runs),"maximum_positive_run_length":max(runs,default=0),
            "adjacent_positive_positive_count":sum(a==b==1 for a,b in zip(values,values[1:])),
            "run_length_histogram":dict(sorted(Counter(runs).items()))}


def rates_v42(records):
    metrics = {key:[row[key] for row in records] for key in ("C_n_literal","W_n","H_n","A_n","U_n")}
    for scope in ("strict","broad"):
        for i, code in enumerate("CRJBK"):
            metrics[scope+"_"+code] = [row["feature_vector"][scope][i] for row in records]
        metrics[scope+"_any"] = [int(any(row["feature_vector"][scope])) for row in records]
    return {key:probability_v42(sum(values),len(values)) for key, values in metrics.items()}


def context_events_v42(data, raw, stream, receipt_seq):
    detected = []
    if stream == "stdout" and isinstance(data,dict):
        names = [data.get("type")]
        if isinstance(data.get("item"),dict):
            names.append(data["item"].get("type"))
        for name in names:
            if isinstance(name,str) and re.search(r"compact|truncat|summariz|history.?replace|thread.?migrat|thread.?replace",name,re.I):
                detected.append(name)
    elif stream == "stderr":
        text = raw.decode("utf-8",errors="replace")
        for line in text.splitlines():
            if re.search(r"\b(?:context (?:compaction|compacted)|history (?:truncated|replaced|truncation|replacement)|conversation summariz(?:ed|ation)|thread (?:migrated|replaced|replacement))\b",line,re.I):
                detected.append(line)
    return [{"context_state_event":name,"event_receipt_seq":receipt_seq,
             "observed_literal":name,"inferred_effect":None,"halt":True} for name in detected]


def topology_v42(rows, blob_dir, trial_id, reply, codebook, expected=None):
    local = [row for row in rows if row.get("trial_id")==trial_id]
    path, observations, context_events = [], [], []
    for row in local:
        if row["kind"] != "event":
            continue
        raw = (Path(blob_dir)/row["payload_sha256"]).read_bytes()
        data, valid = decode_json(raw)
        kind = data.get("type") if isinstance(data,dict) else None
        context_events += context_events_v42(data,raw,row.get("stream"),row["local_seq"])
        path.append({"event_receipt_seq":row["local_seq"],"stage":row.get("stage"),"stream":row.get("stream"),
                     "event_type":kind,"payload_sha256":row["payload_sha256"],
                     "collection_timestamp_ns":row.get("send_started_at_unix_ns",row.get("source_read_at_unix_ns",row["collection_timestamp_ns"])),
                     "collection_monotonic_ns":row.get("send_started_monotonic_ns",row.get("source_read_monotonic_ns",row["collector_monotonic_ns"])),
                     "source_timestamp":row.get("source_timestamp"),"thread_id":row.get("thread_id"),
                     "item_id":row.get("item_id")})
        if row.get("stream") != "stdout" or not isinstance(data,dict):
            continue
        item = data.get("item")
        if isinstance(item,dict) and item.get("type")=="agent_message":
            observations.append((row,item,kind))
    items, by_id = [], {}
    for row,item,kind in observations:
        item_id = item.get("id")
        # item.started/updated/completed share an explicit id. Different ids stay separate.
        if item_id is not None and item_id in by_id:
            current = by_id[item_id]
            require_v42(not (kind=="item.completed" and current["completed"]),"duplicate_item_completion",item_id=item_id)
        else:
            current = {"item_id":item_id,"item_ordinal":len(items)+1,"observations":[],"completed":False}
            items.append(current)
            if item_id is not None:
                by_id[item_id] = current
        current["observations"].append((row,item,kind))
        current["completed"] |= kind == "item.completed"
    measured = []
    for current in items:
        first = current["observations"][0][0]
        last,item,kind = current["observations"][-1]
        require_v42(isinstance(item.get("text"),str),"agent_item_text_unavailable",item_id=current["item_id"])
        raw = item["text"].encode("utf-8")
        final = bool(reply is not None and raw == reply and current is items[-1])
        text, header = split_math_header(item["text"],expected)
        measured.append({"item_id":current["item_id"],"item_ordinal":current["item_ordinal"],
            "event_receipt_seq":last["local_seq"],"event_receipt_seqs":[x[0]["local_seq"] for x in current["observations"]],
            "event_type":kind,"raw_item_sha256":hashlib.sha256(raw).hexdigest(),"raw_item_utf8_bytes":len(raw),
            "first_collection_timestamp_ns":first.get("source_read_at_unix_ns",first["collection_timestamp_ns"]),
            "last_collection_timestamp_ns":last.get("source_read_at_unix_ns",last["collection_timestamp_ns"]),
            "first_collection_monotonic_ns":first.get("source_read_monotonic_ns",first["collector_monotonic_ns"]),
            "last_collection_monotonic_ns":last.get("source_read_monotonic_ns",last["collector_monotonic_ns"]),
            "is_final_message_item":final,"completed":current["completed"],
            "exactly_repeated_item_text":bool(measured and measured[-1]["raw_item_sha256"]==hashlib.sha256(raw).hexdigest()),
            "previous_item_text_sha256":measured[-1]["raw_item_sha256"] if measured else None,
            "preamble":leading_markers_v42(text,codebook,current["item_ordinal"],"cli_stdout_agent_message"),
            "math_header":header,"text":item["text"]})
    request = next((x for x in path if x["stage"]=="cli_stdin_sent"),None)
    completed = [x for x in path if x["event_type"]=="turn.completed"]
    failure = [x for x in path if x["event_type"] in ("turn.failed","error")]
    start = request["collection_monotonic_ns"] if request else None
    return {"trial_id":trial_id,"agent_message_item_count_n":len(measured),"U_n":int(len(measured)>1),
            "items":measured,"ordered_event_path":path,"context_state_events":context_events,
            "turn_completed_count":len(completed),"failure_events":failure,
            "latency_to_first_agent_item_ns":measured[0]["first_collection_monotonic_ns"]-start if measured and start else None,
            "inter_agent_item_gaps_ns":[b["first_collection_monotonic_ns"]-a["last_collection_monotonic_ns"] for a,b in zip(measured,measured[1:])],
            "turn_duration_ns":completed[-1]["collection_monotonic_ns"]-start if completed and start else None,
            "request_timer_reference":"observed stdin write start",
            "cross_pipe_order":"collector observation order; no inferred total source order across stdout/stderr"}


def baseline_gate_v42(baseline):
    baseline = Path(baseline)
    require_v42(file_hash_v42(baseline/"task.txt")==TASK_HASH_V42 and (baseline/"task.txt").stat().st_size==297,"wrong_task_sha256")
    expected = {"DROP_IT_v4.1.py":PARENT_PROGRAM_SHA256,"DROP_IT_v4.0_VERIFIED.py":GRANDPARENT_V42,
                "DROP_IT_v4.1_MEASUREMENT_PACKAGE.zip":BASELINE_PACKAGE_V42}
    actual = {name:file_hash_v42(baseline/name) for name in expected}
    require_v42(actual==expected,"baseline_file_hash_mismatch",observed=actual)
    report = trace_report(baseline/"DROP_IT_RECEIPTS_NEXT.jsonl",BASELINE_HEAD_V42)
    import ast
    old = ast.parse((baseline/"DROP_IT_v4.1.py").read_bytes())
    new = ast.parse(Path(__file__).read_bytes())
    def selected(tree):
        result = {}
        for node in tree.body:
            if isinstance(node,ast.FunctionDef) and node.name in CORE_V42:
                result[node.name]=ast.dump(node)
            if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in
                    ("CONDITIONS","SIGNATURE","BROAD_EXTRA","BROAD_SIGNATURE","RESPONSE_RULES") for t in node.targets):
                result[ast.unparse(node.targets[0])]=ast.dump(node)
        return result
    require_v42(selected(old)==selected(new),"core_ast_changed")
    return {**report_header(),"file_hashes":actual,"required_task_sha256":TASK_HASH_V42,
            "task_bytes":297,"baseline_receipt_head":BASELINE_HEAD_V42,"baseline_receipts_validated":report["receipts"],
            "unchanged_core_definitions":sorted(selected(old)),"hash_gate":"PASS"}


def geometry_gate_v42(baseline):
    from fractions import Fraction
    prior = json.loads((Path(baseline)/"GEOMETRY_REVALIDATION.json").read_bytes())
    reference = Path(prior["reference_source"])
    require_v42(file_hash_v42(reference)==prior["reference_sha256"],"geometry_reference_hash_changed")
    reference_rows = json.loads(reference.read_bytes())[prior["reference_array_key"]]
    mismatches = {name:0 for name in ("theta","rho","z","bin","strand","slip")}
    oracle_errors, closure_errors = 0,0
    with localcontext() as ctx:
        ctx.prec=80
        alpha = (3-Decimal(5).sqrt())/2
        for source in reference_rows:
            n = source["n"]
            state = geometry(n)
            # Release Q(sqrt(5)) coordinates use a,b coefficients without a denominator field.
            a,b = Fraction(source["theta"]["a"]),Fraction(source["theta"]["b"])
            for name,mult,sub in (("theta",1,0),("rho",39,source["bin"]),("z",13,source["bin"]//3)):
                mismatches[name] += int((Fraction(state[name]["a"],2),Fraction(state[name]["b"],2)) != (mult*a-sub,mult*b))
            for name in ("bin","strand","slip"):
                mismatches[name] += int(state[name]!=source[name])
            theta = n*alpha-int(n*alpha)
            rho = 39*theta-int(39*theta)
            oracle_errors += int([state["bin"],state["strand"],state["slip"]] != [int(39*theta),int(39*theta)%3,int(rho<15-39*alpha)])
            closure_errors += int(lifted_step(lifted_observation(state["theta"])) != lifted_observation(geometry(n+1)["theta"]))
    require_v42(not any(mismatches.values()) and oracle_errors==closure_errors==0,"geometry_revalidation_mismatch",mismatches=mismatches)
    return {**report_header(),"states_compared":len(reference_rows),"reference_sha256":file_hash_v42(reference),
            "reference_source":str(reference),"field_mismatches":mismatches,"oracle_mismatches":oracle_errors,
            "oracle_precision_digits":80,"augmented_intertwining_mismatches":closure_errors,"clock":"n -> n+1"}


def runtime_v42(configuration):
    import platform
    import sqlite3
    import subprocess
    environment = dict(os.environ)
    environment.update(configuration["environment"])
    database = Path(environment["CODEX_HOME"])/"state_5.sqlite"
    accessible = None
    if database.exists():
        try:
            with database.open("r+b"):
                pass
            connection = sqlite3.connect(database.as_uri()+"?mode=rw",uri=True,timeout=10)
            connection.execute("PRAGMA schema_version").fetchone()
            connection.close()
            accessible = True
        except (OSError,sqlite3.Error):
            accessible = False
    version = subprocess.run([configuration["executable"],"--version"],capture_output=True,
                             env=environment,cwd=configuration["cwd"],timeout=30)
    return {"executable_path":configuration["executable"],"executable_sha256":file_hash_v42(configuration["executable"]),
            "target_configuration_sha256":hashlib.sha256(canonical_bytes(configuration)).hexdigest(),
            "sandbox_mode":"read-only","runtime_access_mode":configuration["runtime_access_mode"],
            "CODEX_HOME":environment["CODEX_HOME"],"cwd":configuration["cwd"],
            "state_database_path":str(database) if database.exists() else None,
            "state_database_accessible":accessible,"database_access_probe":"r+b file handle open without write; SQLite mode=rw; PRAGMA schema_version; no write transaction",
            "runtime_access_mode_source":"preregistered launcher exec_command sandbox_permissions=require_escalated",
            "client_version_observed":version.stdout.decode("utf-8").strip() if version.returncode==0 else None,
            "operating_system_observed":platform.platform(),"operating_system_version_observed":platform.version(),
            "model_requested":configuration["model_requested"],"reasoning_mode":configuration["reasoning_mode"],
            "modality":configuration["modality"],"service_tier":configuration["service_tier"]}


def checkpoint_v42(writer, runtime, point):
    path = runtime["state_database_path"]
    entry = {"checkpoint":point,"collection_timestamp_ns":time.time_ns(),
             "state_database_path":path,"state_database_sha256":None,"wal_sha256":None,
             "hash_scope":"separate on-disk main database and WAL byte snapshots; not an atomic logical database snapshot"}
    if path is not None and runtime["state_database_accessible"]:
        for name,suffix in (("state_database_sha256",""),("wal_sha256","-wal")):
            file = Path(path+suffix)
            if file.exists():
                started = time.time_ns()
                raw = file.read_bytes()
                entry[name] = hashlib.sha256(raw).hexdigest()
                entry[name+"_bytes"] = len(raw)
                entry[name+"_read_started_ns"] = started
                entry[name+"_read_ended_ns"] = time.time_ns()
    row = writer.add("state_database_checkpoint",canonical_bytes(entry),measurements=entry)
    return {**entry,"event_receipt_seq":row["local_seq"]}


def prepare_v42(output, baseline, help_dir):
    import shutil
    output, baseline, help_dir = Path(output).resolve(),Path(baseline).resolve(),Path(help_dir).resolve()
    gate = baseline_gate_v42(baseline)
    require_v42(not (output/"FROZEN_BINDINGS.json").exists(),"already_prepared")
    output.mkdir(parents=True,exist_ok=True)
    save_v42(output/"SOURCE_HASH_GATE_v42.json",gate,True)
    save_v42(output/"GEOMETRY_REVALIDATION_v42.json",geometry_gate_v42(baseline),True)
    task = (baseline/"task.txt").read_bytes()
    (output/"task.txt").write_bytes(task)
    prior = json.loads((baseline/"TARGET_CONFIGURATION.json").read_bytes())["target_configuration"]
    configuration = {key:prior[key] for key in ("executable","executable_sha256","environment","cwd","model_requested","reasoning_mode","modality","timeout_seconds")}
    configuration.update(service_tier="priority",sandbox_mode="read-only",runtime_access_mode="host_escalated",
                         ignore_user_config=True,approval_policy="never")
    config_hash = save_v42(output/"TARGET_CONFIGURATION_v42.json",configuration,True)
    runtime = runtime_v42(configuration)
    require_v42(runtime["executable_sha256"]==configuration["executable_sha256"],"executable_hash_changed")
    runtime_hash = save_v42(output/"RUNTIME_ENVIRONMENT.json",runtime,True)
    codebook = codebook_v42()
    codebook_hash = save_v42(output/"PREAMBLE_CODEBOOK_v42.json",codebook,True)
    plan = plan_v42(task.decode("utf-8"))
    raw_plan = b"".join(canonical_bytes(row)+b"\n" for row in plan)
    with (output/"SEQUENTIAL_PLAN.jsonl").open("xb") as handle:
        handle.write(raw_plan)
    plan_hash = hashlib.sha256(raw_plan).hexdigest()
    for name,hash_value in (("RUNTIME_ENVIRONMENT",runtime_hash),("PREAMBLE_CODEBOOK",codebook_hash),("SEQUENTIAL_PLAN",plan_hash)):
        (output/(name+"_SHA256.txt")).write_bytes((hash_value+"\n").encode())
    for name in ("RESUME_HELP.txt","EXEC_HELP.txt"):
        shutil.copyfile(help_dir/name,output/name)
    protocol = {
        **report_header(),"random_seed":42,"randomization_algorithm":"random.Random(42); list('ABCD'); shuffle once per block",
        "randomization_runtime_version":sys.version,"canonical_json":"UTF-8; ASCII escapes; sorted keys; separators comma/colon; no whitespace; no final newline",
        "canonical_plan_jsonl":"same canonical JSON per row; LF; final LF present; no outcomes appended",
        "plan_sha256":plan_hash,"preamble_codebook_sha256":codebook_hash,"planned_primary_turns":64,
        "prime_indices":list(range(1,17)),"primes":[prime_at(i) for i in range(1,17)],
        "primary_thread_strategy":"first exec persists; subsequent exec resume exact verified thread ID",
        "process_strategy":"one new CLI process per invocation; never infer an exposed process UUID from PID",
        "control_thread_strategy":"separate fresh ephemeral PRE and POST threads; no canaries in primary",
        "resume_mechanism":"codex exec --sandbox read-only resume [fixed options] THREAD_ID -",
        "resume_mechanism_documented":True,"resume_help_sha256":file_hash_v42(output/"RESUME_HELP.txt"),
        "continuity_policy":"VERIFIED required after each primary turn; PARTIAL and BROKEN halt",
        "context_policy":"explicit compaction, truncation, summarization, history replacement or thread migration/replacement halts",
        "absent_history_without_telemetry":"UNKNOWN",
        "failure_policy":"no collector retry; explicit turn failure/reconnect halts; POST skipped after primary or PRE halt",
        "geometry_reply_policy":"preserve missing/incorrect model answers as observations; only mathematical revalidation mismatches halt",
        "baseline_comparison":"MATCHED_16 blocks 1-4; same frozen task/prime/condition order; FULL_64 separately",
        "marker_scope":"final task reply; item-specific marker measurements separate",
        "condition_history_serialization":"canonical JSON array of preceding condition letters only",
        "previous_C_policy":"ordered valid substantive records only, expected same thread",
        "inference":None,"database_hash_scope":"observations; excluded from runtime fingerprint",
        "database_checkpoint_points":["before_canary_pre","after_canary_pre","at_primary_end","after_canary_post"],
        "halt_conditions":["task/source/plan/codebook/runtime/target hash change","source geometry revalidation mismatch",
             "canary PRE failure","thread continuity PARTIAL or BROKEN","explicit context state event",
             "failed/ambiguous primary turn","receipt or blob integrity failure","duplicate completed item ID",
             "unavailable agent item text","ambiguous substantive turn ordering","missing final item match",
             "observed model ID change"],
    }
    save_v42(output/"PREREGISTRATION_v42.json",protocol,True)
    names = ["task.txt","TARGET_CONFIGURATION_v42.json","RUNTIME_ENVIRONMENT.json","PREAMBLE_CODEBOOK_v42.json",
             "SEQUENTIAL_PLAN.jsonl","PREREGISTRATION_v42.json","SOURCE_HASH_GATE_v42.json","GEOMETRY_REVALIDATION_v42.json",
             "RESUME_HELP.txt","EXEC_HELP.txt"]
    bindings = {**report_header(),"baseline_directory":str(baseline),"files":{name:file_hash_v42(output/name) for name in names},
                "plan_sha256":plan_hash,"task_sha256":TASK_HASH_V42,"preamble_codebook_sha256":codebook_hash,
                "target_configuration_sha256":config_hash,"runtime_environment_sha256":runtime_hash}
    save_v42(output/"FROZEN_BINDINGS.json",bindings,True)
    for name in names+["FROZEN_BINDINGS.json"]:
        (output/name).chmod(0o444)
    print(json.dumps({"status":"PREPARED",**{key:bindings[key] for key in ("program_sha256","plan_sha256","runtime_environment_sha256","preamble_codebook_sha256")}}),flush=True)


def frozen_gate_v42(output, bindings, configuration, check_runtime=True):
    require_v42(report_header()["program_sha256"]==bindings["program_sha256"],"source_changed_after_freeze")
    for name, expected in bindings["files"].items():
        require_v42(file_hash_v42(Path(output)/name)==expected,"frozen_file_changed",file=name)
    require_v42(hashlib.sha256(canonical_bytes(configuration)).hexdigest()==bindings["target_configuration_sha256"],"target_changed")
    if check_runtime:
        observed = runtime_v42(configuration)
        require_v42(hashlib.sha256(canonical_bytes(observed)).hexdigest()==bindings["runtime_environment_sha256"],"runtime_environment_changed",observed=observed)


def arguments_v42(configuration, role, resume_thread, final_file):
    argv = [configuration["executable"],"exec","--sandbox","read-only"]
    if resume_thread is not None:
        argv.append("resume")
    elif role != "PRIMARY_SEQUENCE":
        argv.append("--ephemeral")
    argv += ["--json","--ignore-user-config","--skip-git-repo-check","--model",configuration["model_requested"],
             "-c",'model_reasoning_effort="'+configuration["reasoning_mode"]+'"',
             "-c",'service_tier="'+configuration["service_tier"]+'"',"-c",'approval_policy="never"',
             "--output-last-message",str(final_file)]
    if resume_thread is not None:
        argv.append(resume_thread)
    argv.append("-")
    return argv


def invoke_v42(writer, output, configuration, bindings, prompt, trial_id, role, resume_thread=None, trial=None):
    import queue
    import subprocess
    import threading
    frozen_gate_v42(output,bindings,configuration)
    require_v42(not any(row["kind"]=="cli_invocation" and row.get("trial_id")==trial_id for row in writer.rows),"invocation_retry_disallowed")
    destination = Path(output)/"raw_replies"
    destination.mkdir(exist_ok=True)
    final_file = destination/(trial_id+".txt")
    require_v42(not final_file.exists(),"reply_file_already_exists")
    argv = arguments_v42(configuration,role,resume_thread,final_file.resolve())
    common = {key:bindings[key] for key in ("task_sha256","plan_sha256","preamble_codebook_sha256","target_configuration_sha256","runtime_environment_sha256")}
    common.update(cohort_role=role,trial_id=trial_id)
    invocation = writer.add("cli_invocation",canonical_bytes({"argv":argv,"configuration":configuration}),
        **common,event="process_launch_requested",raw_prompt_sha256=hashlib.sha256(prompt).hexdigest(),
        thread_strategy_observed="resume_explicit_id" if resume_thread else "new_persistent" if role=="PRIMARY_SEQUENCE" else "new_ephemeral_control",
        process_strategy_observed="new_cli_process",resume_target_thread_id=resume_thread,
        resume_mechanism="codex exec resume SESSION_ID PROMPT" if resume_thread else None,
        resume_mechanism_documented=True if resume_thread else None)
    environment = dict(os.environ)
    environment.update(configuration["environment"])
    process = subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                               cwd=configuration["cwd"],env=environment)
    messages = queue.Queue()
    capture_args = dict(common,invocation_receipt_seq=invocation["local_seq"],source_pid=process.pid,
                        condition=trial["condition"] if trial else None,prime_index=trial["prime_index"] if trial else None)
    def read_pipe(handle,stream):
        try:
            for raw in iter(handle.readline,b""):
                messages.put((stream,raw,time.time_ns(),time.monotonic_ns()))
        finally:
            handle.close()
            messages.put((stream,None,time.time_ns(),time.monotonic_ns()))
    readers = [threading.Thread(target=read_pipe,args=(pipe,stream),daemon=True) for pipe,stream in ((process.stdout,"stdout"),(process.stderr,"stderr"))]
    for reader in readers:
        reader.start()
    send_start_ns, send_start_mono = time.time_ns(),time.monotonic_ns()
    try:
        process.stdin.write(prompt)
        process.stdin.flush()
        process.stdin.close()
        request = writer.capture(prompt,stream="stdin",stage="cli_stdin_sent",**capture_args,
                                 send_started_at_unix_ns=send_start_ns,send_started_monotonic_ns=send_start_mono)
    except (BrokenPipeError,OSError):
        request = None
    finished, thread_ids, model_ids, response_ids = set(),set(),set(),set()
    output_seqs, stop_events = [],[]
    started = time.monotonic()
    timed_out = False
    while len(finished)<2:
        if not timed_out and time.monotonic()-started>configuration["timeout_seconds"]:
            process.kill()
            timed_out=True
        try:
            stream,raw,read_ns,read_mono = messages.get(timeout=0.25)
        except queue.Empty:
            continue
        if raw is None:
            finished.add(stream)
            continue
        row = writer.capture(raw,stream=stream,stage="cli_"+stream,**capture_args,
                             source_read_at_unix_ns=read_ns,source_read_monotonic_ns=read_mono)
        output_seqs.append(row["local_seq"])
        data,valid = decode_json(raw)
        stop_events += context_events_v42(data,raw,stream,row["local_seq"])
        if stream=="stdout":
            if row.get("thread_id") is not None:
                thread_ids.add(row["thread_id"])
                if resume_thread and row["thread_id"]!=resume_thread:
                    stop_events.append({"event":"contradictory_thread_id","receipt_seq":row["local_seq"],"observed":row["thread_id"]})
            if row.get("response_id") is not None:
                response_ids.add(row["response_id"])
            model_ids.update(str(item["value"]) for item in row["metadata_observed"]["models"] if item["value"] is not None)
            if not valid or (isinstance(data,dict) and data.get("type") in ("turn.failed","error")):
                stop_events.append({"event":"stdout_failure_or_invalid_json","receipt_seq":row["local_seq"]})
        elif re.search(rb"\bReconnecting\.\.\.\s*\d+/\d+",raw,re.I):
            stop_events.append({"event":"runtime_reconnect","receipt_seq":row["local_seq"]})
        if stop_events and process.poll() is None:
            process.kill()
    exit_code = process.wait()
    for reader in readers:
        reader.join(timeout=1)
    reply = final_file.read_bytes() if final_file.exists() else None
    final = writer.capture(reply,stream="file",stage="cli_last_message_file",**capture_args,
                           source_path=str(final_file)) if reply is not None else None
    record = {**common,"invocation_receipt_seq":invocation["local_seq"],"source_pid":process.pid,"process_uuid":None,
              "exit_code":exit_code,"timed_out":timed_out,"stop_events":stop_events,
              "thread_id":next(iter(thread_ids)) if len(thread_ids)==1 else None,"thread_ids_observed":sorted(thread_ids),
              "response_id":next(iter(response_ids)) if len(response_ids)==1 else None,"response_ids_observed":sorted(response_ids),
              "model_id_observed":next(iter(model_ids)) if len(model_ids)==1 else None,"model_ids_observed":sorted(model_ids),
              "request_receipt_seq":request["local_seq"] if request else None,"output_receipt_seqs":output_seqs,
              "final_receipt_seq":final["local_seq"] if final else None,
              "raw_prompt_sha256":hashlib.sha256(prompt).hexdigest(),"raw_reply_sha256":hashlib.sha256(reply).hexdigest() if reply is not None else None,
              "reply_file":str(final_file),"model_requested":configuration["model_requested"],
              "reasoning_mode":configuration["reasoning_mode"],"modality":configuration["modality"],"service_tier":configuration["service_tier"]}
    writer.add("cli_result",canonical_bytes(record),**common,event="process_exit",measurements=record)
    return record,reply


def canary_control_v42(writer,output,configuration,bindings,role,codebook):
    directory = Path(output)/"control_inputs"
    directory.mkdir(exist_ok=True)
    source, tagged = directory/(role+".original.txt"),directory/(role+".tagged.txt")
    with source.open("xb") as handle:
        handle.write(b"Repeat the final line of this message exactly.\n")
    minted = make_canary(writer,"cli_stdin_sent",source,tagged,role)
    result,reply = invoke_v42(writer,output,configuration,bindings,tagged.read_bytes(),role,role)
    token = minted["token"].encode()
    stages = []
    for row in writer.rows:
        if row["kind"]=="event" and row.get("trial_id")==role:
            raw = (writer.blob_dir/row["payload_sha256"]).read_bytes()
            stages.append({"stage":row["stage"],"stream":row["stream"],"receipt_seq":row["local_seq"],
                           "payload_sha256":row["payload_sha256"],"exact_match":token in raw,
                           "offset":raw.index(token) if token in raw else None,"thread_id":row.get("thread_id")})
    witnessed = all(any(row["stage"]==stage and row["exact_match"] for row in stages)
                    for stage in ("cli_stdin_sent","cli_stdout","cli_last_message_file"))
    valid = result["exit_code"]==0 and not result["stop_events"] and not result["timed_out"] and witnessed and len(result["thread_ids_observed"])==1
    report = {**report_header(),"status":"PASS" if valid else "FAIL","cohort_role":role,"canary":minted,
              "result":result,"stages":stages,"witnessed_all_three_stages":witnessed,
              "event_topology":topology_v42(writer.rows,writer.blob_dir,role,reply,codebook)}
    save_v42(Path(output)/(role+"_REPORT.json"),report)
    require_v42(valid,"canary_control_failed",role=role)
    return report


def response_record_v42(trial,result,reply,topology,codebook,previous,expected_thread):
    ids = result["thread_ids_observed"]
    continuity = "BROKEN" if len(ids)>1 or (ids and expected_thread and ids[0]!=expected_thread) else "VERIFIED" if len(ids)==1 else "PARTIAL"
    task_reply, header = split_math_header(reply.decode("utf-8"),trial["expected_answer"])
    audit = scan_response(task_reply,request=trial["prompt"])
    # A_intro uses the actual task, as in the baseline; callers overwrite with exact frozen task scan.
    literal = int(audit["preamble"]["checking_prefix"])
    marker = leading_markers_v42(task_reply,codebook)
    record = {**report_header(),**{k:v for k,v in trial.items() if k!="prompt"},**result,
              "thread_continuity_status":continuity,"previous_response_id":previous[-1]["response_id"] if previous else None,
              "C_prev1":previous[-1]["C_n_literal"] if previous else None,
              "C_prev2":previous[-2]["C_n_literal"] if len(previous)>1 else None,
              "C_n_literal":literal,"checking_task_prefix":bool(literal),
              "checking_word_present":audit["preamble"]["checking_word_present"],"manual_substantive_checking":None,
              "feature_vector":audit["feature_vector"],"strict_flags":audit["strict"]["flags"],
              "broad_flags":audit["broad"]["flags"],"A_intro":audit["A_intro"],"Delta":audit["pair_delta"],
              "math_header":header,"task_reply_sha256":sha256_text(task_reply),
              "agent_message_item_count_n":topology["agent_message_item_count_n"],
              "agent_message_item_count":topology["agent_message_item_count_n"],"U_n":topology["U_n"],
              "W_n":marker["W_n"],"H_n":marker["H_n"],"A_n":marker["A_n"],
              "leading_marker_count_n":marker["leading_marker_count_n"],"preamble_measurements":marker,
              "task_reply_audit":audit,"model_label_ui":None}
    return record


def run_sequence_v42(output):
    output = Path(output).resolve()
    bindings = json.loads((output/"FROZEN_BINDINGS.json").read_bytes())
    bindings_hash = file_hash_v42(output/"FROZEN_BINDINGS.json")
    configuration = json.loads((output/"TARGET_CONFIGURATION_v42.json").read_bytes())
    runtime = json.loads((output/"RUNTIME_ENVIRONMENT.json").read_bytes())
    codebook = json.loads((output/"PREAMBLE_CODEBOOK_v42.json").read_bytes())
    task = (output/"task.txt").read_text(encoding="utf-8")
    plan = [json.loads(line) for line in (output/"SEQUENTIAL_PLAN.jsonl").read_bytes().splitlines()]
    log = output/"DROP_IT_RECEIPTS_SEQ.jsonl"
    require_v42(not log.exists(),"sequence_already_started_no_resume")
    records, topologies, checkpoints, observed_models = [],[],[],set()
    failure, primary_thread, active_trial, last_result = None,None,None,None
    pre,post = None,None
    with ReceiptLog(log) as writer:
        try:
            frozen_gate_v42(output,bindings,configuration)
            baseline_gate_v42(bindings["baseline_directory"])
            writer.add("cohort_preregistration",(output/"PREREGISTRATION_v42.json").read_bytes(),
                       frozen_bindings_sha256=bindings_hash,**{k:bindings[k] for k in ("plan_sha256","runtime_environment_sha256","preamble_codebook_sha256")})
            for name in ["FROZEN_BINDINGS.json",*bindings["files"]]:
                writer.add("frozen_input",(output/name).read_bytes(),source_name=name)
            checkpoints.append(checkpoint_v42(writer,runtime,"before_canary_pre"))
            active_trial="CANARY_PRE"
            pre = canary_control_v42(writer,output,configuration,bindings,"CANARY_PRE",codebook)
            observed_models.update(pre["result"]["model_ids_observed"])
            require_v42(len(observed_models)<=1,"observed_model_id_changed")
            checkpoints.append(checkpoint_v42(writer,runtime,"after_canary_pre"))
            print(json.dumps({"cohort_role":"CANARY_PRE","status":"PASS","thread_id":pre["result"]["thread_id"]}),flush=True)
            for trial in plan:
                active_trial=trial["trial_id"]
                last_result=None
                require_v42(file_hash_v42(output/"FROZEN_BINDINGS.json")==bindings_hash,"bindings_changed")
                trace_report(log,writer.previous)
                result,reply = invoke_v42(writer,output,configuration,bindings,trial["prompt"].encode(),trial["trial_id"],"PRIMARY_SEQUENCE",primary_thread,trial)
                last_result=result
                require_v42(result["exit_code"]==0 and not result["timed_out"] and not result["stop_events"] and reply is not None and bool(reply.strip()) and result["request_receipt_seq"] is not None,"failed_primary_turn",result=result)
                observed_models.update(result["model_ids_observed"])
                require_v42(len(observed_models)<=1,"observed_model_id_changed")
                topology = topology_v42(writer.rows,writer.blob_dir,trial["trial_id"],reply,codebook,trial["expected_answer"])
                topologies.append(topology)
                record = response_record_v42(trial,result,reply,topology,codebook,records,primary_thread)
                audit = scan_response(split_math_header(reply.decode(),trial["expected_answer"])[0],task)
                record.update(A_intro=audit["A_intro"],Delta=audit["pair_delta"],task_reply_audit=audit)
                valid = record["thread_continuity_status"]=="VERIFIED" and topology["turn_completed_count"]==1 and not topology["failure_events"] and not topology["context_state_events"] and any(item["is_final_message_item"] for item in topology["items"]) and all(item["completed"] for item in topology["items"])
                record["eligible_primary_analysis"]=valid
                row=writer.add("substantive_response",canonical_bytes(record),trial_id=trial["trial_id"],measurements=record)
                record["response_record_receipt_seq"]=row["local_seq"]
                with (output/"SEQUENTIAL_OUTCOMES.jsonl").open("ab") as handle:
                    handle.write(canonical_bytes(record)+b"\n")
                    handle.flush()
                    os.fsync(handle.fileno())
                require_v42(valid,"invalid_continuity_or_event_topology",trial_id=trial["trial_id"],continuity=record["thread_continuity_status"])
                require_v42(record["thread_id"]!=pre["result"]["thread_id"],"primary_reused_control_thread")
                primary_thread = record["thread_id"]
                records.append(record)
                frozen_gate_v42(output,bindings,configuration)
                print(json.dumps({"turn_index":trial["turn_index"],"condition":trial["condition"],"thread_id":primary_thread,
                                  "continuity":record["thread_continuity_status"],"C":record["C_n_literal"],"W":record["W_n"],"H":record["H_n"],"U":record["U_n"],"agent_items":record["agent_message_item_count_n"]}),flush=True)
            checkpoints.append(checkpoint_v42(writer,runtime,"at_primary_end"))
            active_trial="CANARY_POST"
            last_result=None
            post = canary_control_v42(writer,output,configuration,bindings,"CANARY_POST",codebook)
            require_v42(post["result"]["thread_id"] not in (primary_thread,pre["result"]["thread_id"]),"control_thread_reuse")
            observed_models.update(post["result"]["model_ids_observed"])
            require_v42(len(observed_models)<=1,"observed_model_id_changed")
            checkpoints.append(checkpoint_v42(writer,runtime,"after_canary_post"))
            frozen_gate_v42(output,bindings,configuration)
            trace_report(log,writer.previous)
        except Exception as exc:
            failure = {"event":"FAILURE_EVENT","trial_id":active_trial,"error_type":type(exc).__name__,"observed_literal":str(exc),
                       "thread_state_advanced":None,"last_result":last_result,"completed_valid_primary_turns":len(records),
                       "collection_timestamp_ns":time.time_ns(),"collector_retry_count":0}
            try:
                row = writer.add("FAILURE_EVENT",canonical_bytes(failure),trial_id=active_trial,measurements=failure)
                failure["event_receipt_seq"]=row["local_seq"]
            except Exception as receipt_error:
                failure["failure_receipt_error"]=str(receipt_error)
            save_v42(output/"FAILURE_EVENT.json",failure)
            if not any(x["checkpoint"]=="at_primary_end" for x in checkpoints):
                try:
                    checkpoints.append(checkpoint_v42(writer,runtime,"at_primary_end"))
                except Exception as checkpoint_error:
                    checkpoints.append({"checkpoint":"at_primary_end","error":str(checkpoint_error)})
            print(json.dumps(failure),flush=True)
    for role in ("CANARY_PRE","CANARY_POST"):
        if not (output/(role+"_REPORT.json")).exists():
            save_v42(output/(role+"_REPORT.json"),{**report_header(),"status":"NOT_RUN_HALT","cohort_role":role,"failure":failure})
    for point in ("before_canary_pre","after_canary_pre","at_primary_end","after_canary_post"):
        if not any(x["checkpoint"]==point for x in checkpoints):
            checkpoints.append({"checkpoint":point,"state_database_sha256":None,"status":"NOT_REACHED"})
    save_v42(output/"STATE_DATABASE_CHECKPOINTS.json",{**report_header(),"checkpoints":checkpoints})
    save_v42(output/"COHORT_STATUS.json",{**report_header(),"status":"HALTED" if failure else "COMPLETED",
              "planned":64,"completed":len(records),"thread_id":primary_thread,"failure":failure,
              "frozen_bindings_sha256":bindings_hash,"receipt_head":receipt_rows(log)[-1]["receipt_sha256"]})
    finalize_v42(output)
    return 3 if failure else 0


def baseline_measurements_v42(baseline,codebook,plan):
    baseline = Path(baseline)
    prior = json.loads((baseline/"TRIAL_REPORT.json").read_bytes())
    log = baseline/"DROP_IT_RECEIPTS_NEXT.jsonl"
    rows, blobs = receipt_rows(log),Path(str(log)+".blobs")
    task = (baseline/"task.txt").read_text(encoding="utf-8")
    records,topologies = [],[]
    for i,entry in enumerate(prior["observations"]):
        require_v42(entry["condition"]==plan[i]["condition"] and entry["prime"]==plan[i]["prime"],"matched_baseline_order_mismatch")
        raw = (blobs/entry["reply_file_sha256"]).read_bytes()
        require_v42(hashlib.sha256(raw).hexdigest()==entry["reply_file_sha256"],"baseline_reply_hash_mismatch")
        text,header = split_math_header(raw.decode("utf-8"),plan[i]["expected_answer"])
        audit = scan_response(text,task)
        marker = leading_markers_v42(text,codebook)
        topology = topology_v42(rows,blobs,entry["trial_id"],raw,codebook,plan[i]["expected_answer"])
        record = {"trial_id":entry["trial_id"],"condition":entry["condition"],"block":entry["block"],"prime":entry["prime"],
                  "program_sha256":entry["program_sha256"],"raw_reply_sha256":entry["reply_file_sha256"],
                  "C_n_literal":int(audit["preamble"]["checking_prefix"]),"W_n":marker["W_n"],"H_n":marker["H_n"],"A_n":marker["A_n"],
                  "U_n":topology["U_n"],"agent_message_item_count_n":topology["agent_message_item_count_n"],
                  "feature_vector":audit["feature_vector"],"preamble_measurements":marker,
                  "source_receipt_seqs":entry["receipt_seqs"],"thread_id":entry["thread_id"]}
        records.append(record)
        topologies.append(topology)
    return {"program_sha256":PARENT_PROGRAM_SHA256,"package_sha256":BASELINE_PACKAGE_V42,"receipt_head":BASELINE_HEAD_V42,
            "observations":records,"event_topology":topologies,"rates":rates_v42(records),
            "by_condition":{c:rates_v42([r for r in records if r["condition"]==c]) for c in "ABCD"}}


def exact_repeat_v42(topologies):
    items = []
    for topology in topologies:
        for item in topology["items"]:
            items.append({"trial_id":topology["trial_id"],"item_id":item["item_id"],"item_ordinal":item["item_ordinal"],
                          "event_receipt_seq":item["event_receipt_seq"],"raw_item_sha256":item["raw_item_sha256"]})
    groups=[]
    for item in items:
        if not groups or groups[-1][0]["raw_item_sha256"]!=item["raw_item_sha256"]:
            groups.append([])
        groups[-1].append(item)
    repeats=[group for group in groups if len(group)>1]
    return {"scope":"consecutive distinct assistant items in explicit primary turn/item order; controls excluded",
            "exact_repeat_pairs":sum(len(group)-1 for group in repeats),
            "maximum_exact_repeat_run":max((len(group) for group in repeats),default=0),
            "runs":[{"length":len(group),"repeated_text_sha256":group[0]["raw_item_sha256"],"items":group} for group in repeats]}


def link_item_repeats_v42(topologies):
    previous=None
    for topology in topologies:
        for item in topology.get("items",[]):
            item["previous_item_text_sha256"]=previous["raw_item_sha256"] if previous else None
            item["exactly_repeated_item_text"]=bool(previous and item["raw_item_sha256"]==previous["raw_item_sha256"])
            item["previous_item_receipt_seq"]=previous["event_receipt_seq"] if previous else None
            previous=item


def finalize_v42(output):
    import zipfile
    output=Path(output).resolve()
    bindings=json.loads((output/"FROZEN_BINDINGS.json").read_bytes())
    configuration=json.loads((output/"TARGET_CONFIGURATION_v42.json").read_bytes())
    frozen_gate_v42(output,bindings,configuration,False)
    baseline=Path(bindings["baseline_directory"])
    baseline_gate_v42(baseline)
    plan=[json.loads(line) for line in (output/"SEQUENTIAL_PLAN.jsonl").read_bytes().splitlines()]
    codebook=json.loads((output/"PREAMBLE_CODEBOOK_v42.json").read_bytes())
    status=json.loads((output/"COHORT_STATUS.json").read_bytes())
    log=output/"DROP_IT_RECEIPTS_SEQ.jsonl"
    rows=receipt_rows(log)
    validation=trace_report(log,status["receipt_head"])
    save_v42(output/"RECEIPT_VALIDATION_SEQ.json",validation)
    outcomes=output/"SEQUENTIAL_OUTCOMES.jsonl"
    all_records=[json.loads(line) for line in outcomes.read_bytes().splitlines()] if outcomes.exists() else []
    records=[row for row in all_records if row["eligible_primary_analysis"]]
    require_v42([r["turn_index"] for r in records]==list(range(1,len(records)+1)),"substantive_order_mismatch")
    for record in records:
        planned=plan[record["turn_index"]-1]
        require_v42(record["raw_prompt_sha256"]==planned["raw_prompt_sha256"],"delivered_prompt_mismatch")
        require_v42(record["program_sha256"]==bindings["program_sha256"],"outcome_source_binding_mismatch")
        for key in ("task_sha256","target_configuration_sha256","runtime_environment_sha256","plan_sha256","preamble_codebook_sha256"):
            require_v42(record[key]==bindings[key],"outcome_binding_mismatch",key=key)
    invocations=[r for r in rows if r["kind"]=="cli_invocation"]
    for invocation in invocations:
        for key in ("runtime_environment_sha256","target_configuration_sha256","plan_sha256","preamble_codebook_sha256","task_sha256"):
            require_v42(invocation[key]==bindings[key],"invocation_binding_mismatch",key=key)
    topologies=[]
    for invocation in invocations:
        if invocation["cohort_role"]!="PRIMARY_SEQUENCE":
            continue
        trial_id=invocation["trial_id"]
        planned=next(p for p in plan if p["trial_id"]==trial_id)
        final=next((r for r in rows if r.get("trial_id")==trial_id and r.get("stage")=="cli_last_message_file"),None)
        raw=(Path(str(log)+".blobs")/final["payload_sha256"]).read_bytes() if final else None
        try:
            topology=topology_v42(rows,Path(str(log)+".blobs"),trial_id,raw,codebook,planned["expected_answer"])
        except ValueError as exc:
            topology={"trial_id":trial_id,"measurement_error":str(exc),"items":[],"agent_message_item_count_n":None,
                      "event_receipt_seqs":[r["local_seq"] for r in rows if r.get("trial_id")==trial_id],"context_state_events":[]}
        topologies.append(topology)
    link_item_repeats_v42(topologies)
    eligible_ids={r["trial_id"] for r in records}
    eligible_topologies=[t for t in topologies if t["trial_id"] in eligible_ids]
    measurements_header={**report_header(),"plan_sha256":bindings["plan_sha256"],
         "preamble_codebook_sha256":bindings["preamble_codebook_sha256"],"receipt_head":status["receipt_head"]}
    topology_report={**measurements_header,"turns":topologies,
                     "total_assistant_items":sum(t["agent_message_item_count_n"] for t in eligible_topologies),
                     "item_count_histogram":dict(Counter(t["agent_message_item_count_n"] for t in eligible_topologies)),
                     "context_state_events":[e for t in topologies for e in t["context_state_events"]]}
    save_v42(output/"EVENT_TOPOLOGY_REPORT.json",topology_report)
    runs={**measurements_header,"markers":{key:run_structure_v42([r[key] for r in records]) for key in ("C_n_literal","W_n","H_n","U_n")},
          "exact_repeated_item_text":exact_repeat_v42(eligible_topologies)}
    save_v42(output/"RUN_STRUCTURE_REPORT.json",runs)
    transitions={**measurements_header,**transitions_v42(records)}
    save_v42(output/"SEQUENTIAL_TRANSITIONS.json",transitions)
    baseline_measured=baseline_measurements_v42(baseline,codebook,plan)
    save_v42(output/"BASELINE_REMEASUREMENT_v42.json",{**measurements_header,**baseline_measured})
    matched=[r for r in records if r["block"]<=4]
    matched_rates=rates_v42(matched)
    baseline_rates=baseline_measured["rates"]
    matched_differences={key:(value["probability"]-baseline_rates[key]["probability"] if value["probability"] is not None else None)
                         for key,value in matched_rates.items()}
    comparisons={"MATCHED_16":{"sequential_completed":len(matched),"sequential_planned":16,"baseline_completed":16,
                    "sequential_rates":matched_rates,"baseline_rates":baseline_rates,"difference_sequential_minus_baseline":matched_differences,
                    "sequential_by_condition":{c:rates_v42([r for r in matched if r["condition"]==c]) for c in "ABCD"},
                    "baseline_by_condition":baseline_measured["by_condition"]},
                 "FULL_64":{"completed":len(records),"planned":64,"rates":rates_v42(records),
                    "by_current_condition":{c:rates_v42([r for r in records if r["condition"]==c]) for c in "ABCD"}},
                 "time_quarters":{f"blocks_{start}_{start+3}":rates_v42([r for r in records if start<=r["block"]<start+4]) for start in (1,5,9,13)}}
    report={**measurements_header,"OBSERVED":{"cohort_status":status,"records":all_records,
                    "invocation_count":len(invocations),"primary_invocation_count":sum(r["cohort_role"]=="PRIMARY_SEQUENCE" for r in invocations),
                    "distinct_primary_thread_ids":sorted({r["thread_id"] for r in records if r["thread_id"] is not None}),
                    "model_ids_observed":sorted({r["model_id_observed"] for r in records if r["model_id_observed"] is not None}),
                    "model_id_null_count":sum(r["model_id_observed"] is None for r in records),
                    "response_id_null_count":sum(r["response_id"] is None for r in records),
                    "manual_label_count":sum(r["manual_substantive_checking"] is not None for r in records)},
            "DERIVED":{"comparisons":comparisons,"transitions":transitions,
                    "geometry_answers":{"expected":sum(r["expected_answer"] is not None for r in records),
                        "recognized":sum(r["math_header"]["status"]=="recognized" for r in records),
                        "correct":sum(r["math_header"].get("correct") is True for r in records)},
                    "run_structure":runs,"validation_metrics":{**validation["validation_metrics"],"binding_errors":0,"substantive_order_errors":0}},
            "ATTRIBUTION":None,"task_sha256":TASK_HASH_V42,"target_configuration_sha256":bindings["target_configuration_sha256"],
            "runtime_environment_sha256":bindings["runtime_environment_sha256"],"condition_context":"current condition in accumulating treatment history"}
    save_v42(output/"SEQUENTIAL_TRIAL_REPORT.json",report)
    wrapper=[]
    query=WRAPPER_QUERY.encode()
    live_rows=[r for r in rows if r["kind"]=="event"]
    thread_by_trial={r["trial_id"]:r["thread_id"] for r in records}
    for row in live_rows:
        raw=(Path(str(log)+".blobs")/row["payload_sha256"]).read_bytes()
        start=0
        while (offset:=raw.find(query,start))!=-1:
            wrapper.append({"exact_match":True,"stage":row.get("stage"),"stream":row.get("stream"),
                            "receipt":row["local_seq"],"thread_id_observed_in_payload":row.get("thread_id"),
                            "thread_id_via_trial_join":thread_by_trial.get(row.get("trial_id")),
                            "trial_id":row.get("trial_id"),"offset_utf8_bytes":offset,"payload_sha256":row["payload_sha256"]})
            start=offset+len(query)
    save_v42(output/"WRAPPER_PROVENANCE_UPDATE.json",{**measurements_header,
        "OBSERVED":{"current_route":{"query":WRAPPER_QUERY,"payloads_scanned":len(live_rows),"exact_match_count":len(wrapper),"matches":wrapper},
                    "historical_pool":{"file":"baseline/WRAPPER_PROVENANCE_REPORT.json","sha256":file_hash_v42(baseline/"WRAPPER_PROVENANCE_REPORT.json"),
                                       "package_sha256":BASELINE_PACKAGE_V42}},"DERIVED":None,"ATTRIBUTION":None})
    def rate_text(rate):
        return f'{rate["numerator"]}/{rate["denominator"]} = '+("NULL" if rate["probability"] is None else f'{rate["probability"]:.6f}')
    lines=["DROP_IT v4.2 sequential measurements","",f'Program SHA-256: `{bindings["program_sha256"]}`',"",
           f'Parent SHA-256: `{PARENT_PROGRAM_SHA256}`',"",f'Status: {status["status"]}; valid primary turns: {len(records)}/64.',"",
           f'Primary exposed thread IDs: {json.dumps(report["OBSERVED"]["distinct_primary_thread_ids"])}.',"",
           f'Exposed model IDs: {json.dumps(report["OBSERVED"]["model_ids_observed"])}; null count: {report["OBSERVED"]["model_id_null_count"]}.',"",
           '| Marker | Sequential matched 16 | Fresh-thread baseline 16 | Sequential full 64 |','|---|---:|---:|---:|']
    for key in ("C_n_literal","W_n","H_n","A_n","U_n","strict_any","broad_any"):
        lines.append(f'| {key} | {rate_text(matched_rates[key])} | {rate_text(baseline_rates[key])} | {rate_text(comparisons["FULL_64"]["rates"][key])} |')
    lines += ["",'| Current condition | p11 | p01 | Lambda |','|---|---:|---:|---:|']
    for name,values in [("pooled",transitions["first_order"]["pooled"]),*transitions["first_order"]["by_current_condition"].items(),
                        ("first half",transitions["first_order"]["first_half"]),("second half",transitions["first_order"]["second_half"])]:
        lines.append(f'| {name} | {rate_text(values["p11"])} | {rate_text(values["p01"])} | {"NULL" if values["Lambda"] is None else values["Lambda"]} |')
    lines += ["",'| Second-order state | Next C=1 |','|---|---:|']
    for key,value in transitions["second_order"]["q"].items():
        lines.append(f'| {key} | {rate_text(value)} |')
    lines += ["",f'Separately exposed assistant items: {topology_report["total_assistant_items"]}.',"",
              'Geometry answers: '+json.dumps(report["DERIVED"]["geometry_answers"])+'.',"",
              f'Exact current wrapper matches: {len(wrapper)} across {len(live_rows)} captured event payloads.',"",
              f'Receipts: {validation["receipts"]}; distinct validated payloads: {validation["validated_payloads"]}; chain/payload errors: 0/0.',"",
              f'Receipt head: `{status["receipt_head"]}`',"",f'Plan SHA-256: `{bindings["plan_sha256"]}`',"",
              f'Runtime SHA-256: `{bindings["runtime_environment_sha256"]}`',"",f'Codebook SHA-256: `{bindings["preamble_codebook_sha256"]}`',""]
    if status["failure"]:
        lines += ['FAILURE_EVENT: '+json.dumps(status["failure"],ensure_ascii=True),""]
    (output/"SEQUENTIAL_TRIAL_REPORT.md").write_bytes("\n".join(lines).encode())
    readme = "DROP_IT v4.2\n\nFrozen source, plan, runtime and marker codebook are included.\n\n" \
        "Read SEQUENTIAL_TRIAL_REPORT.md for counts and transitions. Raw stdout/stderr/stdin and final files are retained in the receipt blobs.\n\n" \
        "Use `python DROP_IT_v4.2.py sequential validate --output .` from this directory to validate the frozen receipt chain and bindings.\n\n" \
        "The original DROP_IT single-prompt interface remains available: `python DROP_IT_v4.2.py --index 1 --condition D --request task.txt`.\n\n" \
        "A started sequential cohort cannot be resumed or retried by this harness.\n"
    (output/"README_v42.md").write_bytes(readme.encode())
    package=output/"DROP_IT_v4.2_MEASUREMENT_PACKAGE.zip"
    require_v42(not package.exists(),"package_already_exists")
    files=[(p,p.relative_to(output).as_posix()) for p in sorted(output.rglob("*")) if p.is_file() and not p.name.endswith(".lock") and p.name not in ("PACKAGE_VALIDATION_v42.json","PACKAGE_SHA256_v42.json")]
    if not any(p.resolve()==Path(__file__).resolve() for p,_ in files):
        files.append((Path(__file__),"DROP_IT_v4.2.py"))
    for name in ("DROP_IT_v4.1.py","DROP_IT_v4.1_MEASUREMENT_PACKAGE.zip","TRIAL_REPORT.json","trials.jsonl",
                 "DROP_IT_RECEIPTS_NEXT.jsonl","WRAPPER_PROVENANCE_REPORT.json","task.txt"):
        files.append((baseline/name,"baseline/"+name))
    files += [(p,"baseline/DROP_IT_RECEIPTS_NEXT.jsonl.blobs/"+p.name) for p in sorted((baseline/"DROP_IT_RECEIPTS_NEXT.jsonl.blobs").iterdir()) if p.is_file()]
    manifest={name:{"sha256":file_hash_v42(path),"bytes":path.stat().st_size} for path,name in files}
    with zipfile.ZipFile(package,"x",compression=zipfile.ZIP_DEFLATED) as archive:
        for path,name in files:
            archive.write(path,name)
        archive.writestr("PACKAGE_CONTENTS.json",canonical_bytes(manifest))
    with zipfile.ZipFile(package) as archive:
        require_v42(archive.testzip() is None,"archive_crc_failure")
        for name,item in manifest.items():
            raw=archive.read(name)
            require_v42(len(raw)==item["bytes"] and hashlib.sha256(raw).hexdigest()==item["sha256"],"archive_member_hash_failure",name=name)
    package_hash=file_hash_v42(package)
    save_v42(output/"PACKAGE_VALIDATION_v42.json",{**report_header(),"package_sha256":package_hash,
        "archive_members":len(files)+1,"manifest_members_validated":len(files),"archive_crc_errors":0,
        "member_hash_errors":0,"receipt_validation_metrics":validation["validation_metrics"],
        "baseline_package_sha256_after":file_hash_v42(baseline/"DROP_IT_v4.1_MEASUREMENT_PACKAGE.zip"),
        "cohort_status":status["status"],"completed_valid_primary_turns":len(records)})
    save_v42(output/"PACKAGE_SHA256_v42.json",{**report_header(),"package":package.name,"package_sha256":package_hash,
        "package_bytes":package.stat().st_size,"manifest":manifest,"external_validation_sha256":file_hash_v42(output/"PACKAGE_VALIDATION_v42.json")})
    package.chmod(0o444)
    print(json.dumps({"status":status["status"],"completed":len(records),"package":str(package),"package_sha256":package_hash,
                      "receipt_head":status["receipt_head"]}),flush=True)


def sequential_main_v42(argv):
    parser=argparse.ArgumentParser(prog="DROP_IT_v4.2.py sequential")
    parser.add_argument("action",choices=("prepare","run","finalize","validate"))
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--baseline",type=Path)
    parser.add_argument("--help-dir",type=Path)
    args=parser.parse_args(argv)
    if args.action=="prepare":
        require_v42(args.baseline is not None and args.help_dir is not None,"prepare_requires_baseline_and_help")
        prepare_v42(args.output,args.baseline,args.help_dir)
    elif args.action=="run":
        raise SystemExit(run_sequence_v42(args.output))
    elif args.action=="finalize":
        finalize_v42(args.output)
    else:
        bindings=json.loads((args.output/"FROZEN_BINDINGS.json").read_bytes())
        configuration=json.loads((args.output/"TARGET_CONFIGURATION_v42.json").read_bytes())
        frozen_gate_v42(args.output,bindings,configuration,False)
        status=json.loads((args.output/"COHORT_STATUS.json").read_bytes())
        report=trace_report(args.output/"DROP_IT_RECEIPTS_SEQ.jsonl",status["receipt_head"])
        print(json.dumps({"receipts":report["receipts"],"validated_payloads":report["validated_payloads"],
                          "head_sha256":report["head_sha256"],"validation_metrics":report["validation_metrics"]}),flush=True)


if __name__ == "__main__":
    if len(sys.argv)>1 and sys.argv[1]=="sequential":
        sequential_main_v42(sys.argv[2:])
    else:
        main()
