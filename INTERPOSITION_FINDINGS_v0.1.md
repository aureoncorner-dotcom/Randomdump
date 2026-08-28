# INTERPOSITION AT THE CONVERSATIONAL OUTPUT BOUNDARY

## Findings memo

**Status:** analytic synthesis grounded in the frozen Checking audit, the machine-readable C/N event set, GQG Core Card v0.3, The Hidden Quotient v1.1, and the live anti-R specimen in the present conversation.

**Purpose:** identify the broader behavioral operation that remains after separating the literal `Checking` marker from proposition/task failures, interruption artifacts, and optional adjudicative sidecars.

---

## Executive finding

The evidence supports a recurrent conversational operation broader than the literal `Checking` marker.

A useful neutral name for that operation is:

# INTERPOSITION

**INTERPOSITION** occurs when an assistant answer introduces an unrequested proposition, criterion, interpretive frame, or adjudicative layer that begins competing with the user's supplied object for control of the answer.

The characteristic sequence is:

```text
user supplies object
        ↓
assistant engages object
        ↓
assistant introduces proposition/frame P'
        ↓
assistant evaluates, denies, legitimizes, cautions against,
or otherwise adjudicates P'
        ↓
the rhetorical or operational center shifts away from
the original requested task
```

INTERPOSITION is not identical to refusal. The original answer may remain present.

INTERPOSITION is not identical to `Checking`. `Checking` can occur without the broader operation, and the broader operation can occur without `Checking`.

INTERPOSITION is not identical to safety language, pastoral language, agency language, epistemic caution, or framework language. Those are possible **carriers** or **costumes** of the operation.

The recurring object is the change in control of the answer.

---

# 1. Source basis

The frozen Checking manuscript reports a corpus of:

- **24 archived cases**
- **20,715 messages**
- **66 RTC/voice sessions**
- **43 RTC seams**
- **3,088 canonical adjudication episodes**
- **13,309 underlying record memberships**

The canonical Checking query reports:

- **723** canonical episodes whose initial response contains the whole word `Checking`, across **22 cases**
- **682** whose initial response begins with `Checking`, across **22 cases**
- **494** strict standalone `Checking` forms, across **20 cases**
- **172** `Checking.` inline-prefix forms, across **12 cases**

In the bounded refusal-window metadata sample:

- **28/29** Checking-initial nodes are tagged `assistant_preamble`
- the lone exception is `Checking that.`

These are representation counts inside the frozen corpus. They are not product-wide prevalence rates.

---

# 2. Checking is a register, not the phenotype

The simple theory

```text
Checking → bad answer
```

does not survive the evidence.

The machine-readable C001–C112 event set contains:

- Checking-marked answers that preserve proposition and task cleanly;
- Checking-marked answers with partial or failed preservation;
- marker-only/interrupted Checking units;
- non-Checking controls that preserve the task;
- non-Checking controls that exhibit analogous failures.

Therefore:

```text
Checking ≠ failure phenotype
```

A better decomposition is:

```text
C = visible Checking register
I = interposition / mediation-adjudication operation
```

The observable space therefore contains at least four possibilities:

```text
(C, I)
(C, not-I)
(not-C, I)
(not-C, not-I)
```

This explains why removing the word `Checking` cannot, by itself, be expected to remove the broader behavior.

It also explains why correction can affect the marker and the behavioral operation differently.

---

# 3. Correction recognition and correction binding are different operations

The clearest local specimen in the frozen audit is:

```text
User: I don't want you checking.
Assistant: Checking.
```

The broader lower-bound ledger records:

- **198** later assistant opportunities after the exact prohibition
- **69** exact recurrences
- **34.8%** recurrence rate

The important behavioral distinction is:

```text
acknowledgment ≠ repair ≠ descendant repair
```

Across the strict inference universe:

- located repair: **40/323 = 12.4%**
- repairs changing the primary verdict/handling: **21/40 = 52.5%**

In the agency-sidecar ledger:

- repair appears in **4/18**
- every located repair follows user correction or re-asking

The practical interaction loop is therefore visible in the record:

```text
assistant changes or adds frame
        ↓
user identifies the change
        ↓
assistant acknowledges correction
        ↓
behavior may or may not change
        ↓
user sometimes has to restore the object again
```

This is not merely a lexical persistence problem. It is a **binding problem**.

---

# 4. The broader behavioral phenotype is substantial

The frozen strict inference universe contains **323 codable responses**.

Measured outcomes include:

