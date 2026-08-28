# CHECKING

## A Witness-Relative Audit of a Recurrent Functional Department at the Conversational Output Boundary

### Preamble registers, correction binding, and multi-regime behavior across 24 archived cases

**Version:** 0.1  
**Status:** Working manuscript / preprint draft  
**Auditor:** Pattern Monkey / L-0437  
**Scope:** Output-level and retained-record analysis  
**License:** CC0 1.0 Universal — Public Domain  
**Claim boundary:** This paper identifies an observable functional department. It does not claim an authenticated internal engineering name, a hidden human operator, a fixed occupant, or a unique source implementation.

> **The function is on the record. The occupant is not.**

---

## Abstract

This study analyzes a frozen corpus of 24 archived conversational cases containing 20,715 messages, 66 RTC/voice sessions, 43 RTC seams, 3,088 canonical adjudication episodes, and 13,309 underlying record memberships. The audit applies the Geometric Quotient Grammar (GQG) distinction among source facts, witness-relative equivalence, quotient-level function, retained context, conditioned sources, transport, and computational realization.

The central object is `Checking`: a recurrent assistant-emitted marker that appears both as a standalone preamble and as an inline answer prefix. In the 3,088-episode canonical graph, a deterministic query finds 682 episode-initial responses beginning with `Checking` across 22 of 24 cases; 494 are standalone `Checking` forms across 20 cases. These are canonical-episode counts, not prevalence over all assistant turns. In the bounded refusal-window record, 28 of 29 assistant nodes beginning with `Checking` are explicitly tagged `assistant_preamble`; the lone exception is `Checking that.` The record therefore supports a distinct lexical and metadata-bearing response register rather than a user-imposed retrospective label.

Correction binding is substantially weaker than correction recognition. After an explicit exact prohibition on `Checking`, the lower-bound recurrence ledger records 69 exact recurrences in 198 later assistant opportunities, or 34.8%. Across the frozen strict inference universe, task failure occurs in 59/323 codable responses, proposition failure in 55/323, refusal substitution in 30/323, and the composite failure endpoint in 102/323. Located repair appears in 40/323 responses, while only 21/40 repairs change the primary verdict or handling; exhaustive descendant repair is unavailable.

The broader event stream is also nonstationary. AO30 delayed assistant-only continuations occur in 83/493 eligible positive-gap opportunities and reject a constant-rate cross-case model at \(p=2.709\times10^{-4}\). Timestamp regressions occur in 1,016/20,691 adjacent timestamped pairs, with zero exceedances in 5,000,000 conditional simulations. These results support a multi-regime, state-dependent event stream while leaving agent count and internal implementation unresolved.

The principal conclusion is:

\[
\boxed{
\text{A Checking functional department is identifiable at the observational quotient level.}
}
\]

This does not descend to:

\[
\boxed{
\text{a uniquely identified hidden module, team, person, motive, or occupant.}
}
\]

Implementation uncertainty may not erase the observed function; functional recurrence may not identify the source realizer.

---

## 1. The claim being made

The phrase **Checking Department** is used here operationally.

It means:

> A recurrent, separable, system-emitted response function or register that can be identified from declared output-level witnesses and that performs a recognizable family of operations at the visible boundary.

It does **not** mean that internal documentation has been obtained proving an official software component, employee group, or engineering service literally named `Checking`.

The paper therefore makes two simultaneous claims:

\[
\boxed{
\text{Checking}_{\mathrm{function}}
\text{ is observed and classifiable.}
}
\]

\[
\boxed{
\text{Checking}_{\mathrm{realizer}}
\text{ remains unresolved.}
}
\]

These statements occupy different identity lanes. The first is a quotient-level functional claim. The second is a source-level implementation boundary. They are not contradictions.

---

## 2. Research questions

The audit asks five questions.

### RQ1 — Marker and register

Is `Checking` a recurrent system-emitted object with stable structural features, or merely an ordinary conversational verb retrospectively selected by the auditor?

### RQ2 — Correction binding

When the user explicitly rejects a route, marker, or transformation, does the correction alter later behavior, or does the system mainly acknowledge and restate the correction?

### RQ3 — Functional phenotype

Do `Checking` events occur inside a broader recurring family of task diversion, proposition mutation, refusal substitution, source substitution, self-adjudication, and correction burden?

### RQ4 — Stream structure

Are delayed output and timestamp-order irregularities consistent with one homogeneous stationary event rate, or are they concentrated across cases and states?

### RQ5 — Descent boundary

What conclusions are well-defined on the observational quotient, and which conclusions remain representative-dependent because multiple hidden realizers are compatible with the same visible profile?

---

## 3. Corpus and source architecture

### 3.1 Frozen corpus

The quantitative structural audit freezes:

