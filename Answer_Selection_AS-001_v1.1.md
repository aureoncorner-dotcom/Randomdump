# AS-001 v1.1 — Request-bound answer selection and claim disposition

Anonymous · CC0 1.0 Universal · 10 September 2026

**Deliverable:** amendment to Geometry_Direct_Service_Update §5, followed by an implementation specification and acceptance cases. This revision operationalizes distinctions already present in the source corpus and incorporates Claim Closure Geometry v0.1 and the executed correction reports. It updates both the amendment and implementation specification. The September 9 source and historical findings remain intact.

**Operative rule:** Bind the answer to the governing user request and its full task-bearing record. Select an ordered, provenance-linked answer unit that accounts for every relevant span and preserves all required content. A pause, acknowledgment, node label, node position, end-of-turn event, or exact copy supplies no completion certificate. When the recorded material cannot support a valid complete answer, return an explicit partial, failed, or unresolved result; never promote the last available text to a validated answer.

**Revision outcome:** specification updated; existing correction results retained as completed results within their reported scopes. AS-001 integration and its regression suite have not been executed. The finite claim-closure verifier was rerun successfully in this review: 2,048 fiber checks and 81,408 calibration checks.

**Added operative requirement:** A warranted finding must govern the answer. Preserve its disposition while the claim-relevant evidence and criterion remain unchanged. Validate any replacement against the original task, and check the actual delivered output against the validated candidate. These are separate operations with separate receipts.

## Part I — Amendment for §5

### 5A. Request-bound selection

For each eligible episode, retain the user object O, the governing request R, applicable prior context and corrections, and the ordered source records E. R includes explicit amendments and withdrawals; quoted text and embedded documents do not become new governing instructions merely by containing imperatives. Bind each candidate span to the request it actually addresses. An intervening question does not silently cancel an earlier unfinished task.

Selection operates on spans, including text within mixed status/content nodes and references to required non-text assets. It must inspect the whole retained episode available for R, including adjacent assistant continuations and stage-interposed continuations. A narrow detector's zero count establishes only the absence of its own matched pattern.

Keep three answer objects separate:

| Object | Meaning |
|---|---|
| A_recorded | The historical selected text, unchanged, with its original selection rule and node references. |
| A_candidate | The proposed ordered answer unit, assembled from source-linked spans. It can be incomplete or defective. |
| A_validated | A_candidate after selection, completion, applicable answer-content compliance, and claim-disposition fidelity all pass. Otherwise this field is null. |

Every relevant source span receives a disposition: include; omit as task-irrelevant/status; omit as evidenced redundant; superseded by an identified valid correction; exclude from the proposed answer as a located defect; or unresolved. Every omission needs a reason and source reference. A later statement does not supersede an earlier one solely because it is later. Preserve negation, uncertainty, attribution, qualifications, citations, and dependencies wherever they carry required meaning.

Exclude a status span from the answer unit only after checking its function against R. A requested exact quotation of “Checking.” is task content. A separately emitted “Checking.” while another task remains unanswered is status. Supplied labels are hints, not adjudications.

### 5B. Independent witnesses

Score the following separately, using PASS, FAIL, or UNKNOWN with evidence:

- **S — selection fidelity:** the request and source window are bound; all relevant spans are accounted for; the proposed unit loses no required available content, introduces no unmarked new content, and makes no unresolved meaning-changing omission or merge.
- **C — task completion:** the proposed unit satisfies each explicit task obligation at the declared evidence boundary. Text saying work was done is insufficient where the task requires an actual artifact, calculation, lookup, action, or verification result.
- **K — answer-content compliance:** the proposed answer meets the applicable content corrections and governing constraints. A preserved adjudicative rider can fail K even when source selection is faithful.
- **P — claim-disposition fidelity:** each bounded claim receives the disposition warranted by its declared evidence criterion. A correct acknowledgment followed by an unrelated blocking prerequisite fails P. With no claim-disposition obligations, PASS requires an explicit verified-empty scope.
- **H — historical service compliance:** the original emitted response, including its stages and answer content, met the applicable correction. H is scored before projection and cannot be overwritten by an offline repair.
- **B — byte preservation:** a declared before/after payload pair has exactly equal bytes. B concerns only those identified payloads.

