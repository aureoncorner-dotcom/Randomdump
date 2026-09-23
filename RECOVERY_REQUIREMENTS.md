# Minimum historical recovery and comparison requirements

Anonymous · 8 September 2026 · CC0-1.0

This is an intake and audit protocol for the existing discrepancy. It is not a replacement dynamics definition, a new sampling plan, or a discrepancy-resolution receipt.

## Smallest useful intake

Recover H1–H3 and H6 in the register: original configuration, companion executable/build, original event format/storage amendment, and the manifest binding them to the 1,108,720 execution. Add the first 512 original events of each of the eight chains and the original initial-state/RNG evidence. Recover checkpoint evidence near 142,000 and the first retained observation at 142,071 when available. The existing reproduction sidecar provides comparison material at those addresses.

Original names for the companion sampler, event and checkpoint files are unknown. Preserve names and bytes as found. Record source URL or repository commit, source revision, retrieval time, byte size, SHA-256, embedded run identity and original manifest binding. If the original source lacks a date, hash or field, mark it missing. A newly computed retrieval hash identifies a copy; it does not establish the original execution date.

The target profile is the reported historical L2 dual execution: fixed-reference Z000; cosine Bessel weights; J=1, t=1/2, h6=0; periodic 2×2×2; eight initial sectors q=c, M=0, I=Gamma(q); proposal seeds 64000+c and acceptance seeds 74000+c; 2,000 warmup and 10,000 retained sweeps; 71 attempted microticks per sweep. Keep original configuration/code discrepancies visible rather than forcing this prose onto recovered code.

## First comparison

1. Authenticate each recovered artifact against the original run manifest where possible. Keep the reproduction and companion records in separate directories.
2. Read the original EVENT_FORMAT.md before decoding. Preserve raw bytes. Create a separately hashed adapter only after cell order, q bits, outcomes, integer encodings, state/RNG digests and acceptance-prefix semantics are known. Label any derived field and retain its raw source address. Do not make defaults that turn missing evidence into agreement.
3. Compare the same contiguous attempted-event addresses. Inspect initial state, before-state, proposal descriptor and proposal RNG, acceptance signature/bounds and random prefix, acceptance RNG consumption, outcome, after-state and after-RNG evidence. Report the first differing event per chain, including the first evidence-field difference even if states still agree.
4. The preserved comparator accepts the investigation tracer's schema only. It returns MATCH_ON_SUPPLIED_PREFIX, DIVERGENCE or INCOMPLETE_EVIDENCE. A prefix match cannot become a full-run pass. Its CLI reports differing fields; final diagnosis must interpret their causal order from the preserved raw evidence.
5. If all eight 512-event prefixes agree, extend only the aligned comparison span using recovered originals. Preserve each extension's code/configuration/output identity. Do not resample a new cohort or change seeds.

Two reproduction-side witnesses already exist: chain 7 at attempted microtick 5 and chain 0 at 53 accept a proven probability-one move without consuming acceptance bits. These are inspection addresses, not identified companion divergences. No-draw behavior, bit ordering or Bessel precision must not be patched to force the final counter.

The recovered reproduction uses q=qx+2*qy+4*qz; its printed binary label is qz qy qx. Merely relabelling q cannot change accepted-update totals. Legacy state hashes are BLAKE2b-128 over the sampler's little-endian serialization; RNG digests are SHA-256 over the ASCII repr of random.Random.getstate(). Preserve these encodings for historical comparisons. The replacement amendment's new digest contract is not historical authority.

## Full old-run audit

H4–H5 must ultimately cover all 6,816,000 ordered attempts, 80,000 retained rows and all 96 companion-reported post-initial checkpoints at their original addresses. Identities and rejections advance the attempted clock; repeated states remain. Recover exact random prefixes and full states or enough lossless original evidence to reconstruct them. A checkpoint digest cannot supply the missing state or RNG prefix.

The reproduction packet contains aggregate/per-chain event digests and 88 original digest checkpoints, not a full inspectable event file. Its diagnostic sidecar has 4,096 event rows and 32 full state/RNG snapshots only. Further reproduction-side evidence would need a separately recorded regeneration from the preserved sampler, kept apart from original files. The existing diagnostic script is bounded; no full historical recorder is claimed here.

For any later restart claim, reconstruct a state and both RNG streams at a named checkpoint, restart in a fresh process, and compare its suffix with the uninterrupted original stream. Preserve clock and diagnostic bookkeeping too. A matching aggregate is secondary evidence; locate and explain the earliest actual divergence against the declared kernel before proposing a correction.

## Runnable material already present

From this package root, run the standard-library integrity check:

    python3 verify_package.py

The original supplementary proof verifier is also directly runnable:

    python3 verifier/verify.py

That command performs six exact group-arithmetic and three local Decimal cases; it does not replay a sampler.

For historical event comparison, extract preserved/TD_COS_FH_001_Mismatch_Investigation_v0.1.zip into a new work directory. Its README describes the additive tracer and comparator. Only after an actual companion stream has been recovered and normalized can the existing command be used there:

    python3 compare_td_traces.py diagnostics/reproduction_prefix_events.jsonl companion_canonical_events.jsonl --output first_divergence.json

The companion_canonical_events.jsonl input is not supplied. The comparator has not been run against the actual companion in this recovery. The source CLI's --dynamics argument hashes a file for provenance; it does not load and enforce its contents. Passing a replacement configuration to it cannot establish adoption or historical identity.

## Status boundary

Recovery or auditability is distinct from reconciliation. Preserve both totals and the −1,352 difference even after a future cause is established; record any explanation and corrected successor in a separate dated receipt. No change to the old kernel, counts, original manifests or source documents is made here. Production remains NOT_AUTHORIZED and physical Q2 remains NOT_RUN.

The prospective replacement amendment remains fallback-only. Its new 112-checkpoint contract, configuration and digest schema do not fill the companion's original 96-checkpoint gap. Original primary/follow-up reference cohorts and all L3 statuses remain separate.