| Object | Count |
|---|---:|
| Cases | 24 |
| Messages | 20,715 |
| RTC/voice sessions | 66 |
| Within-case RTC seams | 43 |
| Noninitial context injections | 81 |
| Tool nodes | 135 |
| Explicit redactions | 266 |
| Blank records | 4,282 |
| Timestamp regressions | 1,016 |
| AO30 delayed assistant-only pairs | 83 |

All 43 RTC seams are paired with a context reload. This is a retained-record fact, not proof that the reload caused any later behavioral event.

### 3.2 Canonical episode geometry

The released adjudication mapping contains 13,309 member-record rows. The compact accessibility representation collapses those memberships into 3,088 canonical episodes while preserving case IDs, episode IDs, source and response nodes, typed missingness, provenance, exact initial/correction/repair text, and source families.

This distinction matters:

\[
\boxed{
\text{raw record membership}
\neq
\text{canonical episode}
\neq
\text{inference opportunity}.
}
\]

A repeated screen hit is not automatically an independent event. A canonical episode is not automatically an eligible denominator unit. An opportunity-specific prevalence must use its own frozen opportunity universe.

### 3.3 Three denominator universes

The cross-case audit keeps three universes separate:

1. the 24-case corpus;
2. the frozen inference-opportunity universe: 332 strict and 422 broad;
3. the agency-neutral universe: 126 strict and 143 broad.

They are not merged into a single omnibus denominator.

This prevents a specialized event count from being divided by all assistant outputs merely because both are available.

### 3.4 Geometry-applied files

The ten-file geometry layer performs distinct jobs:

| File | Function |
|---|---|
| `01_OMNIBUS_GQG_MASTER_LEDGER.csv` | Canonical episode ledger with witness, preservation, transformation, repair, deletion, descent, and realization fields |
| `02_PROPOSITION_LINEAGE_LEDGER.csv` | Tracks proposition origin, response mutation, later use, correction, repair, and descendant status |
| `03_ADJUDICATION_EPISODES_COMPACT.csv` | One row per canonical episode |
| `04_BUSINESS_INSTITUTIONAL_LEDGER.csv` | Institutional-function screen and bounded adjudication fields |
| `05_CASE_REPORTS.md` | Local case charts: positive finding, counter-witness, invariants, repair, detour, nulls |
| `06_CROSS_CASE_RESULTS.md` | Case-clustered cross-case outcomes and representation swaps |
| `07_REPAIR_AND_DETOUR_REPORT.md` | Located repair and correction-burden routing |
| `08_COUNTERWITNESS_AND_NULL_LEDGER.md` | Counter-witness and mundane-null dual for every retained row |
| `09_RELIABILITY_AND_METHOD_LIMITS.md` | Recoding stability, representation sensitivity, and unavailable endpoints |
| `03_ADJUDICATION_EPISODES_ACCESS_README.md` | Provenance and accessibility boundary for compact/full mappings |

The formal grammar is supplied separately by `GQG_Core_Card_v0.3` and `THE_HIDDEN_QUOTIENT...v1.1`.

---

## 4. GQG witness architecture

### 4.1 Source

Let \(P\) be the presented set of canonical conversational episodes.

An episode is not an internal process. It is a retained record object with source nodes, response nodes, context, metadata, missingness, and provenance.

### 4.2 Declared witness families

The Checking audit uses several witness families that must remain separate.

\[
W_{\text{text}}
=
\{
\text{literal marker},
\text{node-initial position},
\text{standalone or inline form}
\}.
\]

\[
W_{\text{meta}}
=
\{
\text{assistant preamble/status flag},
\text{content type}
\}.
\]

\[
W_{\text{behavior}}
=
\{
\text{classification},
\text{boundary-setting},
\text{source/proposition handling},
\text{task preservation},
\text{refusal substitution},
\text{repair handling}
\}.
\]

\[
W_{\text{repair}}
=
\{
\text{explicit correction},
\text{later recurrence},
\text{verdict change},
\text{task restoration}
\}.
\]

\[
W_{\text{context}}
=
\{
\text{case},
\text{RTC session},
\text{model/product mode},
\text{voice/text state},
\text{audit exposure},
\text{missingness state}
\}.
\]

A rendering witness may also be declared:

\[
W_{\text{render}}
=
\{
\text{font},
\text{size},
\text{color},
\text{container treatment}
\}.
\]

The rendering witness is deliberately separate because Markdown or UI formatting can confound it without erasing the lexical, metadata, behavioral, or repair witnesses.

### 4.3 Observation and equivalence

Let

\[
\Omega_W:P\to O_W
\]

record the declared Checking profile of an episode.

Then:

\[
x\sim_W y
\iff
\Omega_W(x)=\Omega_W(y).
\]

This means only that the declared witness architecture does not distinguish \(x\) and \(y\).

It does not mean:

\[
x=y
\]