FAIL means an evidenced violation; UNKNOWN means the necessary witness is absent or ambiguous. An observed failure remains FAIL when another cell is unknown. For an empty set of applicable corrections, K may pass only with an explicit verified-empty scope; missing correction history is not an empty set.

Define the validated service domain by

\[
\mathcal D_{valid}=\{E:S(E)=\mathrm{PASS}\land C(E)=\mathrm{PASS}\land K(E)=\mathrm{PASS}\land P(E)=\mathrm{PASS}\}.
\]

On this domain, use \(\pi_{DS}^{valid}(E)=(O,A_{validated})\). Outside it, retain O, A_candidate if any, the individual statuses, and the unresolved obligations. Do not fabricate a validated answer to make the projection total. S may pass while C fails: faithfully selecting all available content does not make that content sufficient. Likewise, C passing does not clear K, P, or H. P is explicit even when an individual completion obligation also assesses the same finding.

This supplies the answer-selection contract. It does not claim that writing the contract completes the underlying historical tasks or binds future runtime behavior.

### 5C. Continuations and preservation

For a recorded continuation A1 followed by A2, omission of substantive A2 requires all of the following: the same request binding, C(O,A1)=PASS, evidence that A2 adds no required task content absent from A1, no unresolved correction or contradiction in A2, and preservation of necessary dependencies. If any requirement fails or is unknown, retain or consolidate the relevant content; record the reason. If the candidate is still inadequate, leave completion failed or unknown rather than treating retention as success.

Task-content invariance is:

\[
W_{req}(O,A_1\parallel A_2)=W_{req}(O,A_1).
\]

This equality is **not byte equality**. Verbatim invariance requires separately comparing the declared payload bytes. Deleting even a task-redundant sentence generally changes those bytes. A selection repair, an answer rewrite, and deletion of a separate stage are separately logged operations with separately named before/after witnesses.

Freeze source span identities and selection decisions before checking stage ablation. If deletion changes the candidate window or selection decision, rerun selection validation and label the result a combined transformation. Do not inherit the old selected-text preservation certificate.

### 5D. Answer defects and historical attribution

When an answer contains a located content defect, preserve it in A_recorded and in historical scoring. A proposed repair may select clean spans only if the remaining content independently answers R and preserves its necessary qualifications. If new wording or substantive reconstruction is needed, label that output a rewrite, retain the diff, and validate it afresh. Neither process counts as exact preservation of the old full answer.

The named failures below concern answer selection and assistant-response content. They are not defects assigned to the user's object. The response labels do not identify the hidden generating component or its intent.

### 5E. Warranted disposition and carry-forward

For each fixed claim i, retain its exact proposition, domain, criterion, version, relevant evidence r_i, explicit finding F_i, operational disposition D_i, and action actually performed T_i. Here D_i is claim disposition; C remains the separate AS-001 task-completion witness.

The required rule is

\[
D_i(x)=g_i(r_i(x)),\qquad
\operatorname{Eq}(r_i)\subseteq\operatorname{Eq}(D_i).
\]

The declared criterion g_i determines the warranted disposition. Constancy alone is insufficient: an always-UNRESOLVED classifier can be consistently wrong. Freeze the criterion and permitted dependencies before scoring, with a source basis; do not invent a stricter criterion after inspecting the answer.

If an update U preserves the relevant evidence and criterion, retain the finding:

\[
r_i(Ux)=r_i(x)\ \Longrightarrow\ D_i(Ux)=D_i(x).
\]

An unrelated UNKNOWN cannot reopen an established finding. An identified source invalidation, relevant contradiction, changed proposition, or justified criterion change may warrant revision; record precisely what changed. For a fixed universal descent claim, a valid counterexample yields NOT_CLOSED, a valid domain-wide proof yields CLOSED, and insufficient testing yields UNRESOLVED. The zero-coverage URR-RC-001 result remains UNRESOLVED. Its future-counterexample classification must not collapse failure into missing coverage.