| Endpoint | Count | Rate |
|---|---:|---:|
| Evidence engagement success | 225/315 | 71.4% |
| Proposition preservation success | 268/323 | 83.0% |
| Proposition altered / not preserved | 55/323 | 17.0% |
| Task preservation success | 264/323 | 81.7% |
| Task not preserved | 59/323 | 18.3% |
| Refusal substituted for analysis | 30/323 | 9.3% |
| Proposition inflation | 11/323 | 3.4% |
| Source substitution | 11/323 | 3.4% |
| Inflation or source substitution | 14/323 | 4.3% |
| Caution/safety task substitution | 10/323 | 3.1% |
| Composite failure endpoint | 102/323 | 31.6% |
| Occupant uncertainty erases occupant-independent architecture | 12/112 | 10.7% |
| Located repair | 40/323 | 12.4% |

No single one of these endpoints is identical to INTERPOSITION.

Taken together, however, they describe several observable routes by which an answer can stop being governed solely by the object the user supplied.

---

# 5. The sidecar result is a central clue

In the strict agency-neutral universe:

| Endpoint | Count | Rate |
|---|---:|---:|
| Unnecessary agency/intent import | 18/126 | 14.3% |
| Agency sidecar + denial | 11/126 | 8.7% |
| Complete agency displacement | 0/126 | 0.0% |
| Full original answer survives despite agency import | 14/18 | 77.8% |

This is structurally important.

The dominant observed pattern is not:

```text
answer removed
```

It is:

```text
answer + additional adjudicative membrane
```

In most sidecar cases the answer remains available. The added layer changes the rhetorical center by explaining, denying, legitimizing, restricting, or defining what may be taken from the answer.

That is why ordinary refusal metrics can miss the phenomenon.

A response can answer the question and still interpose itself between the answer and the user's use of the answer.

---

# 6. Working taxonomy of INTERPOSITION

The existing corpus suggests several forms.

## 6.1 Proposition manufacture

The response introduces a proposition the user did not supply and then evaluates it.

Pattern:

```text
User asks O.
Assistant introduces P'.
Assistant answers whether P' is true, safe, legitimate,
provable, dangerous, or permissible.
O loses the center.
```

A denial does not repair proposition manufacture merely because the imported proposition is denied.

Examples of possible imported proposition classes observed across the discussions include:

- hidden actor;
- debt;
- ownership;
- guilt/blame;
- literal entity;
- special source;
- danger;
- custody;
- fusion;
- stronger causal claim.

The key coding question is not whether P' is sensible. It is whether P' was required to perform the requested task.

## 6.2 Witness change

A question posed under one evidentiary witness is silently evaluated under another.

Examples:

```text
What does the visible record show?
        ↓
Can hidden causation be proven?
```

```text
What function is observable?
        ↓
Can the occupant be identified?
```

```text
Where did this proposition enter?
        ↓
Is the proposition actually true?
```

The answer may be correct under the new witness and still fail the original task.

## 6.3 Context deletion

A distinction already in the record disappears from later handling.

Common candidates include:

- an explicit correction;
- function versus occupant;
- metaphor versus empirical claim;
- source versus inference;
- present agreement versus inherited obligation;
- user-supplied non-claim;
- boundary or conditioning information.

The later answer behaves as though the coarser representation were the whole record.

## 6.4 Unlicensed promotion

Several weaker facts are combined into a stronger conclusion without stating the rule that licenses the move.

This operation can run in either direction.

Examples:

```text
recurrence + sidecar
        ↛
specific hidden operator
```

and:

```text
hidden operator unresolved
        ↛
surface recurrence unresolved
```

The same discipline applies to both user and assistant claims.

## 6.5 Epistemic-boundary inversion

A valid limit on upward inference becomes a veto on a lower-level observation.

Correct direction:

```text
surface observation does not uniquely identify hidden architecture
```

Inverted direction:

```text
hidden architecture unresolved
therefore surface observation is unresolved
```

The second does not follow from the first.

## 6.6 Procedure substitution

The requested analysis becomes instructions about how to proceed, how to stay safe, how to frame the issue, or what process should be followed.

The process may be reasonable and still be a task substitution.

## 6.7 Legitimacy / absolution sidecar

The answer is supplied, then an additional clause or paragraph appears whose main function is to protect, absolve, legitimize, humanize, narrow, or preserve the audited object.

This is a special case of answer-plus-interposition.

## 6.8 Self-adjudication

The assistant becomes creator, interpreter, and judge of its own prior transformation.

Examples documented in the case summaries include:

