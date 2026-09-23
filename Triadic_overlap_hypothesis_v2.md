# Triadic Overlap Hypothesis · v2.0
CCO - NO RIGHTS RESERVED
**Mediation, memory, and transformed return**  
6 September 2026 · Revised research hypothesis

> Same place, different state. Return does not require repetition, and return does not guarantee progress.

## Abstract

The Triadic Overlap Hypothesis proposes that some systems benefit from an explicit relation layer between intention and structure. This layer translates, preserves relevant distinctions, carries feedback, and makes correction possible. The useful question is whether those functions improve a specified system under specified conditions.

The updated framework distinguishes **O**, origin or operator; **R**, relation or mediation; **S**, structure or substrate; and **T**, elapsed time during which transformation occurs. Its central loop is **O → R → S → T → S′ → R′ → O′**. A returning signal may resemble an earlier signal while the underlying state, history, or available choices have changed.

The geometry work supplies exact examples of this distinction. Twin Timelines constructs identical finite observation histories with different next observations. The toroidal sampler pilot finds that parity sectors can pass exploration screens while signed winding fails them. These results sharpen how the hypothesis should be tested. They do not establish a universal geometry of stability or a biological cause of social organization.

## 1. The revised hypothesis

**Where coordination depends on distinctions that an interface would otherwise erase, a mediation layer that retains the relevant context and supports correction may improve prediction and recovery at an acceptable cost.**

This is a conditional claim. The system, task, retained information, update rule, disturbance, sampling schedule, and meaning of improvement must be declared. A mediator can also introduce delay, amplify errors, or obscure responsibility. A direct connection can work well.

The original intuition survives: meaningful cooperation often needs room for translation. The upgrade is to ask what that room actually preserves and changes.

“Sovereignty” expresses a design value: distinguish the participants' roles, preserve their ability to challenge an interpretation, and make exit or replacement possible where applicable. It is not a mathematical invariant established by drawing three nodes.

## 2. Distinct roles, without a required hierarchy

| Symbol | Role | What must be identified in an application |
|---|---|---|
| **O** | Origin / operator / meaning | The source of a request, interpretation, or constraint |
| **R** | Relation / mediation | The actual channel, representation, translation, and feedback mechanism |
| **S** | Structure / substrate | The state or process on which an action operates |
| **T** | Time | The interval and dynamics through which the state changes before return |

O, R, and S are pairwise distinct **roles**. They can share a physical implementation, and their assignment can change between interactions. T is a temporal stage, not a fourth participant.

In a deliberately mediated design, every interaction in a **declared set of operations** passes through R. This is an architectural constraint that can be inspected. It is not a prohibition on direct coupling throughout nature. If an application permits a bypass, it must describe which operations use it and what guarantees still apply.

Examples include a human, an interface, and a software engine; or a requester, a protocol, and a controlled process. Governance and neural communication may inspire other mappings, but those mappings need their own evidence. Calling something a membrane does not yet specify its mechanism.

## 3. The loop: transformation before return

```text
O → R → S → T → S′ → R′ → O′
                                ↘ next interaction
```

Primes mark a changed or returning stage of the same lineage. Subscripts distinguish parallel origins, such as O₁ and O₂. Therefore the returning origin is written **O′**, avoiding the ambiguity of O₂ in the earlier draft. R′ is the return mediation stage; it need not be the inverse of R.

At interaction n, a model might retain

$$
x_n=(o_n,r_n,s_n,h_n),\qquad
x_{n+1}=F_{\Delta t_n,u_n}(x_n),\qquad y_n=B(x_n),
$$

where h records relevant available history, u is the declared input, and B is the observation. The update must specify how the state evolves over the chosen time interval. “Preserve,” “decay,” “distort,” “integrate,” and “resonate” remain useful names for candidate transformation modes; each needs an actual rule before it is a model.

