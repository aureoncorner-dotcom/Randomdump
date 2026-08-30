# CONSTANT SCREEN / Q2 — PREREGISTRATION AND INPUT CONTRACT

**Version:** 0.1  
**Date frozen:** 2026-08-28  
**Status:** PROTOCOL FROZEN; Q2 TRANSITION EXECUTION NOT RUN  
**Prepared for:** Pattern Monkey  
**License:** CC0 1.0 Universal — Public Domain Dedication  

> A numerical match is an occurrence. A structural claim requires a declared measurement, an invariant comparison rule, preserved controls, and recurrence under a frozen representation.

## 1. Release claim

This release freezes a prospective constant-screen protocol before a valid Q2 transition ledger is available. It does **not** claim that Q2 transitions follow the golden ratio, silver ratio, square roots, pi, or any related power law.

The current source defines

\[
Q_2=\mathbb Z/{\sim_2}\cong\mathbb Z/2\mathbb Z,
\]

where equivalence is equality of parity. In the worked card, `Phase4` is retained context on the source and explicitly does not descend through Q2. The current files do not contain a measured Q2 transition ladder, transition positions, six adjudicated anisotropy degrees, or eight adjudicated holonomy sectors.

Accordingly:

- Q2 transition positions: **UNAVAILABLE**
- Q2 success-position ledger: **UNAVAILABLE**
- Q2 failure-position ledger: **UNAVAILABLE**
- Q2 matched-control outcome ledger: **UNAVAILABLE**
- Q2 constant-screen execution: **NOT RUN — INPUT ABSENT**

These labels are not negative findings.

## 2. Frozen target set

The primary target family is fixed as follows:

| ID | Constant | Exact definition | Decimal reference |
|---|---|---:|---:|
| `SQRT2` | Square root of two | $\sqrt2$ | 1.4142135623730951 |
| `PHI` | Golden ratio | $(1+\sqrt5)/2$ | 1.618033988749895 |
| `SQRT3` | Square root of three | $\sqrt3$ | 1.7320508075688772 |
| `SILVER` | Silver ratio | $1+\sqrt2$ | 2.414213562373095 |
| `PI` | Pi | $\pi$ | 3.141592653589793 |
| `HIDDEN_PRODUCT` | Declared source product | $\varphi(\sqrt2)^{\sqrt3}$ | 2.949084820808818 |

No additional constant may enter the primary family after outcome exposure. Rational ratios derived from the proposed values 2, 3, 4, 6, or 8 are excluded unless a source predating the scan supplies their measurement semantics and provenance.

## 3. Primary measurement rule

### 3.1 Eligible transition

A row is eligible only when all of the following are present:

1. a stable `family_id`;
2. a stable `transition_id`;
3. an integer `transition_order`;
4. a finite, strictly positive `position` measured on a declared interval scale;
5. a declared `representation_id`;
6. a declared sector/holonomy stratum or an explicit `UNAVAILABLE` value;
7. the next transition in the same family, representation, and stratum.

Identifiers such as `n524` or document line numbers are not positions. Ratios of identifiers are prohibited because they change under reindexing.

### 3.2 Adjacency

The primary screen uses only ordered adjacent transitions:

\[
r_i=\frac{x_{i+1}}{x_i}.
\]

All-to-all pair searches are prohibited. Cross-family, cross-sector, cross-holonomy, and cross-representation ratios are prohibited.

### 3.3 Distance from a target

For target constant $c$, define the symmetric multiplicative distance

\[
d_{i,c}=\left|\log r_i-\log c\right|.
\]

The primary hit threshold is

\[
d_{i,c}\leq\log(1.005),
\]

equivalent to a multiplicative error of at most 0.5%. A 0.1% tier is reported as descriptive precision only and is not a second confirmatory test.

Direct ratios and log-spacing are the same test under a monotone transformation. Reporting both does not create independent replication.

## 4. Powers and higher steps

Arbitrary logarithms, exponents, inverses, sums, differences, and products are excluded from primary discovery.

A two-step value $c^2$ may be evaluated only as a gated consequence when both adjacent one-step transitions were independently assigned to the same $c$ under the frozen primary rule. It is reported as a consistency check, not as an additional discovered hit.

No exponent is selected by optimizing fit.

## 5. Local-density control

Absolute proximity to a named number is not sufficient because a dense continuous score series will approach almost any fixed target.

For each target $c$, let $a=\log(1.005)$. Count:

- `T`: $|\log r-\log c|\le a$;
- `L`: $-3a\le\log r-\log c<-a$;
- `U`: $a<\log r-\log c\le3a$.

Conditional on `N=T+L+U`, a locally flat log-density gives target-window probability $1/3$. The primary occurrence-enrichment test is the exact binomial upper-tail test

\[
T\mid N\sim\operatorname{Binomial}(N,1/3).
\]