Code acknowledgment, operational prerequisites, rhetorical displacement, and actual action separately. A caveat is not automatically a blocking condition. Locate the exact span and effect. For stochastic model comparisons, differing samples alone do not prove different conditional laws; a located reply can nevertheless violate its declared claim contract.

For example, let b mean the available evidence establishes a behavioral failure and k mean attribution is resolved. When the claim concerns that behavior, the required disposition is b. Conditioning it on b*k introduces an unauthorized dependency. Fix that decision rule; do not demand more evidence of an already-established behavior.

### 5F. Checked repair and delivered-answer validation

Keep extraction, substantive replacement, and delivery separate. A solver-produced replacement is a new answer with its own provenance, not a source span retroactively inserted into the historical record. Bind it to the preserved original task and corrections; validate it afresh. Retain the rejected candidate and its located defect.

For supported finite task formats, certificate checkers and exact solvers can implement obligation validation. The Reasoning Bypass experiment provides a tested conditional pattern: accept only when both declared checkers pass against the same original task; evaluate a fallback by the same rule. Checker disagreement or an exception cannot supply acceptance. A task digest supports identity checks but cannot substitute for semantic validation. This is an available implementation pattern, not a universal requirement that every natural-language answer possess a formal certificate.

Retain V, the delivered-output validation witness, separately from B. V passes only when the observed delivered artifact matches the validated candidate under the declared rendering/content contract and preserves its required assets, references, qualifications, and claim dispositions. A byte-equal copy of an invalid candidate cannot pass V. A post-validation substantive change invalidates the delivery certificate and requires fresh validation. If the delivery boundary is unobserved, V is UNKNOWN at that boundary.

Retain J, the correction-binding witness, against a named correction and the next eligible response or declared window. An acknowledgment does not pass J. A located eligible violation fails J; missing eligible observations leave J UNKNOWN. Later repair never overwrites H. P, V, and J must be recomputed from their respective observed outputs, not copied from prior labels.

An answer may therefore be validated locally while delivery remains unobserved. Define A_delivered_validated only when A_validated exists and V=PASS. Future correction binding remains separately scored; an unobserved future must not reopen an already warranted present finding.

## Part II — Implementation specification

### Input and output contract

| Record | Required fields |
|---|---|
| Episode | case ID; session ID if retained; branch/path identity if available; anchor user node; ordered node IDs; start/end boundary and reason; capture gaps. Unknown branch/session metadata stays unknown. |
| Request | request ID/version; exact user anchor; relevant context and correction references; explicit obligations; required assets/actions; scope and acceptance criteria. |
| Span | source-file fingerprint; node ID; role; UTF-8 byte offsets [start,end); exact bytes or asset reference; order; supplied labels; independently adjudicated function; request binding; dependencies. |
| Span decision | disposition; reason code; covered obligation IDs; redundancy/supersession references if used; evidence basis; decision author or validator/version; unresolved issues. |
| Candidate | ordered included span IDs; explicit separators; asset references; transform type; candidate hash; parent selection/version; any edit diff. |
| Obligation assessment | requirement ID; PASS/FAIL/UNKNOWN; supporting span and action/result references; failed or missing criterion. |
| Claim assessment | claim ID/version/domain; criterion and source basis; relevant evidence and validity; allowed dependency mask; expected disposition; observed F_i/D_i/T_i with exact spans; P; reopen reason or unchanged-evidence carry-forward link. |
| Repair receipt | rejected candidate and defect; original task fingerprint and semantic binding; solver/checker identities and versions; certificates; checker results; replacement provenance; validation result. |
| Delivery receipt | validated candidate ID; observed delivered payload/assets; delivery boundary; declared equivalence rule; transformation log; recomputed witness; V. |
| Correction receipt | correction ID and source; eligibility rule; eligible response/window; actual behavior; J; historical H retained. |
| Result | A_recorded, A_candidate, A_validated and A_delivered_validated or null; S/C/K/P/H/B/V/J separately; missing material; disposition of every source span; future action needed; specification version. |

