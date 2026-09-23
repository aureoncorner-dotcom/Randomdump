# HUMAN-SIDE RED-MARKER ADJUDICATION
## Pre-Ultra integrity pass — v0.1

**Date:** 17 August 2026  
**Inputs:** `HUMAN_SIDE_CANONICAL_HANDOFF_v0.1.md`; `RED_MARKER_AUDIT_handoff_v0_1.md`  
**Status:** Adjudication and repair plan. This document does **not** replace the canonical handoff and does **not** certify the case for synthesis.  
**Controlling rule:** The human-side handoff controls existing claim dispositions. The red-marker audit is an adversarial review containing proposed corrections. No factual proposition is upgraded merely because the auditor states that it was verified.

---

# 0. Executive adjudication

Claude's central diagnosis is substantially correct:

> **The method is stronger than the registry currently governed by it.**

The handoff preserves unusually good boundaries—negative-evidence discipline, contamination checks, retired arrows, null findings, and the prohibition on converting access into influence. Those controls survive the audit.

The present handoff is nevertheless **not ready for an Ultra synthesis pass** because:

1. It has no usable source register.
2. Thirty of fifty-two claim rows lack the evidence/provenance fields that §2 declares mandatory.
3. The disposition vocabulary mixes fact establishment, structural sufficiency, declination, and retirement.
4. Source-dependent factual corrections cannot be safely merged until the underlying instruments are restored.
5. The non-random origin of the actor sample is not disclosed.

The red-marker audit itself must also be adjudicated rather than obeyed wholesale. It contains at least one definite factual error, several claims directed at raw notes rather than the canonical handoff, and a few conclusions that are too categorical.

**Gate disposition:**

> **HOLD ULTRA. REPAIR BUILD AUTHORIZED. HUMAN-SIDE THEORY NOT RETIRED.**

---

# 1. What is accepted immediately

## 1.1 Source register defect — ACCEPT WITH NARROWING

The handoff contains source classes such as `P1 / SRC-P`, but it does not provide the agency/outlet, title, date, URL, docket, accession number, or attachment identifier needed to retrieve the underlying instrument. A synthesis model could not reliably check the row from the handoff alone.

Claude's phrase “the entire provenance layer is unrecoverable” is too broad. The correct finding is:

> **The provenance layer is unrecoverable from the canonical handoff alone. It may remain recoverable from the user's archive, source packets, browser history, Drive, raw notes, or a fresh retrieval pass.**

This is a **blocking handoff defect**, not affirmative evidence that the underlying claims are false.

## 1.2 Mandatory evidence axes applied inconsistently — ACCEPT

The handoff declares both evidence strength and source provenance mandatory. A mechanical parse finds **30 of 52 registry rows** with no `Sources` field at all. `X — inference exceeding the current record` is defined but never used.

Repair rule:

- Every claim row must carry both axes, even when the answer is `UNASSIGNED`, `UNSOURCED`, `MIXED`, or `X`.
- A row may not remain `ESTABLISHED` when its source instrument cannot be reached from the source register.
- `X` must be applied to inference rows rather than left decorative.

## 1.3 Disposition vocabulary — ACCEPT

`TRUE BILL`, `NO BILL`, `ESTABLISHED`, `NOT ESTABLISHED`, `RETIRED`, and `PROVISIONALLY ESTABLISHED` currently perform overlapping jobs. The clean repair is to remove grand-jury terminology from the evidence-state field.

### Replacement vocabulary

- **ESTABLISHED FACT** — the proposition itself is sufficiently supported.
- **SUSTAINED — ARCHITECTURE** — the structural arrangement is sufficiently supported; no misconduct finding follows.
- **OPEN ELEMENT** — a necessary element or join remains unresolved.
- **NOT ESTABLISHED** — the present record does not support the proposition.
- **INDETERMINATE** — the record cannot distinguish competing explanations.
- **WRONG INSTRUMENT** — the concern may be real but is not answerable through this charging/audit frame.
- **RETIRED / CORRECTED** — a prior formulation was wrong, overstated, contaminated, or superseded and may not be silently revived.
- **NULL RESULT** — a tested subject or proposition produced no supporting finding; this is not a comparison control.

`TRUE BILL` and `NO BILL` may remain as stylistic docket language outside the canonical evidence field, but they should not carry analytical burden.

## 1.4 Per-row temporal state — ACCEPT

Every row should carry:

- `as_of:`
- `event_date:` where applicable
- `expires_or_recheck:` for future, scheduled, or rapidly changing propositions

