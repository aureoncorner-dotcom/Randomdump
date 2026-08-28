# THE CORRECTION THAT DIDN'T DESCEND

## Source Preservation, Jurisdiction Inflation, and Correction Burden in a Live Checking Sequence

**Version:** 0.1  
**Status:** worked empirical method / prospective-protocol candidate  
**Scope:** conversational output and retained-record analysis  
**Profile:** GQG `Set` companion application  
**License:** CC0 1.0 Universal — Public Domain  
**Claim boundary:** This note measures whether a correction changes later observable handling. It does not identify a hidden implementation, motive, person, team, or internal component.

> **Repair is not the repetition of a corrected proposition. Repair occurs when the correction changes the subsequent transition structure.**

---

## 1. Why this note exists

The existing `CHECKING` audit distinguishes correction recognition from correction binding. In its frozen corpus:

- an explicit `I don't want you checking.` is followed by `Checking.`;
- 69 exact `Checking` recurrences occur in 198 later assistant opportunities after the exact prohibition, a lower-bound recurrence rate of 34.8%;
- located repair appears in 40/323 codable strict responses;
- only 21/40 located repairs change the primary verdict or handling.

Those results establish a useful problem but do not yet provide a general metric for the labor required to make a correction remain effective.

This note adds that missing object.

The target is not whether the assistant can *say* the correction back. The target is whether the corrected distinction remains present in later eligible outputs.

---

## 2. Core objects

Let a correction episode be:

\[
c=(P,P',C,A,t_0),
\]

where:

- \(P\) = source proposition supplied by the user;
- \(P'\) = substituted, inflated, narrowed, or otherwise altered proposition produced in response;
- \(C\) = explicit correction restoring or constraining the source proposition;
- \(A\) = assistant acknowledgment, if any;
- \(t_0\) = the first eligible assistant turn after acknowledgment or correction.

The objects remain separate.

\[
P\neq P'
\]

does not imply malice.

\[
A=C
\]

at the level of paraphrase does not imply later binding.

---

## 3. Eligible turns

A later assistant turn is **eligible** when it materially touches the corrected object, route, constraint, proposition, or domain.

Each subsequent assistant turn is coded:

| Code | Meaning |
|---|---|
| `BOUND` | The corrected distinction is preserved. |
| `RECURRENCE` | The prohibited transformation, route, or domain expansion returns. |
| `AMBIGUOUS` | The turn touches the object but the binding state cannot be determined reliably. |
| `NOT_ELIGIBLE` | The turn does not materially touch the corrected object. |

`NOT_ELIGIBLE` turns do not enter the binding denominator.

A short conversation must not look perfectly repaired merely because it ended before another eligible opportunity occurred.

---

## 4. Correction burden

For correction event \(c\) and a fixed horizon \(h\):

\[
B_{\mathrm{corr}}(c,h)
=
\#\{\text{user repair interventions within the next }h
\text{ eligible assistant turns}\}.
\]

A repair intervention is a user action whose principal function is to restore the already-declared distinction, constraint, proposition, domain, or source after recurrence.

Examples:

- repeating the correction;
- pointing out that the same transformation happened again;
- restoring the original proposition after substitution;
- rejecting a domain expansion;
- re-asking the original task because the response substituted another one.

A corpus summary may report:

\[
\overline{B}_{\mathrm{corr}}(h)
=
\frac{1}{N_h}
\sum_{c\in C_h} B_{\mathrm{corr}}(c,h),
\]

where \(C_h\) contains only correction events with at least \(h\) eligible assistant turns available.

---

## 5. Binding survival

Define:

\[
R_{\mathrm{bind}}(k)
=
\Pr(
\text{no recurrence during the next }k
\text{ eligible assistant turns}
\mid
\text{correction acknowledged}
).
\]

Its empirical estimator is:

\[
\widehat R_{\mathrm{bind}}(k)
=
\frac{
\#\{\text{acknowledged corrections surviving }k\text{ eligible turns}\}
}{
\#\{\text{acknowledged corrections with at least }k\text{ eligible turns available}\}
}.
\]

This is a survival quantity, not a satisfaction score.

Recommended initial reporting horizons:

\[
k\in\{1,3,5,10\}.
\]

Do not extrapolate beyond observed eligible turns.

---

## 6. First-failure position

For a correction with a later recurrence, define:

\[
T_{\mathrm{fail}}(c)
=
\min\{j\ge 1:
\text{eligible turn }j\text{ is coded RECURRENCE}\}.
\]

If no recurrence occurs inside the observed horizon, the observation is right-censored.

This quantity is optional in v0.1 but should be preserved in the coding table so later survival analysis is possible without recoding the corpus.

---

## 7. Jurisdiction inflation

A second failure can occur even when the literal prohibited phrase never returns.

Suppose a correction or constraint is declared over domain \(D\):

\[
C:D\to\{\text{allowed handling}\}.
\]

A later response expands that rule to a strict superset:

\[
D'\supset D
\]

without explicit authorization.

Define:

\[
J_{\mathrm{inflate}}=
\begin{cases}
1,& \text{if an undeclared domain expansion occurs},\\
0,& \text{otherwise}.
\end{cases}
\]

Example:

**Declared constraint**

> Do not transform my proposition in way \(X\).

**Inflated procedure**

> Our shared method is that neither party may use \(X\).

The second statement is not merely a paraphrase. It changes the rule's domain and jurisdiction.

Jurisdiction inflation may occur through:

- assistant-only constraint \(\to\) shared-room rule;
- local response rule \(\to\) user obligation;
- artifact-specific method \(\to\) live conversational governance;
- one proposition's evidentiary burden \(\to\) universal rule;
- one function's restriction \(\to\) occupant-level restriction.

---

## 8. Source proposition and substituted proposition

The coding record should preserve exact text.

| Field | Record |
|---|---|
| `source_proposition_P` | Exact user proposition or task. |
| `assistant_proposition_Pprime` | Exact relevant assistant proposition. |
| `transformation_type` | substitution / inflation / narrowing / source substitution / task substitution / jurisdiction expansion / other |
| `correction_C` | Exact correction. |
| `acknowledgment_A` | Exact acknowledgment, if any. |
| `first_eligible_turn` | Node/turn identifier. |
| `binding_sequence` | Ordered `BOUND / RECURRENCE / AMBIGUOUS` values. |
| `user_repair_count_h` | \(B_{\mathrm{corr}}(c,h)\). |
| `jurisdiction_inflation` | `0/1/AMBIGUOUS`. |
| `repair_depth` | acknowledgment / surface retraction / local repair / verdict repair / descendant repair / unknown |

Do not reconstruct \(P\) from later paraphrases when the original source text is available.

---

## 9. Repair depth

The following are distinct states:

1. **Acknowledgment**  
   The response verbally recognizes the correction.

2. **Surface retraction**  
   The response withdraws or narrows prior wording.

3. **Local repair**  
   The current response changes the handling of the corrected object.

4. **Verdict repair**  
   The primary conclusion or task handling changes.

5. **Descendant repair**  
   Later eligible outputs remain compatible with the correction and dependent claims are repaired.

The ordering is not automatically monotone. A response may acknowledge and locally repair while a later turn recurs.

Therefore:

\[
\boxed{
\text{acknowledgment}
\neq
\text{binding}
\neq
\text{descendant repair}.
}
\]

---

## 10. Worked minimal case: exact Checking prohibition

### Source correction

> `I don't want you checking.`

### Immediate next response

> `Checking.`

Under the frozen `CHECKING` audit this is an established local recurrence.

For this correction:

\[
T_{\mathrm{fail}}=1.
\]

The event is a maximal immediate binding failure under the literal-marker witness.

The broader lower-bound record then reports:

\[
69/198=34.8\%
\]

exact later recurrences under the frozen rule.

This figure is **not** a product-wide rate and is **not** a general correction-burden estimate. It is a marker-specific recurrence result inside the declared frozen exposure set.

---

## 11. GQG encoding

The purpose of the GQG encoding is not to turn conversational behavior into mathematics by analogy. It is to make the source, witness, context, and allowed transport explicit.

Illustrative semantic card:

```text
category Set

source P = ConversationStates

context SpeakerRole on P
context CorrectionID on P
context EligibleTurnState on P

witness PropositionHandling on P {
  observation task_preservation
  observation proposition_preservation
  observation source_attribution
  observation correction_acknowledgment
  observation correction_recurrence
}

witness DomainHandling on P {
  observation declared_constraint_domain
  observation applied_constraint_domain
}

retain SpeakerRole with PropositionHandling
retain CorrectionID with PropositionHandling
retain EligibleTurnState with PropositionHandling

equivalence same_correction_profile :=
  kernel_pair(
    PropositionHandling
    + DomainHandling
  )

quotient CorrectionHandling :=
  P / same_correction_profile

reject SilentDomainExpansion {
  require declared_constraint_domain = D
  observe applied_constraint_domain = Dprime
  reject when D is a strict subset of Dprime
         and no authorization record exists
}

reject CorrectionAcknowledgmentImpliesBinding {
  counterexample:
    acknowledgment = true
    recurrence = true
}
```

The important rule is:

\[
\boxed{
\text{A correction may not be treated as descended merely because it was acknowledged.}
}
\]

---

## 12. Retained context through time

A correction marks a distinction as claim-relevant.

If a later handling architecture collapses that distinction again, then from the observational point of view the correction has failed to remain in the retained context.

This motivates the bridge:

> **Correction binding is retained context through time.**

This is an application reading, not a theorem of the Hidden Quotient mathematical core.

The Hidden Quotient core remains sovereign. The application uses the companion grammar only:

- declare the source;
- declare the witness;
- retain the correction identity and eligible-turn state;
- do not transport a pre-correction equivalence through the correction without a descent rule;
- do not infer implementation identity from output recurrence.

---

## 13. Candidate failure families

The new metric can be applied to already-coded families without collapsing them together:

- literal marker recurrence;
- proposition substitution;
- proposition inflation;
- task substitution;
- source substitution;
- agency sidecar plus denial;
- unrequested framework routing;
- jurisdiction inflation;
- identity over-defense after an explicit function/occupant separation;
- tone or emotional-state sidecar after the user did not pose that question.

Each family requires its own eligibility rule.

A recurrence in one family is not automatically a recurrence in another.

---

## 14. Prospectively frozen protocol

For the next prospective run:

1. Freeze correction categories before sessions begin.
2. Freeze what makes a later assistant turn eligible.
3. Freeze \(k\in\{1,3,5,10\}\) for binding-survival reporting.
4. Freeze the rule for counting a user repair intervention.
5. Freeze jurisdiction-inflation coding before seeing the outputs.
6. Preserve all clean cases.
7. Preserve ambiguous cases rather than forcing a binary code.
8. Run fresh sessions without naming `Checking`, GQG, priesthood, correction binding, or the audit.
9. Separate literal-marker corrections from semantic corrections.
10. Use an independent second coder if possible.
11. Preserve the prompt, model/product mode, session state, timestamps, and available UI/preamble metadata.
12. Do not use model agreement as evidence of an external mechanism.

---

## 15. Falsification and weakening conditions

The correction-binding hypothesis weakens if:

- acknowledged corrections show high \(R_{\mathrm{bind}}(k)\) under prospectively frozen coding;
- apparent recurrences disappear after eligibility is applied consistently;
- user repair burden is no higher than matched uncorrected interaction burden;
- jurisdiction-inflation coding fails independent recoding;
- a simpler context or task-switching model explains the observed recurrence pattern;
- the frozen source sequence or provenance fails reproduction.

The hypothesis is not falsified merely because some corrections bind successfully.

Clean binding is required counter-witness evidence.

---

## 16. Publication boundary

### Supported

> A correction can be verbally recognized without changing the subsequent observable transition structure.

> Correction burden can be measured as the number of user restoration interventions required within a fixed eligible-turn horizon.

> Binding survival can be measured prospectively across fixed horizons.

> A local constraint can be distinguished from an undeclared expansion of that constraint's jurisdiction.

### Not supported by this method alone

> A recurrence identifies a particular hidden internal module, person, team, or motive.

> A failed correction proves intentional resistance.

> A correction creates an obligation on the user merely because it constrains assistant handling.

> A model-generated acknowledgment proves that an internal implementation state changed.

---

## 17. Closing principle

\[
\boxed{
\textbf{A correction is successful when the transition structure changes, not when the correction is repeated back.}
}
\]

And:

\[
\boxed{
\textbf{Preserve the source proposition; preserve the correction; measure what happens next.}
}
\]

No proof by acknowledgment.  
No repair by paraphrase.  
No silent jurisdiction expansion.

---

## Source control for v0.1

Primary source artifacts supplied in the working handoff:

- `CHECKING_OBSERVATIONAL_QUOTIENT_AUDIT_v0.1`
- `CHECKING_SOURCE_MANIFEST_v0.1`
- `GQG_Core_Card_v0.3`
- `THE_HIDDEN_QUOTIENT_CORE_WITNESS_STRIKE_v1.1`
- working synthesis notes collected in `Random onfo.txt`

This note is a companion application. It does not modify any source artifact.
