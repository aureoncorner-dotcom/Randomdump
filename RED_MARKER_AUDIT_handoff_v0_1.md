# RED-MARKER AUDIT
## HUMAN_SIDE_CANONICAL_HANDOFF v0.1 — data integrity pass

**Auditor scope:** factual accuracy, internal consistency, source integrity, methodological validity.
**Explicitly out of scope per request:** ideological critique, tone, whether the thesis is worth pursuing.
**Audit date:** 17 August 2026 (same as the document's stated evidence cutoff).
**Method:** handoff read in full against the raw notes; ~10 load-bearing checkable claims verified against live sources.

---

## 0. Top-line

The instrument is better than the material it governs. The methodology section (§1–3) is genuinely disciplined — the negative-evidence rule, the contamination gate, and the "access ≠ influence" prohibition are the kind of thing most investigative documents don't have. The problem is that **the registry does not actually obey its own instrument**, and one structural defect makes the whole thing unusable as a handoff in its current form.

Ranked by severity:

1. **The source register does not exist.** Fatal for a handoff.
2. **The evidence-class axis (P1–P6) is declared mandatory and then applied to about half the rows.**
3. **Three factual errors and one significant omission** found in a sample of ~10 verifications.
4. **The disposition vocabulary is not controlled** — "true bill" is doing three incompatible jobs.
5. **Sample-selection problem is unaddressed**, and it's the first thing a hostile reader will hit.

Nothing here says the corridors are wrong. Most of what I spot-checked held up. But the document currently cannot survive an adversarial read, and several of the failures are unforced.

---

# PART A — Structural defects that will break the synthesis pass

## A1. There is no source register. This is the critical defect.

§12 instructs the synthesis model: *"Attached primary sources control factual content"* and *"Attach primary instruments to every load-bearing claim."*

**There are no attached primary sources.** Not one row in the registry contains a URL, a document title, a docket number, a filing date, an accession date, or an outlet name. Every row says `P1 / SRC-P` and stops.

Worse, the raw notes — the only place where sourcing was ever attached — carry it as dead tool-call artifacts:

```
citeturn610338news39
fileciteturn3file3L128-L143
citeturn769136search1
```

These are internal handles from another model's retrieval session. They resolve to nothing. **The entire provenance layer of this investigation is currently unrecoverable.** The SRC-P/V/L/A taxonomy is a label on an empty box.

Concretely: `PL-02` asserts DoD modification P00005 to contract W911QX-24-D-0012 for $795M and is dispositioned ESTABLISHED / P1 / SRC-P. That claim is probably correct. But the handoff gives the synthesis model no way to reach the DoD contract announcement, and no date for it. The model will either fabricate a citation or drop the claim.

**Fix before anything else:** every row needs `source_1 … source_n` with outlet/agency, document title, date, and URL or docket. If a source can't be re-found, the row is not P1 — it's unsourced, and it should say so.

## A2. P1–P6 is declared mandatory and then inconsistently applied

§2 opens: *"Two independent axes are mandatory."*

Rows carrying **neither** axis: `RP-06`, `CR-08`, `CR-09`, `TC-02`, `TC-03`, `TC-04`, `PL-04`, `PL-07`, `PL-08`, `PL-10`, `PL-11`, `PL-12`, `PL-13`, `PL-14`, `PA-02`, `PA-04`, `PA-05`, `PA-07`, `PA-08`, `JU-01` through `JU-11` (all eleven), and the entire §7 join table.

That's roughly 60% of the registry violating a rule the document calls mandatory two pages earlier. A synthesis model reading this will reasonably conclude the axis is decorative.

Also: **`X — Inference exceeding the current record` is defined and then never used once.** A classification scheme with an unused "this is inference" bucket, in a document whose central risk is inference-creep, is a scheme that isn't being run.

## A3. "TRUE BILL" is doing three incompatible jobs

The document invokes a *"skeptical reasonable factfinder... after hearing the strongest innocent explanation"* (§1.1) — that's a **trial persuasion** standard. It simultaneously uses **true bill / no bill**, which is grand jury vocabulary — an *ex parte* probable-cause finding where the defense is not heard at all.

These are different burdens, and the document slides between them. Then "TRUE BILL" gets used for at least three distinct things:

| Usage | Actual meaning | Example |
|---|---|---|
| Structural claim survives | "architecture supported" | `RP-05` |
| A discrete fact is proven | "this happened" | Packet 2 result, "conflict architecture and chronology" |
| A behavioral capacity is demonstrated | "he can do this" | `PA-01` Bannon |

And **NO BILL** is doing two:
- "affirmatively not supported on the record" (`CR-09`, `PL-14`)
- "claim withdrawn / venue cancelled" (`PA-07`)

`PA-07` is dispositioned **"RETIRED / NO BILL"** — that's two different stopping states stapled together, and §3 lists them as separate categories.

A no bill is a declination to charge, not an exoneration. Using it as one is the single most quotable error in the document.

**Fix:** pick one burden and state it. Then either drop the grand-jury vocabulary entirely or define each label operationally in §3 with a worked example.

## A4. Claims present in the notes are silently absent from the registry

The handoff claims to be *"the adjudicated state of the record"* and instructs the synthesis model that *"raw conversation is provenance/brainstorming history, not authoritative claim state."*

So anything not in the registry is, by the document's own rule, dead. Yet these live claims from the notes have **no registry row at all**:

- **WorldClaw / World Liberty AI-platform arrangement** — no row. Notes treat it as a live State↔Capital↔Crypto↔Tech junction.
- **OCC conditional trust-bank charter approval for World Liberty** — no row. This is arguably the *strongest* item in Packet 2B, because unlike the pardon chronology it is a live federal regulatory decision touching a presidential-family entity.
- **MGX / Abu Dhabi $2B specificity** — `TC-03` compresses this to "a large Binance-related investment," losing the foreign-sovereign-capital element entirely.
- **Rubio / State Department Palantir orders (~$33M)** — no row.
- **Treasury/IRS Palantir work** — no row.
- **Clark Minor (HHS CIO, ex-Palantir)** — no row, despite being the second revolving-door node and directly relevant to `PL-06`.
- **Bondi's own disclosure package** (TMTG/DJT, Renatus, Ballard, Newsmax, Pfizer client list) — no row anywhere, despite Bondi being AG for the entire first year of the evidentiary window.

This is the most damaging kind of silent loss, because the instruction hierarchy in §12 tells the next model to *ignore the notes*. Six live threads get deleted by an authority rule.

**Fix:** either add rows (even as `INDETERMINATE — not yet worked`) or add an explicit §4.x "Known-live, not yet adjudicated" list so nothing vanishes by omission.

## A5. No per-row dates or as-of stamps

The document has one global cutoff (17 Aug 2026). Individual rows have none. That matters acutely for:

- **`PA-07` (Powerscourt).** The retreat was scheduled 12–16 August 2026. That window **closed the day before this document's cutoff.** "Actual 2026 co-attendance not established" is a claim with a five-day-old expiry on it. It is now directly checkable and will read as stale within a week.
- **`PL-09` (Barbaccia).** His departure is dated 31 August 2026 — *fourteen days after the cutoff*. The row describes a future event in the past-tense register of an adjudicated finding.
- **`CR-01`–`CR-09`.** Blanche's title changed on 8 August 2026. Rows written against "Deputy AG / Acting AG" need a status stamp.

**Fix:** every row gets `as_of:` and, where the claim concerns a future or in-progress event, `expires:`.

---

# PART B — Factual findings (verified against live sources)

## B1. ✅ Verified and correct

I checked these because I doubted them or because they were load-bearing. They hold:

- **Blanche confirmed AG 8 August 2026, 50–49.** Correct. Collins and Murkowski voted no; McConnell absent. He is the 88th AG.
- **Bondi fired April 2026; Blanche acting AG from 2 April 2026.** Correct.
- **Barbaccia → Palantir return.** Correct, and *better sourced than the handoff admits* — see B5.
- **Powerscourt cancellation.** Correct. Hotel and Powerscourt Estate both confirmed; event was 12–16 August at Powerscourt Hotel, Co. Wicklow.
- **CMS→ICE→Palantir custody chain.** Correct in substance — see B3 for the chronology error.
- **Comcast co-CEO structure** (raw notes). Correct — Cavanagh became co-CEO effective January 2026. I expected this to be an error and it isn't.
- **Josh D'Amaro, Disney CEO** (raw notes). Correct — named 3 Feb 2026, effective 18 March 2026.

## B2. ❌ `TC-01` — the stated range is wrong at the bottom end

Handoff: *"public analyses place the total roughly in the **$1.2B–$1.4B+** range."*

Published figures on the same certified filing (OGE released it 30 June 2026, 927 pages, CY2025):

| Outlet | Figure | Framing |
|---|---|---|
| Reuters / TIME / NBC | **>$1.4B** | "from his family's crypto ventures" |
| AP | ~$1.2B | "crypto businesses" (narrower) |
| **CNBC** | **>$580M** | **"crypto-related income"** |

The $580M figure is not fringe — it's CNBC's headline number on the same document. **The handoff's range excludes the lowest published mainstream estimate by a factor of two.**

That is exactly the failure mode §1.4 warns about ("a preferred hypothesis was protected"), and it's the number a hostile reader will find in ninety seconds. The range as stated makes the document look like it went shopping.

**Fix:** state it as **~$580M – $1.4B+, definition-dependent**, and name each outlet's denominator. Then do what `TC-01` already correctly says to do — recalculate from the filing itself and publish your own taxonomy. Until that recalculation happens, this row should not be ESTABLISHED; it should be `INDETERMINATE — competing denominators`.

**Also missing and useful:** total 2025 income was >$2B, of which crypto was the largest single source. That ratio is a stronger and more defensible framing than any single aggregate.

## B3. ❌ `PL-06` — the chronology is wrong, and the correct one is better

Handoff and notes give: AP obtained an agreement July 2025 → California AG told the court March 2026 → July 2026 filings show ICE shared with Palantir.

**Actual sequence per the court record:**

1. **December 2025** — Judge Vince Chhabria (N.D. Cal.) rules CMS *may* share certain Medicaid details with ICE, with limits.
2. **7 January 2026** — CMS improperly shares a dataset of millions, including citizens and lawfully present people, exceeding the order. A separate Minnesota refugee dataset also included U.S. citizens.
3. **Late May 2026** — Chhabria temporarily pauses CMS→ICE sharing after the government admits the January overage.
4. **16 July 2026** — Motion by 20+ Democratic AGs; declaration of California DAG Anna Rich reveals ICE onward-shared the dataset to Palantir. Reported 17 July.
5. **After** — CMS *again* inadvertently re-shared the same dataset with ICE, per a DOJ filing.

The handoff's version omits the December 2025 order (the legal baseline), omits the 7 January 2026 transfer (**the actual improper act**), and misdates the California AG filing. This isn't cosmetic — the January date is the anchor for the whole chain, and it's absent.

## B4. ⚠️ `PL-06`/`PL-07` — the transfer mechanism is missing, and it's the most important detail

Per the Rich declaration: **the data was shared over a Microsoft Teams chat, and deletion was accomplished by deleting the chat.**

This is the single most consequential fact in the packet and it appears nowhere in the handoff.

It cuts hard in **both** directions, which is exactly why it belongs in:

- **Against ingestion:** an ad hoc Teams share is not a system integration. It is strong support for `PL-07`'s NOT ESTABLISHED disposition on ELITE ingestion, and the handoff currently leaves that row supported only by absence of evidence.
- **Against custody controls:** transferring millions of protected records via a chat app, and treating chat deletion as data purge, is a governance failure far more concrete than "custody exposure."

Also missing: officials **acknowledged copies remained accessible to ICE users after asserting deletion** and were still working to locate them. The notes mention "six ICE users"; I could not verify that specific count — flag it as unsourced.

Also worth capturing: NPR reports directly that ELITE is used by ICE agents to display addresses of noncitizens subject to deportation. The notes hedge this as "reporting says ICE's ELITE targeting tool draws address-related information from HHS data." The direct version is cleaner and better sourced.

## B5. ❌ `PL-09` — wrong acquisition target, and one date error

Two problems:

**(a) The date is wrong.** The notes say Barbaccia added the GSA Technology Transformation Services acting-director role in **February 2026**. Reporting says **May 2026**, alongside a senior-adviser role to the GSA Administrator. Fix or drop.

**(b) The "primary source" instruction is incoherent.** `PL-09` says the return-to-Palantir component "should be primary-source confirmed before publication."

There is no primary source for a future private-sector employment decision. There is no filing, no contract, no charter. What exists is:

- **GSA Administrator Edward Forst stating it publicly, on stage**, at a U.S. Digital Corps graduation ("Luckily, Palantir gets you back in that way")
- a **White House official confirming it to FedScoop**
- two additional sources confirming to Nextgov

That is about as good as this class of fact gets. The handoff is holding out for an instrument that cannot exist, which will cause the synthesis model to under-weight a properly sourced claim.

**Fix:** reclassify as `ESTABLISHED — on-record official statement + multi-outlet confirmation`. The honest missing instrument here is his **post-employment ethics guidance and any 18 U.S.C. §207 restrictions**, not a "primary source for the return."

## B6. ❌ Attribution inflation on WorldClaw (notes, would propagate)

Notes: *"Reuters explicitly reports that the arrangement is legal."*

Reuters reported no indication of a legal violation, and quoted seven outside experts calling the arrangement inconsistent with the administration's own China-tech posture. **"No indication of illegality" ≠ "reported as legal."** News outlets don't make legality findings.

This is a small error with an outsized cost: it is precisely the inversion the document's own contamination gate exists to catch, and it happens to *favor the subject*, which means it will be read as sloppiness rather than bias — but sloppiness in both directions is still sloppiness.

Also unverified in the notes: *"a World Liberty executive advises the venture."* Did not appear in any Reuters-derived account I checked. Verify or cut.

Verified specifics if you keep this thread: 43 of 90 models on the platform are from Chinese developers (Alibaba, Baidu, Z.ai, DeepSeek, Moonshot); USD1 accepted as payment; Trump family owns 38% of World Liberty; Reuters could not determine the financial terms between the two entities.

## B7. 🔴 `PA-06` — the biggest miss in the document

The handoff and notes describe Dialog through **Auren Hoffman** only ("Dialog chair Auren Hoffman — founder of SafeGraph and LiveRamp"), and reach for **Joe Lonsdale** as the Palantir connection.

**Dialog was co-founded by Peter Thiel.** Thiel co-founded Palantir. He is named in essentially every account of the leak, usually in the headline.

You have a Palantir packet and an access-network packet, and the person who co-founded both the company in Packet 3 and the network in Packet 4 **is not named anywhere in either document.** The notes explicitly say "the existence of the shared room/network cannot be used as the missing Palantir procurement-influence arrow" — correct, and still correct with Thiel. But a common *founder* is a materially different structural fact from a common *cofounder-of-one-thing attendee*, and it is a fact you already had available for free.

This one is not an overreach. It's an under-reach, and it's the kind that makes a reader wonder what else got skipped.

Other verified Dialog specifics the handoff omits: founded 2006; 2026 registration list names **222** people with membership status and attendee type; leaked session titles include "Navigating WWIII," "Battlefield Technologies," "Build-a-Cult," "Build-a-Party," "Disinformation and Deepfakes"; named members include Ted Cruz and Treasury Secretary Scott Bessent. Notably, **Axios reported on Dialog membership in August 2025, pre-leak** — that's an independent, non-leak-derived source line, which is exactly what your SRC-L rules should want.

## B8. ⚠️ `PA-06` — the source outlet issued a retraction on this exact story

WIRED and The Guardian **retracted** a claim that Jeffrey Epstein was invited to a 2014 Dialog meeting. The invitation went to physicist Lisa Randall, and the "Jeff Epstein" on the attendee list was a different person — a former Oracle executive.

Your `SRC-L` class is defined as *"leak-derived document independently authenticated by a named outlet."* An authenticated leak where the authenticating outlet had to retract a headline identification is a live caution about that class, and the document should carry it. Right now `PA-06` is `P4 / SRC-L` with no note.

It also happens to be a good-faith argument *for* your methodology: the outlet corrected. Say so.

## B9. ⚠️ The "Timekeeper receipt" is load-bearing on an unverified date

The notes flag Bondi's TMTG sale (2 April 2025) against her removal (2 April 2026) as "a cute symmetry and nothing more." The handling is correct — the notes explicitly refuse to draw inference.

But: I confirmed Bondi was fired in April 2026 and Blanche became acting AG on 2 April 2026. I did **not** independently confirm the 2 April 2025 disclosure-sale date. If that date is off by a day, the observation is not merely uninteresting — it's false, and it's sitting in a document that already has a stated exclusion of symbolic material.

**Recommendation:** either verify both dates to primary sources, or delete it. It carries zero evidentiary weight by the document's own rules and non-zero credibility risk. This is a free cut.

## B10. Minor precision items

- **Blanche BTC bracket.** Notes give "$100,000–$250,000" once and "$100,001–$250,000" elsewhere. OGE brackets are $100,001–$250,000. Use the bracket verbatim; it signals you read the form.
- **Blanche DAG confirmation.** Notes say 5 March 2025. Wikipedia gives assumption of office 6 March 2025; a Grassley release references a 52–46 vote dated 19 February 2025. Three variants. Pin it to the Senate roll call.
- **Task force "statutory membership."** The anti-Christian-bias task force was created by **executive order**, not statute. "Statutory membership" is a category error that a lawyer will catch instantly. Use "membership designated by the establishing order."
- **ICE contract number.** `70CTD022FR0000170` appears once and is never re-verified. Check against FPDS/USAspending before publication — a wrong contract number discredits an entire procurement section.
- **Possible double count.** The notes list a $795M Maven modification *and* "a Maven/CDAO order with a potential value above $600 million" as separate items. These may be nested or overlapping. `PL-02` only carries the $795M. Reconcile explicitly or the reader will assume inflation.
- **Late filing fees.** OGE's standard late fee is **$200**, and the disclosure doesn't state a total. The notes handle this well ("a disclosure-compliance fact, not evidence the transactions were illicit"); the $200 figure makes the deflation concrete and should survive into the handoff. It currently doesn't appear at all.

---

# PART C — Methodological problems

These are where the document is most vulnerable, because they can't be fixed by adding citations.

## C1. Sample selection — the mythology chose the board

The notes say it plainly: *"we did not need Revelation whatsoever to find this structure,"* and *"the labels would be describing a political network we already independently demonstrated, rather than creating it."*

The first clause is true. The second is not established.

Revelation didn't supply the evidence — but it supplied **the list of people to investigate**. The board was assembled as a casting chart, and then each name was worked for disclosures, contracts, and relationships. That's a selection procedure, and it determines what you find.

Run the counterfactual: take any twenty senior officials of any administration, pull their 278s, ethics agreements, PTRs, prior employers, and their agencies' major vendors. You will find crypto holdings, defense-contractor holdings, revolving doors, sole-source justifications, and donor proximity. Financial disclosure exists *because* these are common.

The handoff's §0 formulation ("multiple independently documented pathways...") is carefully worded and survives this. But `JU-11`'s "durable political-selection architecture" and Corridor C's "vendor-dependency" framing implicitly claim these patterns are *notable*, and notability requires a comparison class the document doesn't have.

**Fix — and this is cheap:** run the same extraction on a matched control set. Twenty senior officials from a prior administration. Or the twenty largest federal IT vendors, checked for the same sole-source/proprietary-IP lock-in pattern as Palantir. Publish the control results even if they're boring. **A control set is the single highest-leverage addition available to this document.** It converts "we found things about these people" into "these people differ from baseline in X ways," which is the difference between a dossier and a finding.

## C2. The "negative controls" are not controls

The notes designate Gabbard and Hegseth as "excellent negative controls," and `JU-10` designates Kavanaugh/Barrett as a "negative control."

These are members of the treatment group whose rows failed. That is a null result — valuable, and correctly preserved — but it is not a control. A control is a comparison population selected *without reference to the hypothesis*.

Calling failed rows "controls" implies the sample was validated. It wasn't. Rename them **null results** and the document gets more honest for free.

## C3. No base rates anywhere

Every "notable" claim needs a denominator the document doesn't supply:

- **`PL-04` (ICE lock-in).** What fraction of large federal IT systems have sole-source continuations justified by incumbent proprietary architecture? If it's 60%, "textbook rising bypass cost" describes federal IT procurement generally, not Palantir specifically. If it's 5%, you have something real. **You currently don't know which, and the row is dispositioned PROVISIONALLY ESTABLISHED.**
- **`PL-09` (revolving door).** How many senior federal technology officials come from and return to a major vendor? GAO and OGE have published on this.
- **`CR-01`–`CR-05` (Blanche).** How often do incoming officials hold assets in a sector they will regulate, and how often does policy action precede completed divestiture? If it's routine, the chronology is still a real §208 question but stops being an outlier. If it's rare, that's a finding.

Base rates would likely *strengthen* the Blanche row and *weaken* the Palantir procurement row. That asymmetry is itself worth knowing before publication rather than after.

## C4. Source concentration is undisclosed

§1.1 requires *"independent bricks"* and the notes list *"independence of the sources"* as a scoring axis. Neither is applied.

**ProPublica alone** supports, at minimum: Thomas/Crow, Alito/Singer, Gorsuch/Duffy, Johnson/Berger, the Barbaccia disclosure summary, the DOJ statement on Blanche's clearance, and the Leo pre-Marble funding figure. That is one outlet load-bearing across three of five packets.

ProPublica is a strong outlet with a corrections practice — that's not the point. The point is that the document repeatedly presents single-outlet-derived rows as independent bricks, and a single-source failure would cascade across packets that currently appear to corroborate each other.

**Fix:** add a `source_concentration` field, or a table showing per-outlet claim counts. Where ProPublica is the sole source, say so on the row.

## C5. Model convergence is treated as corroboration

The notes get this half right — *"Copilot and DeepSeek are mostly synthesis validators, not new evidentiary witnesses"* — and then immediately violate it: *"All four outside reviews are independently landing on essentially the same surviving structure... a pretty remarkable degree of agreement."*

Four models reading the same summary and agreeing is **correlated error, not independent confirmation.** It is close to zero evidence about the world. It tells you the document is internally legible, which is worth something, but nothing about whether the claims are true.

The handoff mostly avoids importing this — good — but §12's authority hierarchy doesn't prohibit it, and the raw notes will be in the synthesis model's context. Add an explicit rule: **model agreement never upgrades a disposition.**

## C6. Three distinct clearance instruments are being conflated

`CR-08` and the Priority 1 queue list "written §208 determination, waiver, ethics memorandum, contemporaneous advice, or equivalent clearance" as if these are variants of one document. They are legally distinct, produced by different actors, with different paper trails:

1. **A §208(b)(1) waiver** — written, issued by the *appointing official* in advance, requires a finding that the interest is not so substantial as to affect service integrity. For a Deputy AG this is a narrow and identifiable set of possible issuers.
2. **A regulatory exemption under 5 C.F.R. Part 2640** — operates automatically. **No waiver, no document, nobody signs anything.** If DOJ is relying on an exemption, there is *no instrument to produce*, and your Priority 1 acquisition would come back empty while the clearance claim remained true.
3. **A determination that no "particular matter" existed** — an ethics-official legal opinion, not a waiver at all.

This matters directly: **the document's `CR-07` boundary rule ("lack of response does not prove the clearance does not exist") is correct but incomplete.** Option 2 means the clearance could be valid *and* unproduceable *and* nonexistent as a document, simultaneously. That's a fourth negative-evidence state your §1.1 rule 7 doesn't currently enumerate.

**Fix:** split `CR-08`'s missing instrument into 1/2/3 with separate acquisition paths, and add "no instrument exists because none was required" to the negative-evidence taxonomy.

## C7. The gift-to-adult-children fact is under-analyzed and cuts both ways

The notes record that Blanche gifted BTC, SOL, ADA and ETH in whole or part to adult children and a grandchild, via transactions not requiring PTR reporting. The handoff drops this entirely.

It's legally significant. **§208 imputes the financial interests of a spouse and minor children — not adult children.** So a gift to an adult child genuinely extinguishes the imputed interest, which is real counterevidence on the conflict question.

It also raises a separate question about timing and about whether a Certificate of Divestiture was sought (see C8), and about whether "divestiture" as used in the ethics agreement was satisfied by gift versus sale.

Either way — **counterevidence the document collected and then lost in the handoff.** §12 says "preserve null results." This is one.

## C8. Certificates of Divestiture are never mentioned

The standard OGE pattern for a required divestiture is a **Certificate of Divestiture (CD)**, which permits capital-gains deferral and is issued by OGE on agency request. CDs are dated, indexed, and obtainable.

For both Blanche and Patel, a CD (or its absence) would independently date and document the divestiture process, and would be far easier to obtain than the §208 clearance you've made Priority 1. It appears nowhere in the acquisition checklist.

**This is the cheapest unclaimed instrument in the document.**

## C9. "Discriminability" is defined and never operationalized

The notes propose scoring each claim on six axes: directness of record, independence of sources, temporal fit, mechanism, pattern/repetition, survival of the innocent explanation.

No scale. No weights. No threshold. No worked example. Not one row in the registry carries a score.

As written, "discriminability" is a word standing where a method should be. Either build the rubric with a scored exemplar row, or cut the claim that you have one — because a reviewer will ask for a scored row and there isn't one.

## C10. The handoff is not self-contained

§1 and the notes repeatedly invoke governing instruments that are **not included**: the Capture instrument, the Conduct Docket, Coup2's Palace test and contamination rule, the Priesthood invocation/operation threshold, Timekeeper rules.

The Palace threshold in particular is cited as the standard `PA-03` and `PA-04` are adjudicated against, and it's absent. The synthesis model cannot check whether the disposition follows from the rule.

**Fix:** inline the operative text of every invoked standard, or drop the references and state the tests directly in §1.

## C11. The one-year mythology claim is unproven as stated

§11 says the mythic material "may not upgrade a human actor, infer coordination, establish intent, or close an open evidentiary element." Good rule, and the registry appears to follow it.

But the *stronger* claim in the notes — that a reader could "rip every myth page out and still have a coherent institutional investigation" — has one hole: **the myth selected the sample** (C1). The document should state that limitation explicitly rather than claim full separability. A skeptical reader who spots it unaided will discount everything else.

Suggested honest phrasing: *"The symbolic framework determined which actors were examined. It supplied no evidence, and no disposition rests on it. Sample selection is therefore non-random, and the findings should be read as claims about these actors rather than as base-rate claims about government generally."*

That sentence costs nothing and forecloses the strongest available attack.

---

# PART D — Priority fix list before the synthesis pass

**Blocking — do not run Ultra without these:**

1. Build the source register. Every row: outlet/agency, title, date, URL/docket. (§A1)
2. Apply P1–P6 and SRC to every row, or delete the mandatory language. (§A2)
3. Fix or restate `TC-01`'s range to include the ~$580M figure; downgrade to INDETERMINATE pending your own recalculation. (§B2)
4. Correct the `PL-06` chronology: Dec 2025 order → 7 Jan 2026 improper transfer → late May 2026 pause → 16 July 2026 motion. (§B3)
5. Add the Teams-chat transfer/deletion mechanism to `PL-06`/`PL-07`. (§B4)
6. Add Peter Thiel to `PA-06`. (§B7)
7. Restore dropped claims or add an explicit "live but unadjudicated" section. (§A4)

**High value, low cost:**

8. Split `CR-08`'s missing instrument into waiver / regulatory exemption / no-particular-matter determination; add "no instrument was required" to the negative-evidence taxonomy. (§C6)
9. Add Certificates of Divestiture to the acquisition queue for Blanche and Patel. (§C8)
10. Restore the adult-children gift fact as counterevidence. (§C7)
11. Add the WIRED/Guardian retraction note to `PA-06`. (§B8)
12. Rename "negative controls" → "null results." (§C2)
13. Add the sample-selection limitation sentence. (§C11)
14. Cut the Bondi date symmetry, or verify both dates. (§B9)
15. Reclassify `PL-09`; the real missing instrument is §207 post-employment guidance. (§B5)

**Structural, before publication:**

16. Resolve the true-bill / trial-standard mismatch and give each disposition label an operational definition with an example. (§A3)
17. Add per-row `as_of` and `expires`. (§A5)
18. Build the control set. (§C1)
19. Add base-rate work for `PL-04`, `PL-09`, and the Blanche chronology. (§C3)
20. Add source-concentration disclosure. (§C4)
21. Add an explicit rule that model agreement never upgrades a disposition. (§C5)
22. Build the discriminability rubric with one scored exemplar, or cut the claim. (§C9)
23. Inline the operative text of the Capture / Coup2 / Priesthood / Timekeeper standards. (§C10)

---

# PART E — What holds up

Worth saying plainly, since the rest of this is red ink.

- **The corrections ledger (§5) is the best thing in the document.** Nine corrections preserved, including several that killed attractive claims. `JU-05` retiring the Seid→SCOTUS arrow on straightforward chronology is a genuinely disciplined move most documents in this genre would not make.
- **The negative-evidence rule (§1.1.7)** — distinguishing *not found* / *not produced* / *no response* / *withheld* / *does not exist* — is more careful than most professional investigative standards. C6 shows it needs a fifth state, but the axis is right.
- **`CR-07`'s boundary** ("lack of response does not prove nonexistence") is the correct call and was made against the document's own interest.
- **`PL-07` NOT ESTABLISHED** is correctly dispositioned and is the row most likely to be attacked. B4's Teams-chat detail makes it defensible rather than merely cautious.
- **§9's do-not-state list** is well-constructed and is the thing most likely to keep the synthesis model honest.
- **Packet 2's structure** — established chronology, open legal element, no bill on intent — is the model the other packets should follow. It is the only packet where the three tiers are cleanly separated.

The instrument is sound. The registry hasn't caught up to it yet, and the provenance layer is missing. Fix the source register first; everything else is downstream of being able to check anything.