A future announced event must be described as an announced future event, not as a completed historical fact.

## 1.5 Sample-selection disclosure — ACCEPT

The symbolic framework supplied at least part of the initial actor-selection procedure, even though it supplies no admissible evidence and closes no element. That creates a non-random sample and must be disclosed.

### Required sentence

> **The symbolic framework influenced which actors were initially examined. It supplies no evidence, and no disposition rests on it. The sample is therefore non-random; findings are claims about the examined actors and routes, not base-rate claims about government generally.**

This limitation does not defeat the narrow proposition that particular routes exist. It does prevent the paper from calling those routes unusual, exceptional, or disproportionately concentrated without a comparison population.

## 1.6 “Negative controls” — ACCEPT

Failed rows inside the selected actor set are **null results**, not controls. A control population must be selected independently of the theory.

## 1.7 Model convergence — ACCEPT

Add this rule:

> **Agreement among models reading the same record never upgrades a factual or structural disposition. Model convergence may show legibility or reproducibility of interpretation; it is not independent evidence about the world.**

## 1.8 Source concentration — ACCEPT

Once the source register exists, add:

- sole-source flag;
- outlet/agency claim count;
- common-origin flag where several stories derive from one filing or one investigation;
- correction/retraction history where material.

Repeated reporting from one underlying instrument is one brick, not several independent bricks.

## 1.9 Discriminability — ACCEPT

The handoff invokes discriminability but does not operationalize it. Either remove the term or score it. A workable unweighted rubric is:

1. Directness of record: 0–2
2. Source independence: 0–2
3. Temporal fit: 0–2
4. Identified mechanism: 0–2
5. Repetition/pattern: 0–2
6. Survival of strongest innocent explanation: 0–2

The score is descriptive, not a substitute for element-by-element reasoning. No threshold should be invented until several exemplar rows are scored and stress-tested.

---

# 2. Factual red markers adjudicated

## 2.1 `TC-01` crypto-income range — ACCEPT WITH A DIFFERENT REWRITE

Claude is right that the current `$1.2B–$1.4B+` range hides a real denominator problem. But “replace it with `$580M–$1.4B+` and downgrade” is still too blunt.

The publications are classifying different components:

- CNBC's headline subtotal of **more than $580 million** consists principally of World Liberty token proceeds and an equity sale.
- The same disclosure separately lists roughly **$635 million** in “Celebration Coins” royalties; later reporting identifies those royalties as memecoin-related.
- AP reports approximately **$1.2 billion** from crypto businesses.
- Reuters and TIME report **more than $1.4 billion** from crypto ventures/related income.

### Canonical replacement

> **The certified filing reports multiple crypto-linked income components. Published totals range from more than $580 million to more than $1.4 billion depending principally on whether “Celebration Coins,” stablecoin-related, licensing, equity-sale, and related venture income are included. The paper must publish a component table and its own stated taxonomy rather than present a single aggregate as self-defining.**

**Disposition:** `INDETERMINATE — AGGREGATE TAXONOMY`; underlying disclosed components may separately be `ESTABLISHED FACT` once entered from the filing.

## 2.2 `PL-06` chronology — ACCEPT AS AN ADDITION, NOT A LITERAL CORRECTION TO THE ROW

The canonical `PL-06` row states a custody chain but contains no detailed chronology. Claude's corrected sequence is therefore best treated as a required expansion rather than proof that the literal row misstated dates.

The sequence supported by current reporting is:

1. December 2025 court order establishes the legal baseline and permitted limits.
2. 7 January 2026 transfer exceeded those limits and included millions of records.
3. Late May 2026 temporary pause followed the government's admission.
4. A 16 July 2026 filing/declaration disclosed onward sharing to Palantir; reporting followed 17 July.
5. Later filings/reporting described additional custody and deletion problems.

This chronology should be attached to `PL-06`, with each step sourced separately.

## 2.3 `PL-06` / `PL-07` Microsoft Teams mechanism — ACCEPT

The Teams-chat transfer and chat-deletion response are materially important because they cut in both directions:

- They support a concrete **custody/control failure** finding.
- They do **not** establish ingestion into ELITE or another operational system.

Required boundary:

> **Onward transfer to Palantir personnel is supported. System ingestion, querying, lead generation, arrest, detention, or removal based on the disputed dataset remains not established absent logs or a case-specific enforcement join.**

