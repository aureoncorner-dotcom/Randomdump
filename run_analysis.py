#!/usr/bin/env python3
"""Frozen v0.1 lunar/calendar cluster analysis.

The script reads only the frozen ledger, downloads or reuses a frozen USNO
primary-phase snapshot, performs the specified 10,000 matched permutations,
and writes machine-readable outputs beside this file.
"""

from __future__ import annotations

import calendar
import csv
import hashlib
import json
import platform
import sys
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import numpy as np


ROOT = Path(__file__).resolve().parent
LEDGER_PATH = ROOT / "ledger_input.csv"
SPEC_PATH = ROOT / "FREEZE_SPEC.md"
MANIFEST_PATH = ROOT / "FREEZE_MANIFEST.json"
PHASE_SNAPSHOT_PATH = ROOT / "usno_primary_phases_2025_2026.json"

B = 10_000
BASE_SEED = 20_260_826
TARGET_DAYS = np.arange(1, 29, dtype=np.int16)
DAY19_INDEX = 18
PHASE_ORDER = ["New Moon", "First Quarter", "Full Moon", "Last Quarter"]
COHORTS_TO_TEST = ["P1", "S1", "S2"]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def child_seed(label: str) -> int:
    digest = hashlib.sha256(f"{BASE_SEED}|{label}".encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big", signed=False)


def fetch_or_load_phase_snapshot() -> dict[str, Any]:
    if PHASE_SNAPSHOT_PATH.exists():
        return json.loads(PHASE_SNAPSHOT_PATH.read_text(encoding="utf-8"))

    responses: dict[str, Any] = {}
    sources: list[str] = []
    for year in (2025, 2026):
        url = f"https://aa.usno.navy.mil/api/moon/phases/year?year={year}"
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "LunarDateLedger-v0.1/2026-08-26"},
        )
        with urllib.request.urlopen(request, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
        if "phasedata" not in payload:
            raise RuntimeError(f"USNO response for {year} lacks phasedata")
        responses[str(year)] = payload
        sources.append(url)

    snapshot = {
        "fetched_at_utc": datetime.now(timezone.utc).isoformat(),
        "authority": "U.S. Naval Observatory Astronomical Applications Department",
        "time_standard": "UTC as returned by the USNO primary-phase API",
        "sources": sources,
        "responses": responses,
    }
    PHASE_SNAPSHOT_PATH.write_text(
        json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return snapshot


def parse_phases(snapshot: dict[str, Any]) -> list[tuple[datetime, str]]:
    phases: list[tuple[datetime, str]] = []
    for year_payload in snapshot["responses"].values():
        for row in year_payload["phasedata"]:
            hour, minute = (int(x) for x in row["time"].split(":"))
            when = datetime(
                int(row["year"]),
                int(row["month"]),
                int(row["day"]),
                hour,
                minute,
                tzinfo=timezone.utc,
            )
            phases.append((when, row["phase"]))
    phases.sort(key=lambda item: item[0])
    return phases


@dataclass
class Event:
    raw: dict[str, str]
    start_local: datetime | None
    end_local: datetime | None
    zone: ZoneInfo | None
    memberships: set[str]

    @property
    def event_id(self) -> str:
        return self.raw["event_id"]

    @property
    def included(self) -> bool:
        return self.raw["inclusion_status"] == "INCLUDED"


def parse_local(value: str, zone: ZoneInfo) -> datetime | None:
    if not value:
        return None
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is not None:
        return dt.astimezone(zone)
    return dt.replace(tzinfo=zone)


def load_events() -> list[Event]:
    events: list[Event] = []
    with LEDGER_PATH.open(newline="", encoding="utf-8") as fh:
        for raw in csv.DictReader(fh):
            zone = ZoneInfo(raw["timezone"]) if raw["timezone"] else None
            start = parse_local(raw["event_start_local"], zone) if zone else None
            end = parse_local(raw["event_end_local"], zone) if zone else None
            memberships = {
                token for token in raw["cohort_memberships"].split("|") if token
            }
            if raw["inclusion_status"] == "INCLUDED" and (start is None or end is None):
                raise ValueError(f"Included event lacks bounds: {raw['event_id']}")
            events.append(Event(raw, start, end, zone, memberships))
    return events


def interval_distance_hours(start: datetime, end: datetime, phase: datetime) -> float:
    if phase < start:
        return (start - phase).total_seconds() / 3600.0
    if phase > end:
        return (phase - end).total_seconds() / 3600.0
    return 0.0


@dataclass
class EventOptions:
    event: Event
    start_days: np.ndarray
    calendar_distance: np.ndarray
    calendar_hits: np.ndarray
    lunar_any_hours: np.ndarray
    lunar_by_phase_hours: np.ndarray
    nearest_phase_index: np.ndarray
    observed_index: int


def build_options(event: Event, phases: list[tuple[datetime, str]]) -> EventOptions:
    assert event.start_local is not None and event.end_local is not None
    assert event.zone is not None

    original_start = event.start_local
    original_end = event.end_local
    exact_point = original_start == original_end

    if exact_point:
        calendar_span_days = 1
        interval_span_days = 0
    else:
        interval_span_days = (original_end.date() - original_start.date()).days
        if interval_span_days < 1:
            raise ValueError(f"Unsupported non-point interval: {event.event_id}")
        calendar_span_days = interval_span_days

    days_in_month = calendar.monthrange(original_start.year, original_start.month)[1]
    max_start_day = days_in_month - calendar_span_days + 1
    start_days = np.arange(1, max_start_day + 1, dtype=np.int16)
    if original_start.day > max_start_day:
        raise ValueError(f"Observed placement cannot preserve span: {event.event_id}")
    observed_index = int(np.where(start_days == original_start.day)[0][0])

    calendar_distance = np.empty((len(start_days), len(TARGET_DAYS)), dtype=np.float64)
    calendar_hits = np.empty((len(start_days), len(TARGET_DAYS)), dtype=np.int8)
    lunar_any = np.empty(len(start_days), dtype=np.float64)
    lunar_phase = np.empty((len(start_days), len(PHASE_ORDER)), dtype=np.float64)
    nearest_phase_index = np.empty(len(start_days), dtype=np.int32)

    phase_times = [row[0] for row in phases]
    phase_names = [row[1] for row in phases]

    for option_index, start_day in enumerate(start_days.tolist()):
        option_start = datetime(
            original_start.year,
            original_start.month,
            start_day,
            original_start.hour,
            original_start.minute,
            original_start.second,
            original_start.microsecond,
            tzinfo=event.zone,
        )
        option_end = option_start if exact_point else option_start + timedelta(days=interval_span_days)

        included_first = start_day
        included_last = start_day + calendar_span_days - 1
        for target_index, target_day in enumerate(TARGET_DAYS.tolist()):
            hit = included_first <= target_day <= included_last
            calendar_hits[option_index, target_index] = int(hit)
            if hit:
                calendar_distance[option_index, target_index] = 0.0
            else:
                calendar_distance[option_index, target_index] = min(
                    abs(target_day - included_first), abs(target_day - included_last)
                )

        start_utc = option_start.astimezone(timezone.utc)
        end_utc = option_end.astimezone(timezone.utc)
        distances = np.array(
            [interval_distance_hours(start_utc, end_utc, p) for p in phase_times],
            dtype=np.float64,
        )
        nearest_index = int(np.argmin(distances))
        nearest_phase_index[option_index] = nearest_index
        lunar_any[option_index] = float(distances[nearest_index])
        for phase_index, phase_name in enumerate(PHASE_ORDER):
            relevant = [
                distances[i] for i, name in enumerate(phase_names) if name == phase_name
            ]
            lunar_phase[option_index, phase_index] = float(min(relevant))

    return EventOptions(
        event=event,
        start_days=start_days,
        calendar_distance=calendar_distance,
        calendar_hits=calendar_hits,
        lunar_any_hours=lunar_any,
        lunar_by_phase_hours=lunar_phase,
        nearest_phase_index=nearest_phase_index,
        observed_index=observed_index,
    )


def lower_tail_p(null: np.ndarray, observed: float) -> float:
    return float((1 + np.count_nonzero(null <= observed + 1e-12)) / (len(null) + 1))


def upper_tail_p(null: np.ndarray, observed: float) -> float:
    return float((1 + np.count_nonzero(null >= observed - 1e-12)) / (len(null) + 1))


def interval_summary(values: np.ndarray) -> dict[str, float]:
    q025, q975 = np.quantile(values, [0.025, 0.975])
    return {
        "mean": float(np.mean(values)),
        "q025": float(q025),
        "q975": float(q975),
    }


def holm_adjust(raw: dict[str, float]) -> dict[str, float]:
    ordered = sorted(raw.items(), key=lambda item: item[1])
    m = len(ordered)
    adjusted_sorted: list[tuple[str, float]] = []
    running = 0.0
    for rank, (name, p_value) in enumerate(ordered):
        adjusted = min(1.0, (m - rank) * p_value)
        running = max(running, adjusted)
        adjusted_sorted.append((name, running))
    return dict(adjusted_sorted)


def analyze_cohort(
    cohort_name: str,
    cohort_options: list[EventOptions],
) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    n = len(cohort_options)
    if n < 2:
        raise ValueError(f"Cohort {cohort_name} is too small for inference")

    observed_calendar_contrib = np.stack(
        [opt.calendar_distance[opt.observed_index] for opt in cohort_options]
    )
    observed_hit_contrib = np.stack(
        [opt.calendar_hits[opt.observed_index] for opt in cohort_options]
    )
    observed_lunar_contrib = np.array(
        [opt.lunar_any_hours[opt.observed_index] for opt in cohort_options]
    )
    observed_phase_contrib = np.stack(
        [opt.lunar_by_phase_hours[opt.observed_index] for opt in cohort_options]
    )

    observed_calendar = np.mean(observed_calendar_contrib, axis=0)
    observed_hits = np.sum(observed_hit_contrib, axis=0)
    observed_lunar = float(np.mean(observed_lunar_contrib))
    observed_phase = np.mean(observed_phase_contrib, axis=0)

    rng_seed = child_seed(f"cohort:{cohort_name}")
    rng = np.random.default_rng(rng_seed)

    draw_calendar_contrib: list[np.ndarray] = []
    draw_hit_contrib: list[np.ndarray] = []
    draw_lunar_contrib: list[np.ndarray] = []
    draw_phase_contrib: list[np.ndarray] = []

    total_calendar = np.zeros((B, len(TARGET_DAYS)), dtype=np.float64)
    total_hits = np.zeros((B, len(TARGET_DAYS)), dtype=np.int16)
    total_lunar = np.zeros(B, dtype=np.float64)
    total_phase = np.zeros((B, len(PHASE_ORDER)), dtype=np.float64)

    for opt in cohort_options:
        draws = rng.integers(0, len(opt.start_days), size=B)
        cal_contrib = opt.calendar_distance[draws]
        hit_contrib = opt.calendar_hits[draws]
        lunar_contrib = opt.lunar_any_hours[draws]
        phase_contrib = opt.lunar_by_phase_hours[draws]
        draw_calendar_contrib.append(cal_contrib)
        draw_hit_contrib.append(hit_contrib)
        draw_lunar_contrib.append(lunar_contrib)
        draw_phase_contrib.append(phase_contrib)
        total_calendar += cal_contrib
        total_hits += hit_contrib
        total_lunar += lunar_contrib
        total_phase += phase_contrib

    null_calendar = total_calendar / n
    null_lunar = total_lunar / n
    null_phase = total_phase / n
    null_best_calendar = np.min(null_calendar, axis=1)

    observed_day19 = float(observed_calendar[DAY19_INDEX])
    observed_day19_hits = int(observed_hits[DAY19_INDEX])
    observed_rank = 1 + int(np.count_nonzero(observed_calendar < observed_day19 - 1e-12))
    best_mean = float(np.min(observed_calendar))
    best_days = [
        int(TARGET_DAYS[i])
        for i in np.where(np.isclose(observed_calendar, best_mean, atol=1e-12))[0]
    ]

    raw_phase_p = {
        PHASE_ORDER[i]: lower_tail_p(null_phase[:, i], float(observed_phase[i]))
        for i in range(len(PHASE_ORDER))
    }
    adjusted_phase_p = holm_adjust(raw_phase_p)

    summary = {
        "n": n,
        "event_ids": [opt.event.event_id for opt in cohort_options],
        "rng_seed": rng_seed,
        "calendar_day19": {
            "observed_mean_distance_days": observed_day19,
            "observed_windows_containing_day19": observed_day19_hits,
            "observed_rank_among_days_1_28": observed_rank,
            "observed_best_target_days": best_days,
            "observed_best_mean_distance_days": best_mean,
            "raw_lower_tail_p_mean_distance": lower_tail_p(
                null_calendar[:, DAY19_INDEX], observed_day19
            ),
            "scan_adjusted_lower_tail_p": lower_tail_p(
                null_best_calendar, observed_day19
            ),
            "upper_tail_p_hit_count": upper_tail_p(
                total_hits[:, DAY19_INDEX], observed_day19_hits
            ),
            "null_mean_distance": interval_summary(null_calendar[:, DAY19_INDEX]),
            "null_hit_count": interval_summary(total_hits[:, DAY19_INDEX].astype(float)),
        },
        "lunar_nearest_primary": {
            "observed_mean_distance_hours": observed_lunar,
            "raw_lower_tail_p": lower_tail_p(null_lunar, observed_lunar),
            "null": interval_summary(null_lunar),
        },
        "lunar_phase_specific": {
            PHASE_ORDER[i]: {
                "observed_mean_distance_hours": float(observed_phase[i]),
                "raw_lower_tail_p": raw_phase_p[PHASE_ORDER[i]],
                "holm_adjusted_p": adjusted_phase_p[PHASE_ORDER[i]],
                "null": interval_summary(null_phase[:, i]),
            }
            for i in range(len(PHASE_ORDER))
        },
    }

    target_scan_rows: list[dict[str, Any]] = []
    for i, target_day in enumerate(TARGET_DAYS.tolist()):
        rank = 1 + int(np.count_nonzero(observed_calendar < observed_calendar[i] - 1e-12))
        target_scan_rows.append(
            {
                "cohort": cohort_name,
                "target_day": target_day,
                "observed_mean_distance_days": float(observed_calendar[i]),
                "observed_hit_count": int(observed_hits[i]),
                "observed_rank": rank,
                "raw_lower_tail_p": lower_tail_p(
                    null_calendar[:, i], float(observed_calendar[i])
                ),
            }
        )

    permutation_rows: list[dict[str, Any]] = []
    for iteration in range(B):
        permutation_rows.append(
            {
                "cohort": cohort_name,
                "iteration": iteration + 1,
                "day19_mean_distance_days": float(null_calendar[iteration, DAY19_INDEX]),
                "best_day_1_28_mean_distance_days": float(null_best_calendar[iteration]),
                "day19_hit_count": int(total_hits[iteration, DAY19_INDEX]),
                "lunar_nearest_primary_mean_hours": float(null_lunar[iteration]),
                "new_moon_mean_hours": float(null_phase[iteration, 0]),
                "first_quarter_mean_hours": float(null_phase[iteration, 1]),
                "full_moon_mean_hours": float(null_phase[iteration, 2]),
                "last_quarter_mean_hours": float(null_phase[iteration, 3]),
            }
        )

    loo_rows: list[dict[str, Any]] = []
    if n >= 3:
        obs_calendar_sum = np.sum(observed_calendar_contrib, axis=0)
        obs_lunar_sum = float(np.sum(observed_lunar_contrib))
        for remove_index, opt in enumerate(cohort_options):
            n2 = n - 1
            obs_calendar_loo = (
                obs_calendar_sum - observed_calendar_contrib[remove_index]
            ) / n2
            obs_day19_loo = float(obs_calendar_loo[DAY19_INDEX])
            obs_lunar_loo = (
                obs_lunar_sum - float(observed_lunar_contrib[remove_index])
            ) / n2

            null_calendar_loo = (
                total_calendar - draw_calendar_contrib[remove_index]
            ) / n2
            null_lunar_loo = (
                total_lunar - draw_lunar_contrib[remove_index]
            ) / n2
            null_best_loo = np.min(null_calendar_loo, axis=1)

            loo_rows.append(
                {
                    "cohort": cohort_name,
                    "removed_event_id": opt.event.event_id,
                    "remaining_n": n2,
                    "day19_observed_mean_distance_days": obs_day19_loo,
                    "day19_raw_lower_tail_p": lower_tail_p(
                        null_calendar_loo[:, DAY19_INDEX], obs_day19_loo
                    ),
                    "day19_scan_adjusted_lower_tail_p": lower_tail_p(
                        null_best_loo, obs_day19_loo
                    ),
                    "lunar_observed_mean_distance_hours": float(obs_lunar_loo),
                    "lunar_raw_lower_tail_p": lower_tail_p(
                        null_lunar_loo, float(obs_lunar_loo)
                    ),
                }
            )

    return summary, target_scan_rows, permutation_rows, loo_rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def event_score_rows(
    events: list[Event],
    options_by_id: dict[str, EventOptions],
    phases: list[tuple[datetime, str]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for event in events:
        base = dict(event.raw)
        opt = options_by_id.get(event.event_id)
        if opt is None:
            base.update(
                {
                    "event_start_utc": "",
                    "event_end_utc": "",
                    "calendar_distance_to_19_days": "",
                    "contains_day19": "",
                    "nearest_primary_phase": "",
                    "nearest_primary_phase_utc": "",
                    "distance_to_nearest_primary_hours": "",
                }
            )
        else:
            assert event.start_local is not None and event.end_local is not None
            idx = opt.observed_index
            phase_idx = int(opt.nearest_phase_index[idx])
            phase_time, phase_name = phases[phase_idx]
            base.update(
                {
                    "event_start_utc": event.start_local.astimezone(timezone.utc).isoformat(),
                    "event_end_utc": event.end_local.astimezone(timezone.utc).isoformat(),
                    "calendar_distance_to_19_days": float(
                        opt.calendar_distance[idx, DAY19_INDEX]
                    ),
                    "contains_day19": int(opt.calendar_hits[idx, DAY19_INDEX]),
                    "nearest_primary_phase": phase_name,
                    "nearest_primary_phase_utc": phase_time.isoformat(),
                    "distance_to_nearest_primary_hours": float(
                        opt.lunar_any_hours[idx]
                    ),
                }
            )
        rows.append(base)
    return rows


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    expected = manifest["files"]
    actual_hashes = {
        "FREEZE_SPEC.md": sha256_file(SPEC_PATH),
        "ledger_input.csv": sha256_file(LEDGER_PATH),
    }
    if actual_hashes != expected:
        raise RuntimeError(
            "Frozen input hash mismatch; create a new version instead of silently rerunning"
        )

    snapshot = fetch_or_load_phase_snapshot()
    phases = parse_phases(snapshot)
    events = load_events()

    options_by_id: dict[str, EventOptions] = {}
    for event in events:
        if event.included:
            options_by_id[event.event_id] = build_options(event, phases)

    cohort_results: dict[str, Any] = {}
    target_scan_rows: list[dict[str, Any]] = []
    permutation_rows: list[dict[str, Any]] = []
    loo_rows: list[dict[str, Any]] = []

    for cohort_name in COHORTS_TO_TEST:
        cohort_options = [
            options_by_id[event.event_id]
            for event in events
            if event.included and cohort_name in event.memberships
        ]
        summary, scans, permutations, loo = analyze_cohort(
            cohort_name, cohort_options
        )
        cohort_results[cohort_name] = summary
        target_scan_rows.extend(scans)
        permutation_rows.extend(permutations)
        loo_rows.extend(loo)

    technical_event = next(
        event for event in events if event.event_id == "TECH_2026_08_20_0830"
    )
    technical_opt = options_by_id[technical_event.event_id]
    technical_idx = technical_opt.observed_index
    technical_phase_idx = int(technical_opt.nearest_phase_index[technical_idx])
    technical_phase_time, technical_phase_name = phases[technical_phase_idx]

    result = {
        "analysis_version": "0.1",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "retrospective_exploratory",
        "permutations_per_test": B,
        "base_seed": BASE_SEED,
        "frozen_input_hashes": actual_hashes,
        "phase_snapshot_sha256": sha256_file(PHASE_SNAPSHOT_PATH),
        "cohorts": cohort_results,
        "technical_T1": {
            "event_id": technical_event.event_id,
            "estimated_event_utc": technical_event.start_local.astimezone(
                timezone.utc
            ).isoformat(),
            "nearest_primary_phase": technical_phase_name,
            "nearest_primary_phase_utc": technical_phase_time.isoformat(),
            "distance_hours": float(
                technical_opt.lunar_any_hours[technical_idx]
            ),
            "inferential_test": "not_run_n_equals_1",
        },
        "holdout_status": "PENDING_NEXT_UNOPENED_ARCHIVE_BATCH",
    }

    (ROOT / "results_summary.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_csv(
        ROOT / "event_scored.csv",
        event_score_rows(events, options_by_id, phases),
    )
    write_csv(ROOT / "calendar_target_scan.csv", target_scan_rows)
    write_csv(ROOT / "permutation_distributions.csv", permutation_rows)
    write_csv(ROOT / "leave_one_out.csv", loo_rows)

    environment = {
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "timezone_database": "system zoneinfo",
        "script_sha256": sha256_file(Path(__file__)),
    }
    (ROOT / "run_environment.json").write_text(
        json.dumps(environment, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