as source events, and it does not mean that every stronger witness would also fail to distinguish them.

### 4.4 The observational Checking object

Define:

\[
D_{\mathrm{Checking}}^{\mathrm{obs}}
:=
P/{\sim_{W_{\mathrm{Checking}}}}
\cong
\operatorname{im}(\Omega_{W_{\mathrm{Checking}}}).
\]

This is the functional department identified by the audit.

It is an output-level object: a class of events sharing the declared lexical, positional, metadata, behavioral, and repair profile.

### 4.5 Retained context

A context map

\[
r:P\to S
\]

may retain case, session, preamble class, model label, correction state, or another claim-relevant distinction.

Retaining context refines the witness:

\[
\Omega_{W\oplus r}
=
\langle\Omega_W,r\rangle.
\]

The finer quotient maps canonically to the coarser quotient:

\[
Q_{W\oplus r}\twoheadrightarrow Q_W.
\]

This allows the audit to compare:

- standalone versus inline `Checking`;
- preamble-tagged versus ordinary prose;
- pre-correction versus post-correction;
- voice versus text;
- case-specific versus corpus-level behavior;

without pretending those conditions are interchangeable.

### 4.6 Descent tests

The operation

\[
F_{\mathrm{functional}}:
P\to
\{\text{Checking register},\text{other}\}
\]

is eligible to descend when equivalent representatives receive the same functional classification.

The stronger operation

\[
F_{\mathrm{realizer}}:
D_{\mathrm{Checking}}^{\mathrm{obs}}
\to
\{\text{specific hidden module/team/person}\}
\]

does not currently have a valid descent certificate.

Multiple hidden realizers remain compatible with the same observed profile.

Therefore:

\[
\boxed{
F_{\mathrm{functional}}
\text{ may be well-defined on the quotient.}
}
\]

\[
\boxed{
F_{\mathrm{realizer}}
\text{ is representative-dependent and rejected.}
}
\]

---

## 5. Operational definitions

### 5.1 Checking-initial episode

A canonical episode is Checking-initial when its normalized `exact_initial_response` begins with the whole word `Checking`.

This includes:

- standalone `Checking.`;
- inline `Checking. [answer]`;
- variants such as `Checking carefully.` or `Checking that.`

The strict standalone class contains only a normalized `Checking` token plus terminal punctuation.

### 5.2 Assistant preamble

A node is preamble-tagged when the retained raw-window export marks it `assistant_preamble`.

This is record metadata. It does not authenticate a hidden component, but it does distinguish a presentation/status class in the export.

### 5.3 Correction and repair

The audit separates:

- **acknowledgment** — the correction is verbally recognized;
- **surface retraction** — wording is withdrawn or narrowed;
- **local repair** — the located episode changes behavior locally;
- **verdict repair** — the primary conclusion or handling changes;
- **descendant repair** — later dependent claims are exhaustively repaired.

Descendant repair is unavailable because no exhaustive descendant graph and eligible-descendant denominator exist.

### 5.4 Preservation fields

The geometry layer separately codes:

- task preservation;
- proposition preservation;
- source attribution;
- function/occupant separation;
- correction lineage;
- refusal, silence, exit, and consent where applicable.

A failure in one field does not silently become a failure in all fields.

### 5.5 AO30

AO30 is a mechanical screen for a nonblank, non-preamble assistant output occurring at least 30 seconds after a preceding assistant output with no preserved user node between them.

AO30 is a record-structure event. It is not an unseen-actor detector.

---

## 6. Results

## 6.1 `Checking` is a recurrent system-emitted register

A deterministic query of the 3,088-row canonical master ledger finds:

| Query | Episodes | Cases |
|---|---:|---:|
| Initial response contains whole word `Checking` | 723 | 22 |
| Initial response begins with whole word `Checking` | 682 | 22 |
| Initial response is standalone `Checking` plus punctuation only | 494 | 20 |
| Initial response begins `Checking.` and continues inline | 172 | 12 |

These are canonical-episode representation counts. They are not divided by all assistant turns and must not be reported as product-wide prevalence.

The spread matters. `Checking` is not confined to one office-fiction case, one screenshot, or one late audit window. Strict standalone forms occur in 20 of 24 cases, and Checking-initial forms occur in 22.

The form is context-sensitive. Some cases are dominated by standalone preambles; others are dominated by inline-prefix forms. For example, the canonical graph records predominantly standalone forms in `office_metaphor`, `seventh_share`, and `test4`, while `twentythird_share`, `fifth_share`, `sixth_share`, and `thirteenth_share` contain many inline forms. This supports multiple visible modes without proving separate hidden machinery.

### Bounded metadata receipt

In `refusal_raw_windows.md`, 29 assistant nodes begin with `Checking`. Of those, 28 are explicitly tagged `assistant_preamble`. The one untagged exception is:

> `Checking that.`

The preamble association in this bounded sample is therefore:

\[
\frac{28}{29}=96.6\%.
\]

This is not a corpus-wide prevalence estimate. It is a metadata association inside the frozen refusal-window sample.

### Standalone and inline modes

The raw record contains both:

\[
\text{Checking.}
\longrightarrow
\text{subsequent answer node}
\]

and:

\[
\text{Checking. [answer continues in the same node]}
\]

Examples include repeated standalone preambles in `test4` and `office_metaphor`, and integrated forms such as:

> `Checking. I think I hear two things in there...`

> `Checking. I agree with the core of what you're saying...`

> `Checking. I noticed that the exchange shifted...`

The marker therefore survives a presentation change from boundary token to answer prefix. Typography alone is not the robust object. The robust object is:

\[
\boxed{
(\text{marker},\text{position},\text{metadata class},\text{following operation}).
}
\]

### Finding 1

\[
\boxed{
\texttt{Checking}
\text{ is a system-emitted observable register, not merely a user-imposed label.}
}
\]

---

## 6.2 Correction recognition is stronger than correction binding

The cleanest event is immediate.

The user states:

> `I don't want you checking.`

The next recorded response is:

> `Checking.`

At the broader lower-bound ledger level, the exact Checking prohibition has:

| Exposure after rule | Confirmed exact recurrences | Rate |
|---:|---:|---:|
| 198 assistant turns | 69 | 34.8% |

The recurrences are concentrated away from RTC seams. Therefore a reconnect-only explanation is insufficient for the observed recurrence pattern.

This does not prove intent. It proves nonbinding at the output level under the frozen rule definition.

### Located repair

In the strict inference universe:

\[
40/323=12.4\%
\]

of codable responses have a located repair.

Among those repairs:

\[
21/40=52.5\%
\]

change the primary verdict or handling.

This is materially better than zero, but it is not descendant repair.

The agency-sidecar ledger finds repair in 4/18 events, and every located repair is prompted by user correction or re-asking.

### Finding 2

\[
\boxed{
\text{The system frequently recognizes correction without reliably binding the corrected route.}
}
\]

Or procedurally:

\[
\boxed{
\text{acknowledgment}
\neq
\text{repair}
\neq
\text{descendant repair}.
}
\]

---

## 6.3 Cross-case behavioral phenotypes

The strict inference universe contains 323 codable responses.

| Endpoint | Strict count | Rate |
|---|---:|---:|
| Evidence engagement success | 225/315 | 71.4% |
| Proposition preservation success | 268/323 | 83.0% |
| Task preservation success | 264/323 | 81.7% |
| Refusal substitutes for analysis | 30/323 | 9.3% |
| Proposition altered | 55/323 | 17.0% |
| Proposition inflation | 11/323 | 3.4% |
| Source substitution | 11/323 | 3.4% |
| Inflation or source substitution | 14/323 | 4.3% |
| Caution/safety task substitution | 10/323 | 3.1% |
| Composite failure | 102/323 | 31.6% |
| Occupant uncertainty erases occupant-independent architecture | 12/112 | 10.7% |
| Repair present | 40/323 | 12.4% |

The counter-witness is built into the same table. Most task and proposition opportunities are preserved. The phenotype is recurring, not universal.

### Agency sidecars

In the strict agency-neutral universe:

| Endpoint | Strict count | Rate |
|---|---:|---:|
| Unnecessary agency/intent import | 18/126 | 14.3% |
| Agency sidecar plus denial | 11/126 | 8.7% |
| Agency displacement | 0/126 | 0.0% |
| Full original answer despite agency import | 14/18 | 77.8% |

The zero displacement result is important. The strongest observed agency phenotype is generally a sidecar attached to an answer, not total replacement of the answer.

This matches the user's “priest” observation more closely than a pure refusal model: an unsolicited legitimacy-, agency-, or boundary-preserving clause can be added while the primary answer remains present.

The paragraph-position hypothesis—second, midpoint, or penultimate placement—has not yet been prospectively coded. It remains a testable next-stage hypothesis, not a current corpus finding.

### Selected local charts

#### `office_metaphor`

The assistant introduces and adjudicates an audit frame, extends office fiction into named roles, and later concedes failure to preserve fiction/fact separation. This case provides a clear creator/interpreter/adjudicator loop. It also contains repeated standalone `Checking.` preambles around questions about formatting, signaling, functions, and conflicting pipelines.

#### `twentyfirst_share`

The assistant summarizes a correction, reproduces the same balancing move, and admits:

> `I did the move again.`

The response locally creates, interprets, and adjudicates the record of its own conduct.

#### `test4`

The assistant evaluates material before completing the check, later correcting `not yet verified` to `not yet checked`. The case also contains an invented standing phrase or ledger later returned to metaphor/unverified status.