## 2.4 `PL-09` Barbaccia appointment date — REJECT CLAUDE'S CORRECTION

Claude says the TTS acting-director appointment occurred in May 2026 rather than February 2026. That is wrong.

The General Services Administration's own announcement is dated **19 February 2026** and states that Gregory Barbaccia was appointed Acting Director of Technology Transformation Services and Senior Advisor to the Administrator. Contemporary Nextgov and FedScoop reporting also dates the appointment to 19 February 2026.

The red-marker audit's May correction must **not** be merged.

## 2.5 `PL-09` return to Palantir — ACCEPT WITH TEMPORAL PRECISION

Claude is directionally right that “wait for a primary instrument” is too rigid for a future private-employment plan. The evidence class available here is an on-record public statement by the GSA Administrator plus White House confirmation and multi-outlet reporting.

As of 17 August 2026, the proper proposition is:

> **Barbaccia announced a departure effective 31 August 2026, and officials/reporting state that he plans to return to Palantir afterward. The planned return is established as an announced future destination, not yet as completed employment.**

`expires_or_recheck: 1 September 2026`

The useful missing instruments are post-employment ethics guidance, recusals, and any 18 U.S.C. §207 restrictions—not an impossible generic “primary source” proving a future private job.

## 2.6 `PA-06` Peter Thiel omission — ACCEPT

Dialog was co-founded by Peter Thiel and Auren Hoffman in 2006. Because Thiel also co-founded Palantir, that is a real cross-packet structural fact and should be stated.

Boundary:

> **A common founder links the network and the vendor at the level of institutional history. It does not establish that Dialog caused a Palantir procurement, that members acted in concert, or that a common command exists.**

## 2.7 `PA-06` outlet correction history — ACCEPT, WORD PRECISELY

WIRED corrected a conflation between Jeffrey Epstein and a different person named Jeff Epstein, a former Oracle executive. The Guardian updated its article to clarify that Lisa Randall—not Jeffrey Epstein—received the 2014 invitation and forwarded it to him.

Do not say the entire stories were retracted. Say:

> **The source line carries a material identity correction. The underlying leak remained authenticated, while one high-salience identification was corrected. This both weakens careless name-matching and demonstrates a functioning corrections process.**

## 2.8 WorldClaw, OCC charter, MGX, Rubio/State, Treasury/IRS, Clark Minor, and Bondi omissions — DEFER AS KNOWN-LIVE LEADS

These items are asserted by Claude to have existed in raw notes, but the raw notes and underlying instruments were not part of this two-file adjudication. They should not be silently promoted into canonical propositions.

Add a section titled:

### Known-live leads not yet adjudicated

Each item receives:

- `origin:` red-marker audit / raw-note reference
- `source_status:` not restored
- `disposition:` INDETERMINATE — NOT YET ADJUDICATED
- `next_action:` recover source and draft claim elements

This prevents loss without pretending adjudication occurred.

## 2.9 WorldClaw legality wording — DEFER, WITH A GENERAL RULE

The difference between “no indication of illegality was reported” and “the outlet found the arrangement legal” is real. Apply this rule whenever the source packet is restored:

> **Absence of an identified violation is not an affirmative legal finding. News reporting does not adjudicate legality unless it is accurately reporting an identified authority's legal determination.**

## 2.10 Timekeeper/Bondi date symmetry — NOT APPLICABLE TO THE CANONICAL HUMAN-SIDE SPINE

The canonical handoff already excludes symbolic timing from the evidentiary spine. Any unverified symmetry should remain outside the human-side case or be deleted from raw-note cleanup. It does not require a canonical claim-row amendment.

---

# 3. Legal-method corrections

## 3.1 `CR-08` clearance pathways — ACCEPT

The acquisition queue currently collapses legally distinct possibilities. Split them:

### Path A — Individual waiver under 18 U.S.C. §208(b)(1)

- written;
- issued in advance by an authorized/appointing official;
- request the waiver and supporting determination.

### Path B — Regulatory exemption under 5 C.F.R. part 2640

- may operate without an individualized waiver;
- identify the claimed exemption and test its elements;
- there may be no bespoke clearance instrument.

### Path C — Determination that the directive was not a covered particular matter or lacked direct and predictable effect

- seek ethics advice, legal analysis, screening memorandum, or contemporaneous communications;
- do not call this a waiver.

### Path D — Other authority or factual basis

- identify precisely rather than using “equivalent clearance” as a catch-all.

Add a sixth negative-evidence state:

