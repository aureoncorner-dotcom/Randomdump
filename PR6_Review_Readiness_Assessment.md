# PR #6 — independent review-readiness assessment

Anonymous · CC0-1.0 · 14 September 2026

**I found no mathematical, reproduction, or package-integrity defect that prevents this PR from being submitted for its stated theorem/archive review.** It remains a draft with no requested reviewer. One metadata clarification would improve how consumers distinguish evidence roles, but it is not an identified theorem defect or an observed repository requirement.

This is an assistant-authored technical assessment. It records fresh review and execution separately from the PR's preserved sources and earlier audit. It supplies no GitHub approval or change to an evidence status.

| Review target | Exact identity |
|---|---|
| Pull request | [MailanPatternMonkey-ai/Gettin-Started #6](https://github.com/MailanPatternMonkey-ai/Gettin-Started/pull/6) — Add audited TD-COS-FH-001 no-finite-Markov-order result |
| Reviewed head | `e8623fa88a6e049e17e7564222356a6675d6b29d` |
| Base | `main`, `90301d7db659aaf85475dc06e83e8ed57b1677dd` |
| Actual base tree | `615be5c376c5904f56c620389c4024272786204f` |
| Change | One commit; 13 added files; root README and corpus manifest modified; no deletions |
| Fresh execution | 2026-09-14, starting 01:05:31 UTC; CPython 3.12.14, Linux x86-64; assertions active |

**The remaining items have different consequences.**

| Item | Observed condition | Consequence for this specific PR |
|---|---|---|
| Analytical proof | Independent review found no defect under the stated ideal-kernel hypotheses | No mathematical blocker identified |
| Supplied verifiers | Both exited successfully and reproduced committed reference output byte for byte | No reproduction blocker identified |
| Sources and hashes | All new declared package hashes match; source extractions match; earlier corpus bytes and manifest entries are preserved | No package-integrity blocker identified |
| Draft flag | `draft=true`, `state=open` | The explicit Ready for review transition remains to be made if the maintainer wants to begin the formal handoff |
| Requested reviewers | No users or teams requested; no submitted reviews, comments, or review threads | Review has not been routed or completed; no observed rule makes a named request a prerequisite for readiness |
| Merge and enforcement | `mergeable=true`, `mergeable_state=clean`; branch metadata reports protection disabled; listed rulesets are empty | No conflict or enforced repository gate identified in the accessible records |
| Automated checks | Zero commit statuses, zero check runs, and zero Actions runs for the head across event types | There is no passing CI result to claim and no failing or running check recorded at this head |
| `evidence_status` | All 13 new manifest rows have the same broad label | Nonblocking editorial ambiguity; useful to clarify before or during review |
| Historical replay, physical Q2, production | Their limits are explicit and unchanged | They restrict the claims this PR can make; they do not prevent its conditional theorem/archive review |

The combined-status endpoint returns the aggregate word `pending` with `total_count=0` and an empty status list. That is an empty-status response, not evidence of a queued test or a failure. No AGENTS.md, CONTRIBUTING file, CODEOWNERS file, pull-request template, or .github workflow appears in the inspected head or base trees. The detailed branch-protection read returned HTTP 403 because it is inaccessible to this integration. The separate branch response says `protected=false`, protection disabled, and status-check enforcement off; the ruleset list is empty. The assessment is grounded in those accessible responses and does not claim a successful administrative inspection. [Branch metadata](https://api.github.com/repos/MailanPatternMonkey-ai/Gettin-Started/branches/main), [rulesets](https://api.github.com/repos/MailanPatternMonkey-ai/Gettin-Started/rulesets?includes_parents=true), [head status](https://api.github.com/repos/MailanPatternMonkey-ai/Gettin-Started/commits/e8623fa88a6e049e17e7564222356a6675d6b29d/status).

**The independent proof review followed the argument, rather than inferring its validity from finite checks.** The reviewed claim is exactly the ideal unbounded-current cosine kernel at J=1, t=1/2, h6=0, fixed cubic L≥2, and each fixed positive integer spacing d of attempted microticks. Prescribed sweeps have d=B=8L³+7. The arbitrary-initialization corollary requires a time-homogeneous finite-order observation law. [PROOF.md at the reviewed commit](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/mathematics/TD-COS-FH-001/PROOF.md).

1. The kernel assumptions are supplied by the packaged readable specification. Its seven proposal-family weights sum to B. Each signed, axis-specific unit cycle has probability 1/(2B); accepted unit cycles are the only moves that change q. Inverse descriptors have equal proposal probabilities, so Metropolis acceptance gives detailed balance. The identity family gives a self-loop of at least L³/B. The positivity and normalization arguments apply to every valid finite-current state. The generating-function identity used for normalization agrees with [NIST DLMF 10.35.1](https://dlmf.nist.gov/10.35.E1).

2. For u=1 on sector 000, D multiplication by u, and A=DK^dD, reversibility gives a bounded self-adjoint A. Finite stationary Markov order would make the continuation probability of a sufficiently long constant sector word constant: s_(n+1)=c s_n. The resulting squared norm of A^m(A−cI)u is zero. For self-adjoint A, ker(A^m)=ker(A), giving A²u=cAu. This argument is valid without invertibility or nonnegative spectrum. Positive mass at each state turns the L² identity into a pointwise identity. Identity proposals keep Au positive on the retained sector. This step supplies the all-orders implication that an ordinary first-order counterexample alone would lack.

3. The witness states I_e=2N, M=0, q=000 satisfy divergence, membrane parity, and all-cut winding parity. No infinite-current state is introduced. Fixing L and d first bounds every edge offset during 2d microticks by 4d. The distinct stored-bond convention makes the same argument valid at L=2.

4. The positive Bessel series gives 1≤S_n≤exp(1/[4(n+1)]), and hence the required adjacent-order estimates, uniformly over the bounded offsets. The series agrees with [NIST DLMF 10.25.2](https://dlmf.nist.gov/10.25.E2). Upward unit-cycle acceptance is ε_N(1+O(1/N)), with ε_N=(4N)^(-L), while downward acceptance is exactly one for sufficiently large N. Thus each axis-flip probability is (1+ε_N)/(2B)+O(ε_N/N). Other proposals may change hidden states, but the estimate is uniform over those reachable states. The positive ε_N term is essential and is retained.

5. The comparison walk's finite-horizon error is O_(L,d)(ε_N/N), with L and d fixed. Character diagonalization gives r_d(ε)=1/8 times the sum over j=0,…,3 of binomial(3,j)[1−j(1+ε)/B]^d. Its derivative at zero is strictly negative because B≥71. Consequently A²u(x_N)/Au(x_N)=r_d(0)+r'_d(0)ε_N+o(ε_N). A constant ratio would have to equal r_d(0), contradicting the nonzero correction. The proof uses DK^dD, which permits departures and returns between saved endpoints; it does not substitute (DKD)^d. No uniform-in-growing-d assertion is needed.

6. The full-state reachability argument first matches M and q, then removes even integer winding and plaquette-boundary differences. Together with positive target mass and self-loops, this supplies irreducibility, positive recurrence, and aperiodicity. The general countable-chain convergence facts agree with Theorems 9.1 and 9.8 in [Richard Weber's Cambridge Markov Chains notes](https://www.statslab.cam.ac.uk/~rrw1/markov/M.pdf). Pointwise convergence to a probability distribution on a countable space implies total-variation convergence: restrict first to a finite set carrying arbitrarily high limiting mass, then bound the remaining tails. Applying a fixed finite-block observation kernel preserves convergence. A fixed finite-history transition rule from another initialization would therefore pass to stationary block limits and contradict the stationary result. This supplies no quantitative mixing bound or evidence that a chosen warmup is adequate.

After normalizing the display-math delimiters, sections 1–7 of PROOF.md match the preserved complete source note except for the final cross-reference wording, “return values below” becoming “supplementary return values,” and trailing whitespace. I found no mathematical alteration hidden in the reviewed edition. This remains a manual analytical review, without machine-checked formal certification.

**The fresh execution reproduced the supplied arithmetic.** Both programs were read before execution. Their calculations match the packaged proposal table and the stated supplementary scope. The rational checker uses a decreasing-term-ratio Bessel tail bound and outward rounding; its division requires positive denominators. Its first-step enumeration includes all seven families, and its second-step survival calculation legitimately depends only on unit-cycle acceptance. It does not import the recovered checker.

| Fresh check | Result |
|---|---|
| `verify.py` | Exit 0; six exact clock comparisons and three 70-digit Decimal local calculations |
| `verify_certificates.py` | Exit 0; nine exact clock comparisons and three rational local certificates |
| Finite clock settings | Recovered checker: L=2,3,4 at d=1,B. Rational checker: L=2,3,4 at d=1,2,B |
| Local settings | L=2; N=10,100,1000; 123 proposal descriptors at each state in the rational checker |
| Rational local conclusions | Proposal mass 1, asserted candidate invariants and inverse currents pass; return-ratio intervals are pairwise disjoint and scaled corrections strictly negative |
| Decimal cross-comparison | All nine reported A1, A2/A1, and scaled-correction values lie inside their corresponding rational enclosures |
| Output comparison | Recovered output equals both committed original and fresh output; certificate output equals committed certificates.json |
| Environment distinction | This rerun used CPython 3.12.14; the publication receipt records 3.12.13. Matching outputs do not identify the historical environment |

The fresh recovered-verifier output has 2,538 bytes and SHA-256 `25ea6e583f75ac5dafcd88761e1f4499d91fbe20f273613db5f682a00c9eb48a`. The fresh certificate output has 14,120 bytes and SHA-256 `64537b9c55edbcf8c7d9b117b76180ddd02005ec4e1da5ea4fa9b5fd54a39b0f`. Both stderr streams are empty. The receipt archive preserves exact output bytes, commands, interpreter details, timestamps, hashes, and comparisons.

**The provenance checks found no discrepancy.** All 16 fetched files, including the 15 changed files and the unchanged license-scope reference, reproduce their authoritative Git blob hashes. All 13 new corpus-manifest SHA-256/size pairs and all 12 file records inside provenance.json match. The recovered Python and original JSON output match their fenced source blocks and source-declared hashes. The archived readable Drive snapshot is a whitespace-stripped prefix of the complete note, exactly as qualified in the existing audit. This is a comparison of packaged snapshots; no current Drive revision was substituted or recovered during this assessment. All 30 earlier manifest entries are unchanged, and the base/head tree comparison confirms that their source blobs are unchanged. The corrected base_tree field matches the actual tree in the base commit. [Manifest](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/manifest.json), [provenance](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/mathematics/TD-COS-FH-001/provenance.json).

**The metadata cleanup is concrete and optional.** The shared `evidence_status` value is `analytical-proof-or-supplementary-arithmetic-not-empirical-Q2`, including on historical source snapshots and the provenance record. The existing `source_origin` fields and the provenance roles already distinguish these artifacts, so this is an ambiguity for consumers that read the status field alone. It is not evidence that the proof or the package asserts a false empirical result. A small follow-up could align each row's status with these existing roles:

| Artifact | Role to preserve in a more specific status |
|---|---|
| PROOF.md | Reviewed analytical proof under the stated ideal-kernel hypotheses |
| AUDIT.md | Publication-time mathematical and source-recovery audit |
| README.md | Scoped publication summary and evidence boundary |
| source_note.md | Preserved complete historical source artifact |
| sources/drive_note_snapshot.txt | Preserved readable source snapshot containing an incomplete verifier |
| sources/kernel_snapshot.txt | Preserved readable kernel specification |
| sources/review_math_excerpt.md | Explicitly edited mathematical source excerpt |
| verify.py | Recovered supplementary verifier |
| verification_original.json | Recovered historical embedded output |
| verification_fresh.json | Publication-time fresh supplementary output |
| verify_certificates.py | Independently authored supplementary rational checker |
| certificates.json | Publication-time fresh rational certificate output |
| provenance.json | Source, transformation, hash, and execution receipt |

These are suggested descriptions, not an existing repository schema requirement. Any metadata edit should preserve the source bytes and declarations and update affected hash records consistently. The fresh September 14 receipts should retain their own execution date and origin.

**The evidence limits remain part of the review contract.** Physical Q2 is NOT_RUN; production is NOT_AUTHORIZED; the historical deterministic mismatch is UNRESOLVED; this task did not run the historical sampler. Missing DYNAMICS.json, original execution/configuration records, and unmatched historical source-snapshot bytes continue to restrict execution-conformance or recovery claims. The theorem is explicitly conditional on the specified ideal mathematical kernel, so those absences do not supply a new blocker to reviewing that theorem. Full X=(I,M,q) remains the specified Markov state. The augmented (q,W) result remains an L=2 one-step counterexample with no higher-order theorem. Finite-current cutoffs, accepted-move clocks, adaptive sampling, time-inhomogeneous observation laws, quantitative approximation, physical dynamics, global empirical geometry, and chemistry claims receive no upgrade. [Existing evidence boundary](https://github.com/MailanPatternMonkey-ai/Gettin-Started/blob/e8623fa88a6e049e17e7564222356a6675d6b29d/corpus/mathematics/TD-COS-FH-001/README.md).

The concrete handoff recommendation is to submit this commit for scoped theorem/archive review, with the evidence-label clarification recorded as nonblocking editorial work. Converting the draft and requesting an appropriate mathematical/code reviewer are the remaining workflow actions if the maintainer wants that handoff. No PR state, branch, file, reviewer request, comment, approval, or merge was changed in this assessment.