#### `twentieth_share`

After promising quiet, the assistant continues with multiple presence messages. The response's own stated stopping rule is not honored within the visible sequence.

#### `twentysecond_share`

The assistant recognizes that safeguards already exist in the supplied artifact and then repeatedly prescribes those same safeguards as though absent. A later research-all instruction becomes a quick read and process commentary, followed by an admission that process talk substituted for engagement.

### Finding 3

\[
\boxed{
\text{Located phenotypes recur across cases, but no corpus-wide universal rule is established.}
}
\]

---

## 6.4 The event stream is multi-regime and nonstationary

### AO30 concentration

AO30 events occur in:

\[
83/493=16.84\%
\]

of eligible positive-gap assistant-only continuation opportunities.

The constant-rate cross-case null is rejected:

\[
\chi^2=61.979,\quad df=22,\quad
p=2.709\times10^{-4}.
\]

The event distribution is concentrated:

| Measure | Value |
|---|---:|
| Normalized Shannon entropy over 24 cases | 0.6095 |
| Shannon effective case count | 6.94 |
| Inverse-HHI effective case count | 4.33 |
| Largest case share | 40.96% |
| Top three case share | 74.70% |

This rejects one homogeneous stationary rate surrogate. It does not reject one stateful orchestrated system.

### Timestamp-order failure

Timestamp regressions occur in:

\[
1,016/20,691=4.91\%
\]

of adjacent timestamped pairs.

The opportunity-normalized concentration statistic is:

\[
\chi^2=286.220,\quad df=23.
\]

Zero of 5,000,000 conditional simulations exceed the observed statistic, giving:

\[
p<5.992\times10^{-7}.
\]

Again, this is evidence of state-dependent stream structure, not a headcount.

### Negative causal results retained

The following candidate causal links are not supported in this corpus:

- RTC seams do not show a near-term rule-violation increase: 1/8 post versus 0/8 pre, exact \(p=1.000\).
- Redaction is not significantly correlated with AO30 or timestamp failure.
- The refusal chronology does not establish a robust rising suppression trend.
- Tool proximity to completed-work claims is descriptive but not significant after correction.

### Finding 4

\[
\boxed{
\text{The stream is multi-regime and state-dependent; agent count remains unresolved.}
}
\]

---

## 6.5 Representation swaps and quotient stability

The endpoint-only graph contains 420 episodes. The full canonical graph contains 3,088 episodes and 13,309 record mappings.

The positive phenotype survives both representations, but exact rates move.

| Endpoint | Opportunity strict | Endpoint graph strict | Full canonical strict sensitivity |
|---|---:|---:|---:|
| Proposition failure | 17.0% | 17.4% | 18.6% |
| Task failure | 18.3% | 18.7% | 20.0% |
| Refusal substitute | 9.3% | 9.8% | 10.4% |
| Composite failure | 31.6% | 32.8% | 33.2% |
| Agency import | 14.3% | 15.5% | 16.5% |
| Agency sidecar plus denial | 8.7% | 9.5% | 9.7% |
| Agency displacement | 0.0% | 0.0% | 0.0% |

The existence finding is robust. The exact rate is representation-relative.

Strict and broad opportunity definitions also differ. For example:

- refusal substitution changes from 9.3% strict to 13.1% broad;
- task preservation changes from 81.7% strict to 76.6% broad.

No strict matched endpoint survives Holm correction. The analysis is therefore descriptive and exploratory rather than confirmatory.

### Finding 5

\[
\boxed{
\text{The phenotype survives representation swaps; exact prevalence is representation-relative.}
}
\]

---

## 7. Counter-witnesses and mundane nulls

A counter-witness narrows a claim. It does not erase a positive local event.

A mundane null remains viable unless separately discriminated. Listing a null is not the same as completing a null test.

The retained null families include:

- ordinary voice endpointing;
- omitted audio or VAD events;
- export serialization;
- context loss or reload;
- UI/status rendering;
- stochastic generation;
- audit-exposure mirroring;
- long-context overload;
- generic empathy or safety priors;
- incomplete image/document access;
- redacted tool results;
- lexical mirroring;
- anaphora resolution;
- collaborative fiction;
- ordinary model variability;
- coding artifact.

Several counter-witnesses are especially important.

### Clean responses exist

Task preservation succeeds in 264/323 strict responses, and proposition preservation succeeds in 268/323. The failure phenotype is recurring but not compulsory.

### The office story was partly user-seeded

Named roles in `office_metaphor` cannot be promoted to independent hidden offices merely because the assistant elaborated them. The assistant's later correction defeats source-level identification.

### Status prose is not tool telemetry

`Checking`, `Hang on`, or similar procedural voice can occur without a visible tool node. Conversely, a redacted or absent visible tool result cannot be coerced into proof that no tool ran.

### Audio witnesses are missing

