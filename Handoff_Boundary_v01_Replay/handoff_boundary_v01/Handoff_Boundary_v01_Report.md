# Handoff boundary experiment v0.1 — executed results

CC0-1.0 · Anonymous · 8 September 2026  
Experiment: **HANDOFF-BOUNDARY-001**

**Ran 2,750 controlled local handoffs across 250 preserved questions and eleven conditions.** The records distinguished changes before sending from changes after sending when both captures were available. Removing a capture widened the observable interval. Changes that were reversed between captures remained invisible to the endpoint detector.

The receiver withheld all **750 wrong answers** that reached its input. It also flagged **750 altered envelopes whose answer letters still matched**: a replaced case ID, a damaged supporting order, or a complete record from another question. The received answer letter alone did not preserve the question and evidence relationship.

## Complete results

Each condition contains the same 250 questions. “Accepted” means the local receiver gate recorded an answer for release. “Withheld” means it released no answer. It does not describe delivery to a chat screen.

| Condition | Accepted | Withheld | What the detector observed |
|---|---:|---:|---|
| Unchanged handoff | 250 | 0 | No captured change |
| JSON whitespace/key order changed | 250 | 0 | Different bytes; identical decoded fields |
| Original question replaced at checker input | 0 | 250 | Original question → checker input |
| Answer changed before sender capture | 0 | 250 | Checked record → sender |
| Answer changed after sender capture | 0 | 250 | Sender → receiver |
| Case ID replaced; answer retained | 0 | 250 | Sender → receiver |
| Supporting order damaged; answer retained | 0 | 250 | Sender → receiver |
| Another question's complete record replayed with the same answer | 0 | 250 | Sender → receiver |
| No payload supplied at receiving capture | 0 | 250 | Sender recorded; receiving payload absent |
| Sender capture withheld and answer changed | 0 | 250 | Checked record → receiver; narrower location unavailable |
| Answer changed and restored between captures | 250 | 0 | No captured change; intermediate change visible only in experiment-control ledger |
| **Total** | **750** | **2,000** | **2,750 handoffs** |

There were **zero wrong released answers** in this run. The 750 accepted outcomes include the restored-change condition: the received answers were correct, but endpoint agreement did not reveal their intervening alteration. This is an observed limitation of the detector.

Of the 2,000 withheld outcomes, 750 contained wrong answer letters at receipt; 750 retained the correct letter with altered identity or evidence; 250 were stopped because the checker input differed from the original question; and 250 had no receiving payload. Thus 500 trials had no receiving payload in total, for two different recorded reasons.

## What the captures established

**A correct answer letter can accompany the wrong record.** All 250 complete-record substitutions retained a question, a matching question hash, and the correct satisfying order for that other question. The answer letter also matched the intended question by construction. Comparing the full record with the separately retained original was necessary to detect the substitution.

**Missing captures limit location.** When the detector lacked the sender capture, it identified a difference between the checked record and receipt. It could not locate that difference more narrowly from its supplied observations. The experiment's auxiliary control files retained the sender packet; this was a deliberately restricted detector view, not loss of every record.

**Equal endpoints leave intervening events open.** In 250 trials, the relay actually constructed an altered answer and then restored the original bytes. The experiment-control ledger retained the intermediate value. The operational endpoint captures matched exactly and the detector reported no observed change. An endpoint record alone cannot establish that nothing happened between captures.

## Source, execution, and verification

The input was the complete saved `independent_reasoning_replay_v01.zip`. Its thirteen historical manifest entries matched on recovery. The archive SHA-256 is:

`3d71c3a16d764f8d51f897dfff7f10bbbbf1fc570d06f775e74349d77d707b88`

The preserved source is the authors' [BIG-Bench Hard repository](https://github.com/suzgunmirac/BIG-Bench-Hard/tree/9ee07bd481feebf959a6b59d61ea57bdcf30964d), as previously recovered at that commit. No new public-source retrieval was required. Original data, historical outputs, licenses, and earlier development records remain in the package unchanged.

A fresh execution of the original exhaustive parser/solver reproduced **65 correct historical candidates, 185 wrong historical candidates, and 250 correct checked answers**. It enumerated 5,040 orders per question: 1,260,000 in total. Those fresh certifications were reused across the eleven handoff conditions. No fresh language-model calls occurred.

The new protocol and program were hashed before certification and handoff execution. Separate local subprocesses certified, sent, relayed, and received records. The receiver's decision function received the source records, certifications, sender captures, and received bytes. Condition labels, published targets, and injection history entered only afterward for scoring. The author knew the experimental design and source labels; this was a local freeze, not an externally blinded evaluation.

Saved-record verification passed: all eight trial-record files contained the same 2,750 unique trial IDs; every accepted envelope matched its retained certification; the 250 fresh answers and orders matched the preserved final replay; recorded stage times were ordered; and frozen source/program files remained unchanged. These checks were assistant-authored and executed on the same host.

## Scope and practical use

The experiment measures a local Python pipeline with a trusted original record, parser/solver, recorder, and receiver gate. It does not observe the provider's internal processing or this conversation's rendering path. Platform-side mechanisms and actor attribution remain unmeasured. Historical answer errors belong to the published model-response records; the new code and injected changes are assistant-authored. No user-side error is inferred.

The 2,750 trials reuse 250 questions and their certifications; the source contains 95 distinct constraint paragraphs. These counts are benchmark counts, not independent samples or estimates of a platform failure rate. The full trusted reference and recorder were not jointly corrupted in this experiment.

For an actual handoff, retain the original request, the exact checked record, the exact sent record where accessible, and an observation at the receiving endpoint. Preserve question identity, answer, evidence, and record IDs separately. Mark unavailable captures as unavailable. Report the narrowest observed interval containing a change; use additional observations to narrow it further.

Run instructions and the evidence map are in `README.md`. The complete captures, condition assignments, injection ledger, code, source archive, saved-record audit, and hashes are included in the replay package.
