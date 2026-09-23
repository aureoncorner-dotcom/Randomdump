# Review of the four additional documents

**Compared with TOROIDAL MASTER v0.1 on September 5, 2026**

The new files support a targeted mathematical addition to the master. They do not replace its newer curved-tube correction, modulo-six winding construction, or reference-sampler specification, and they supply no new executed field-simulation result. The acoustic design also contains dimensional conflicts that should be resolved before it is treated as a cutting plan.

The most useful mathematical improvement is a precise way to identify and measure information lost under a projection. A further calculation below proves that parity alone fails to close the **complete Villain FH-REF-1 kernel specified in the master**, extending the earlier elementary-move result. This is a proof about that declared transition law; its software implementation remains unwritten.

## 1. What each file contributes

| Supplied file | Contribution | Relationship to our master | Recommended treatment |
|---|---|---|---|
| TOROIDAL_GEOMETRY_HANDOFF_v1.0.md, September 3 | Clear separation of geometry, ensemble, quotient, update rule, clocks, and evidence; explicit Villain counterexample | Mostly corroborates corrections already incorporated September 5 | Retain as an earlier synthesis and source map |
| TOROIDAL_GEOMETRY_OMNIBUS_v1.1.md, September 3 | Extends the handoff with the witness-relative non-descent set, detailed coverage statuses, reported Drive validation templates, and provenance links | Useful additions in E.3–E.4, G.1–G.2, K.4–K.5; some mathematical wording needs correction | Import the corrected concepts below, not the whole older status register |
| monkey_myth_source_pass_memo_2026-09-04.md | Source distinctions and row-level publication recommendations for comparative mythology | Separate evidence domain; no equation or physical prediction added to the field model | Retain as a humanities source memo with its qualifications |
| Five_String_Acoustic_Resonator_Rev_A.docx, August 13 | Passive string-resonator concept, dimensions, parts, and measurement sequence | Separate mechanical/acoustic prototype; no specified mapping to the gauge model | Revise geometry and load calculations before fabrication |

The Omnibus was compared directly with the Handoff. Its principal additions are the witness-relative set, a more detailed status vocabulary, a typed D1 readout, reported zero-coverage scans, an eleven-artifact validation scaffold, and expanded source and lineage tables. These are chiefly definitions and reported project records, not new measurements.

Both geometry documents explicitly describe themselves as non-governing syntheses. Their embedded execution/adoption instructions are reviewed as historical document content. They do not revoke the user's authorization to review and improve this project, and their older `OPEN` labels do not undo corrections already incorporated in our master.

## 2. Corrections in the master that should be retained

| Topic | Additional documents | Existing master |
|---|---|---|
| Finite-source winding | Mod-two cut pairing proposed; integer volume-average winding correctly restricted | Also supplies the stronger current class modulo six, with its domain |
| Curved TTSC geometry | Requests a metric correction or straight/slender scope | Supplies an exact field for the declared circular-tube metric |
| Complete sampling rule | Older worm schedule remains unresolved | Specifies lazy random-scan FH-REF-1 and FULL-REF-1, with detailed balance and untruncated connectivity arguments |
| Reduced dynamics | Same-parity elementary-move counterexample | Also tests the insufficiency of `(q,W)` and gives a restricted sector-only `(q,S)` repair |
| Two clocks | Retains separate clocks and unlabelled-site period | Also derives relative phase, sampling aliases, and the distance-only counterexample |
| Audit storage | Extensive proposal receipts and inherited large inventory | Identifies the storage conflict and specifies a replay-based working design |
| Statistics | Rejects nonsignificance as agreement | Also addresses per-measurement reweighting, covariance, and incompatible fit-window requirements |

These differences reflect chronology and scope. None establishes production validation or a physical confinement/deconfinement verdict.

## 3. Repair the new non-descent geometry

### 3.1 Keep the witness-relative set

Omnibus E.3 defines a projection `pi: X -> Q` and a witness `w: X -> Y`, then asks which labels conceal different witness values:

$$N_w(\pi)=\{q\in\pi(X):\exists x,y\in\pi^{-1}(q),\ w(x)\ne w(y)\}.$$

This is useful and correct. On the attained label set `pi(X)`, the set is empty exactly when there is a unique set map `w_bar` such that

$$w=\bar w\circ\pi.$$

