#!/usr/bin/env python3
"""CTA-TG-X773: exploratory eight-body toroidal non-descent pilot.

This is a new run. It does not reproduce, repair, or backfill PRP-0.1.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.metadata
import json
import math
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import swisseph as swe


RUN_ID = "CTA-TG-X773"
STATUS = "EXPLORATORY_NEW_RUN_NO_PRP_BACKFILL"
START_DATE = date(1775, 1, 1)
TARGET_DATE = date(2026, 9, 1)
TARGET_JD_UT = 2461284.9861152545
EXCLUSION_DAYS = 365
EPISODE_SEPARATION_DAYS = 180
TOP_N = 13

BODY_SPECS = [
    ("Mercury", swe.MERCURY),
    ("Venus", swe.VENUS),
    ("Mars", swe.MARS),
    ("Jupiter", swe.JUPITER),
    ("Saturn", swe.SATURN),
    ("Uranus", swe.URANUS),
    ("Neptune", swe.NEPTUNE),
    ("Pluto", swe.PLUTO),
]

INNER = {"Mercury", "Venus", "Mars"}
OUTER = {"Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"}


def wrap_deg(values: np.ndarray) -> np.ndarray:
    """Wrap angles to [-180, 180)."""
    return (values + 180.0) % 360.0 - 180.0


def rms(values: np.ndarray, axis: int = 1) -> np.ndarray:
    return np.sqrt(np.mean(np.square(values), axis=axis))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def separated_local_minima(metric: np.ndarray, eligible: np.ndarray, n: int) -> list[int]:
    local = np.zeros(metric.shape[0], dtype=bool)
    local[1:-1] = (metric[1:-1] <= metric[:-2]) & (metric[1:-1] < metric[2:])
    candidates = np.flatnonzero(local & eligible)
    ordered = candidates[np.argsort(metric[candidates])]
    chosen: list[int] = []
    for index in ordered:
        if all(abs(int(index) - previous) >= EPISODE_SEPARATION_DAYS for previous in chosen):
            chosen.append(int(index))
            if len(chosen) == n:
                break
    return chosen


def separated_high_scores(score: np.ndarray, eligible: np.ndarray, n: int) -> list[int]:
    candidates = np.flatnonzero(eligible)
    ordered = candidates[np.argsort(score[candidates])[::-1]]
    chosen: list[int] = []
    for index in ordered:
        if all(abs(int(index) - previous) >= EPISODE_SEPARATION_DAYS for previous in chosen):
            chosen.append(int(index))
            if len(chosen) == n:
                break
    return chosen


def main() -> None:
    output_dir = Path(__file__).resolve().parent
    number_of_days = (TARGET_DATE - START_DATE).days + 1
    dates = [START_DATE + timedelta(days=offset) for offset in range(number_of_days)]
    jds = TARGET_JD_UT - np.arange(number_of_days - 1, -1, -1, dtype=np.float64)

    requested_flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    longitudes = np.empty((number_of_days, len(BODY_SPECS)), dtype=np.float64)
    target_source_state: dict[str, dict[str, float | int]] = {}
    returned_flags: set[int] = set()

    for day_index, jd_ut in enumerate(jds):
        for body_index, (body_name, body_number) in enumerate(BODY_SPECS):
            values, return_flag = swe.calc_ut(float(jd_ut), body_number, requested_flags)
            longitudes[day_index, body_index] = values[0]
            returned_flags.add(int(return_flag))
            if day_index == number_of_days - 1:
                target_source_state[body_name] = {
                    "longitude_deg": values[0],
                    "latitude_deg": values[1],
                    "distance_au": values[2],
                    "returned_flag": int(return_flag),
                }

    pair_names: list[str] = []
    pair_groups: list[str] = []
    pair_columns: list[np.ndarray] = []
    for i, (name_i, _) in enumerate(BODY_SPECS):
        for j in range(i + 1, len(BODY_SPECS)):
            name_j = BODY_SPECS[j][0]
            pair_names.append(f"{name_i}-{name_j}")
            if name_i in INNER and name_j in INNER:
                pair_groups.append("inner")
            elif name_i in OUTER and name_j in OUTER:
                pair_groups.append("outer")
            else:
                pair_groups.append("cross")
            pair_columns.append(wrap_deg(longitudes[:, i] - longitudes[:, j]))

    directed = np.column_stack(pair_columns)
    target_directed = directed[-1]
    directed_residual = wrap_deg(directed - target_directed)
    reflected_residual = wrap_deg(directed + target_directed)
    shell_residual = np.abs(directed) - np.abs(target_directed)

    d_dir = rms(directed_residual)
    d_ref = rms(reflected_residual)
    d_shell = rms(shell_residual)
    d_best_global_lift = np.minimum(d_dir, d_ref)
    coherence_residual = d_best_global_lift - d_shell
    lift_gap = d_dir - d_shell
    branch = np.where(d_dir <= d_ref, "identity", "reflection")

    group_masks = {
        group: np.array([value == group for value in pair_groups], dtype=bool)
        for group in ("inner", "outer", "cross")
    }
    group_metrics: dict[str, np.ndarray] = {}
    for group, mask in group_masks.items():
        group_metrics[f"dir_{group}"] = rms(directed_residual[:, mask])
        group_metrics[f"shell_{group}"] = rms(shell_residual[:, mask])

    eligible = np.ones(number_of_days, dtype=bool)
    eligible[max(0, number_of_days - EXCLUSION_DAYS) :] = False

    directed_indices = separated_local_minima(d_dir, eligible, TOP_N)
    shell_indices = separated_local_minima(d_shell, eligible, TOP_N)

    shell_threshold = float(np.quantile(d_shell[eligible], 0.001))
    non_descent_eligible = eligible & (d_shell <= shell_threshold)
    non_descent_score = coherence_residual / np.maximum(d_shell, 1e-12)
    non_descent_indices = separated_high_scores(non_descent_score, non_descent_eligible, TOP_N)

    pluto_index = [name for name, _ in BODY_SPECS].index("Pluto")
    relative_to_pluto = wrap_deg(longitudes[:, :pluto_index] - longitudes[:, [pluto_index]])
    unwrapped_relative = np.rad2deg(np.unwrap(np.deg2rad(relative_to_pluto), axis=0))

    rows: list[dict[str, object]] = []
    rank_sets = [
        ("DIRECTED_RECURRENCE", directed_indices, d_dir),
        ("SHELL_RECURRENCE", shell_indices, d_shell),
        ("NON_DESCENT_CANDIDATE", non_descent_indices, -non_descent_score),
    ]
    for ranking, indices, ordering_metric in rank_sets:
        sorted_indices = sorted(indices, key=lambda idx: float(ordering_metric[idx]))
        for rank, index in enumerate(sorted_indices, start=1):
            turns = (unwrapped_relative[-1] - unwrapped_relative[index]) / 360.0
            winding = np.rint(turns).astype(int)
            closure = wrap_deg(relative_to_pluto[-1] - relative_to_pluto[index])
            row: dict[str, object] = {
                "run_id": RUN_ID,
                "ranking": ranking,
                "rank": rank,
                "date": dates[index].isoformat(),
                "jd_ut": f"{jds[index]:.10f}",
                "d_dir_deg": f"{d_dir[index]:.9f}",
                "d_ref_deg": f"{d_ref[index]:.9f}",
                "d_shell_deg": f"{d_shell[index]:.9f}",
                "best_global_lift_deg": f"{d_best_global_lift[index]:.9f}",
                "coherence_residual_deg": f"{coherence_residual[index]:.9f}",
                "lift_gap_deg": f"{lift_gap[index]:.9f}",
                "preferred_global_branch": branch[index],
                "non_descent_score": f"{non_descent_score[index]:.9f}",
                "dir_inner_deg": f"{group_metrics['dir_inner'][index]:.9f}",
                "dir_outer_deg": f"{group_metrics['dir_outer'][index]:.9f}",
                "dir_cross_deg": f"{group_metrics['dir_cross'][index]:.9f}",
                "shell_inner_deg": f"{group_metrics['shell_inner'][index]:.9f}",
                "shell_outer_deg": f"{group_metrics['shell_outer'][index]:.9f}",
                "shell_cross_deg": f"{group_metrics['shell_cross'][index]:.9f}",
                "pluto_chart_winding_vector": ";".join(
                    f"{BODY_SPECS[i][0]}:{int(winding[i])}" for i in range(pluto_index)
                ),
                "pluto_chart_max_closure_deg": f"{np.max(np.abs(closure)):.9f}",
            }
            rows.append(row)

    results_path = output_dir / "cta_tg_x773_results.csv"
    with results_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    try:
        package_version = importlib.metadata.version("pyswisseph")
    except importlib.metadata.PackageNotFoundError:
        package_version = "UNAVAILABLE"

    receipt = {
        "run_id": RUN_ID,
        "status": STATUS,
        "governance": {
            "relation_to_prp_0_1": "NEW_EXPLORATORY_RUN; NO REPRODUCTION CLAIM; NO PARAMETER BACKFILL",
            "claim_boundary": "GEOMETRIC DISCOVERY ONLY; NO GLOBAL-SYNCHRONIZATION OR MECHANISM CLAIM",
        },
        "source": {
            "engine": "Swiss Ephemeris through PySwissEph",
            "pyswisseph_distribution_version": package_version,
            "swisseph_python_module_version": getattr(swe, "__version__", "UNAVAILABLE"),
            "swisseph_engine_version": getattr(swe, "version", "UNAVAILABLE"),
            "requested_flags": requested_flags,
            "returned_flags_observed": sorted(returned_flags),
            "effective_ephemeris": "Moshier fallback when returned flag is 260",
            "coordinate_frame": "apparent geocentric tropical ecliptic longitude of date",
            "topocentric_correction": False,
            "sidereal_conversion": False,
        },
        "sampling": {
            "start_date_proleptic_gregorian": START_DATE.isoformat(),
            "end_date_proleptic_gregorian": TARGET_DATE.isoformat(),
            "states": number_of_days,
            "step_days": 1,
            "target_jd_ut": TARGET_JD_UT,
            "daily_sampling_rule": "target_jd_ut minus integer numbers of days",
            "target_neighborhood_excluded_days": EXCLUSION_DAYS,
            "episode_separation_days": EPISODE_SEPARATION_DAYS,
        },
        "body_set_ordered": [name for name, _ in BODY_SPECS],
        "target_source_state": target_source_state,
        "witnesses": {
            "directed": "RMS wrapped residual over all 28 labelled signed pairwise separations",
            "shell": "RMS residual over absolute values of all 28 labelled pairwise separations",
            "reflected_lift": "RMS wrapped residual against the global reflection of the target",
            "coherence_residual": "min(d_dir,d_ref)-d_shell; positive values measure failure of a shell fit to lift to one coherent identity/reflection branch",
            "non_descent_score": "coherence_residual/max(d_shell,1e-12), ranked only within the best 0.1 percent of eligible shell states",
            "transport": "integer winding of seven Pluto-chart relative phases from candidate to target, obtained by daily unwrap",
        },
        "exploratory_choices": {
            "shell_quantile_for_non_descent_candidates": 0.001,
            "shell_threshold_deg_realized": shell_threshold,
            "top_n_each_ranking": TOP_N,
            "inner_bodies": sorted(INNER),
            "outer_bodies": sorted(OUTER),
            "angle_wrap_implementation": "[-180,180)",
        },
        "artifacts": {
            "script": Path(__file__).name,
            "script_sha256": sha256_file(Path(__file__).resolve()),
            "results": results_path.name,
            "results_sha256": sha256_file(results_path),
        },
        "result_summary": {
            "best_directed_date": dates[directed_indices[0]].isoformat(),
            "best_directed_rms_deg": float(d_dir[directed_indices[0]]),
            "best_shell_date": dates[shell_indices[0]].isoformat(),
            "best_shell_rms_deg": float(d_shell[shell_indices[0]]),
            "largest_screened_non_descent_date": dates[non_descent_indices[0]].isoformat(),
            "largest_screened_non_descent_score": float(non_descent_score[non_descent_indices[0]]),
            "shell_best_0_1_percent_threshold_deg": shell_threshold,
        },
    }

    receipt_path = output_dir / "cta_tg_x773_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(receipt["result_summary"], indent=2, sort_keys=True))
    print(f"wrote {results_path}")
    print(f"wrote {receipt_path}")


if __name__ == "__main__":
    main()