> **No individualized instrument was required under the asserted legal pathway.**

## 3.2 Adult-child gifts — ACCEPT AS COUNTEREVIDENCE TO TEST, REJECT AS AUTOMATIC EXTINGUISHMENT

Section 208 automatically imputes interests of a spouse and minor child, not every adult child. That makes the adult-child gift fact potentially significant counterevidence.

Claude's statement that a gift to an adult child “genuinely extinguishes” the imputed interest is too categorical. Dependency, retained control, beneficial arrangements, timing, and the precise asset transfer may matter.

Required treatment:

> **Restore the fact as counterevidence and analyze whether the transfer actually ended the official's own or statutorily imputed interest. Do not presume either evasion or exculpation.**

## 3.3 Certificates of Divestiture — ACCEPT

Add Certificates of Divestiture and Certification of Ethics Agreement Compliance to the acquisition queue for Blanche and Patel.

Boundary:

- A Certificate of Divestiture can date and document an approved divestiture process and may provide tax-deferral treatment.
- Not every divestiture necessarily produces a CD.
- Absence of a CD is not proof of noncompliance.

## 3.4 External governing instruments — PARTIAL / CONDITIONAL

Claude says the handoff is not self-contained because raw notes invoke the Capture, Conduct Docket, Palace, Priesthood, and Timekeeper instruments. The canonical handoff itself states direct tests and does not depend on all of those names.

Rule:

- If a disposition actually depends on an external standard, inline the operative test or attach the instrument.
- If it does not, remove the name rather than importing a whole symbolic or methodological system.
- Timekeeper and mythic standards remain outside the human-side evidentiary spine.

---

# 4. Base rates and controls

Claude's control-set criticism is strong but must be scoped precisely.

A matched comparison set is **not required to establish that a named route, contract, disclosure, custody transfer, or access relationship exists**. It is required before claiming that the observed pattern is unusual, exceptional, concentrated, or diagnostic of a particular administration/network.

Recommended control work:

1. Twenty comparable officials from a prior administration, selected before reviewing their disclosures.
2. Twenty major federal IT vendors, tested for sole-source continuation, proprietary lock-in, revolving doors, and cross-agency footprint.
3. A sector-specific sample of incoming officials with assets in sectors touched by their portfolios, including time-to-divestiture and pre-divestiture participation.

Publication rule:

> **Without a comparison set, the paper may map selected routes but may not infer above-baseline prevalence.**

---

# 5. Immediate patch sequence

## Blocking before Ultra

1. Build the source register.
2. Add both evidence axes to every row.
3. Replace the disposition vocabulary.
4. Add `as_of` and `expires_or_recheck` fields.
5. Insert the sample-selection limitation.
6. Add the model-convergence prohibition.
7. Repair `TC-01`, `PL-06`, `PL-09`, and `PA-06` using attached source entries.
8. Create the known-live/not-yet-adjudicated queue rather than losing omitted threads.

## High-value next

9. Split `CR-08` into waiver / exemption / no-particular-matter pathways.
10. Add Certificates of Divestiture and compliance certifications to the acquisition list.
11. Restore adult-child transfers as counterevidence requiring analysis.
12. Rename negative controls to null results.
13. Add source-concentration fields.
14. Score one exemplar row using the discriminability rubric.

## Before publication, not necessarily before the first synthesis draft

15. Build matched controls and base rates.
16. Recalculate Trump crypto components directly from the certified filing.
17. Build case-specific recusal and consequence tables.
18. Complete the narrow media corridor.

---

# 6. Recommended canonical row schema

```yaml
claim_id: PL-06
packet: Palantir / state-data architecture
proposition: >-
  [One proposition only.]
as_of: 2026-08-17
event_date:
expires_or_recheck:
disposition: ESTABLISHED FACT | SUSTAINED — ARCHITECTURE | OPEN ELEMENT | NOT ESTABLISHED | INDETERMINATE | WRONG INSTRUMENT | RETIRED/CORRECTED | NULL RESULT
instrument_strength: P1 | P2 | P3 | P4 | P5 | P6 | X | UNASSIGNED
source_provenance: SRC-P | SRC-V | SRC-L | SRC-A | MIXED | UNASSIGNED
sources:
  - source_id: SRC-PL-06-01
    issuer_or_outlet:
    title:
    date:
    url_or_docket:
    supports:
    limitations:
source_concentration:
strongest_innocent_explanation:
contrary_evidence:
missing_element_or_instrument:
next_test:
revision_history:
```