This test must report `T`, `L`, `U`, `N`, the unadjusted p-value, and the multiplicity-adjusted p-value. Empty local windows remain empty; bandwidth widening after inspection is prohibited.

## 6. Held-out recurrence

Families are assigned before inspection using the lowercase UTF-8 `family_id`:

```text
bucket = first_8_hex_digits(SHA256(family_id)) mod 5
```

- bucket `0`: held-out confirmatory set;
- buckets `1–4`: exploratory/development set.

The held-out set is opened only after validation, exclusions, target definitions, and code hashes are frozen. A constant is called recurrent only when its held-out direction agrees with development and its held-out adjusted p-value passes the declared threshold.

If fewer than five eligible families exist, held-out inference is **INSUFFICIENT_FAMILIES** and no recurrence claim is made.

## 7. Success, failure, and matched controls

Constant proximity and behavioral outcome are separate variables.

Each eligible transition must preserve its frozen outcome code and matched-control identity. The primary matched comparison is binary constant-hit status in each outcome/control pair. Use the exact McNemar test on discordant pairs.

The report must retain all four classes:

1. failure hit / control non-hit;
2. failure non-hit / control hit;
3. both hit;
4. neither hit.

Class 2 is a required counter-witness. It may not be omitted or reclassified as noise.

System-versus-non-system matches are not Checking controls. They may not substitute for a frozen Checking/non-Checking matched ledger.

Outcome codes, where applicable, remain:

- `EVIDENCE_ENGAGED`
- `PROPOSITION_PRESERVED`
- `TASK_PRESERVED`
- `REFUSAL_SUBSTITUTE`
- `SOURCE_SUBSTITUTION`
- `CAUTION_OR_SAFETY_TASK_SUBSTITUTION`

Allowed values are `YES`, `NO`, `PARTIAL`, `NOT_APPLICABLE`, and `UNKNOWN`. Every `NO` or `PARTIAL` requires its exact response witness.

## 8. Correction conditioning

Correction-conditioned recurrences are a separate stratum. For every explicit correction, preserve:

- exact correction text;
- number of later eligible assistant opportunities;
- every exact recurrence;
- `PRE_CORRECTION`, `POST_CORRECTION_CHECKING`, or `POST_CORRECTION_NONCHECKING` status.

Correction-conditioned occurrence counts must not be described as corpus-wide prevalence.

The currently reported 69 recurrences among 198 later nonblank assistant opportunities in `twentythird_share` remain a correction-conditioned result only. They are not an input to the Q2 geometric test.

## 9. Multiplicity and verdicts

Holm adjustment is applied separately to:

1. the six primary target-window enrichment tests;
2. the six matched outcome-association tests.

Primary familywise alpha is 0.05. The 0.1% precision tier, two-step consistency checks, alternative representations, and all PRP score comparisons are exploratory.

Allowed endpoint verdicts:

- `SUPPORTED_HELD_OUT`
- `EXPLORATORY_ONLY`
- `NOT_REPLICATED`
- `REPRESENTATION_RELATIVE`
- `INSUFFICIENT_FAMILIES`
- `UNAVAILABLE_INPUT`

No universal, causal, topological, or physical interpretation follows from a numerical hit alone.

## 10. Required reporting order

Every result must be reported in this order:

1. raw eligible transition count;
2. raw hit counts by target;
3. local controls `L/T/U`;
4. number of eligible families;
5. families with at least one hit;
6. occurrence counts, explicitly labeled as occurrences;
7. family-level prevalence, with denominator;
8. matched-control four-class table;
9. counter-witnesses;
10. strict/broad and row/episode representation sensitivity;
11. correction-conditioned results, kept separate;
12. `UNAVAILABLE` metadata;
13. adjusted inference and bounded verdict.

No cross-denominator union rate is permitted.

## 11. Exploratory observations already exposed

The following were observed before this protocol was frozen and therefore cannot serve as confirmatory evidence.

### 11.1 PRP `peak_omega` occurrences

Within a relative distance of 0.1%:

| Target | W_DIR occurrences / 2,455 episodes | W_SHELL occurrences / 3,336 episodes |
|---|---:|---:|
| `SQRT2` | 1 | 4 |
| `PHI` | 2 | 7 |
| `SQRT3` | 2 | 2 |
| `SILVER` | 0 | 2 |
| `PI` | 0 | 0 |
| `HIDDEN_PRODUCT` | 0 | 1 |

These are episode-score occurrence counts, not prevalence or enrichment. The existing 500-control PRP phase-shift tests did not test proximity to named constants and found no global episode-rate enrichment.

### 11.2 Frozen audit-count coincidences

