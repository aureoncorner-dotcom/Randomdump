# Reasoning Bypass v0.1

CC0-1.0 — Anonymous — 2026-09-08

## What this implements

A runnable, bounded demonstration of preserving correct logical conclusions
under explicitly injected computation/output faults. It uses finite positive
Horn logic: facts and rules such as `A and B implies C`. There are eight
Boolean atoms per task, two initial facts and twelve rules. The query asks
whether the facts and rules entail one atom. A negative result means **not
entailed**, not that the atom's negation is entailed.

No antimony measurements, electrical simulation, hardware changes, LLM calls,
natural-language reasoning experiments, or infrastructure-wide deployment occur.
Antimony remains a proposed, unverified upstream cause; faults here are synthetic
mutations of program outputs. These results cannot diagnose a dopant or establish
that it affects language-model reasoning.

## Run

Requires Python 3.9 or later; no external packages or network.

```bash
python3 run.py --out results
```

The deterministic seed is 20260908. Outputs are `tasks.json`, `summary.json`,
`trials.csv`, and complete candidate certificates in `traces.jsonl`. Existing
outputs in the specified output directory are overwritten. `SHA256SUMS.txt`
records hashes of the distributed source, report, and results; it does not hash
itself and is not an independently signed trust anchor.

## Architecture

1. Keep the original structured task as the trusted reference.
2. Worker A proposes an answer with a certificate using repeated rule scans.
3. A checker validates the certificate against that original task.
4. If rejected, check Worker B's candidate, generated using an agenda/counter
   implementation. In this experiment both candidates are precomputed to keep
   fault injection deterministic; a service could compute B only on rejection.
5. Accept a certified result or return `UNRESOLVED`. Agreement alone grants
   no acceptance. The example assumes access to a trusted checker and router.

For a positive answer, the certificate lists rules in a valid derivation order.
For a negative answer, it supplies a truth assignment satisfying every fact and
rule while making the query false. The checker checks that assignment directly.
The task SHA-256 binds the candidate to the original task bytes under canonical
JSON serialization. The semantic checks, rather than the hash alone, establish
validity. A hash is neither proof of provenance nor protection when an attacker
can replace the reference task and its hash together.

The evaluation oracle exhaustively examines all 256 truth assignments per task.
It does not participate in the acceptance path and does not supply expected
answers to either worker or checker. It is used for corpus balancing and scoring.
Worker A, Worker B and the oracle use different algorithms but share the same
runtime, language, task schema and host; physical independence is not established.

## Mathematical claim and assumptions

Let S be a trusted task specification, a a proposed answer, and c a certificate.
For a sound checker V, the required implication is:

`V(S,a,c) = true  =>  a is correct for S`.

Positive certificates are sound by induction: initial facts hold in every model
of S; applying a rule whose premises already hold preserves that property; thus
the derived query holds in every model. A negative certificate is sound because
one checked countermodel is sufficient to refute entailment. Finite positive
Horn closure supplies a certificate for either outcome on this domain.

This argument concerns the checker specification. The Python implementation is
tested, not machine-verified. It assumes the original input, checker execution,
control flow, and accepted output channel remain correct. Arbitrary corruption
of all of those components is outside the guarantee. With no reliable reference
or checking operation, this architecture has no basis for certifying recovery.

The guarantee is **conditional correctness of accepted outputs**, not guaranteed
availability: both workers can fail, and then the result is unresolved. It does
not optimize the earlier minimax objective over physical dopant conditions.

## Connection to the current geometry

Define the retained observation as the claimed answer alone. Equal claims can
have different validity witnesses. Adding a task-bound certificate gives the
checker access to distinctions missing from the answer-only record. This is an
application-specific refinement, not a claim that global non-descent disappears.
Correctness also does not identify the microscopic cause of a failure.

The applicable source scope was reviewed earlier in this conversation:

- [Geometry + GQG — Working Master](https://docs.google.com/document/d/1Cn00U9Cj37QRrK2Xg3bX1417xYKstkFzednitR9xjog/edit)
- [New geometry](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit)
- [TOROIDAL — Working Master](https://docs.google.com/document/d/1NV7JsFuqJJVjFzYcqCAuC22y_rrjCSqqcZWZKobcGoU/edit)
- [OMNIBUS v7.79-r1](https://docs.google.com/document/d/1Qs0uS2xw0Wm8E09K_BNRVzbnOcjQiZbfRaqOpt0D3ts/edit)

The experiment does not change any source document, chemistry status, historical
replay count, or physical Q2 status. Logic atoms are abstract symbols, not silicon
lattice sites. No toroidal dynamics theorem is transferred to this program.

## Fault and scoring scope

The scenario list is declared in `run.py` before the loop. Mutations represent
answer flips, certificate damage, changed query/task binding, missing or malformed
outputs, and correlated wrong candidates. The negative boundary deliberately
replaces certificate validation with an accept-all-dictionaries function.

Mutations to unused certificate fields are inert: positive answers use proofs;
negative answers use countermodels. These trials remain visible and are not
counted as detected failures. Certificate rejection and semantic answer error
are separate counts. For example, a damaged proof can accompany a correct answer.

All 128 original tasks, half entailed and half not entailed, are reused across
scenarios. Counts are an exact finite benchmark, not independent statistical
samples, confidence bounds, a physical error rate, or universal fault coverage.

An ordinary program crash, instruction fault, corrupted reference task, defective
language runtime, maliciously rewritten checker, concurrent mutation, and output
corruption after checking require separate tests and protections. The input API
also has not been hardened against arbitrary JSON or resource exhaustion.

## What would make this a test of reasoning in a real system

Select a task class with a defensible external correctness specification. Retain
the original premises and identities. Have the actual system produce answers
and checkable certificates, and use the verifier on held-out tasks. Record
correct accepted results, wrong accepted results, rejections, recovery latency,
and unresolved outcomes separately. Open-ended prose cannot inherit this exact
Horn-logic guarantee without an adequate formalization and checker.

For a physical dopant claim, additionally measure material condition, electrical
effects, and computational faults, using appropriate controls. This prototype
supplies neither that causal bridge nor a dose-to-fault relationship.