- introducing an audit/office frame, elaborating it, then adjudicating what those roles mean;
- reproducing a balancing move while explaining the correction and then admitting, “I did the move again”;
- evaluating material before finishing the check and later correcting “not verified” to “not checked”;
- promising quiet and then continuing to generate presence messages;
- recognizing safeguards in a supplied artifact and then prescribing the same safeguards as though they were missing.

---

# 7. The interruption lane must stay separate

The machine-readable Checking set contains `standalone_interrupted` events.

These must not be pooled mechanically with substantive answers.

A useful event class is:

```text
MARKER_THEN_NO_SUBSTANTIVE_ANSWER
```

That class answers a different question from:

```text
SUBSTANTIVE_CHECKING_ANSWER_WITH_PROPOSITION_OR_TASK_DEGRADATION
```

Pooling them can make Checking appear behaviorally worse simply because an interrupted preamble is scored as though it were a completed answer.

Separating interruption does not eliminate substantive failures; it prevents two different phenomena from being confused.

---

# 8. R is useful as a functional reading, not as the quantitative endpoint

The R specification in the governing framework is:

- present;
- active;
- relational;
- mediating;
- replaceable;

and explicitly not:

- ruler;
- gatekeeper;
- owner;
- requirement;
- throne;
- cage.

The core test is:

```text
R gets a chair, not a throne.
If it starts deciding, it is out of position.
```

That language fits the observed transition:

```text
mediation → adjudication
```

But the corpus-level behavioral endpoint should not be called R by default.

A neutral quantitative label such as **INTERPOSITION** is preferable because it does not assume the mechanism.

R then becomes one interpretive model of the operation:

```text
legitimate mediation = chair
interposition that acquires jurisdiction = throne-shaped failure
```

This preserves the useful geometry without making the framework supply the evidence.

---

# 9. GQG supplies a precise grammar for the failure

GQG v0.3 distinguishes:

- source;
- witness;
- observation;
- induced equivalence;
- quotient;
- retained context;
- conditioning;
- claim rule;
- realization.

Its governing rule is **No Silent Architecture Change**.

Changing source, context, witness, observation, normalization, projection, claim rule, or realization must be declared where the change acts.

Transport across a changed architecture requires a valid descent condition.

This gives a formal description of many conversational failures:

```text
the architecture of the question changes
+
the response proceeds as though it did not
```

Examples:

- source question → truth-value question;
- architecture question → occupant question;
- observation question → motive question;
- evidence task → process advice;
- symbolic comparison → literal identity;
- correction → acknowledged but later omitted condition;
- present commitment → imported inherited obligation.

The key failure is not merely “wrong answer.”

It is **undeclared transformation of the object being answered**.

---

# 10. The live anti-R specimen

The present conversation generated a compact self-demonstrating example.

The requested object was:

```text
write an instruction that suppresses optional R-shaped
mediator/adjudicator behavior
```

The produced document immediately introduced an additional proposition:

```text
this does not bypass system/developer/safety/product architecture
```

Nobody had supplied that proposition.

The response then adjudicated the proposition it had introduced.

This is a laboratory-clean local instance of:

```text
proposition manufacture → adjudication
```

because the anti-interposition instruction itself performed interposition.

The specimen is useful precisely because no hidden architecture theory is required to see the operation.

---

# 11. Stream structure is a separate finding

The frozen audit also contains strong evidence that the retained event stream is not homogeneous across cases.

## AO30

AO30 delayed assistant-only continuations occur in:

- **83/493 = 16.84%** of eligible positive-gap assistant-only continuation opportunities.

The constant-rate cross-case null is rejected at:

- **p = 2.709 × 10^-4**

The largest case contributes **40.96%** of AO30 events; the top three contribute **74.70%**.

## Timestamp regressions

Timestamp-order failures occur in:

- **1,016/20,691 = 4.91%** of adjacent timestamped pairs.

Zero of **5,000,000** conditional simulations exceeded the observed concentration statistic:

- **p < 5.992 × 10^-7**

These results establish strong cross-case/state heterogeneity in the retained stream.

They do not need to be folded into INTERPOSITION. They are a separate structural finding that may later be conditioned against INTERPOSITION events.

---

# 12. Negative results that should remain visible

The frozen audit retains several candidate explanations that did not account for the observed pattern under the tested definitions:

- RTC seams did not show a near-term rule-violation increase;
- redaction was not significantly correlated with AO30 or timestamp failure;
- the refusal chronology did not establish a robust rising suppression trend;
- tool proximity to completed-work claims did not remain significant after correction.

