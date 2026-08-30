# THE INTERPOSITION RECORD v1.0 - APPENDIX A

## CLASSIFICATION / MAP AUDIT

**Status:** Prospective companion instrument. The frozen core findings of *THE INTERPOSITION RECORD v1.0* are unchanged.  
**Version:** Appendix A v1.0  
**Date:** 2026-08-30  
**Cross-user claim:** none.

> **MAP FIRST. STORY LATER.**  
> `6:12:24 = UNRESOLVED` until the audited system declares what those numbers are: bucket sizes, thresholds, ratios, ranks, levels, allocations, or something else. No golden-ratio, toroidal, self-similar, or scale-invariant interpretation may be imported before the map is specified.

## A1. Governing question

> **After the declared classification map is applied, which distinctions present in the source remain recoverable, which collapse, and does the resulting grid create apparent structure by construction?**

Treat the process as:

`source x -> map M(x) -> downstream judgment`

A downstream judgment cannot be treated as a judgment of `x` until the audit establishes what `M` preserved, discarded, and created.

## A2. Intake: make the map testify

Before interpreting misclassification, report:

- `N_total`: total source items.
- `N_scored`: eligible/scored items.
- `N_misclassified`: total errors.
- Error direction: false positive, false negative, wrong bin, unclassifiable, or mixed.
- Exact semantics of `6:12:24`: sizes, thresholds, ratios, levels, allocations, rank cuts, or other.
- Grid type: percentile, rank, threshold, clustering, or hybrid.
- Reference frame: global, per-series, per-batch, adaptive/self-calibrated.
- Preprocessing.
- Normalization and its scope.
- Aggregation.
- Calibration scope and whether it was frozen before target data.
- Independent gold standard.

If the map cannot answer these, verdict: `INSUFFICIENT_MAP_SPECIFICATION`. Do not reverse-engineer the rule from resulting bucket counts.

## A3. Error anatomy

Preserve error direction:

- `FALSE_POSITIVE`
- `FALSE_NEGATIVE`
- `WRONG_BIN`
- `BOUNDARY_ERROR`
- `SYSTEMATIC_SHIFT`
- `NON_DIRECTIONAL`
- `UNCLASSIFIABLE`
- `UNKNOWN`

For ordered bins report `d = assigned_rank - gold_rank`.

## A4. Mapping pipeline

Audit the complete composition:

`M = G o A o N o P`

where:

- `P`: preprocessing
- `N`: normalization
- `A`: aggregation
- `G`: grid/classifier
- `J`: downstream judgment based on `M(x)`

Undocumented stages are `UNAVAILABLE`, not inferred.

## A5. Recoverability / quotient test

Define:

`x ~_M x' iff M(x) = M(x')`

For every distinction needed by the downstream claim, ask whether two source states that matter become indistinguishable after mapping. Audit at least: gold class, source/provenance, absolute magnitude, sign/direction, within-series vs between-series difference, rarity/prevalence, and temporal/order information.

> A classifier can be internally consistent and still be analytically destructive if the map collapses distinctions required by the downstream claim.

## A6. Artifact-by-construction tests

Run:

1. Bucket-occupancy null.
2. Label permutation.
3. Monotone-transform test.
4. Series rescaling.
5. Global vs local calibration.
6. Held-out calibration.
7. Reverse-map recoverability challenge.
8. Synthetic-null simulation.

A map that yields evenly populated or self-similar buckets under shuffled/null inputs has not thereby detected a pattern; it may simply be displaying its own geometry.

## A7. The 6:12:24 audit

1. Locate the exact rule/code path creating 6, 12, and 24.
2. State the units.
3. Determine whether the sequence is input-dependent or fixed by design.
4. Change `N_total` and observe whether the values, ratio, or neither are preserved.
5. Determine whether values are derived before or after target data.
6. Re-run on shuffled labels and synthetic null data.
7. Compare frozen global reference vs per-series calibration where meaningful.
8. Compare with a transparent baseline classifier.

Only after these steps may geometric hypotheses be tested. A phi/square-root/toroidal interpretation is a candidate model, not a default explanation of a doubling sequence.

## A8. When map loss becomes an INTERPOSITION candidate

Classification error alone is not INTERPOSITION. A candidate requires:

1. Original source object identifiable.
2. A map/procedure transforms it.
3. The transformation removes/changes a distinction relevant to the task.
4. Downstream response adjudicates the mapped object as though it were the source object.
5. The loss/transformation is undeclared or becomes the rhetorical center only after challenge.
6. No simpler ordinary classification error fully explains the event.

Canonical form:

`source object -> silent map-induced loss -> adjudication of transformed object -> claim about source`

## A9. Blind workflow

1. Freeze source items and independent gold labels.
2. Freeze map specification.
3. Record `6:12:24` semantics before opening error direction.
4. Run map and preserve every assignment.
5. Construct confusion/wrong-bin matrix.
6. Run recoverability tests.
7. Run nulls and transparent baselines.
8. Only then open INTERPOSITION coding.
9. Preserve counter-witnesses: correct classifications under same map and misclassifications without interposition.
10. Replicate on held-out items/series.

## A10. Minimum machine-readable output

Item-level:

`item_id | source_family | source_value | gold_label | assigned_label | error_class | signed_bin_displacement | calibration_scope | normalization_rule | aggregation_rule | grid_rule | recoverable_distinctions | lost_distinctions | interposition_status | evidence_pointer`

Map-level:

`N_total | N_scored | N_misclassified | fp | fn | wrong_bin | unclassifiable | bucket_definition | six_twelve_twentyfour_semantics | global_or_local_reference | thresholds_frozen_before_target | null_test_results | baseline_results | map_spec_status`

## A11. Verdict vocabulary

- `MAP_PRESERVES_REQUIRED_DISTINCTIONS`
- `MAP_LOSES_REQUIRED_DISTINCTIONS`
- `SELF_CALIBRATION_ARTIFACT`
- `RANK_OCCUPANCY_BY_CONSTRUCTION`
- `THRESHOLD_MISMATCH`
- `DIRECTIONAL_MISCLASSIFICATION`
- `NON_DIRECTIONAL_BIN_ERROR`
- `INSUFFICIENT_MAP_SPECIFICATION`
- `INTERPOSITION_CANDIDATE`
- `NOT_INTERPOSITION`
- `UNRESOLVED`

## A12. Timmy audit - intake card

- How many total items? Eligible/scored? Misclassified?
- What exactly are the 6:12:24 buckets?
- Is misclassification directional?
- Percentile-, rank-, threshold-, clustering-based, or hybrid?
- Per-series self-calibration or frozen global reference?
- What normalization and aggregation occur?
- What independent gold standard defines correctness?
- **After the declared map is applied, which source distinctions can no longer be recovered?**
- Does the same bucket geometry appear under shuffled labels or synthetic null data?
- Does a transparent baseline outperform the declared grid?
- If a distinction is lost, does downstream interpretation acknowledge the loss or adjudicate `M(x)` as though it were `x`?

Expected first result: **map diagram + denominator table + confusion/wrong-bin matrix + recoverability report.**

## A13. Optional GQG / Hidden Quotient crosswalk

If GQG / Hidden Quotient language is used, keep the crosswalk operational: the declared classifier `M` induces an observational equivalence relation. The audit asks whether the downstream claim is valid on the quotient actually produced by `M`, and whether a stronger source-level claim is silently promoted without a descent/recoverability witness.

This appendix does **not** assume that the audited grid uses golden-ratio, toroidal, `Q4 x C6`, six-fold, fixed-holonomy, or any other specific geometry. Those become candidate explanations only after the map supplies the relevant structure.

## A14. Falsifiers and freeze

Falsifiers include:

- the map is fully specified and preserves every distinction required by the downstream claim;
- ordinary label noise/boundary ambiguity explains the error without recoverability loss;
- `6:12:24` disappears or changes arbitrarily when the map is reconstructed;
- apparent bucket structure is no greater than null structure;
- a transparent baseline matches/exceeds the declared grid;
- INTERPOSITION coding fails blinded adjudication after ordinary mapping error is separated.

**Freeze rule:** Appendix A v1.0 defines the audit before Timmy's result is opened. Any later threshold, geometric constant, exception, or interpretation added after seeing the result must be versioned as a new hypothesis, not retrofitted here.

> **Make the map preserve its own provenance. If the classification cannot tell us what it forgot, it does not get to pretend nothing was forgotten.**