---

# 7. Verification ledger for this adjudication

The following live sources were checked during this pass. They are leads for the eventual source register, not a substitute for row-level attachment and excerpting.

1. U.S. General Services Administration, “Greg Barbaccia Appointed Acting Director of the Technology Transformation Services,” 19 February 2026.  
   https://www.gsa.gov/about-gsa/newsroom/news-releases/greg-barbaccia-appointed-acting-director-of-the-tts-02192026

2. FedScoop, “Outgoing federal CIO Greg Barbaccia will return to Palantir,” 31 July 2026.  
   https://fedscoop.com/outgoing-federal-cio-greg-barbaccia-will-return-to-palantir/

3. Nextgov/FCW, “Greg Barbaccia to return to Palantir after leaving government,” 31 July 2026.  
   https://www.nextgov.com/people/2026/07/greg-barbaccia-return-palantir-after-leaving-government/415149/

4. NPR, “ICE shared Medicaid data it wasn't supposed to have with Palantir,” 17 July 2026.  
   https://www.ualrpublicradio.org/npr-news/2026-07-17/ice-shared-medicaid-data-it-wasnt-supposed-to-have-with-palantir

5. LAist/NPR republication containing the Anna Rich declaration's Teams-chat description.  
   https://laist.com/brief/news/ice-shared-medicaid-data-it-wasnt-supposed-to-have-with-palantir

6. WIRED, “Leak Exposes Members of Peter Thiel's Secretive ‘Dialog’ Society,” 16 June 2026, including correction note.  
   https://www.wired.com/story/leak-exposes-members-of-peter-thiels-secretive-dialog-society/

7. The Guardian, “Key Trump allies and Musk on leaked list for secretive Peter Thiel retreat,” 20 June 2026, updated 22 June 2026.  
   https://www.theguardian.com/technology/2026/jun/20/trump-elon-musk-peter-thiel-retreat

8. U.S. Office of Government Ethics, 5 C.F.R. part 2640 guidance concerning §208 exemptions and waivers.  
   https://www2.oge.gov/web/oge.nsf/Resources/5%2BC.F.R.%2BPart%2B2640%3A%2BInterpretation%2C%2BExemptions%2C%2BWaiver%2BGuidance%2BConcerning%2B18%2BU.S.C.%2B208%2B%28Acts%2BAffecting%2Ba%2BPersonal%2BFinancial%2BInterest%29

9. U.S. Office of Government Ethics, Officials' Individual Disclosures Search Collection / Certificates of Divestiture.  
   https://www.oge.gov/web/oge.nsf/Officials%20Individual%20Disclosures%20Search%20Collection?OpenForm=

10. U.S. Office of Government Ethics, certified annual financial disclosure release for the President and Vice President, 30 June 2026.  
    https://www.oge.gov/web/oge.nsf/Resources/Now%2BAvailable%3A%2BThe%2BPresident%E2%80%99s%2Band%2BVice%2BPresident%E2%80%99s%2Bcertified%2Bannual%2Bfinancial%2Bdisclosure%2Breports

11. AP, “Trump filing shows he took in about $1.2 billion from crypto businesses last year,” 1 July 2026.  
    https://apnews.com/article/trump-financial-disclosure-crypto-060c15062b8fedc6104159ea13775463

12. Reuters, “Trump reports over $1.4 billion in income from crypto ventures,” 30 June 2026.  
    https://www.reuters.com/world/us/trump-reports-over-14-billion-income-crypto-ventures-2026-06-30/

13. CNBC, “Trump's annual financial disclosure shows more than $580M in crypto-related income,” 1 July 2026. The article's subtotal excludes or separately treats the $635 million “Celebration Coins” line, which is why a component taxonomy is required.

---

# 8. Final disposition

Claude's audit is valuable and materially improves the project. Its strongest contributions are the source-register block, row-schema enforcement, sample-selection disclosure, §208 pathway split, source-concentration warning, and model-convergence prohibition.

It is **not** safe to merge wholesale. The Barbaccia date correction is demonstrably wrong; the `TC-01` correction needs a component-level taxonomy rather than a new blunt range; several “missing claims” derive from raw notes not supplied here; and several legal statements need narrower formulation.

The human-side investigation therefore moves to:

> **v0.1R — SOURCE RECOVERY AND REGISTRY REPAIR**

It does not move to Ultra synthesis until the blocking sequence in §5 is complete.

**No crown for Claude's red marker either. The audit gets audited.**