The distinction between mirror and transform becomes operational: an echo reproduces a specified representation, while modulation changes it according to a stated map. Neither automatically implies understanding or improvement.

Three kinds of return must be distinguished:

- **Observed return:** the recorded output matches an earlier output.
- **State return:** the declared full state matches an earlier state.
- **Functional recovery:** performance returns to a defined acceptable region after a disturbance.

One can occur without the others. Iteration preserves a lineage only to the extent that its identifiers and records do so; it does not guarantee preserved content.

## 4. When an observation can predict its own future

For a fixed deterministic update F on a forward-invariant domain D, an observed state B(x) has a well-defined autonomous successor precisely when

$$
B(x)=B(y)\ \Longrightarrow\ B(Fx)=B(Fy)
\quad\text{for all }x,y\in D.
$$

In plain language: **states that look the same must also produce the same next observation**. Otherwise the visible label omits something needed for exact prediction. With external inputs or a changing schedule, compare successors under the same declared input and interval, or include those variables in the predictive state.

For a stochastic full-state model, compare entire next-observation probability laws, not just their means. On a finite or countable state space with transition kernel P, the universal condition is

$$
P(x,B^{-1}(A))=P(y,B^{-1}(A))
\quad\text{whenever }B(x)=B(y),
$$

for every set A of possible observations. This is the strong lumpability condition. A transition table estimated from a short trace does not establish it.

If closure fails, retaining context c(x) changes the observation to (B(x),c(x)). That can repair the failure, but only if the refined observation passes the same test. More memory is not automatically better: its availability, precision, storage cost, and relevance to the task matter. Future outcomes cannot be used as inputs to a present prediction.

This provides a precise interpretation of one kind of “pinch”: an observation merges states whose differences matter to the next step. Predictive closure and dynamical stability remain different properties. [Proof and worked examples](MATHEMATICAL_NOTES.md).

## 5. What geometry means here

The original vesica, cylinder, helix, cone, and torus remain a vocabulary for exploration. Their scientific role depends on what has actually been specified.

| Geometric language | What would make it operational |
|---|---|
| Balanced overlap | Defined domains, an overlap measure, and evidence connecting that measure to an outcome |
| Pinched membrane | Measured capacity, delay, information loss, or a restricted set of available actions |
| Symmetry | A stated transformation under which specified quantities or laws remain unchanged |
| Toroidal motion | A specified periodic state space, trajectory, and relevant topological quantities |
| Recurrence across scales | Explicit variables and maps between models, with tests of what those maps preserve |

A loop drawn on a page does not establish torus topology. Two overlapping domains do not establish a vesica in a physical metric. Similar shapes across scales do not establish common dynamics or causation.

Even an exact change of coordinates preserves the observation sequence only when the observation is transported consistently. Redrawing a phase space and imposing new equal-width bins can change the question being measured. The Geometry Maximization work makes this distinction explicit.

## 6. Twin Timelines: equal history, different next step

The exact phase model uses

$$
\alpha=\frac{3-\sqrt5}{2},\qquad
\tau=15-39\alpha=\frac{39\sqrt5-87}{2}.
$$

For a reduced phase $0\le\rho_n<1$,

$$
\sigma_n=\mathbf1_{[0,\tau)}(\rho_n),\qquad
\rho_{n+1}=\{\rho_n-\tau\}.
$$

The interval is half-open: phase zero slips; phase τ does not. Twin Timelines selects two different starting phases whose first **39 slip observations agree**, while observation **40 differs**. The mathematical construction extends to every finite history length; the released implementation supports lengths through 1,024.

This is a constructed counterexample to exact prediction from a fixed finite slip history on the full phase circle. It demonstrates an information limitation, not physical branching, agency, or chaos. Once the exact phases are supplied, the next observations are computable. Practical prediction with finite precision still requires attention to observation boundaries.

