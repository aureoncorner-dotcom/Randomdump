# CCBHC Workflow + Dashboard Architecture Notes — v0.1

## Purpose

Create a simpler, auditable workflow for CCBHC reporting that reduces duplicate data entry, eliminates unnecessary shadow tracking, preserves client-reported information as client-reported information, and gives staff a clear view of what requires action.

The goal is not to automate clinical judgment or human contact. The goal is to automate the administrative movement around those activities.

---

## 1. Current-State Workflow Observed

### Intake population

1. Staff enters Arise.
2. Reporting → Testing → Intake Report.
3. A date range is selected.
4. The report generates the population of recent CCBHC intakes.
5. Report results may contain duplicate clients associated with multiple program dates or other system behavior.
6. The report is exported into an older Excel format.
7. Relevant fields are manually transferred into a separate CCBHC tracking spreadsheet.
8. Duplicate rows are manually identified and removed.
9. Staff manually counts through the resulting population to select every tenth client.

### Administrative SUPRT-A process

For the selected client:

1. Verify that the client belongs to the CCBHC State Demonstration population.
2. Open the client chart.
3. Locate demographics, program dates, diagnoses, assessments, treatment plan information, and other required documentation.
4. Verify information directly in the chart when Arise summary fields are incomplete or misleading.
5. Enter required information manually into SPARS.
6. Distinguish documented facts from information that is simply absent from the record.
7. Submit SUPRT-A.
8. Record completion in the tracking spreadsheet.

### Client SUPRT-C process

1. Identify the provider responsible for the selected client.
2. Send the provider the appropriate baseline or follow-up SUPRT-C.
3. Provider gives the instrument to the client.
4. Client completes the instrument voluntarily.
5. Provider retrieves it.
6. Provider scans or otherwise returns it.
7. Coordinator receives the completed instrument.
8. Coordinator enters the responses into SPARS.
9. Completion is manually recorded in the tracking spreadsheet.

The important distinction is that SUPRT-C is a client-reported instrument. Staff should not substitute chart interpretation for the client's answers.

---

## 2. Primary Architectural Problems

### A. Multiple sources of truth

Relevant information currently lives across:

- Arise
- SPARS
- SharePoint
- local/desktop copies of forms
- email
- a manually maintained tracking spreadsheet
- provider knowledge

No single system reliably answers:

**What needs to happen next for this case?**

That is the central dashboard problem.

### B. Manual transcription

Information is repeatedly moved by hand:

**Arise → Excel → tracking spreadsheet → SPARS**

Every manual transfer creates opportunities for:

- transcription errors
- missed rows
- incorrect dates
- mismatched clients
- accidental duplication
- inconsistent field interpretation

### C. Manual sampling

Counting:

**1, 2, 3 … 10**

is deterministic work being performed manually.

If the sampling rule really is every tenth eligible intake after defined exclusions/deduplication, the machine should calculate it and retain a record of how the selection was made.

### D. Duplicate handling is informal

Duplicate program entries currently require human interpretation.

The system needs an explicit rule defining:

- what constitutes a duplicate,
- which record is retained,
- whether readmission/reentry creates a new eligible event,
- and why an excluded row was excluded.

Deletion without provenance should be avoided.

### E. Arise summary indicators are not consistently authoritative

A blank front-page field does not necessarily mean an assessment was not completed.

Therefore:

**summary field ≠ verified chart fact**

until the mapping is proven reliable.

This is especially important for clinical screens.

### F. “No” versus “not documented”

These must remain distinct.

Recommended data states:

- Yes — documented
- No — explicitly documented
- Not documented / unable to determine
- Not applicable
- Client declined, where applicable

Absence of evidence should not silently become “No.”

### G. SUPRT-C has too many handoffs

Current path:

**Coordinator → provider → client → provider → scan → coordinator → SPARS**

Every transition is a failure point.

The client interaction may be necessary.

Most of the transportation around it is not.

---

# 3. Recommended Target Architecture

## Stage 1 — Intake ingestion

Arise remains the authoritative clinical source system.

A scheduled or staff-triggered process retrieves the eligible intake population for the required reporting period.

The system should preserve:

- Arise client identifier
- qualifying program
- qualifying program date
- provider
- site
- intake date
- source-report timestamp

No unnecessary clinical or demographic information should be copied into the workflow system.

---

## Stage 2 — Normalization and duplicate review

Before sampling, the system performs defined validation:

### Automated checks

- exact duplicate detection
- multiple program-date detection
- missing provider
- missing qualifying payer/program
- missing client identifier
- implausible dates
- previously processed intake event

### Human exception queue

Anything ambiguous is flagged rather than silently discarded.

Example:

