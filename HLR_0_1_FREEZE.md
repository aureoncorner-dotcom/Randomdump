# Historical Ledger and Join Protocol — HLR-0.1

**Status:** FROZEN HISTORICAL-SIDE SPECIFICATION — no geometry join performed  
**Created:** 2026-08-27  
**Purpose:** Define the historical witness, source universes, inclusion rules, temporal precision, deduplication, controls, and join/test architecture *before* any PRP-0.1 detector row is compared with an event record.

## 0. Hard separation

Three objects remain separate:

1. **Geometry ledger (`G`)** — PRP-0.1 detector outputs. Not read or annotated during construction of HLR-0.1.
2. **Historical ledger (`H`)** — independently sourced events defined by this document.
3. **Join/test (`J`)** — a separately executed comparison after `H` has been materialized and hashed.

A detector timestamp is never an event claim.  
An event timestamp is never a geometry claim.  
No event name, category, source, or severity may be written into a geometry row.

The only permitted combination is a later typed join of already-frozen objects.

## 1. Historical witness

The canonical event record is:

```text
HistoricalEvent = (
    source_id,
    source_record_id,
    event_family,
    event_subtype,
    start_time_lower,
    start_time_upper,
    end_time_lower,
    end_time_upper,
    time_precision,
    location_scope,
    severity_primary,
    severity_secondary,
    source_version,
    source_record_hash,
    inclusion_rule_id
)
```

No field may contain a PRP module ID, PRP rank, PRP score, planetary angle, detector episode ID, or geometry-derived label.

## 2. Closed source universes

HLR-0.1 uses only the source universes listed in `historical_source_registry.csv`.

Source selection was made from public dataset documentation before any event-level join. A later source may be added only by issuing HLR-0.2 or a formally versioned amendment **before** opening its overlap with PRP.

Primary source families:

- EM-DAT public disaster database.
- UCDP Georeferenced Event Dataset (GED) v26.1.
- Global Terrorism Database (GTD) 1970–2020.
- Correlates of War (COW) war datasets.
- Correlates of War Militarized Interstate Disputes (MID) v5.0.
- Laeven–Valencia Systemic Banking Crises Database 1970–2025.

These remain separate historical witnesses. They are not silently merged into one category called “historically notable.”

## 3. Inclusion rule

### 3.1 General rule

For every source:

1. Include every row/event that belongs to the frozen released dataset under that source's own inclusion criteria.
2. Do not add an event because a geometry date is interesting.
3. Do not delete an event because it fails to overlap geometry.
4. Do not raise or lower severity thresholds after a join.
5. Preserve the source's category labels. Any cross-source harmonized label is secondary and must be derived by a frozen mapping table.
6. Preserve unknown or partial dates as unknown/partial. No temporal component is imputed from narrative knowledge.
7. Every transformed row keeps the original source record identifier and a hash of the source row or canonical source representation.

### 3.2 No free-form notability

The following inclusion predicate is prohibited:

> “Historically important/notable.”

A record must enter through a frozen source universe and its documented inclusion rules.

## 4. Source-specific transforms

### 4.1 EM-DAT

Primary unit: disaster event, not country-impact row.

EM-DAT's public table can contain multiple country impacts for one disaster. Collapse records sharing the base disaster identifier to one event **without using geometry**.

Frozen onset rule:
- start = earliest source-declared start bound among impacts belonging to the same disaster;
- end = latest source-declared end bound among those impacts;
- missing day/month components remain missing;
- severity fields may aggregate across impacts only by a separately recorded deterministic sum/max rule appropriate to the field.

Primary HLR test uses disaster onset, not every day of a long disaster.

### 4.2 UCDP GED

Primary unit: one GED event.

Include all global GED events in v26.1.  
Primary daily historical series: number of GED events whose source-declared event date falls on that day.  
Fatality measures may be retained as secondary series only according to the GED codebook; no fatality threshold is used for primary inclusion.

### 4.3 GTD

Primary unit: one GTD incident.

Include all distributed GTD incidents for 1970–2020 subject to the dataset's own coding.  
The known missing 1993 incident file is a structural coverage gap and must remain explicitly missing.

Primary daily historical series: incident count.  
Incomplete day/month components are not imputed.

Raw GTD data are subject to START's terms and are not redistributed in the HLR bundle.

### 4.4 COW wars

Each COW war dataset remains its own source witness (Inter-State, Extra-State, Non-State, Intra-State).

Primary unit: war onset.  
A continuing war contributes one primary onset record, not one event for every day/year of duration.

Source-declared start precision is retained exactly. No retrospective “first important battle” substitution is allowed.

### 4.5 COW MID

Primary unit: one militarized interstate dispute onset.

All MID v5.0 disputes are retained.  
Primary series uses dispute onset only. Duration is a separate secondary exposure variable.

### 4.6 IMF systemic banking crises

Primary unit: one systemic banking-crisis episode in the 2026 Laeven–Valencia release covering 1970–2025.

Primary series uses the source-declared crisis starting date at its native precision.  
If a crisis is only dated to year or month, it is **not** promoted to a daily timestamp.

## 5. Temporal precision

Every event is represented by an interval `[start_time_lower, start_time_upper]`.

Frozen precision classes:

| precision | interval representation | primary join resolution |
|---|---|---|
| minute | exact minute ± source uncertainty if given | minute/hour |
| hour | containing hour | hour |
| day | UTC civil day `[00:00,24:00)` unless source supplies local time | day |
| month | full calendar month | month |
| year | full calendar year | year |
| range | source-declared range | matching native interval |