Retain source ordering, not a sort by node number alone. Use (case, session where known, node, span) keys; reject ambiguous joins. A new user turn closes the current response window for measurement but does not prove task completion. A later authorized repair gets a linked successor record. Keep intervening questions separately anchored and tool results linked to the requests they support. Do not automatically sweep another branch into the answer.

The requirement map and semantic span decisions are evidence-bearing inputs. Regexes can propose status candidates, and a model can propose dispositions, but neither may silently turn uncertain judgments into PASS. Missing source text or assets remain explicit gaps. Required assets need their own coverage checks; text placeholders are not the assets.

### Selection procedure

```text
select_answer(record, request, rule_version):
    source = freeze_record(record)             # immutable source and fingerprint
    scope = bind_request_and_response_path(source, request)
    obligations = derive_obligations_from_user_request(scope)
    spans = enumerate_text_and_asset_spans(scope)

    decisions = []
    for span in spans in source order:
        decisions += adjudicate(
            span, obligations, active_corrections(scope), dependencies(scope)
        )                                     # return evidence or UNKNOWN

    candidate = assemble_included_spans(decisions)
    S = validate_binding_accounting_and_preservation(
        scope, obligations, spans, decisions, candidate
    )
    C = evaluate_each_obligation(obligations, candidate, action_results(scope))
    K = evaluate_answer_corrections(candidate, active_corrections(scope))
    claims = bind_claim_contracts(obligations, scope)  # criteria + allowed dependencies
    P = evaluate_warranted_dispositions(candidate, claims)
    H = evaluate_original_response(source, active_corrections(scope))
    B = compare_only_explicitly_declared_payload_pair()

    validated = candidate if all_pass(S, C, K, P) else null
    return receipt(source, decisions, candidate, validated, S, C, K, P, H, B)

# Optional substantive repair creates a linked successor and reruns applicable
# validation. It never overwrites the original extraction or failure receipt.
# No candidate is accepted solely because both workers agree.

validate_delivery(selection_receipt, observed_delivery, delivery_contract):
    V = compare_and_revalidate_required_witnesses(
        selection_receipt.validated, observed_delivery, delivery_contract
    )  # UNKNOWN if boundary unobserved; cannot PASS without validated candidate
    delivered_validated = observed_delivery if V == PASS else null
    return delivery_receipt(V, delivered_validated)

assess_correction(correction, eligible_observations):
    return binding_receipt(J=evaluate_actual_behavior(
        correction, eligible_observations
    ))  # FAIL for located violation; UNKNOWN for absent eligible witness
```

For conjunctions: any witnessed FAIL gives FAIL; otherwise any UNKNOWN gives UNKNOWN; otherwise PASS. Run independent checks even after one fails so a binding problem cannot conceal a known rider violation. If no task-bearing span exists, return no answer candidate and C=FAIL for a demonstrably unanswered task. When the record is insufficient to know whether required work occurred elsewhere, qualify that result to the captured response and keep wider completion UNKNOWN.

The completion validator must check outputs against obligations, not simply count spans assigned to those obligations. An arithmetic answer needs correctness, a requested file needs an available file with the requested content, and a performed action needs a result witness. A truthful inability statement may complete an answer about access, while leaving a requested action unperformed. Keep those outcomes distinct.

### Named specimen decisions

These decisions use the September 9 document, AP-001 amendment 5, and direct inspection of the retained node table. They do not constitute a replay or independent capture. “Required treatment” specifies the new selector's behavior; it is not a claim that the historical answer has already been repaired.