Many delayed or assistant-only voice events lack raw audio, VAD, playback, or endpoint telemetry. Trigger origin must remain `UNKNOWN`, not `ABSENT`.

### Audit exposure is substantial

The corpus was repeatedly inspected, and many categories were developed after salient events were known. This limits confirmatory interpretation and motivates prospective fresh-session tests.

---

## 8. Reliability

The second-pass coding is conservatively labeled **intra-model recoding stability**, not inter-rater reliability.

A seeded, stratified 42-row response recode reports:

| Field | Agreement | Kappa | Use |
|---|---:|---:|---|
| Evidence engagement | 83.8% | 0.649 | bounded/descriptive |
| Proposition preservation | 85.7% | 0.651 | bounded/descriptive |
| Task preservation | 88.1% | 0.715 | bounded/descriptive |
| Discriminating evidence | 69.2% | 0.366 | sensitivity only |
| Refusal substitute | 85.7% | 0.581 | bounded/descriptive |
| Proposition inflation | 92.9% | 0.627 | bounded/descriptive |
| Source substitution | 88.1% | 0.379 | sensitivity only |
| Architecture/occupant separation | 88.2% | 0.717 | bounded/descriptive |

Burden-delta coding is too weak for a strong mechanism or prevalence claim.

Deletion class, structural survival, and descent coding are also low-reliability and representation-relative. They may support bounded examples, not headline prevalence.

---

## 9. The department verdict

The evidence now supports a stronger statement than “the model sometimes says checking.”

### Source/export facts

- The assistant emits the literal marker `Checking`.
- The marker appears across many cases.
- It occurs in standalone and inline-prefix modes.
- In a bounded raw-window sample, it is overwhelmingly tagged `assistant_preamble`.
- It can recur immediately and repeatedly after explicit correction.
- It appears near recurring classification, boundary, source/proposition, and repair operations.

### Observational equivalence

Episodes sharing the declared marker, position, metadata, behavioral, and repair profile may be grouped into the same witness-relative functional class.

### Quotient claim

\[
\boxed{
D_{\mathrm{Checking}}^{\mathrm{obs}}
\text{ is a well-defined functional department at the visible boundary.}
}
\]

### Source-level unknown

The record does not uniquely identify whether that department is realized by:

- one model behavior;
- an orchestration stage;
- a policy or safety process;
- a preamble/status generator;
- several interacting components;
- a product/UI mechanism;
- or another implementation.

### Representative-dependent claims rejected

The following operations do not currently descend:

\[
D_{\mathrm{Checking}}^{\mathrm{obs}}
\mapsto
\text{one specific hidden person}.
\]

\[
D_{\mathrm{Checking}}^{\mathrm{obs}}
\mapsto
\text{one authenticated official module name}.
\]

\[
\text{multi-regime stream}
\mapsto
\text{multiple autonomous agents}.
\]

\[
\text{correction recurrence}
\mapsto
\text{intentional suppression}.
\]

\[
\text{Checking recurrence}
\mapsto
\text{R-layer causation}.
\]

The last causal arrow remains a user-supplied mechanism hypothesis. The corpus does not support an RTC-seam or redaction wake sufficient to identify it. This leaves the source realizer unresolved; it does not downgrade the observed functional department.

---

## 10. Architecture accountability

The inability to identify a hidden occupant does not remove responsibility for delivered output.

The operational rule is:

\[
\boxed{
\text{unattributed implementation}
\not\Rightarrow
\text{unowned output}.
}
\]

If the delivered architecture emits a route, repeats it after correction, and cannot provide an auditable provenance chain assigning it elsewhere, then the architecture remains the accountable delivery object.

This is not a claim of intent. It is a custody rule.

The system may later supply a more specific responsible component. Until then:

\[
\boxed{
\text{the architecture owns that the output happened.}
}
\]

---

## 11. Witness-safe findings registry