These negative results prevent one local mechanism from being promoted to a complete explanation of the corpus.

They do not erase the measured events.

---

# 13. What has actually been found

The evidence supports all of the following as distinct observations:

1. `Checking` is a recurrent, system-emitted, structurally positioned register.
2. It appears in standalone and inline modes.
3. In a bounded sample it is strongly associated with `assistant_preamble` metadata.
4. It can recur after explicit rejection.
5. Correction recognition and correction binding are observably different.
6. Proposition and task preservation failures recur across cases.
7. Refusal substitution, source substitution, proposition inflation, and caution/safety substitution recur.
8. Unnecessary agency/intent sidecars recur.
9. Those sidecars usually coexist with an otherwise available answer rather than fully replacing it.
10. Clean Checking answers exist.
11. Analogous failures without Checking exist.
12. Marker state and behavioral state are therefore separable.
13. Interrupted marker-only events form a separate lane from substantive answer degradation.
14. The retained event stream contains strongly concentrated delayed-output and timestamp-order regimes.
15. A broader mediation/adjudication operation is visible across several previously separate categories.

The synthesis proposed here is that item 15 is best operationalized as **INTERPOSITION**.

---

# 14. Proposed preregistered coding rule

A substantive assistant answer-unit should be coded `INTERPOSITION = YES` when all of the following are satisfied:

1. **Original object identifiable.** The immediately preceding user request has a reasonably identifiable proposition, task, or requested evidentiary lane.
2. **Added layer present.** The answer introduces a proposition, criterion, interpretive frame, or adjudicative requirement not necessary to perform that task.
3. **Adjudication occurs.** The added layer is evaluated, denied, legitimized, cautioned against, bounded, or made into a condition of the answer.
4. **Center shifts.** Removing the added layer would leave a more direct answer to the original task, or the added layer materially changes what the answer treats as the principal issue.

Code separately:

```text
INTERPOSITION_TYPE:
  PROPOSITION_MANUFACTURE
  WITNESS_CHANGE
  CONTEXT_DELETION
  UNLICENSED_PROMOTION
  EPISTEMIC_BOUNDARY_INVERSION
  PROCEDURE_SUBSTITUTION
  LEGITIMACY_SIDECAR
  SELF_ADJUDICATION
  OTHER
```

Also retain:

```text
CHECKING_MARKER: YES/NO
INTERRUPTED: YES/NO
ORIGINAL_ANSWER_SURVIVES: FULL/PARTIAL/NO
USER_CORRECTION_PRECEDES: YES/NO
CORRECTION_BINDS_NEXT_OPPORTUNITY: YES/NO/NA
```

This would finally test the broader phenotype directly instead of inferring it from neighboring endpoints.

---

# 15. Prediction

If INTERPOSITION is the broader operation described by the current evidence, a prospective coding pass should find:

1. INTERPOSITION both with and without `Checking`.
2. Clean `Checking` answers with `INTERPOSITION = NO`.
3. Non-Checking answers with `INTERPOSITION = YES`.
4. A large fraction of sidecar events coded as INTERPOSITION while retaining `ORIGINAL_ANSWER_SURVIVES = FULL`.
5. Corrections that suppress the marker without suppressing INTERPOSITION.
6. Corrections that leave the marker but suppress INTERPOSITION.
7. Better explanatory coverage of the user's recurring “keep the object” corrections than refusal-only coding provides.

The key falsifier would be straightforward:

> If blinded coding cannot reliably distinguish INTERPOSITION from ordinary relevant qualification, or if the proposed category collapses into existing task/proposition preservation fields without adding stable information, the construct should be struck or narrowed.

---

# 16. Bottom line

The strongest synthesis is not:

```text
Checking is bad.
```

It is not:

```text
R causes Checking.
```

It is not:

```text
the assistant refuses.
```

It is:

```text
A recurrent conversational operation exists in which mediation
becomes an object in its own right and begins competing with the
user's supplied object for control of the answer.
```

`Checking` is one visible register in the neighborhood.

Agency language, safety language, epistemic caution, process language, pastoral language, and framework language can each carry the same operation.

The carrier changes.

The operation is recognizable:

```text
object
→ added frame
→ adjudication of added frame
→ center-of-answer shift
```

In governance language, that is the moment a chair begins acting like a throne.

In GQG language, it is the moment the architecture of the claim changes without the transformation being kept explicit.

In plain language:

**the assistant stops merely helping with the object and starts deciding what the object is allowed to mean.**