The proof is immediate: define `w_bar(q)` using any member of the fiber; it is well defined exactly when the witness is constant there. Restricting to `pi(X)` avoids irrelevant empty-fiber extension issues. This is a set-theoretic statement. Claims of continuous or measurable factorization require the corresponding additional assumptions.

For stochastic closure the witness is the **whole conditional distribution of the next projected state**, not one observed next state or one scalar average. For a countable full-state model and finite Q,

$$w(x)=\bigl(P_\pi(x,q')\bigr)_{q'\in Q},\qquad
P_\pi(x,q')=\sum_{z:\pi(z)=q'}P(x,z).$$

For a continuous full-state model use the kernel probability `P(x,pi^{-1}(B))` for measurable blocks B rather than summing individual points.

### 3.2 Correct the boundary and coverage claims

E.3 calls `Q minus N`, `N`, and `boundary(N)` a geometric partition and interprets the boundary as where a projection becomes inadequate. This is not justified as written.

First, no topology on Q is specified. With the natural **discrete topology on the eight parity labels**, every subset is open and closed, so its topological boundary is empty. More generally, those three sets are not a disjoint partition: the boundary can overlap N and its complement. If a topological partition is intended, use `interior(N)`, `boundary(N)`, and `interior(Q minus N)` after specifying the topology.

For a genuinely parameter-dependent study, define `N_lambda` for a declared family of kernels and put a topology on the parameter domain. A boundary in that domain then has a defined meaning. For a finite sector graph, an explicitly defined graph edge boundary is another option, but it is a different object and does not establish a physical bifurcation.

Second, the exact set `Q minus N` is not the set of fibers that happened to be covered by a scan. Separate mathematical truth from the evidence record:

* **Proved clean:** witness constancy proved or exhaustively checked on the declared fiber.
* **Located failure:** valid unequal-witness pair established.
* **Sample consistent:** tested observations meet a stated statistical rule.
* **Unknown or untested:** insufficient coverage or precision.

Zero observed failures in zero comparisons belongs to the last category. A finite noisy test cannot establish exact equality of continuous probability parameters merely because it accepts a nonzero equivalence margin.

### 3.3 Predicting one step is weaker than a closed replacement state

E.3's refinement principle needs an explicit distinction. The refinement

$$\pi'(x)=(\pi(x),w(x))$$

always preserves the chosen witness. In the category of set maps it is the coarsest refinement retaining both `pi` and `w`: any other such record determines this pair. It need not be a practical compression, and it does **not** automatically make `pi'` evolve autonomously.

A checked deterministic example uses six states:

| State | Original label pi | Next state U | Next original label w = pi composed with U | Refined label (pi,w) |
|---|---:|---|---:|---|
| x | 0 | u | 0 | (0,0) |
| y | 0 | v | 0 | (0,0) |
| u | 0 | a | 1 | (0,1) |
| v | 0 | b | 0 | (0,0) |
| a | 1 | a | 1 | (1,1) |
| b | 0 | b | 0 | (0,0) |

The refined record predicts the next **original** label exactly everywhere. Nevertheless x and y share refined label `(0,0)` while their next refined labels differ. The refined state is therefore not closed.

For finite deterministic systems, iteratively split blocks according to successor blocks until the partition stops changing. For finite Markov systems, split according to the vector of transition probabilities into the **current refined blocks**, repeating until stable. For infinite systems, neither finite termination nor a small sufficient state is guaranteed. Our master's restricted `(q,S_x,S_y,S_z)` result has the stronger property because its own update law was explicitly derived for the sector-only schedule.

## 4. A quantitative improvement and a stronger sampler result

### 4.1 Measure the amount of predictive information lost

For an attained fiber define its next-law diameter in total variation:

$$D_\pi(q)=\sup_{x,y\in\pi^{-1}(q)}
\frac12\sum_{q'\in Q}|P_\pi(x,q')-P_\pi(y,q')|.$$

Then `D_pi(q)=0` exactly when strong lumpability holds on that fiber. This turns the yes/no definition into a quantitative diagnostic while preserving the exact zero criterion.

For any single reduced prediction `K(q,.)`, the triangle inequality gives

$$\sup_{x\in\pi^{-1}(q)}
\operatorname{TV}(P_\pi(x,\cdot),K(q,\cdot))\ \ge\ \frac12D_\pi(q).$$

An observed or calculated pair supplies a lower bound on the diameter, not its full value. At `L=2, J=1`, the master's two elementary Villain states give toggle probabilities `0.3678794412` and `0.5033689735`. Their distance is `0.1354895323`; any one toggle prediction for both states must be wrong by at least `0.0677447662` for one of them. That is about **6.77 percentage points** for the conditional elementary move.

These are exact-law calculations evaluated numerically, not estimates from a run. Empirical diameter estimates need uncertainty and coverage controls; a small sampled diameter does not bound unobserved fibers without extra assumptions.

### 4.2 Make the Villain failure uniform in the parameters

The Handoff and Omnibus family `x_m` is particularly useful: `M=0`, `I=2m Gamma_alpha`, `q=0`, with `a=L/(2J)>0`. Compare `m=1` with `m=2` rather than relying on one zero-current pair at every parameter:

$$p_1=\frac{1+e^{-5a}}2,\qquad p_2=\frac{1+e^{-9a}}2,$$

$$p_1-p_2=\frac12 e^{-5a}(1-e^{-4a})>0.$$

Thus elementary parity-only closure fails for every finite positive J and L in the stated geometry. This strengthens the explicit argument without claiming that every individual pair must differ at every coupling.

### 4.3 Extend the result to the complete FH-REF-1 kernel

In master §7, a sector proposal occurs with probability `1/4`, then chooses an axis with probability `1/3`. Local plaquette proposals and the idle case cannot change q. Therefore, for a given axis,

$$P_{\mathrm{FH}}(q\oplus e_\alpha\mid x)=\frac1{12}p_\alpha(x).$$

For the `x_1,x_2` pair,

$$P_{\mathrm{FH}}(e_\alpha\mid x_1)
-P_{\mathrm{FH}}(e_\alpha\mid x_2)
=\frac1{24}e^{-5a}(1-e^{-4a})>0.$$

**Consequently the complete Villain FH-REF-1 random-scan kernel is not strongly lumpable through q**, for finite `L>=2`, `J>0`, `0<t<1`, `h6=0`, and untruncated currents. Its target invariance and full-state connectivity are compatible with this result. Sampling correctly does not require the observed parity process to be Markov.

For the master's `x_0,x_1` pair at `L=2,J=1`, the other canonical cycles share no links with the changed cycle. Their transition probabilities are unchanged. The complete-kernel total-variation distance for this pair is therefore `0.1354895323/12 = 0.0112907944`, yielding a worst-case one-law approximation error of at least `0.0056453972` on this pair, about **0.565 percentage points per attempted step**.

This result applies to the specified Villain reference mixture. It does not retrospectively resolve the older worm macro-schedule, and it does not claim a software test or extend the calculation automatically to cosine weights. In FULL-REF-1, q is fixed at zero, so its constant projection closes trivially and carries no eight-sector dynamics.

## 5. Acoustic resonator findings

The Word file has a useful experimental intent: characterize ordinary string, frame, vessel, and room responses, and distinguish those measurements from cultural analogy. However, its subtitle says build-ready while the body correctly calls the design provisional. The following conflicts make **provisional concept pending dimension and load verification** the accurate status.

### 5.1 Anchor bar dimensions do not fit the holes

Section 3, P3 specifies an eight-inch bar with five holes at two-inch centers. The first-to-last hole-center span is

$$b=(5-1)(2\ \mathrm{in})=8\ \mathrm{in}.$$

The end-hole centers would lie at the bar ends. A valid dimension rule is

$$L_{\rm bar}\ge (N-1)s+2e,$$

where e is the required center-to-end allowance determined from the actual holes, material, loading, and connection design. A ten-inch bar gives one-inch center-to-end allowances arithmetically; that example is **not** a certified bar design. Enlarging the bar also changes its fit inside the vessel.

### 5.2 Nominal vessel clearance is not sufficient

The parts permit a three-inch-deep centered spine and a three-inch gap from its front face to the string plane. At two-inch string spacing the outer strings are four inches sideways from center. In that permitted configuration their radius from the vessel axis is

$$r_{\rm outer}=\sqrt{4^2+(3/2+3)^2}=6.0208\ \mathrm{in}.$$

Including the stated one-inch wall clearance requires a clear diameter of at least `14.0416 in`, even before hardware size and string motion. Thus a twelve-inch clear diameter does not satisfy every combination of the allowed dimensions.

This is a counterexample to the blanket fit criterion, not a claim that every possible arrangement fails. Record the actual spine orientation, string-plane offset, and string coordinates. Check the vessel's interior profile **at every occupied height**, including its narrower mouth. Specify whether strings pass through the vessel interior or outside it; the current schematic is not a dimensioned section and does not resolve that routing.

### 5.3 Add the actual tension and frame calculations

For an ideal flexible string at small transverse amplitude,

$$f_1=\frac1{2L}\sqrt{T/\mu},\qquad T=4\mu L^2f_1^2.$$

Here L is speaking length, mu is mass per length, and T is tension in consistent units. Doubling pitch at fixed length and string multiplies tension by four. At `L=0.8128 m` and `T=20 lbf = 88.9644 N`, a 110 Hz fundamental corresponds to `mu=2.7823 g/m`. This is an illustrative ideal-string calculation; the actual manufacturer data and allowable loads determine the selected string. [UNSW string physics](https://newt.phys.unsw.edu.au/jw/strings.html).

The separated string plane also produces eccentric frame loading. For approximately parallel strings, a frame section can carry axial force `P=sum T_i` and bending moment `M=sum T_i e_i`, where each e_i is measured from the relevant structural reference axis. Use actual stock dimensions, connection geometry, bar bending, bearing, joint loads, and appropriate stability calculations. The total string force alone does not certify the spine. [Baker and Haynes, statically equivalent force and moment systems](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics%3A_Open_and_Interactive_%28Baker_and_Haynes%29/04%3A_Moments_and_Static_Equivalence/4.07%3A_Statically_Equivalent_Systems).

The document's 200 lbf restraint rating and general fourfold factor cannot be reconciled by simply comparing the strap rating with total string tension. Anti-tip loading is a separate moment problem involving mass, center of gravity, attachment height, strap angle, and possible slack. Also distinguish working-load ratings from breaking strengths before applying a factor. No actual hardware ratings or structural capacity calculation were supplied.

### 5.4 Use the actual support polygon for tipping

Four equally spaced idealized point feet on a circle of diameter D form a square support polygon. Its least-direction distance from center to an edge is

$$r_{\rm support}=D/(2\sqrt2),$$

not D/2 and not the eight-inch radius of the base board. For a centered center of gravity at height h, with no strap contribution, no sliding, and a rigid assembly, static stability at tilt angle theta requires

$$h\tan\theta<r_{\rm support}.$$

For the specified 13–14 inch foot circle and ten degrees, the corresponding h limits are about 26.07–28.07 inches. Actual foot contact patches, placement, compliance, center-of-gravity offset, and restraint engagement change this calculation. It is a screening model, not certification or an instruction to physically tilt an unverified assembly. Center-of-gravity and support moments are the relevant statics quantities. [Baker and Haynes, center of gravity](https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Engineering_Statics%3A_Open_and_Interactive_%28Baker_and_Haynes%29/07%3A_Centroids_and_Centers_of_Gravity/7.02%3A_Center_of_Gravity).

### 5.5 Make the acoustic measurements interpretable

T3–T5 are useful starting tests, but successive unmeasured plucks and a contact sensor moved between surfaces do not identify a calibrated coupling matrix. Sensor mounting, automatic gain control, excitation amplitude, and position can change the recorded amplitudes.

Use fixed sensor positions or a calibrated remounting procedure, retain a reference response or measured excitation, and record the frequency dependence. With measured force F and output Y, the transfer response is `H(f)=Y(f)/F(f)`. Without an input measurement, label the result as a response ratio under the recorded setup rather than a force-to-response transfer function. Include repeated measurements and separate frame, vessel, top-plate, and room contributions with defined controls.

For one lightly damped isolated mode with amplitude envelope

$$A(t)=A_0e^{-\pi f_0t/Q},$$

the ten-decibel amplitude-decay time obeys

$$Q=\frac{2\pi f_0t_{10}}{\ln 10}\approx2.72875f_0t_{10}.$$

This gives the existing decay-time measurement a model-based interpretation. Beats between modes, changing excitation, clipping, sensor gain changes, or the noise floor invalidate a single-exponential fit. No ringdown, measured spectrum, completed commissioning sheet, or structural test result accompanied this design.

An open vessel and a vibrating string frame are not automatically an experimental realization of the master's three-torus lattice or its prescribed TTSC flow. Such a comparison needs a declared mapping from measured quantities to a prediction of the model.

## 6. Mythology memo and source verification

The memo's main improvement is evidential precision: it separates passages and artifacts from interpretations concerning sovereignty, gender, conquest, and ritual. It explicitly distinguishes cultural design language from physical mechanism. Nothing in the memo establishes toroidal field dynamics or acoustic performance.

A targeted primary-source spot check confirmed that Florentine Codex Book 3, folio 3r contains Coyolxauhqui's decapitation and bodily fragmentation. This supports the memo's correction of the passage location. It does not by itself support every later solar/lunar or political interpretation. [Digital Florentine Codex, Book 3, folio 3r](https://florentinecodex.getty.edu/book/3/folio/3r).

The Viking Society's edition page confirms the cited Anthony Faulkes 2005 edition and second-edition metadata; that catalog page alone does not verify every passage-level Ymir claim. [Viking Society edition record](https://vsnr.org/editions/snorri-sturluson-edda-prologue-and-gylfaginning/).

Other cited destinations yielded limited content or could not be fully retrieved in this pass. I have therefore **not independently certified all eight row decisions**, all translation pins, or the memo's claim that the live workbook was edited. Those are reported claims in the supplied memo. The underlying spreadsheet revision, row-level changes, and complete source excerpts would be the evidence needed for a full workbook audit.

Keep “source supports the narrow motif” distinct from “the motif supports the matrix's broader interpretation.” Repeated motifs also require a specified corpus, comparison criteria, negative cases, and treatment of related textual traditions before being used for a statistical generalization.

## 7. What the Drive references do and do not establish

The Omnibus reports finding eleven A.10 templates, zero eligible D1 comparison pairs, and no populated successor reports during its September 3 search. These are dated claims inside a supplied local document. This review did not inspect the user's live Drive or rerun that search, so they should be recorded as **reported as of September 3**, not as a current exhaustive inventory.

The most useful next files for testing whether evidence has changed are:

* A populated A10-03 transition specification and A10-08 balance/reachability report with the code and run settings they reference.
* A populated A10-05 or A10-07 result with raw quantities, definitions, uncertainties, and truncation information.
* For D1, actual ordered full-state present/successor records, with the update rule, eligibility, resets, and the proposed reduced state.
* For the resonator, actual dimensions, selected-string data, and recorded spectra or decay traces tied to a configuration.

The scaffold's required full enumeration at L=2,3 and its large production inventory should remain feasibility questions. A checklist entry is not evidence that the computation is practical. Our master's smaller validation-first approach remains appropriate.

## 8. Recommended master change

Retain MASTER v0.1 as the baseline. The material in §§3–4 of this review is a concrete candidate addition to its closure section:

1. Add the corrected witness-relative set on attained labels.
2. Separate proof status, sampled coverage, and topological/parameter boundaries.
3. Distinguish one-step witness retention from closed-state refinement.
4. Add the total-variation diameter and its unavoidable-error bound.
5. Record parity non-descent for the complete **Villain FH-REF-1** law, while leaving the older worm schedule and actual software validation separate.

Keep the acoustic corrections in a resonator revision and the mythology memo in its own source record. This review supplies the calculations and proposed wording; it does not silently replace the existing master, alter the four inputs, update Drive, or label any physical experiment as completed.

## 9. Verification and review limits

All three Markdown texts were read and the two geometry versions compared. The Word file's 250 paragraphs, six tables, and one embedded schematic were extracted and reviewed. It contains no native Word math objects. The schematic was visually inspected; the Word page layout was not rendered or certified, and no edited Word document is delivered.

Fifteen focused diagnostics passed, including checks deliberately reproducing the refinement failure and dimensional conflicts. They cover finite examples, the numerical evaluation of derived formulas, and source integrity. They are **not** fifteen successful field or hardware tests. The derivations specify their domains separately from the numerical examples.

The four original files were rechecked by SHA-256 and remain unchanged. Input identities and diagnostic outputs are retained in [the check record](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_New_Files_Checks_2026-09-05.json>). The comparison baseline remains [TOROIDAL MASTER v0.1](<C:/Users/drewd/Documents/Codex/2026-09-05/com/outputs/TOROIDAL_MASTER_v0.1.md>).
