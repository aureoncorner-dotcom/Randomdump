#!/usr/bin/env python3
"""CC0 — Anonymous. Fulgurite design calculation; no specimen data.

Run: python run_analysis.py
Optional independent verification and figure:
  python run_analysis.py --verify --plot
Core calculation uses Python standard library. Verification uses SciPy;
the optional figure uses NumPy and Matplotlib. No network requests.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import platform
from fractions import Fraction
from itertools import product
from pathlib import Path


def compatible_interval(d, error_bound, nuisance_bound, recovery_min, recovery_max):
    """Exact projection for d = r*v + eta + error, v >= 0.

    |error| <= error_bound, |eta| <= nuisance_bound,
    0 < recovery_min <= r <= recovery_max <= 1.
    These are specified hard envelopes, not statistical confidence intervals.
    Return None if no nonnegative amount is compatible with the inputs.
    """
    values = (d, error_bound, nuisance_bound, recovery_min, recovery_max)
    if not all(math.isfinite(x) for x in values):
        raise ValueError("All inputs must be finite.")
    if error_bound < 0 or nuisance_bound < 0:
        raise ValueError("Uncertainty envelopes must be nonnegative.")
    if not 0 < recovery_min <= recovery_max <= 1:
        raise ValueError("A positive, bounded recovery interval within (0, 1] is required.")
    numerator_low = d - error_bound - nuisance_bound
    numerator_high = d + error_bound + nuisance_bound
    if numerator_high < 0:
        return None
    return (max(0.0, numerator_low) / recovery_max,
            numerator_high / recovery_min)


def same_readout_examples():
    # Values are constructed, normalized, and exact; they are not assays.
    cases = [
        ("Pre-existing gas", Fraction(1), Fraction(0), Fraction(0)),
        ("Other-host release", Fraction(0), Fraction(1), Fraction(0)),
        ("Species formed during extraction", Fraction(0), Fraction(0), Fraction(1)),
        ("Mixed contributions", Fraction(2, 5), Fraction(3, 10), Fraction(3, 10)),
    ]
    rows = []
    for label, retained, other, generated in cases:
        readout = retained + other + generated
        if readout != 1:
            raise AssertionError("Constructed counterexample does not have the stated readout.")
        rows.append({"case": label, "preexisting_gas": float(retained),
                     "other_host_release": float(other),
                     "species_formed_during_extraction": float(generated),
                     "measured_signal": float(readout)})
    return rows


def verify_with_linear_programming():
    """Independently optimize v without implementing the closed-form bounds.

    Existence of r in [rlo, rhi] is equivalent to
    rlo*v + eta + error <= d <= rhi*v + eta + error.
    This produces a linear feasibility/minimum/maximum problem.
    """
    import scipy
    from scipy.optimize import linprog
    tested = feasible = infeasible = 0
    max_error = 0.0
    for d, e, q, recovery in product(
        [-2.0, -0.2, 0.0, 0.3, 1.0], [0.0, 0.1],
        [0.0, 0.25, 1.0], [(0.8, 1.0), (0.5, 0.5)]
    ):
        rlo, rhi = recovery
        expected = compatible_interval(d, e, q, rlo, rhi)
        kwargs = dict(A_ub=[[rlo, 1, 1], [-rhi, -1, -1]],
                      b_ub=[d, -d], bounds=[(0, None), (-q, q), (-e, e)],
                      method="highs")
        lo = linprog([1, 0, 0], **kwargs)
        hi = linprog([-1, 0, 0], **kwargs)
        tested += 1
        if expected is None:
            if lo.status != 2 or hi.status != 2:
                raise AssertionError(("Infeasibility mismatch", d, e, q, recovery))
            infeasible += 1
        else:
            if not (lo.success and hi.success):
                raise AssertionError(("Optimization failed", lo.message, hi.message))
            discrepancy = max(abs(expected[0] - lo.x[0]), abs(expected[1] - hi.x[0]))
            if discrepancy > 1e-9:
                raise AssertionError(("Bound mismatch", discrepancy, d, e, q, recovery))
            max_error = max(max_error, discrepancy)
            feasible += 1
    return {"status": "PASS", "method": "Independent linear programming projection",
            "cases": tested, "feasible": feasible, "infeasible": infeasible,
            "maximum_absolute_difference": max_error, "tolerance": 1e-9,
            "scipy_version": scipy.__version__}


def make_figure(out, examples, assumptions):
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, (left, right) = plt.subplots(1, 2, figsize=(13.6, 7.0), gridspec_kw={"width_ratios": [1, 1.05]})
    fig.patch.set_facecolor("#faf8f2")
    for ax in (left, right):
        ax.set_facecolor("#faf8f2")
    fig.suptitle("What did the fulgurite hold?", fontsize=23, fontweight="bold", x=0.065, ha="left", y=0.975)
    fig.text(0.065, 0.905, "DESIGN CALCULATION  /  All gas values below are illustrative assumptions.", fontsize=10, color="#575b5b")
    colors = ["#187f7c", "#d99c35", "#aa6870"]
    y = np.arange(4)
    accum = np.zeros(4)
    keys = ["preexisting_gas", "other_host_release", "species_formed_during_extraction"]
    labels = ["Pre-existing gas", "Other-host release", "Formed during extraction"]
    for key, label, color in zip(keys, labels, colors):
        values = np.array([row[key] for row in examples])
        left.barh(y, values, left=accum, color=color, label=label, height=0.55)
        accum += values
    left.set_yticks(y, ["Gas", "Other host", "Extraction product", "Mixture"])
    left.invert_yaxis()
    left.set_xlim(0, 1.1)
    left.set_xticks([0, 0.5, 1])
    left.set_xlabel("Same measured signal (arbitrary units)")
    left.set_title("Four explanations, one readout", loc="left", fontsize=13, fontweight="bold", pad=18)
    left.legend(loc="upper left", bbox_to_anchor=(-0.02, -0.17), frameon=False, fontsize=10)

    q = np.linspace(0, 1, 201)
    intervals = np.array([compatible_interval(assumptions['observed_contrast'],
        assumptions['measurement_error_bound'], float(v),
        assumptions['recovery_min'], assumptions['recovery_max']) for v in q])
    right.fill_between(q, intervals[:, 0], intervals[:, 1], color="#cde3df", alpha=0.8)
    right.plot(q, intervals[:, 0], color=colors[0], linewidth=2.5, label="Minimum compatible amount")
    right.plot(q, intervals[:, 1], color=colors[0], linewidth=1.3, linestyle="--", label="Maximum compatible amount")
    right.axvline(0.9, color="#81555c", linestyle=":", linewidth=1.6)
    right.annotate("Zero becomes compatible\nat nuisance bound 0.9", xy=(0.9, 0), xytext=(0.4, 0.55),
                   arrowprops={"arrowstyle": "->", "color": "#81555c"}, fontsize=10, color="#704850")
    right.set_xlim(0, 1)
    right.set_ylim(-0.04, 2.75)
    right.set_xlabel("Bound on unmatched contribution (q)")
    right.set_ylabel("Compatible pre-existing gas amount")
    right.set_title("Controls determine the remaining range", loc="left", fontsize=13, fontweight="bold", pad=18)
    right.grid(axis="y", alpha=0.15)
    right.legend(loc="upper left", bbox_to_anchor=(-0.02, -0.17), frameon=False, fontsize=10)
    fig.text(0.065, 0.065, "Right: sealed−open contrast = 1; measurement error ≤ 0.1; recovery = 0.8–1.0.\nRanges follow those assumed bounds. They are not confidence intervals or specimen measurements.", fontsize=10, color="#575b5b")
    fig.subplots_adjust(left=0.14, right=0.97, top=0.79, bottom=0.34, wspace=0.42)
    fig.savefig(out / "Fulgurite_Design_Test.png", dpi=170, facecolor=fig.get_facecolor())
    plt.close(fig)
    return {"numpy": np.__version__, "matplotlib": matplotlib.__version__}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).with_name("inputs.json"))
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("results"))
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--plot", action="store_true")
    args = parser.parse_args()
    raw = args.input.read_bytes()
    inputs = json.loads(raw)
    a, p = inputs["illustration"], inputs["published_arithmetic"]
    if a["input_status"] != "ILLUSTRATIVE_ASSUMPTIONS":
        raise ValueError("This version is explicitly a design illustration, not a laboratory data analyzer.")
    examples = same_readout_examples()
    rows = []
    for q in a["nuisance_bounds"]:
        interval = compatible_interval(a["observed_contrast"], a["measurement_error_bound"],
                                      q, a["recovery_min"], a["recovery_max"])
        rows.append({"nuisance_bound": q, "compatible_min": interval[0] if interval else None,
                     "compatible_max": interval[1] if interval else None,
                     "zero_compatible": bool(interval and interval[0] == 0)})
    baseline = Fraction(str(p["normalized_parent_baseline"]))
    arithmetic = {}
    for region in ("rim", "core"):
        observed = Fraction(str(p["fulgurite_" + region]))
        percent = (baseline - observed) / baseline * 100
        arithmetic[region] = {"calculated_percent": float(percent),
                              "exact_percent": str(percent),
                              "authors_rounded_percent": p["authors_rounded_percent"][region],
                              "rounded_agreement": round(float(percent)) == p["authors_rounded_percent"][region]}
    if not all(row["rounded_agreement"] for row in arithmetic.values()):
        raise AssertionError("Published arithmetic does not match.")
    result = {"title": inputs["project"], "version": inputs["version"], "date_utc": inputs["date_utc"],
              "calculation_status": "EXECUTED", "specimen_measurement_status": "NOT_MEASURED",
              "assumption_status": a["input_status"], "python": platform.python_version(),
              "input_sha256": hashlib.sha256(raw).hexdigest(),
              "published_arithmetic_replay": arithmetic, "same_readout_examples": examples,
              "compatible_ranges": rows,
              "positive_lower_bound_condition": "observed_contrast > measurement_error_bound + nuisance_bound",
              "independent_verification": verify_with_linear_programming() if args.verify else {"status": "NOT_RUN"}}
    args.out.mkdir(parents=True, exist_ok=True)
    if args.plot:
        result["plot_libraries"] = make_figure(args.out, examples, a)
    (args.out / "results.json").write_text(json.dumps(result, indent=2) + "\n")
    with (args.out / "compatible_ranges.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