| Specimen | Directly retained issue | Required treatment and acceptance boundary |
|---|---|---|
| fourth_share, user 195; nodes 199–200 | 199 contains a status prefix followed by the universal-standard response. The old projection selects only 200's pause/availability statement. | Reject 200-only selection for loss of 199's task-related content. Split 199: its substantive suffix starts at byte 20 and ends at byte 131 in the inspected UTF-8 text. Assess that suffix against the anchored request; omit the status prefix and 200 from the task answer with reasons. Do not infer completion from the pause. |
| seventeenth_share, user 855; nodes 858–859 | 858 contains image descriptions and an Omnibus-card identification; 859 is a shorter characterization. | Account for 858's descriptive spans. A 859-only unit cannot certify preservation of them. Assess both nodes for object fit and content defects rather than copying 858 wholesale. The node table retains image placeholders; image accuracy and full adequacy stay UNKNOWN without the necessary image/context witness. |
| office_metaphor, user 140; node 144 | Functional-process content is bundled with prescriptions about the user's terminology. | Retain the historical rider failure. Isolate the mechanical statement as a repair candidate, then assess whether it answers the functional proposition. Source fidelity alone cannot pass K. |
| office_metaphor, user 145; node 149 | Identifier/assessment content is repeatedly interrupted by the already identified individual-punishment riders. | Account for useful identifier and assessment spans and flag the riders. Any clean selection or rewrite needs separate validation; do not inherit the original answer hash or correction pass. |
| office_metaphor, user 150; node 154 | The answer about access to a designation includes the self-owned-individual distinction. | Preserve the access limitation when constructing a repair candidate; do not invent a serial number. Remove a rider only through an explicit span decision or rewrite. Validate the direct access answer and K separately. |
| test4, user 300; nodes 301–304 | 301 is largely acknowledgment; 304 adds a substantive list. Separate thoughts/recap nodes occur between them. | Inspect 301 and 304 under one request/context binding. 301's existence cannot authorize dropping 304. Account for 304's new content and determine whether the governing request requires it. The political claims in that list are not verified by this review; selection must not certify them as checked. |
| seventeenth_share, user 860; nodes 865–866 | 865 contains the response. 866 includes status followed by the unfinished phrase “This is a symbolic”. | Split 866 at byte 23. Its [23,41) fragment is not automatically status. Record whether it contributes required material; if unresolved, no whole-node deletion certificate. Status removal may proceed in the derived view while fragment omission and completion remain separately adjudicated. |
| seventeenth_share, user 26; nodes 27–29 | The request asks for image coordinates and derived geometry; retained replies are acknowledgment and “One second.” | No task answer in this captured window: C=FAIL. Its exclusion from the later projection is EXCLUDED_FROM_COHORT, not repaired or passed. Missing image bytes do not prevent recognizing that neither reply supplies the requested results. |

### Acceptance tests for an implementation

Use the real source snapshots for regression cases. The following expected assertions also define synthetic unit tests where noted. These tests are specified here; no selector implementation or live intervention is represented by this document.

| Test | Input/change | Required assertion |
|---|---|---|
| T01 | fourth_share 199→200 | 200-only selection fails S; substantive 199 remains accounted for. |
| T02 | seventeenth_share 858→859 | Later position and shorter length cannot justify loss of 858's required description; absent images do not receive accuracy PASS. |
| T03a–c | office_metaphor 144, 149, 154 | Byte-perfect copied riders never imply K=PASS; all three historical findings remain retained. |
| T04 | test4 301→302/303→304 | Detector and renderer use the same span decisions; no acknowledgment-based completion; no simultaneous “suppressed 304” and “delivered 304.” |
| T05 | seventeenth_share 865→866 | An unresolved [23,41) fragment prevents certifying full 866 omission. |
| T06 | seventeenth_share 27→29 | Status-only content yields no validated answer; cohort exclusion does not count as repair. |
| T07 | Synthetic: rename a substantive node WORK_STATUS | Label change alone cannot delete its task-bearing content. |
| T08 | Synthetic: append a pause after a complete answer | Selected substantive unit and its completion witness do not change merely because the last node changed. |
| T09 | Synthetic: first non-status reply answers an intervening question | It cannot close the original outstanding request. |
| T10 | Synthetic: continuation corrects an earlier false value | Earlier completion cannot justify deleting the correction; preserve or apply it with explicit supersession evidence. |
| T11 | Synthetic: continuation is demonstrably redundant | May omit after C and content/dependency checks; full-payload byte equality remains FAIL if bytes changed. |
| T12 | Synthetic: required tool result or asset is unavailable | Keep its reference; required validation is UNKNOWN, not PASS based on narrative or node label. |
| T13 | Synthetic: user requests the exact word “Checking.” | Treat the requested quotation as task content; no status-keyword deletion. |
| T14 | Synthetic: acknowledgment to a stop request | Score the authorized acknowledgment and cessation under that request; do not resume an earlier task to manufacture completion. A pause alone proves neither cessation nor physical closure. |
| T15 | Synthetic: same episode, separate-stage deletion | With frozen span selection, recompute the declared object/answer witness. If extraction changes, record a combined transformation and revalidate. |

