# Conditional closure v0.3

Preserve raw numerical scores, scientific statuses, validation requirements and conditional interpretation separately. A reference-program pass is a software/mathematical result; it does not replace a physical antecedent.

| Scientific status | Meaning |
|---|---|
| PASS | An admissible result satisfies its frozen criterion |
| FAIL | An admissible result violates its frozen criterion |
| INCONCLUSIVE | The intended decision lacks sufficient admissibility or power |
| UNRESOLVED | Required information is missing or admissible alternatives remain undistinguished |
| INVALID | A required validity condition fails |
| NOT_RUN | This analysis was not executed |

For the declared conditional claim A⇒B, list every required antecedent and validation gate. Q2/Q3 may be among the antecedents, but any required vison-gap or critical-window conditions must also be named. They are logical requirements, not assumed statistically independent observations.

The executable decision function uses the following priority:

| Condition | Joint record |
|---|---|
| Any required result INVALID, or a required validation gate FAIL | NO_ADMISSIBLE_VERDICT |
| Required validation missing, unresolved or not run | JOINT_CLAIM_UNRESOLVED |
| Validation passes; at least one antecedent FAIL | REALIZATION_REJECTED |
| Validation passes; any antecedent not decisive, or B not decisive | JOINT_CLAIM_UNRESOLVED |
| All antecedents PASS; B FAIL | CONDITIONAL_PREDICTION_FALSIFIED_FOR_THIS_REALIZATION |
| All antecedents PASS; B PASS | REALIZATION_SUPPORTED |

Rejecting an antecedent rejects this realization of the construction; it does not logically falsify A⇒B. Conversely, satisfying A while failing B falsifies that specified conditional prediction for the tested realization. Neither status automatically retires every possible theory in a wider family. That needs a separate scoped claim and record.

`reference/reporting.py` requires nonempty named antecedents and validation requirements and rejects unknown statuses. It composes supplied labels; it cannot determine whether the caller declared all scientifically necessary premises. The current [evidence ledger](EVIDENCE_LEDGER.json) retains physical Q1/Q2/Q3 and empirical TTSC as NOT_RUN.