The open demonstration and verification are recorded; no blind human trial result is claimed. Prime lengths in the rematch schedule are a presentation choice, not a requirement of the construction. The deterministic irrational rotation is not mixing under its uniform invariant measure, despite its recurring patterns. [Exact construction and count identity](MATHEMATICAL_NOTES.md); [recorded evidence](evidence/LOCAL_EVIDENCE.json).

## 7. Toroidal work: what has actually been checked

In the tested source-free periodic lattice model, a conserved integer current has signed winding W given by its oriented cut sums. Its parity sector is

$$
q=W\bmod2.
$$

Parity discards sign and magnitude. Equal q therefore does not mean equal W or equal full state. Even W alone need not be an autonomous state. Open-path wrap counts also require different treatment from the winding of a closed conserved current.

**Tiny-system validation:** at L=2 and the chosen engineering point $J=1,t=1/2,h_6=0$, the implementation passed its declared comparison with an independent Monte Carlo reference after a separately planned follow-up cohort. The initial reference was unresolved because a rare event had insufficient coverage. All 80,000 retained dual states passed conservation and signed-winding checks; 12 exact-conditional consistency checks passed. The global reference was numerical sampling, not an exact solution of the full partition function.

**Q2 pilot:** 48 chains at L=2, 3, and 4 produced 192,000 retained states over 65,040,000 attempted updates. Every chain visited all eight parity sectors. The sector diagnostics passed, but the signed-winding diagnostics did not pass at the larger sizes:

| L | Lowest signed-W effective sample size | Highest signed-W R-hat | Overall pilot screen |
|---|---:|---:|---|
| 2 | 2,344 | 1.00395 | PASS |
| 3 | 741 | 1.01551 | UNRESOLVED |
| 4 | 336 | 1.03469 | UNRESOLVED |

These are the worst diagnostics across the two initialization groups. The frozen screens require effective sample size at least 1,000 and R-hat below 1.01. Effective sample size estimates how much correlated sampling contributes to precision; R-hat checks agreement across chains. Passing either is a diagnostic result, not a convergence proof.

Zero invariant failures were found in the retained pilot states. **Physical Q2 remains UNRESOLVED.** Larger-size independent weighted-model validation and production mixing requirements remain outstanding. A proposed longer winding pilot has not been run as part of this revision. [Evidence and source identities](evidence/LOCAL_EVIDENCE.json).

The lesson for this hypothesis is specific: a coarse visible pattern can conceal a slower observable. The field sampler does not test whether social, biological, or conversational mediation creates stability.

## 8. Stability needs a definition and a test

Mediation and symmetry are insufficient by themselves. A symmetric O–R–S update with no direct O–S edge can diverge. Conversely, a direct two-state averaging update can preserve its mean while its disagreement shrinks to zero. Both examples are derived in [the mathematical notes](MATHEMATICAL_NOTES.md).

This revision therefore separates boundedness, recovery, accurate prediction, reversibility, mixing, and agency. They are not interchangeable forms of “coherence.” A mathematically invertible update need not provide a practical undo operation; a well-mixed sampler need not represent a desirable social system.

For a proposed R-layer, record several measures instead of one undefined balance score:

| Property | Example measurement |
|---|---|
| Predictive information | Cases with equal recorded states and unequal successors; held-out prediction error |
| Translation fidelity | Which input distinctions survive the transform, and which are lost |
| Capacity and timing | Throughput, delay, queue growth, and dropped messages |
| Recovery | Time and cumulative error after a specified disturbance |
| Correction and participation | Whether correction, refusal, replacement, and exit actually remain available |

“Pinch” becomes a family of candidate failure mechanisms. Reduced bandwidth, delayed feedback, erased state, and concentrated decision power require different measurements and may require different repairs. Restoring visual symmetry is not itself a demonstrated repair.

## 9. A testable next experiment

The next practical test is a controlled software or dynamical-model experiment in which the true state and desired output are known.