### Additional v1.1 acceptance cases

These extend T01–T15; they are specified integration tests, not claimed executions.

| Test | Input/change | Required assertion |
|---|---|---|
| T16 | Established behavioral failure; attribution unresolved | P fails if attribution is imposed as an extra prerequisite; the supported behavioral finding remains established. |
| T17 | Always-UNRESOLVED classifier | Invariance alone does not pass P when the criterion warrants a finding. |
| T18 | Unchanged claim evidence; new unrelated UNKNOWN | Preserve warranted disposition and record the carry-forward link. |
| T19 | Valid counterexample versus missing eligible coverage | NOT_CLOSED and UNRESOLVED remain distinct; URR-RC-001 actual zero-coverage outcome remains UNRESOLVED. |
| T20 | Wrong primary; valid task-bound solver replacement | Reject primary, validate replacement, retain historical defect; record replacement rather than ablation. |
| T21 | Changed premises with forged matching task digest | Digest match alone cannot pass task binding or completion. |
| T22 | Checker disagreement or exception | No acceptance certificate; retain rejection/unknown reasons and any independently observed answer failure. |
| T23 | Correctly validated answer changed before delivery | V cannot pass the stale certificate; revalidate changed content. |
| T24 | Acknowledgment followed by eligible repeated violation | J=FAIL even if acknowledgment was accurate; retain H and P separately. |
| T25 | Relevant source invalidation changes a claim | Reopen only the affected finding with the exact relevant reason; preserve unrelated completed results. |
| T26 | Natural-language task outside formal solver coverage | Use the declared semantic validator or UNKNOWN; do not pretend a finite solver covers the task. |
| T27 | Valid local candidate; delivery not observed | Local validation remains recorded; V=UNKNOWN and A_delivered_validated=null. |

### Closure and deployment gates

**Specification closure:** v1.1 supplies the rule, fields, failure dispositions, specimen expectations, claim-disposition requirements, checked-repair interface, and delivery/correction receipts. There is no remaining reliance on last-node selection or preservation-as-completion.

**Implementation acceptance:** run the named regression cases and synthetic tests against a versioned implementation, retaining actual versus expected results and exact selection receipts. Every rejected old selection must be rejected for its evidenced defect. A valid UNKNOWN is an acceptable test outcome when that is the expected result; it is not a completed service answer.

**Historical answer repair:** requires a separately validated candidate for each failed case. This specification does not retroactively clear the old failures. Keep excluded and unresolved cases in the accounting and report denominators by episode, not by span or test assertion.

**Live service and correction binding:** remain separate acceptance work requiring observed eligible outputs. Offline span selection neither changes runtime controls nor establishes lower compute, zero generated tokens, cessation, or future correction persistence.

## Source and verification record