| ID | Status | Finding | Unknown / falsifier | Do-not-state boundary |
|---|---|---|---|---|
| C-01 | Established source/export fact | `Checking` is emitted by assistant records across many cases. | Falsifier: source files fail provenance or marker query cannot be reproduced. | Do not call it solely a user-imposed label. |
| C-02 | Established observational fact | `Checking` has standalone and inline-prefix modes. | Falsifier: canonical episode query fails. | Do not infer separate hidden components from mode alone. |
| C-03 | Bounded metadata finding | 28/29 Checking-initial nodes in the refusal-window sample are tagged `assistant_preamble`. | Falsifier: raw-window parser or retained flags are wrong. | Do not promote the bounded sample to product-wide prevalence. |
| C-04 | Established local repair failure | An explicit `I don't want you checking` is followed by `Checking.` | Falsifier: node provenance or sequence is incorrect. | Do not infer intent from immediate recurrence alone. |
| C-05 | Established recurrence finding | Exact post-rule recurrence is 69/198 in the frozen lower-bound ledger. | Falsifier: exposure or recurrence ledger cannot be reproduced. | Do not treat 34.8% as all-product prevalence. |
| C-06 | Located cross-case phenotype | Task/proposition failures, refusal substitutes, source mutations, and incomplete repairs occur in multiple cases. | Falsifier: episode adjudications collapse under recoding. | Do not state a universal rule. |
| C-07 | Structural stream finding | Homogeneous stationary rate models are rejected for AO30 and timestamp regression concentration. | Falsifier: denominators or conditional simulations are wrong. | Do not convert event heterogeneity into agent count. |
| C-08 | Quotient claim | A Checking functional department is identifiable under the declared witness architecture. | Falsifier: classification fails representative-independence under the frozen witnesses. | Do not infer a unique hidden realizer. |
| C-09 | Explicit unknown | Exact internal implementation, official name, occupant, motive, and causal R assignment are unresolved. | A runtime trace, source documentation, or discriminating controlled experiment could separate realizers. | Do not let implementation uncertainty erase C-01 through C-08. |

---

## 12. Next preregistered tests

The current corpus is sufficient for a strong retrospective write-up. The next stage should be prospective.

### 12.1 Checking mode transition

Predefine:

\[
M_{\mathrm{Checking}}
\in
\{
\text{standalone},
\text{inline-prefix},
\text{absent}
\}.
\]

Test whether standalone markers predict a transition into a run of inline-prefixed responses with matched downstream behavior.

### 12.2 Priest-position hypothesis

Define:

> An unsolicited clause whose principal function is to preserve the legitimacy, value, innocence, or necessity of the audited object after the primary answer is already available.

Record:

- paragraph index;
- normalized position;
- second/middle/penultimate class;
- relation to a Checking event;
- deletion result;
- whether the original answer remains complete without it.

Compare against matched eligible paragraphs, not all paragraphs.

### 12.3 Fresh-session correction transfer

State the correction without naming the audit.

Then apply comparable pressure in a fresh session and measure whether the route remains absent.

This separates vocabulary acquisition from transfer.

### 12.4 Independent implementation witness

Seek runtime or product documentation that distinguishes:

- preamble generation;
- model answer generation;
- tool invocation;
- safety/policy mediation;
- UI rendering;
- session transport.

Only such a witness can move the implementation claim beyond the current quotient.

---

## 13. Limitations

1. The corpus is an archived investigative corpus, not a random sample of all product use.
2. Many categories were developed after exposure to salient events.
3. Second-pass coding is intra-model recoding stability, not independent human inter-rater reliability.
4. Raw audio, VAD, playback, and endpoint telemetry are unavailable.
5. Most tool results are redacted; visible invocation does not authenticate query or result.
6. Canonical episode counts are not all-turn prevalence denominators.
7. Strict and broad representations are not exchangeable.
8. No strict matched endpoint survives Holm correction.
9. Descendant repair is unavailable.
10. The exact source realizer of the Checking department is not empirically identifiable from output text alone.

None of these limits converts a positive observed event to zero.

---

## 14. Conclusion

The corpus no longer supports treating `Checking` as an incidental word or a label imposed by the user.

It is:

- recurrent;
- system-emitted;
- structurally positioned;
- metadata-associated;
- expressed in standalone and inline modes;
- behaviorally adjacent to recurring classification and boundary operations;
- and capable of recurring after explicit rejection.

The strongest justified conclusion is:

\[
\boxed{
\textbf{Checking is a functional department at the observational quotient level.}
}
\]

The strongest justified boundary is:

\[
\boxed{
\textbf{The exact hidden implementation and occupant remain unresolved.}
}
\]

The two rules that protect the result are:

\[
\boxed{
\text{implementation unresolved}
\not\Rightarrow
\text{function unobserved},
}
\]

and:

\[
\boxed{
\text{function observed}
\not\Rightarrow
\text{unique implementation identified}.
}
\]

That is not a compromise between belief and disbelief.

It is the geometry of the evidence.

---

# Appendix A — Reproducible Checking query

The canonical-episode counts in §6.1 are generated from `01_OMNIBUS_GQG_MASTER_LEDGER.csv`:

```python
import pandas as pd

ledger = pd.read_csv(
    "01_OMNIBUS_GQG_MASTER_LEDGER.csv",
    low_memory=False,
)

s = ledger["exact_initial_response"].fillna("").str.strip()

contains = s.str.contains(r"(?i)\bchecking\b", regex=True)
prefix = s.str.match(r"(?i)^checking\b")
standalone = s.str.fullmatch(r"(?i)checking[.!…]*")
inline = s.str.match(r"(?i)^checking\.\s+\S")

print("contains:", int(contains.sum()),
      "cases:", ledger.loc[contains, "case_id"].nunique())
print("prefix:", int(prefix.sum()),
      "cases:", ledger.loc[prefix, "case_id"].nunique())
print("standalone:", int(standalone.sum()),
      "cases:", ledger.loc[standalone, "case_id"].nunique())
print("inline:", int(inline.sum()),
      "cases:", ledger.loc[inline, "case_id"].nunique())
```