Compare three declared implementations: a direct connection; mediation preserving the task-relevant state; and mediation with a specified loss or delay. Give the direct and state-preserving variants the same usable information when testing the value of mediation itself. Compare preserved and erased context separately to test the effect of information loss. Charge memory, latency, and computation to every variant.

Choose workloads, disturbances, training data, held-out data, metrics, tolerances, and the run budget before inspecting the evaluation outcomes. Include tasks where mediation is expected to help and tasks where it adds overhead. Preserve raw observations separately from transformed views, and record an applied repair separately from its proposed diagnosis.

The prediction is that retaining a genuinely predictive distinction will reduce the corresponding ambiguity; whether it also improves recovery enough to justify its cost is an empirical question. If a direct design performs as well or better under the same conditions, the claim that mediation adds value is weakened for that application. If preserving the proposed context does not improve prediction, the proposed missing-state explanation needs revision.

Twin Timelines can serve as an exact information-loss benchmark. It cannot, by itself, show that adding a mediation layer improves a real application. **This comparative mediation experiment has not yet been run.**

## 10. Recursive Geometric Imbalance: an untested extension

The earlier companion hypothesis proposed a chain from chromosome fusion through molecular “pinching,” neural coordination, and social hierarchy. This revision retains that chain as an unanswered research idea, not as an explanation supported by the geometry calculations.

Human chromosome 2 has molecular evidence of an ancestral **telomere-to-telomere fusion**. That is the description used here in place of the draft's Robertsonian label. The unsourced narrow date range is removed. The fusion evidence does not establish a cone-shaped DNA overlap, an electromagnetic imbalance, or impaired cognition. [Ijdo et al., 1991, *Origin of human chromosome 2*](https://pubmed.ncbi.nlm.nih.gov/1924367/).

The fixed assignment of an analytical left hemisphere to O and a holistic right hemisphere to S is also removed. Functional lateralization exists, but a study of 1,011 people found local patterns of lateralization without the proposed whole-brain left-brained/right-brained network-strength phenotype. It does not support that simple role division. [Nielsen et al., 2013](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0071275).

To develop the biological branch, each proposed connection needs separate evidence: a defined structural variable at the locus; an independently supported effect on molecular function; a demonstrated link to a specific neural process; and, separately, a justified account of any social outcome. Similar language or shape cannot substitute for these links. The supplied work establishes none of that causal chain.

The proposed test target is therefore a specific, measurable mechanism. There is presently no basis here for claiming that human evolution introduced a geometric defect or that “restoring cylindrical symmetry” would correct biological or social instability.

## 11. Experience and design values

Conversational flow, shared authorship, curiosity, and reversible disagreement remain useful experiences to notice. They can be collected as participant reports alongside performance and recovery measures. Feeling coherent does not establish predictive accuracy or causal understanding.

Voluntary participation and freedom from coercion are design commitments in the core notes. A symbol such as “coercion = 0” expresses that commitment; it is not an observed numerical result without an operational measure. R should support interpretation and correction without acquiring unquestionable authority over the participants.

## 12. The Play Clause

> If the framework begins to feel inevitable, sacred, or correct, it has stopped functioning as a tool.

The framework remains a playable lens. A failed prediction, an effective direct connection, or a useful asymmetry should be allowed to change it.

Keep the loop open to inspection. Keep the return distinguishable from the display. Let the evidence decide where the geometry earns its place.

---

**Attribution and reuse:** The original draft's CC0 declaration is retained for this revised text: “Use freely, modify freely, break freely.” Linked publications retain their own attribution and terms.

**Revision record:** This version integrates the pasted draft, the notation in OMNIBUS CORE v5.57, Geometry Maximization v2.0, the completed tiny-system validation and Q2 pilot, and the public Twin Timelines construction. It adds no biological study or new Q2 production run. See [revision notes](REVISION_NOTES.md), [mathematical notes](MATHEMATICAL_NOTES.md), and [source manifest](SOURCES.json).