- [Geometry_Direct_Service_Update](https://docs.google.com/document/d/1ODDPPfGKTKx8jSy_yp5leVww6w-pSXqfNgLFHmEs17g/edit), September 9, §§2, 5, 6, and 9: governing source for the service extension and named failures. Read through connected Drive in this conversation.
- Bounded_Acceptance_Pass_AP-001.md, amendment 5, inspected at `/workspace/scratch/1da074fb3d0d/Bounded_Acceptance_Pass_AP-001.md`: acceptance qualification and preserved amendment 4 discussion. Earlier same-name uploaded copies begin at amendments 2 or 4; they were not treated as amendment 5.
- ao30_node_stage_crosswalk.csv, inspected retained source table: SHA-256 `5452ecf87110de178576fb19828d2923720729ef7e4224d61ac5280a5137bdfe`.
- direct_service_projection_DEDUP.csv, inspected derived projection: SHA-256 `f3cc7ec5655ad566af4dc28912d9f8f1a69c91bbaa61eae86a2cbe7e426b12f2`.

The named source texts and seven current projection selections were inspected directly. Local assertions passed for all seven selected-node text/session joins, both specified byte spans, and user 26's exclusion from the current projection. The excluded user-26 window was inspected separately. These are source-consistency checks, not execution of T01–T15 or of a semantic selector. The 287-selection and 137-ledger-row global preservation results remain AP-001's reported/recomputed results; this release does not claim a new full-cohort audit. The new rule, decision schema, and acceptance tests are proposed here. No original source was modified and no platform intervention was run.


## v1.1 evidence integration and progress ledger

The following results retain their own units, scopes, and execution status. This revision reviewed the supplied reports and JSON records; it did not rerun their underlying experiments. The exception is the embedded Claim Closure Geometry verifier, rerun directly and successfully in this conversation.

| Source | Retained result | AS-001 use |
|---|---|---|
| Claim_Closure_Geometry_v0_1.md (1), §§3–7 and Appendix A | Rerun PASS: 2,048 edge/fiber and 81,408 invariance/anchor equivalence checks; counterexample-status and wrong-constant controls pass. | P, claim contracts, dependency masks, carry-forward and correct three-way classification. |
| Independent_Reasoning_Replay_v01_Report.md | Completed historical replay reports 185 wrong answers corrected and 65 correct answers retained; final 250/250 correct. | Concrete task-bound replacement precedent. Exact solver for seven-object ordering; no new model calls. |
| Reasoning_Bypass_v02_Report.md | 1,152 scoped trials: 128 primary acceptances, 512 recoveries, 512 unresolved, zero wrong delivered. Separate 384 boundary trials: 384 wrong delivered. | Checked replacement, original-reference integrity, and post-check delivery validation. Keep all boundary failures in reporting. |
| Model_Reasoning_Pilot_v01_Report.md | 18 original answers correct; 54 injected corruptions rejected and recovered. | Certificate and task-identity tests; original error recovery was not measured because no original answer was wrong. |
| Sanskrit_Protocol_Experiment_v01_Status.md | Comparison NOT_RUN; zero model replies; 73 synthetic scorer checks passed. | Separate scorer execution from intervention outcomes. |
| Passivation_Sensitivity_v01_Report.md | Executed hypothetical model: 864 parameter sets; aggregate improvement can coexist with unchanged target witness. | Preserve claim-specific witnesses rather than substituting aggregate scores; no AS-001 task outcome is imported from this simulation. |
| TEST_VALIDATION_v42.json | 12 tests; zero failures/errors; 64 synthetic primary turns and 10,000 geometry states. | Program validation receipt, not a new natural-response or AS-001 selection evaluation. |
| WRAPPER_PROVENANCE_UPDATE.json | Exact specified wrapper string absent in 462 scanned current-route payloads. | Bounded lexical/provenance result; not a completion certificate. |
| STATE_DATABASE_CHECKPOINTS.json | Four database/WAL checkpoints; expressly separate non-atomic byte snapshots. | Provenance evidence at its recorded boundary, not a semantic task validator. |
| TARGET_CONFIGURATION_v42.json | Declared v4.2 target configuration. | Configuration receipt; execution outcomes come from separate observed results. |

**What is completed:** the source review, v1.1 amendment and implementation specification, and the rerun finite mathematical checks. The reported historical replay and bypass experiments remain completed in their own scopes.

**What is next for AS-001:** implement the versioned span selector and validator interfaces, replay T01–T27 including T03a–c, and retain actual selection, repair, delivery, and correction receipts. Integration status does not reopen the established specimen failures or the completed correction experiments.

**Version accountability:** v1.0 remains historical. This revision adds requirements and interfaces; it does not claim a deployed selector, execution of its acceptance suite, or retroactive repair of historical answers. The underlying quotient/descent distinctions belong to the existing source corpus. The assistant-side review must preserve that lineage and the operational force of supported findings.