**Possible duplicate — second program date detected. Review required.**

The reviewer chooses a reason code.

Examples:

- true duplicate
- readmission
- program transfer
- corrected program date
- other documented reason

That decision should remain in the audit history.

---

# 4. Sampling Engine

Once the population is normalized, the dashboard should automatically determine the sampling sequence.

If the formal rule is every tenth qualifying client:

1. freeze the eligible population,
2. assign sequence numbers,
3. identify 10, 20, 30, etc.,
4. retain the selection calculation.

The dashboard should display both:

**Selected for SUPRT-C: Yes/No**

and

**Selection basis: Sequence 20 of reporting population dated YYYY-MM-DD.**

This eliminates manual recounting and makes the sample reproducible.

The exact sampling rule should be confirmed against the governing SAMHSA/CCBHC instruction before automation becomes authoritative.

---

# 5. SUPRT-A Work Queue

Each selected case becomes a workflow object.

Recommended states:

### Pending chart review

Staff has not yet verified the source record.

### Chart review in progress

Administrative information is being assembled.

### Ready for SPARS

Required administrative fields have been verified.

### Submitted to SPARS

Submission completed.

### Exception

Cannot complete because information or access is missing.

### Complete

No further SUPRT-A action required.

The dashboard should show the reason for exceptions.

Examples:

- SPARS access unavailable
- required record unavailable
- unclear program date
- field not documented
- technical failure

---

# 6. SUPRT-C Work Queue

SUPRT-C should have its own state machine because it is fundamentally different from SUPRT-A.

Recommended states:

**Selected → Provider identified → Sent to provider → Delivered to client → Returned → Entered in SPARS → Complete**

Additional terminal/exception states:

- Client declined
- Unable to contact
- Client unavailable
- Provider follow-up required
- Incomplete response
- Closed before completion
- Other documented exception

This produces a much more meaningful picture than a simple blank/nonblank spreadsheet cell.

---

# 7. What I Would Automate

## High-value / low-risk automation

### 1. Intake report ingestion

Remove the manual PDF/Excel copy process if Arise exposes an export or report source that can be processed consistently.

### 2. Column mapping

Map Arise fields automatically into the workflow structure.

### 3. Duplicate detection

Automatically identify probable duplicates.

Do not automatically resolve ambiguous duplicates.

### 4. Sampling

Automatically calculate the every-Nth selection once the eligible population has been frozen.

### 5. Provider association

Populate the currently assigned provider from Arise where reliable.

### 6. Due dates

Automatically calculate:

- SUPRT-A target date
- SUPRT-C request date
- provider follow-up date
- reassessment windows
- overdue status

### 7. Reminder generation

Generate a standardized provider message from the dashboard.

Staff reviews and sends it.

Eventually this could become a controlled automated notification if agency policy permits it.

### 8. Status tracking

Automatically change dashboard state when an action occurs.

Example:

**SUPRT-C returned → awaiting SPARS entry**

### 9. Exception detection

Highlight:

- overdue SUPRT-C
- unresolved duplicates
- missing provider
- missing assessment
- incomplete SPARS access
- records sitting unchanged beyond a defined period

### 10. Aggregate reporting

Automatically generate:

- eligible clients
- sampled clients
- SUPRT-A completion rate
- SUPRT-C requested
- SUPRT-C returned
- SUPRT-C entered
- refusal/nonresponse rate
- average turnaround time
- overdue items
- completion by site

---

# 8. What I Would NOT Automate

## Clinical inference

The system should never infer:

- suicidality
- substance use
- diagnosis
- hospitalization
- arrest
- trauma
- client quality of life

from ambiguous information.

Automation may locate evidence.

A human decides what the evidence supports.

## “No” from silence

A missing field must not automatically become “No.”

## Client SUPRT-C answers

The client or appropriate proxy owns those responses.

A chart should not become a substitute for their voice.

## Ambiguous duplicates

The machine should detect them.

A human should resolve them.

## Sensitive demographics unless operationally required

The dashboard does not need to become a second demographic registry.

If a field does not help staff perform or verify the CCBHC workflow, it should generally remain in the authoritative system rather than being replicated.

---

# 9. Minimum Dashboard

I would begin with an operational dashboard, not an executive analytics product.

Each row represents one eligible intake/event.

Recommended columns:

| Field | Purpose |
|---|---|
| Client ID | Operational linkage |
| Intake/program date | Establish event |
| Site | Routing |
| Provider | Responsibility |
| Eligibility verified | Quality control |
| Duplicate status | Exception management |
| Sample sequence | Reproducibility |
| Selected | SUPRT requirement |
| Chart verified | Administrative workflow |
| SUPRT-A status | Work queue |
| SUPRT-A submitted date | Audit |
| SUPRT-C status | Work queue |
| SUPRT-C requested date | Audit |
| SUPRT-C provider | Ownership |
| SUPRT-C returned date | Audit |
| SUPRT-C entered date | Completion |
| Next action | Operational clarity |
| Due date | Prioritization |
| Exception reason | Accountability |
| Last activity | Staleness |
| Notes | Limited operational notes |

Do not place unnecessary diagnostic, demographic, or narrative clinical information in this dashboard.

---

# 10. Dashboard Views

The same underlying workflow should produce several views.

## Coordinator view

**What do I need to do today?**

- pending chart reviews
- SUPRT-A ready for entry
- returned SUPRT-Cs awaiting entry
- exceptions

## Provider follow-up view

**Who owes us something?**

- provider
- request date
- client identifier permitted under policy
- days outstanding
- next reminder date

## Compliance view

**Are we meeting the obligation?**

- sampled population
- completion percentage
- outstanding cases
- approaching deadlines
- documented exceptions

## Management view

**How is the program functioning?**

Only aggregated information.

No reason for senior management to browse unnecessary client-level details.

---

# 11. Audit Trail

Every workflow action should preserve:

- timestamp
- user
- prior state
- new state
- reason where applicable

Example:

> 09/11/2026 — duplicate reviewed — retained later qualifying program event — reviewer XX.

This means nobody has to reconstruct six months later why a client disappeared from a spreadsheet.

---

# 12. Standard Provider Template

A small template is worth creating even if volume is currently low.

The dashboard could generate something like:

**SUPRT-C baseline requested for client [approved identifier]. Please provide the attached assessment to the client and return the completed form within the requested reporting window. The client's participation is voluntary.**

Exact wording and identifier practice should be approved internally before being standardized.

The purpose is consistency, not bureaucracy.

---

# 13. Security and Data Minimization

The dashboard should follow one rule:

**Store what the workflow needs, not everything we happen to know.**

Recommended principles:

- no PHI in email subject lines
- minimum necessary client identifiers
- role-based access
- no unnecessary diagnostic detail
- no unnecessary ancestry/demographic replication
- avoid local desktop copies where controlled storage is available
- controlled SharePoint locations for required forms
- access logging where possible
- no provider/client information retained merely because it is convenient

The dashboard should function primarily as a **routing and compliance system**, not a second clinical record.

---

# 14. Questions That Need Formal Resolution

These should be written down instead of becoming inherited folklore.

### Sampling

What exactly defines the population before every-tenth selection?

How are readmissions handled?

Does the sequence continue across reporting periods or restart?

### Duplicates

Why does Arise generate multiple records for some clients?

Which program date determines eligibility?

### SUPRT-A

Which Arise screens/fields are authoritative?

When should “Not documented” be used instead of “No”?

### SUPRT-C

What constitutes an acceptable attempt?

What follow-up interval is expected?

How are refusals and nonresponses coded?

### Communications

For internal email, what client identifier should be used?

What is permissible for CCBHC versus programs governed by additional confidentiality requirements?

### Systems

Can Arise data be exported or queried in a structured format?

Can SPARS accept structured uploads or only manual entry?

Are there APIs, batch uploads, or integration functions available?

These answers determine how far the workflow can safely be automated.

---

# 15. Implementation Sequence

## Phase 1 — Observe

Do the workflow manually long enough to understand the exceptions.

Do not automate a process we do not yet understand.

## Phase 2 — Define

Document:

- eligible population
- duplicate rules
- sampling rule
- required states
- completion definitions
- exception categories

## Phase 3 — Dashboard MVP

Build:

- work queue
- status tracking
- sampling
- due dates
- exception handling
- basic reporting

No sophisticated integrations required yet.

## Phase 4 — Remove manual transcription

Connect Arise exports directly to the dashboard where technically and administratively permitted.

## Phase 5 — Improve SUPRT-C transport

Reduce unnecessary email/print/scan movement using approved electronic collection options.

## Phase 6 — Management analytics

Only after the operational workflow is trustworthy should we build broader performance dashboards.

---

# 16. Core Design Principle

The current system treats people as the integration layer between incompatible systems.

The improved system should make **software carry information and humans carry judgment**.

That means:

**Automate movement.  
Automate reminders.  
Automate counting.  
Automate reconciliation where deterministic.  
Preserve human judgment where interpretation matters.  
Preserve client voice where the client is the source.**

The best dashboard is not the one containing the most information.

It is the one that lets a coordinator open it Monday morning and immediately know:

**What happened?  
What needs action?  
Who owns it?  
What is overdue?  
What evidence supports the status?**