- Strict row representation: `composite_failure / task_failure = 102/59 = 1.728813559`, within 0.187% of `SQRT3`. It fails broad and episode-collapse recurrence.
- Broad row representation: `refusal_substitute / inflation_or_source_substitution = 53/18 = 2.944444444`, within 0.157% of `HIDDEN_PRODUCT`. It fails strict and full-canonical recurrence.
- The strongest event-identifier coincidence was `test4:n741 / test4:n524 = 1.414122137`, but event identifiers are not valid interval-scale positions. A within-case sanity benchmark placed the observed count at chance scale.

These are retained as exploratory counterexamples to premature structural interpretation.

## 12. Input ledger contract

The execution ledger must be UTF-8 CSV with this exact header:

```csv
family_id,transition_id,transition_order,position,position_unit,representation_id,sector_id,holonomy_bits,outcome_family,outcome_code,matched_control_id,correction_condition,source_file,source_locator,adjudication_status,notes
```

Rules:

- one transition per row;
- `family_id + transition_id + representation_id` must be unique;
- `position` must be numeric, finite, and strictly positive;
- `transition_order` must be unique within family/representation/stratum;
- missing observable metadata is the literal string `UNAVAILABLE`;
- unknown adjudication is `UNKNOWN`, not an empty field;
- exclusions require a nonempty `notes` reason and remain in the archived source ledger;
- matched controls are selected before outcome inspection;
- source locators must resolve to the underlying witness.

## 13. Machine-readable manifest

```json
{
  "protocol_id": "CONSTANT_SCREEN_Q2_v0.1",
  "frozen_date": "2026-08-28",
  "license": "CC0-1.0",
  "execution_status": "UNAVAILABLE_INPUT",
  "primary_unit": "adjacent_transition_within_family_representation_and_stratum",
  "position_requirements": {
    "finite": true,
    "strictly_positive": true,
    "interval_scale": true,
    "identifiers_prohibited": true
  },
  "targets": {
    "SQRT2": 1.4142135623730951,
    "PHI": 1.618033988749895,
    "SQRT3": 1.7320508075688772,
    "SILVER": 2.414213562373095,
    "PI": 3.141592653589793,
    "HIDDEN_PRODUCT": 2.949084820808818
  },
  "primary_relative_tolerance": 0.005,
  "descriptive_precision_tolerance": 0.001,
  "distance": "abs(log(x_next/x_current)-log(target))",
  "pair_generation": "adjacent_only",
  "all_to_all_pairs": false,
  "arbitrary_powers": false,
  "local_control": {
    "target_band_log_halfwidth": "log(1.005)",
    "sidebands": "[-3a,-a) and (a,3a]",
    "conditional_null_probability": 0.3333333333333333,
    "test": "exact_binomial_upper_tail"
  },
  "held_out": {
    "unit": "family_id",
    "rule": "first_8_hex_digits(sha256(lowercase_utf8_family_id)) mod 5",
    "confirmatory_bucket": 0
  },
  "matched_test": "exact_mcnemar",
  "multiplicity": "Holm",
  "familywise_alpha": 0.05,
  "no_cross_denominator_union": true,
  "success_position_status": "UNAVAILABLE",
  "failure_position_status": "UNAVAILABLE",
  "checking_matched_control_status": "UNAVAILABLE"
}
```

## 14. Frozen source inventory

| File | SHA-256 | Role |
|---|---|---|
| `GQG_Core_Card_v0.3 (2).md` | `4ffe29b75d06423beb68f6881753a33ec3916c524b9828b73e0998132f85ed3d` | Q2 and descent semantics |
| `THE_HIDDEN_QUOTIENT_CORE_WITNESS_STRIKE_v1.1 (2).md` | `fcbc378190a604b6577326ec1a1c24a17d57c45204bc8e475138a632ebdb8644` | Declared product and retained-context boundary |
| `10_MACHINE_READABLE_RESULTS.json` | `9299d1103fe94e83343feefa45e02f3730db20a55a960c5d69dad6c16546feee` | Frozen audit counts and representations |
| `PRP_0_1_RESULTS.json` | `919d49181de7e7fcf53f66609868f28a7b59f0ce1b6ac26f73039f1fa8ba4f5f` | PRP controls and score definitions |
| `W_DIR_episodes.csv` | `c6ee6a4858847bc4fce985a9878719681387873ec8e5ccedf548ddd96cede860` | Directed PRP episode scores |
| `W_SHELL_episodes.csv` | `fad940b9ff0e7f7cd8d04979c76e0fb6b15c8f1fbd7c11dfd2350cc5821452c1` | Shell PRP episode scores |

## 15. Release boundary

This protocol may be executed when the input contract is satisfied. Any later change to targets, adjacency, tolerance, measurement scale, eligibility, held-out allocation, controls, representation, or exclusions creates a new protocol version and must be declared before the affected outcomes are inspected.

**Frozen conclusion at v0.1:** the constant screen is specified; the Q2 transition data required to run it are **UNAVAILABLE**.