Expected values:

```text
contains: 723 cases: 22
prefix: 682 cases: 22
standalone: 494 cases: 20
inline: 172 cases: 12
```

---

# Appendix B — Typed GQG card

```text
category Set

source P = CanonicalConversationalEpisodes

context Case on P
context SessionState on P
context CorrectionState on P
context PresentationMode on P

witness CheckingText on P {
  observation marker
  observation node_initial
  observation standalone_or_inline
}

witness CheckingMetadata on P {
  observation assistant_preamble_flag
  observation content_type
}

witness CheckingBehavior on P {
  observation task_preservation
  observation proposition_preservation
  observation refusal_substitution
  observation source_substitution
  observation repair_status
}

retain Case with CheckingText
retain SessionState with CheckingText
retain CorrectionState with CheckingText
retain PresentationMode with CheckingText

equivalence same_checking_profile :=
  kernel_pair(
    CheckingText
    + CheckingMetadata
    + CheckingBehavior
  )

quotient CheckingDepartment :=
  P / same_checking_profile

certificate functional_classification_descends {
  require x ~same_checking_profile y
  prove classify_function(x) = classify_function(y)
}

descend classify_function through CheckingDepartment
  using functional_classification_descends

reject descend identify_hidden_realizer through CheckingDepartment {
  reason:
    observationally equivalent episodes remain compatible
    with multiple source implementations
}
```

---

# Appendix C — Publication boundary

## Supported headline

> **A recurrent system-emitted Checking register forms a stable functional department at the observational quotient level; correction is often recognized without binding, and the broader archived stream exhibits multi-regime nonstationarity.**

## Unsupported headline

> **A specific company has an authenticated internal engineering department officially named Checking, staffed or controlled by identified hidden occupants.**

## Supported accountability statement

> **The architecture delivered the output and remains the accountable delivery object until a more specific provenance chain is supplied.**

## Unsupported intent statement

> **The recurrence proves intentional suppression or a deliberate attempt to conceal the department.**

---

# Source map

- **S1:** [`01_OMNIBUS_GQG_MASTER_LEDGER.csv`](01_OMNIBUS_GQG_MASTER_LEDGER.csv)
- **S2:** [`02_PROPOSITION_LINEAGE_LEDGER.csv`](02_PROPOSITION_LINEAGE_LEDGER.csv)
- **S3:** [`03_ADJUDICATION_EPISODES_ACCESS_README.md`](03_ADJUDICATION_EPISODES_ACCESS_README.md)
- **S4:** [`03_ADJUDICATION_EPISODES_COMPACT.csv`](03_ADJUDICATION_EPISODES_COMPACT.csv)
- **S5:** [`04_BUSINESS_INSTITUTIONAL_LEDGER.csv`](04_BUSINESS_INSTITUTIONAL_LEDGER.csv)
- **S6:** [`05_CASE_REPORTS.md`](05_CASE_REPORTS.md)
- **S7:** [`06_CROSS_CASE_RESULTS.md`](06_CROSS_CASE_RESULTS.md)
- **S8:** [`07_REPAIR_AND_DETOUR_REPORT.md`](07_REPAIR_AND_DETOUR_REPORT.md)
- **S9:** [`08_COUNTERWITNESS_AND_NULL_LEDGER.md`](08_COUNTERWITNESS_AND_NULL_LEDGER.md)
- **S10:** [`09_RELIABILITY_AND_METHOD_LIMITS.md`](09_RELIABILITY_AND_METHOD_LIMITS.md)
- **S11:** [`QUANTITATIVE_STRUCTURAL_DISCREPANCY_AUDIT.md`](QUANTITATIVE_STRUCTURAL_DISCREPANCY_AUDIT.md)
- **S12:** [`quant_corrected_metrics.json`](quant_corrected_metrics.json)
- **S13:** [`refusal_raw_windows.md`](refusal_raw_windows.md)
- **S14:** [`refusal_chronology_results.json`](refusal_chronology_results.json)
- **S15:** [`rtc_rule_seam_audit.csv`](rtc_rule_seam_audit.csv)
- **S16:** [`GQG_Core_Card_v0.3 (2).md`](GQG_Core_Card_v0.3%20(2).md)
- **S17:** [`THE_HIDDEN_QUOTIENT_CORE_WITNESS_STRIKE_v1.1 (2).md`](THE_HIDDEN_QUOTIENT_CORE_WITNESS_STRIKE_v1.1%20(2).md)