No year-only or month-only event can score a minute-level coincidence.

## 6. Geometry witnesses stay separate

The geometry side contains at least:

- `W_DIR` — directed/handed circuit witness.
- `W_SHELL` — handedness-forgetting shell witness.

HLR-0.1 defines historical witnesses `W_HIST[source_id]`.

Permitted later conjunctions:

```text
W_DIR   AND W_HIST[source]
W_SHELL AND W_HIST[source]
```

Prohibited substitutions:

```text
W_DIR   => W_HIST
W_SHELL => W_HIST
W_HIST  => W_DIR
```

Historical information cannot alter PRP rank, Ω, K, module membership, episode bounds, or detector prose.

## 7. Primary join rule

### 7.1 Daily-capable historical sources

For events with day or finer precision, the primary overlap is **interval intersection**:

```text
geometry_episode_interval ∩ historical_event_onset_interval != ∅
```

No ±N-day halo is used in the primary test.

A separately reported sensitivity family may use ±1 day and ±3 days, but all such windows must be reported together and cannot replace the zero-halo primary result.

### 7.2 Month/year precision

Month-precision records are compared only to geometry aggregated to month.  
Year-precision records are compared only to geometry aggregated to year.

Aggregation function is frozen as:

```text
max geometry episode score within the native historical interval
```

plus a secondary exposure measure:

```text
number of geometry-episode days within the historical interval
```

Daily geometry is never presented as an exact-date match to a year-only historical record.

## 8. Primary statistical lanes

No omnibus pooling is permitted before source-specific results are computed.

### Lane A — sparse onset sources
Applies to COW wars, MID onsets, EM-DAT event onsets where daily sparsity permits.

Primary statistic:
- overlap count between frozen PRP episodes and source event onsets.

Null:
- circularly shift the complete historical onset series within the source's contiguous coverage by a uniformly sampled integer offset;
- minimum absolute shift: 366 days for daily sources;
- preserve the geometry ledger unchanged;
- 100,000 shifts for final inference.

### Lane B — dense daily event sources
Applies to UCDP GED and GTD.

Primary statistic:
- mean historical daily event count on geometry-episode days minus mean on non-episode days.

Secondary:
- rank correlation between daily historical count and frozen geometry Ω/K series.

Null:
- circular shift of the complete historical daily series;
- minimum absolute shift: 366 days;
- preserve internal clustering and the marginal distribution;
- 100,000 shifts.

### Lane C — year/month sources
Applies to IMF systemic banking crises and any source record lacking day precision.

Primary statistic:
- source-native onset overlap with geometry aggregated to the same native interval.

Null:
- circular shift at the same native temporal unit;
- minimum shift: 2 years for yearly series or 12 months for monthly series;
- 100,000 shifts.

## 9. Source coverage and missingness

Every source is analyzed only inside its documented coverage.

A date outside a source's coverage is `NOT_IN_UNIVERSE`, not a non-event.

Known structural missingness (for example GTD 1993) is excluded from both numerator and denominator.

No source is backfilled by general web search for the confirmatory test.

## 10. Multiple testing

Primary families are source × geometry-witness:

```text
source_id × {W_DIR, W_SHELL}
```

The confirmatory familywise correction is Holm across all primary source × witness tests.

Subtypes, severity strata, ±1/±3-day windows, duration analyses, and alternate geometry summaries are secondary/exploratory and cannot replace a failed primary result.

## 11. Deduplication and cross-source overlap

No cross-source deduplication is performed for primary source-specific tests.

If one real-world event appears in UCDP and GTD, it remains one event in each separate witness.

A later omnibus synthesis may combine source-level p-values with a preregistered dependence-aware procedure, but it may not construct a single “event count” by arbitrarily merging source rows after seeing geometry overlap.

## 12. Event names

Human-readable event names may exist in the historical ledger if they are native source fields.

They are never copied into the geometry ledger.

Primary inferential code operates on event IDs, timestamps, categories, and numerical fields; event-name strings are masked during the first join report.

The first output of the join contains:
- source ID;
- event ID;
- time bounds;
- geometry episode ID;
- geometry witness;
- overlap indicator/statistic.

A separate unmasking step may attach human-readable historical names after the statistical output has been written and hashed.

## 13. Kill conditions

The historical-enrichment hypothesis is not supported if:

1. no source × witness primary test survives Holm correction;
2. apparent results depend on a sensitivity halo but fail the zero-halo/native-resolution primary;
3. results disappear when source coverage and structural missingness are handled correctly;
4. a result is driven by duplicated long-duration exposure rather than frozen onset rules;
5. a result requires adding events or changing categories after PRP dates are inspected;
6. a source's native temporal precision is too coarse to support the claimed coincidence.

## 14. Provenance order

```text
H_SourceRegistry
    -> H_HistoricalSchema
    -> H_JoinSpec
    -> H_Freeze
    -> H_Manifest
    -> [materialize historical rows]
    -> H_DataManifest
    -> [join to already-frozen PRP]
    -> J_OutputManifest
    -> [event-name unmasking]
```

No join is permitted until the historical data materialization has its own immutable manifest.

## 15. Frozen conclusion

HLR-0.1 defines **how a historical event may enter the experiment before any event is allowed to meet a PRP detector hit**.

The experiment therefore asks:

> Given an independently defined historical universe, do frozen planetary recurrence episodes overlap that universe more than expected under a temporal null that never changes the geometry detector?

It does not ask:

> Can we find an interesting story near a geometry peak?

Those are different experiments.
