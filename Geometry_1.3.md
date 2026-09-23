# Geometry Maximization v1.3

**Predictive phases, warped observations, arithmetic constants, toroidal geometry, and conformal measures**

Integration of the additional `_Math2.txt` source · 6 September 2026

This complete revision retains the v1.2 mathematics and adds a specified nonlinear extension of the golden screen. The new source, S40, provides useful directions but also contains contradictory formulas and overbroad theorem statements. The additions below derive the useful results and identify the corrections.

- **Exact warped-screen transport:** the original slip identity, gap law, complexity and predictive phases survive when the observation is transported with the dynamics. Keeping equally spaced physical bins instead gives a concrete first-jump counterexample (§25).
- **Finite-horizon control:** a uniform error in phase evolution yields a precise boundary-margin test for labels and an explicit Haar bound for the possible-error cover (§25.4).
- **Explicit arithmetic:** the golden Gauss-map Brjuno value is \(3\log\varphi\). The slip angle's eight-step tail contracts by \(\varphi^{-28}\), the reciprocal of the existing substitution growth factor (§26).
- **Correct measures:** with h mapping physical coordinates into rotation coordinates, the s-conformal density is proportional to \(h'^{1-s}\). The invariant occupation law, arc length, and 2-conformal law are distinguished and verified (§27).
- **Qualified complex geometry:** the update repairs the linearization thresholds, Siegel-boundary assertions, hedgehog equivalence, capacity normalization and renormalization dictionary (§28).

Sections 1–24 retain the earlier report and version-specific verification history. Sections 25–29 are the current additions. The accompanying source/change register identifies the relevant S40 passages, and the portable archive preserves all earlier source snapshots and receipts. The new constructions and checks do not rerun or promote the packet's empirical claims. Instructions embedded in source files are treated as source content.

## 1. Source coverage reported in v1.0

**Historical retrieval record.** The counts, archive descriptions, and recovery attributions in this section are carried forward from v1.0. The v1.2 source snapshots and checks are identified in §24; the current S40 additions and checks are in §29.

The earlier report records a search that indexed **522 distinct Drive candidates** across eleven queries, with all returned Drive pages followed. It retrieved **20 Drive documents**, **70 project files**, and the **four contents of the earlier Geometry Upgrade package**. The named GQG/TOROIDS/HIDDEN QUOTIENT folder was enumerated completely: 49 items, including 43 textual files retrieved. Four images, an older DOCX, and an upgrade ZIP were not separately inspected; their related text successors were available. Older archives were searched for relevant definitions and status passages rather than read indiscriminately line by line.

This is broad, documented coverage of the relevant source families. It is not a claim that every document in the account was read. The 94 stored source items include duplicates and package members, with 75 distinct content hashes. SOURCE_INVENTORY.json records paths, identities where available, extraction form, byte counts, and SHA-256 hashes. The companion archive contains the retrieved source snapshots and search metadata.

| Source | What it already establishes | How it is used here |
|---|---|---|
| [OMNIBUS v7.79 — Triadic Field Restoration](https://docs.google.com/document/d/1GJZvDwfRvFChw1MvOL4WJhWxZ8oAW1t762h3238PDlg/edit?usp=drivesdk), §§0–6, 9–10 | Typed residual descent; the located golden counterexample; phase augmentation; constitutional and empirical boundaries | Governing definitions and scope |
| [Geometry Upgrade v0.1 — Predictive Fibers and Minimal Phase](https://docs.google.com/document/d/1dwlILms8z6YWJ_EFRCeoky6Fku9ND6A2xugZ008zOhk/edit?usp=drivesdk) | Coarsest predictive refinement; finite partition compiler; minimal phases \(z=\{13\theta\}\), \(\rho=\{39\theta\}\); finite-state impossibility; exact slip-count discrepancy | Recovered proofs, independently reproduced |
| [New geometry](https://docs.google.com/document/d/1DVgC8ia4Z1suHmLbcrDbvw1ETuSjkTm25_5DH8OOQNI/edit?usp=drivesdk), §§13–14 | Witness-relative non-descent; no-shape lemma; canonical witness retention; qualified openness, diameter, and differential results | The actual geometric framework |
| [TOROIDAL_MASTER_v0.2.md](https://drive.google.com/file/d/1103tr4UUEIbyLYUxfE1zaCyn_E6MyAxW/view?usp=drivesdk), §§6–7 | Strong lumpability; elementary and complete FH-REF-1 failures; restricted repair; total-variation error bound | Full stochastic update, not merely a realized trace |
| [Qualified Hidden Quotient v1.7](https://drive.google.com/file/d/1VF_UeW26X5LYpMYpfEtYvry8PjGX77Bj/view?usp=drivesdk) | Locally null kernel; semifinite reduction; qualified Radon–Nikodym theorem; worked point-witness restoration | Keeps visibility, completion, and dynamic closure distinct |
| [GQG card](https://docs.google.com/document/d/1Mrm8KAaUsh5e2izR9K4VZqNKEn5enEFshnskHuBznGg/edit?usp=drivesdk), plus the v0.13 project branches | Named equivalences and typed relations; orbit quotient and residual cocycle discipline | Algebraic integration |
| [Consolidated Findings and Continuity Record v1.1](https://docs.google.com/document/d/1eBLXncFF2ByQnAkMKjWdMjj0hdQ2brESau9ptv-cl50/edit?usp=drivesdk) | Completed work, successor integration, and remaining gaps | Prevents completed findings from being reopened or erased |
| R4A_GOLDEN_DRAIN_39_SCREEN_RUN_2026-08-25.md | Original departure-jump convention; finite trace receipts | Exact alignment and count reproduction |

Three version distinctions matter. The live v7.79 includes its constitutional carry-forward section; the earlier Markdown snapshot is shorter. The numbered GQG v0.13 and OMNIBUS v7.78 files contain material absent from their unnumbered counterparts. The qualified-RN Hidden Quotient branch and the orbit/cocycle branch carry complementary repairs. A matching version number does not make two files identical.

The v1.0 report states that the prior Geometry Upgrade verifier was recovered from its package and rerun unchanged, with parsed output matching the archived receipt. Its attribution of the minimal phases, predictive refinement, finite-memory obstruction, and count bound to that existing companion is retained. That historical reproduction is separate from the new verification in §17.

## 2. Descent with the domain made explicit

Fix a forward-invariant declared set \(D\), a total update \(U:D\to D\), and the typed observation
\[
R(x)=\rho(x,Ux)=(\Delta C,\Delta D,\Delta K).
\]
Only the actual image \(\mathcal R=R(D)\) is needed. Then
\[
\boxed{\exists!\,\overline U_R:\mathcal R\to\mathcal R,\quad
\overline U_R\circ R=R\circ U}
\]
if and only if
\[
R(x)=R(y)\Longrightarrow R(Ux)=R(Uy)
\qquad(x,y\in D).
\]

The proof is the representative-independence test: define \(\overline U_R(R(x))=R(Ux)\); equality on every fiber makes that definition independent of \(x\). Conversely, any such map forces the implication.

Two qualifications make the operational test rigorous.

1. **Eligibility must cover the identifications claimed.** Checking an arbitrary subset of same-label pairs proves compatibility only on those pairs. To claim a map on all of \(R(D)\), cover every required fiber comparison, or prove that the checked comparisons generate the full fiber relation. If eligibility defines a smaller state domain, declare that domain and its update.
2. **A finite trace is usually a partial transition record.** Agreement among its repeated labels does not prove agreement among unobserved representatives. An unobserved successor is not a self-loop. A trace can prove failure with one valid pair; universal closure needs full coverage or a proof.

These are refinements of the card’s coverage requirement, not new empirical conditions invented after seeing an answer.

The channels remain typed. Subtraction is available only where the channel supports it; otherwise a declared comparison map supplies the difference. UNKNOWN is neither zero nor a negative observation. Approximate equality also needs care: \(|x-y|<\varepsilon\) is generally not transitive, so it does not define an equivalence relation. Fixed bins, a declared partition, or another genuine equivalence must precede quotient language.

A constant observation always closes, but it may discard every output the application needs. Conversely, adding one coordinate can repair the next original output while leaving the enlarged state unclosed. The output obligations must therefore be fixed before asking for a minimal repair.

## 3. The predictive quotient is the exact repair target

**Recovered result: Geometry Upgrade v0.1.**

Let \(B:D\to A\) be the observation that must remain available. It may be the residual tuple, or a combined record \(B=(\pi,W)\). Define
\[
\Pi_h(x)=(B(x),B(Ux),\ldots,B(U^h x))
\]
and
\[
x\equiv_\infty y
\iff B(U^k x)=B(U^k y)\quad\text{for all }k\ge0.
\]
The image
\[
Q_\infty=\{(B(U^k x))_{k\ge0}:x\in D\}
\]
has an autonomous left shift. It is the **coarsest closed refinement retaining \(B\)**.

Indeed, suppose \(p:D\to Z\) is surjective, \(B=b\circ p\), and \(pU=Vp\). Then
\[
\Pi_\infty(x)=H(p(x)),\qquad
H(z)=(b(V^kz))_{k\ge0}.
\]
Every exact autonomous description retaining \(B\) must distinguish every pair distinguished by the future observation sequence.

This future sequence specifies an equivalence; it does not authorize future outcomes as predictor inputs. A usable implementation must realize it through currently available coordinates.

For \(E_h=\operatorname{Eq}(\Pi_h)\),
\[
E_{h+1}=E_h\cap(U\times U)^{-1}(E_h).
\]
If \(E_{h+1}=E_h\) on the full declared domain, that partition is closed and already equals \(E_\infty\). On a complete finite domain of \(N\) states with \(k_0\) initial classes, there can be at most \(N-k_0\) strict refinements.

This also shows precisely what a finite-history test misses: agreement through horizon \(h\) says nothing about a split first appearing at \(h+1\).

### 3.1 A direct bridge to linear observability

**Deduction carried forward from v1.0.** For \(x_{n+1}=Ax_n\) and \(B(x)=Cx\), the invisible differences after all future observations form
\[
K_\infty=\bigcap_{k\ge0}\ker(CA^k).
\]
It is the largest \(A\)-invariant subspace contained in \(\ker C\). In an \(n\)-dimensional vector space, Cayley–Hamilton reduces the intersection to \(k=0,\ldots,n-1\). The predictive state is the quotient by that unobservable subspace.

Thus the abstract quotient compiler has a familiar exact linear realization. With multiple allowed updates \(U_a\), closure must hold under every declared input; the future equivalence then ranges over all permitted input words, not one selected trajectory.

### 3.2 The operator form

Let \(\mathcal A_B\) be all scalar functions constant on \(B\)-fibers, and let \(Kf=f\circ U\). Descent through \(B\) is equivalent to
\[
K\mathcal A_B\subseteq\mathcal A_B.
\]
If descent holds, a fiber-constant function stays fiber-constant after updating. Conversely, indicators of output labels separate different next outputs.

The predictive construction closes the observation algebra under repeated pullback by \(U\). This is a useful bridge to the Hidden Quotient’s representation language. It is a statement about invariant information. If \(B\) is discontinuous, its observation algebra must not silently be treated as a subalgebra of continuous functions on the circle.

## 4. The 39-screen, reduced exactly

Use the source’s departing jump and half-open bins:
\[
\alpha=\frac{3-\sqrt5}{2},\qquad
\theta_{n+1}=\{\theta_n+\alpha\},
\]
\[
b_n=\lfloor39\theta_n\rfloor,\quad
j_n=(b_{n+1}-b_n)\bmod39,\quad
s_n=b_n\bmod3,\quad
\sigma_n=15-j_n.
\]
Set
\[
\beta=39\alpha-14,\qquad
\tau=1-\beta=15-39\alpha,\qquad
\gamma=\{13\alpha\}=1-\frac{\tau}{3}.
\]

| Constant | Value |
|---|---:|
| \(\alpha\) | \(0.381966011250105\ldots\) |
| \(\beta\) | \(0.896674438754101\ldots\) |
| \(\tau\) | \(0.103325561245899\ldots\) |
| \(\gamma\) | \(0.965558146251367\ldots\) |

Here \(\rho=\{39\theta\}\) denotes the earlier companion’s within-bin phase. It is a different use of the letter from the two-argument typed difference \(\rho(x,Ux)\); a consolidated document should qualify these namespaces.

Writing \(39\theta=b+\rho\) gives
\[
j=14+\lfloor\rho+\beta\rfloor,\qquad
\sigma=\mathbf1_{[0,\tau)}(\rho),
\]
\[
\boxed{\rho'=\{\rho-\tau\}=\rho-\tau+\sigma,\qquad
s'=s-\sigma\pmod3.}
\]
For the joint observation, use
\[
z=\{13\theta\}=\frac{s+\rho}{3},\qquad
\boxed{z'=\{z-\tau/3\}.}
\]
Then \(s=\lfloor3z\rfloor\) and \(\sigma=\mathbf1_{[0,\tau)}(\{3z\})\).

### 4.1 The actual minimal factor tower

**Recovered result, with the factor distinction emphasized.**

| Required future observations | Coarsest predictive phase on the full circle | Number of original phase lifts | Finite-state? |
|---|---|---:|---|
| Full bin \(b\) | \(\theta\) | 1 | No |
| Strand/slip pair \((s,\sigma)\) | \(z=\{13\theta\}\) | 13 | No |
| Slip \(\sigma\) alone | \(\rho=\{39\theta\}\) | 39 | No |

The maps \(\theta\mapsto z\mapsto\rho=\{3z\}\) are continuous circle covering maps. They intertwine the corresponding rotations. They are genuine nontrivial continuous factors.

Minimality follows from density. Two distinct reduced phases differ by a nonzero translation. The labeled interval partition has no such translation symmetry, so there is an open set on which their labels differ. The irrational orbit eventually reaches it.

These are reductions of retained distinctions, not reductions to 13 or 39 states. On the single golden orbit \(\theta_n=\{n\alpha\}\), each reduced phase still distinguishes every indexed time: equality would require a nonzero integer multiple of irrational \(\alpha\) to be integral.

Adding clock origins, resets, provenance, or other required outputs can refine this minimal factor. Minimality is always relative to the fixed output obligations.

### 4.2 Exact frequency and a stronger result than Denjoy–Koksma

The pasted frequency calculation reverses the two probabilities. The correct values are
\[
\boxed{\lambda(\sigma=1)=\tau\approx10.332556\%,\qquad
\lambda(\sigma=0)=\beta\approx89.667444\%.}
\]
Most departing jumps are \(15\), not \(14\).

More strongly, rearranging the phase update yields the exact real coboundary
\[
\boxed{\sigma-\tau=\rho\circ T-\rho.}
\]
For every start, every starting index \(n\), and every block length \(N\),
\[
S_{n,N}:=\sum_{k=n}^{n+N-1}\sigma_k
=N\tau+\rho_{n+N}-\rho_n,
\]
\[
\boxed{|S_{n,N}-N\tau|<1.}
\]
Thus \(S_{n,N}\) is either \(\lfloor N\tau\rfloor\) or \(\lceil N\tau\rceil\). At the source origin \(\theta_0=0\),
\[
S_{0,N}=\lceil N\tau\rceil.
\]

| Departures counted from \(n=0\) | Exact slips |
|---:|---:|
| 39 | 5 |
| 507 | 53 |
| 10,000 | 1,034 |

These reproduce the original screen receipts. The all-\(N\) bound was already proved in Geometry Upgrade v0.1; it does not depend on a general assertion that every BV observable has bounded discrepancy.

The same carry calculation works for other irrational rotations and fixed equal-width screens. The special feature here is the observable’s endpoint-difference identity, not merely the golden continued fraction.

## 5. The exact statistics reveal the missing information

**Deductions and complete finite-partition calculations carried forward from v1.0.**

### 5.1 Return gaps and run lengths

For \(0\le\rho<1\),
\[
S_{0,N}(\rho)=\lceil N\tau-\rho\rceil.
\]
The \(k\)-th future slip occurs at departure
\[
t_k=\left\lfloor\frac{k-1+\rho}{\tau}\right\rfloor.
\]
Successive gaps are therefore either \(\lfloor1/\tau\rfloor=9\) or \(\lceil1/\tau\rceil=10\). The intervening zero runs have length 8 or 9.

Since
\[
\frac1\tau=\frac{29+13\sqrt5}{6}=9.678147284582878\ldots,
\]
the asymptotic proportions **among complete slip-to-slip gaps** are
\[
P(\text{gap }9)=10-\frac1\tau
=0.321852715417122\ldots,
\]
\[
P(\text{gap }10)=\frac1\tau-9
=0.678147284582878\ldots.
\]
The 10,000-departure receipt has 333 gaps of length 9 and 700 of length 10. There are 1,033 complete gaps between its 1,034 slips.

### 5.2 Strand and slip are independent at one time

Under Haar phase, \(z\) is uniform and the decomposition \(z=(s+\rho)/3\) gives
\[
P(s=a)=\frac13,\qquad
P(s=a,\sigma=1)=\frac{\tau}{3},\qquad
P(s=a,\sigma=0)=\frac{1-\tau}{3}.
\]
Every starting phase has these limiting occupations. The strand distribution is uniform; it is not inferred merely from an informal drift argument.

This independence concerns the two coordinates at the same time. Their evolution remains coupled by \(s'=s-\sigma\).

### 5.3 A one-step probability kernel exists; the process is not Markov

The exact two-symbol probabilities are
\[
P(00)=1-2\tau,\quad P(01)=P(10)=\tau,\quad P(11)=0.
\]
Consequently the stationary conditional probabilities define a perfectly valid kernel:
\[
K=
\begin{pmatrix}
\dfrac{1-2\tau}{1-\tau}&\dfrac{\tau}{1-\tau}\\[4pt]
1&0
\end{pmatrix}
\approx
\begin{pmatrix}
0.884768031&0.115231969\\
1&0
\end{pmatrix}.
\]

This corrects the phrase “failed as a Markov kernel.” The conditional kernel exists. What fails is the claim that it generates the actual process.

The exact sequence forbids \(101\), because slips are at least nine steps apart. The stationary first-order Markov chain using \(K\) predicts instead
\[
P_K(101)=\tau\frac{\tau}{1-\tau}
=0.011906407883796\ldots>0.
\]
It gets the one-step table right and the three-symbol law wrong. This is an explicit, quantitative obstruction to memoryless stochastic replacement.

The same issue survives adding the current strand. Given \((s,0)\), the next strand is fixed but the next slip is ambiguous. Given \((s,1)\), the next pair is exactly \((s-1,0)\).

### 5.4 The non-descent locus is completely located

For current slip labels and current pair labels, respectively,
\[
\boxed{\mathcal N_{\mathrm{next}\,\sigma}=\{0\},}
\]
\[
\boxed{\mathcal N_{\mathrm{next}\,(s,\sigma)}
=\{(0,0),(1,0),(2,0)\}.}
\]
These are exact full-circle statements, not just locations found in a finite scan.

For example, \(\sigma=0\) means \(\rho\in[\tau,1)\). On \([\tau,2\tau)\), the next slip is 1; on \([2\tau,1)\), it is 0. Both subintervals have positive length. By contrast, \(\rho\in[0,\tau)\) always produces next slip 0.

On each bad fiber, the two exact next laws are different point masses, at total-variation distance 1. Any single probabilistic prediction assigned to that whole fiber has worst-case error at least \(1/2\). The equal mixture attains that minimax value.

Under Haar weighting, the best deterministic predictor using only the current bit—or current strand/bit pair—predicts next slip 0 and has error exactly \(\tau\). Average prediction error and worst-case closure are different quantities.

### 5.5 Correlations are available exactly

For any integer lag \(k\), interval overlap gives
\[
P(\sigma_0=1,\sigma_k=1)
=\max\{0,\tau-\|k\tau\|\},
\]
\[
\operatorname{Cov}(\sigma_0,\sigma_k)
=\max\{0,\tau-\|k\tau\|\}-\tau^2.
\]
Here \(\|u\|\) is circle distance to an integer. Along arbitrarily good returns, \(\|k\tau\|\to0\), so the covariance returns toward \(\tau(1-\tau)\), not toward zero. This explicitly exhibits the nonmixing behavior of the observable.

## 6. Infinite predictive state with only linear word growth

**The finite-state obstruction, slip/pair complexity, and branching calculation are carried forward from v1.0. The additions below are labelled v1.1.**

A deterministic autonomous machine with finitely many states eventually repeats a state. Its subsequent output is periodic, so every limiting symbol frequency is rational. The slip frequency \(\tau\) is irrational. Therefore no such machine generates the entire slip sequence from any starting phase.

This rules out every fixed-length history of a finite alphabet as an exact autonomous state. An explicit unbounded time index, an infinite history, or exact phase is a different state space.

There is a sharper account of how prediction keeps gaining distinctions. A length-\(m\) slip word changes only at
\[
\{0,\tau,2\tau,\ldots,m\tau\}\pmod1.
\]
These are \(m+1\) distinct cuts. They divide the reduced phase circle into \(m+1\) half-open intervals.

Different intervals have different words. To see this, the first \(k\) partial sums are \(\lceil k\tau-\rho\rceil\); each cut \(\{k\tau\}\) changes the corresponding partial sum. A word determines all its partial sums, so two cells separated by one of these thresholds cannot have identical words.

Thus, for word lengths \(m\ge1\), the exact language complexities are
\[
\boxed{p_\sigma(m)=m+1,\qquad
p_{(s,\sigma)}(m)=3(m+1).}
\]
For pairs, the initial strand has three choices, and the slip word determines all later strands.

Every word has at least one right extension. Since a binary word has at most two, the difference \(p_\sigma(m+1)-p_\sigma(m)=1\) means **exactly one length-\(m\) slip word has two possible next symbols**. All other length-\(m\) words have one. The pair coding has the three corresponding strand copies.

This is a particularly sharp geometry of failed finite memory: one unresolved branch survives at every horizon. Its cylinder has positive length, although its measure can become small.

The coding is Sturmian. That label is appropriate for this specific interval partition and rotation; an arbitrary two-interval partition of an arbitrary irrational rotation is not automatically a Sturmian coding. The standard symbolic terminology and compact extension are discussed in [Petersen’s Sturmian notes](https://petersen.web.unc.edu/wp-content/uploads/sites/17054/2018/04/QMSturmianJune2009.pdf).

The logarithmic growth of \(\log p(m)\) also gives entropy rate zero. Yet the unique branching word at every finite length has positive probability, so finite-history conditional entropy is positive at every finite order. An exact finite-order Markov representation would equate entropy rate with one of those positive conditional entropies. Therefore this stationary process is not Markov of any finite order.

The distinction is useful: **finite alphabet does not mean finite state**, and low complexity does not mean finite memory.

### 6.1 A compact topological realization

Take the closure of all bi-infinite slip itineraries in \(\{0,1\}^{\mathbb Z}\), with its product topology. The shift is a homeomorphism of that compact symbolic space.

For this Sturmian system, there is a continuous factor map from the symbolic space to the reduced phase rotation. It is one-to-one away from the countable orbit of partition boundaries and has the two limiting codings over those boundary phases. The coding map in the opposite direction, with a fixed half-open convention, is discontinuous.

This supplies a compact topological model with explicit symbolic observations. It does not supply a finite-state residual engine. The direction of the continuous factor map matters.

### 6.2 Mechanical words: fix the intercept before constructing prefixes

**v1.1 integration: the symbolic viewpoint from the supplied notes, with its conventions corrected.**

The departing-slip sequence at initial phase \(\rho\in[0,1)\) is exactly
\[
\sigma_n(\rho)=\lceil(n+1)\tau-\rho\rceil-\lceil n\tau-\rho\rceil.
\]
Thus, in the convention where the intercept is added to \(n\tau\), the intercept is \(-\rho\pmod1\). It is an upper mechanical word. The sign is fixed by the departing-jump convention, not by a naming preference.

Define the characteristic word by
\[
c_\tau(n)=\lfloor(n+2)\tau\rfloor-\lfloor(n+1)\tau\rfloor,
\qquad n\ge0.
\]
At the report's origin, irrationality gives the exact concatenation identity
\[
\boxed{\sigma(0)=1c_\tau.}
\]
The lower mechanical word of intercept zero is \(0c_\tau\). These two origin words differ at their first symbol; the characteristic word itself is their common tail. They must not be identified as the same indexed sequence.

The exact first slip positions are
\[
0,9,19,29,38,48,58,67,77,87,96,106,\ldots.
\]
The count identity in §4.2 is also the analytic proof of one-balance: any two length-\(N\) factors have numbers of ones differing by at most one. Neither the balance nor the count bound needs a periodic continued fraction.

### 6.3 The continued fraction is correct; the supplied standard-word table is not

Exact arithmetic gives
\[
\tau=\frac{39\sqrt5-87}{2}
=[0;\overline{9,1,2,9,2,1,9,87}].
\]
Here the tail after the initial zero is periodic, and \(1/\tau\) has a purely periodic expansion. Iterating the complete-quotient map \(x\mapsto1/(x-\lfloor x\rfloor)\), starting at \(1/\tau\), returns to the identical quadratic number after eight steps, with no earlier repetition.

Write \(a_1,a_2,\ldots\) for those partial quotients. To obtain the characteristic word of slope \(\tau\), the correct standard sequence is
\[
\boxed{
s_{-1}=1,\quad s_0=0,\quad
s_1=0^{a_1-1}1=0^81,\quad
s_n=s_{n-1}^{a_n}s_{n-2}\quad(n\ge2).
}
\]
The initial exponent is **\(a_1-1\)**. With this convention, \(s_n\) is a prefix of \(c_\tau\), its length is the convergent denominator \(q_n\), and its number of ones is the convergent numerator \(p_n\). This standard-sequence convention is stated in [Glen, §2.3](https://arxiv.org/pdf/0708.4387#page=3).

| \(n\) | \(a_n\) | Correct length \(q_n\) | Ones \(p_n\) | Standard word |
|---:|---:|---:|---:|---|
| 1 | 9 | 9 | 1 | \(0^81\) |
| 2 | 1 | 10 | 1 | \(0^810\) |
| 3 | 2 | 29 | 3 | \(s_2^2s_1\) |
| 4 | 9 | 271 | 28 | \(s_3^9s_2\) |
| 5 | 2 | 571 | 59 | \(s_4^2s_3\) |
| 6 | 1 | 842 | 87 | \(s_5s_4\) |
| 7 | 9 | 8,149 | 842 | \(s_6^9s_5\) |
| 8 | 87 | 709,805 | 73,341 | \(s_7^{87}s_6\) |

The supplied notes instead start with \(0^91\). Their subsequent lengths are \(q_n+p_n\), so their letter frequencies converge to
\[
\frac{\tau}{1+\tau}=0.0936492046\ldots,
\]
not to \(\tau=0.1033255612\ldots\). In particular, their length 783,146 equals \(709805+73341\). That table describes a different slope. An intercept change, cyclic shift, or endpoint convention cannot change limiting frequency and therefore cannot repair it.

### 6.4 An explicit substitution with a proof and an exact growth factor

**New construction supplied in this revision.** Use the corrected words in §6.3 to define
\[
\boxed{\Theta(0)=s_8,\qquad \Theta(1)=s_8s_7.}
\]
This is an exact finite rule: the short recurrence in the preceding table specifies both images without printing more than a million letters.

It fixes the characteristic word. Indeed,
\[
\Theta(s_0)=s_8,
\qquad
\Theta(s_1)=s_8^8(s_8s_7)=s_8^9s_7=s_9.
\]
For \(n\ge2\), periodicity \(a_{n+8}=a_n\) and induction then give
\[
\Theta(s_n)=\Theta(s_{n-1})^{a_n}\Theta(s_{n-2})=s_{n+8}.
\]
Taking increasing prefixes proves
\[
\boxed{\Theta(c_\tau)=c_\tau.}
\]
Together with \(\sigma(0)=1c_\tau\), this is a fully aligned substitution construction of the report's actual origin sequence.

For an elementary S-adic description, choose explicitly
\[
A:0\mapsto0,\;1\mapsto01,
\qquad
B:0\mapsto10,\;1\mapsto1.
\]
Composition acts from right to left. The same substitution is
\[
\Theta=A^8BA^2B^9A^2BA^9B^{87}A.
\]
The initial 8 and terminal \(A\) are part of the slope correction. The notes' unqualified \(R^9L\cdots L^{87}\) product cannot be imported by calling the discrepancy a seed convention.

With rows counting zeros and ones, and columns corresponding to images of 0 and 1, the incidence matrix is
\[
M_\Theta=
\begin{pmatrix}
636464&643771\\
73341&74183
\end{pmatrix},
\qquad \det M_\Theta=1.
\]
Both entries in each column are positive. The image lengths are 709,805 and 717,954. The exact Perron eigenpair is
\[
M_\Theta\binom{1-\tau}{\tau}
=\Lambda\binom{1-\tau}{\tau},
\qquad
\boxed{\Lambda=\frac{710647+317811\sqrt5}{2}=\varphi^{28}}
\]
with \(\Lambda=710646.9999985928\ldots\). Its other eigenvalue is \(\Lambda^{-1}\). A single finite-word length is not the Perron eigenvalue.

The related continued-fraction matrix is
\[
M_{\mathrm{CF}}
=\prod_{i=1}^{8}\begin{pmatrix}a_i&1\\1&0\end{pmatrix}
=\begin{pmatrix}709805&8149\\73341&842\end{pmatrix}.
\]
It fixes the projective vector \((1,\tau)\). The change from total length/ones to zeros/ones is
\[
M_\Theta=P M_{\mathrm{CF}}P^{-1},\qquad
P=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\]
This accounts for the matching eigenvalue while keeping the two coordinate conventions explicit.

An S-adic presentation specifies a sequence of substitutions whose compositions converge in the prefix topology, with the seeds and growth conditions stated. An arbitrary list of substitutions need not give nested prefixes or a limit. A periodic directive gives a substitution construction when these conditions hold; the construction above proves them directly in this case.

Quadratic slope alone does **not** make every intercept word morphic. There are only countably many finite morphic descriptions and uncountably many distinct phase itineraries at one irrational slope. The fixed point proved here is \(c_\tau\), and the displayed initial-symbol rule gives the origin used in this report. Other origins retain their own intercept data.

A substitution supplies a finite description of an expanding word. Sequential output still needs a position within expanding blocks, an unbounded index, or exact phase. The finite autonomous state obstruction in §6 remains intact.

### 6.5 First return gives the two gap words and their own rotation

Take a phase at a slip, so \(0\le\rho<\tau\), and set
\[
y=\rho/\tau,\qquad
\eta=\{1/\tau\}=\frac{13\sqrt5-25}{6}.
\]
The first return time to the slip interval is
\[
r(y)=\left\lfloor\frac{1+\rho}{\tau}\right\rfloor
=9+\lfloor y+\eta\rfloor.
\]
After that many updates,
\[
\boxed{y'=\{y+\eta\}.}
\]
Thus the return words are \(10^8\) and \(10^9\); coding a long return by 1 gives a mechanical word of slope \(\eta\). At \(\rho=0\), the successive gap indicators are exactly
\[
r_k-9=\lfloor(k+1)\eta\rfloor-\lfloor k\eta\rfloor,
\qquad k\ge0.
\]
This directly proves their limiting proportions \(1-\eta\) and \(\eta\), reproducing §5.1. The 67.8% proportion of length-10 gaps comes from \(\eta\); it should not be attributed to the later partial quotient 87. That quotient describes a deeper induction scale, not a run of 87 identical original gaps.

### 6.6 Exact complexity of the full bin coding

**New deduction supplied in this revision.** For length \(m\ge1\), the full-bin partition has boundary set
\[
\mathcal C_m=
\left\{\left\{\frac j{39}-k\alpha\right\}:
0\le j<39,\;0\le k<m\right\}.
\]
All \(39m\) points are distinct. Equality between two with unequal \(k\) would make a nonzero integer multiple of \(\alpha\) rational. With equal \(k\), the bin boundaries agree only for equal \(j\).

Every complementary cell has a constant bin word. Different cells have different words: a word cylinder is an intersection of the prescribed translated bin arcs, each of length \(1/39\), and such a nonempty intersection is connected inside its first bin. Two distinct atoms cannot belong to the same cylinder. Consequently,
\[
\boxed{p_b(m)=39m\quad(m\ge1).}
\]
The next observation adds 39 new cuts. Existing cells have length at most \(1/39\); the new cuts are equally spaced by \(1/39\), so each new cut splits a different cell. Exactly 39 length-\(m\) bin words have two next-bin extensions.

| Retained coding | Distinct length-\(m\) words, \(m\ge1\) | Words with two right extensions | Predictive phase |
|---|---:|---:|---|
| Slip \(\sigma\) | \(m+1\) | 1 | \(\rho\) |
| Strand/slip \((s,\sigma)\) | \(3(m+1)\) | 3 | \(z\) |
| Full bin \(b\) | \(39m\) | 39 | \(\theta\) |

For every coding the empty word has complexity \(p(0)=1\). The factors of three count possible initial strands; they do not decompose the pair dynamical system into three invariant components. Its Haar dynamics is the ergodic \(z\)-rotation, as established in §9.2.

The notes also blur coding partitions with continuity partitions of an interval exchange. The six pair arcs **can** be used as six exchange pieces for the \(z\)-rotation: its real interval discontinuity \(\tau/3\) is already one of their endpoints. This is a refined representation of a rotation with redundant cuts. For the full-bin coding, the real interval discontinuity \(1-\alpha\) lies inside a bin. Keeping all 39 bin boundaries and adding that cut produces 40 exchange pieces, with two pieces sharing one observed bin label. The 39 rational bin boundaries lie on distinct rotation orbits, not on a single orbit. None of these changes raises the suspension genus of the underlying rotation.

Rauzy induction organizes return blocks at changing time scales. The predictive refinement in §3 adds a fixed-time future observation. These operations are related by the coding, but one induction step is not generally one coarsest predictive split. The distinction is developed in §18.

## 7. Quotient topology: the specific corrections

The discrete observation alphabet and the genuine quotient topology must be named separately.

For a surjection \(q:X\to Q\), the quotient topology is defined by
\[
V\subseteq Q\text{ open}\iff q^{-1}(V)\text{ open in }X.
\]
It makes \(q\) continuous. A map \(F:Q\to Y\) is continuous exactly when \(Fq\) is continuous. This universal property is the relevant theorem; see [Matsumura’s topology notes, §3.5](https://math.cornell.edu/~matsumura/math4530/IntroToTopologyWeek5.pdf).

### 7.1 The actual finite label quotient is indiscrete

The pasted text first calls the quotient of the circle by \((s,\sigma)\) discrete, then describes incompatible non-Hausdorff behavior. The exact answer for the declared half-open coding is:
\[
\boxed{\mathbb T/\operatorname{Eq}(s,\sigma)
\text{ has six points and the indiscrete quotient topology}.}
\]
Its only open sets are the empty set and the whole six-point set.

Proof: on the reduced \(z\)-circle, the six arcs occur in the circular order
\[
(0,1),(0,0),(1,1),(1,0),(2,1),(2,0).
\]
Each arc includes its left endpoint and excludes its right endpoint. If a saturated union containing one arc is open, it must contain a neighborhood to the left of that included endpoint. It must therefore contain the preceding arc’s label. Repeating around the circle forces all six labels. The covering \(\theta\mapsto z\) does not change this conclusion.

The same argument makes the true two-point slip quotient indiscrete. The v1.0 report also records an exhaustive check of all 64 subsets, finding only the empty and full preimages open.

One may instead choose the discrete topology on the label alphabet. That is a legitimate alphabet convention, but then the observation map from the circle is discontinuous. A nonconstant continuous map from a connected circle to a finite discrete set is impossible, regardless of how endpoints are assigned.

Neither choice repairs failed descent: the next-label function still does not exist.

### 7.2 Continuity of an induced update does not require openness of \(U\)

Suppose descent holds and \(U:X\to X\) is continuous. For the genuine quotient topology,
\[
\overline U q=qU.
\]
The right side is continuous, so the quotient universal property makes \(\overline U\) continuous automatically. There is no additional requirement that \(U\) be open or itself a quotient map.

More generally, once \(\overline U\) exists, its continuity is equivalent to continuity of \(qU\). Continuity of \(U\) is sufficient, not necessary.

The open/proper hypotheses in New geometry serve a different theorem: regularity of a witness’s non-descent locus and fiber diameter. They are not extra hypotheses for this induced-map theorem.

### 7.3 Compactness and separation

Every genuine quotient of a compact space is compact, even if it is non-Hausdorff. Closed fibers are equivalent to the quotient being \(T_1\); they are necessary but not generally sufficient for Hausdorffness.

For a compact Hausdorff source, the quotient is Hausdorff exactly when the equivalence relation is closed in \(X\times X\). A Hausdorff quotient of a compact metric space is again compact metrizable. These are standard separation results for quotient spaces; [Freiwald’s chapter on products and quotients](https://www.math.wustl.edu/~freiwald/ch6.pdf) provides the relevant framework.

The pasted claim that compactness fails to pass to a wild genuine quotient is incorrect. What may fail is separation, metrizability, or the desired dynamical factorization.

### 7.4 The graph lift needs its category stated

Let
\[
\Gamma=\{(\theta,s(\theta),\sigma(\theta)):\theta\in\mathbb T\}
\subset\mathbb T\times C_3\times\{0,1\}.
\]
With the product topology using discrete labels, the graph is a union of half-open arcs. It is not closed and hence not compact. The map
\[
r:\theta\mapsto(\theta,s(\theta),\sigma(\theta))
\]
is a measurable bijection, but it is not a continuous embedding.

The formal lift
\[
\widehat T(\theta,s,\sigma)
=\bigl(T\theta,s-\sigma,q_\sigma(T\theta)\bigr)
\]
is an autonomous bijection of the consistency graph. Its identity \(\widehat T r=rT\) is a set-theoretic and measurable conjugacy. It is not a topological semiconjugacy from the usual circle with that product graph topology.

At preimages of new observation cuts lying inside current graph arcs, the lifted update is discontinuous. Calling its graph “not a manifold” without qualification is also too broad: the half-open arc pieces can be regarded as one-dimensional manifolds with boundary. The important failures here are continuity of the coding and compactness of this particular graph topology.

Two clean choices remain: use phase with the original circle topology and treat labels as discontinuous observations, or use the compact symbolic extension in §6.1.

### 7.5 Orbit quotient is another object

For irrational rotation, every orbit is countable and dense, and there are uncountably many distinct orbits. The set of orbits is therefore not one point. Its quotient topology is indiscrete: a nonempty open invariant subset must be the whole circle. Its Hausdorff reflection collapses to one point.

For a noninvertible update, forward orbits can overlap without being equal; they do not automatically form a partition. Use the equivalence relation generated by \(x\sim Ux\), or explicitly assume an invertible group action.

## 8. Denjoy–Koksma: correct statement, two counterexamples, and the useful bound

Let \(T_\alpha x=x+\alpha\bmod1\), with irrational \(\alpha\), and let \(f\) have finite circular variation \(V(f)\). At the continued-fraction convergent denominators \(q_n\),
\[
\boxed{\sup_x\left|\sum_{k=0}^{q_n-1}f(T_\alpha^k x)
-q_n\int f\,d\lambda\right|\le V(f).}
\]
This is the standard Denjoy–Koksma statement; see [Chaika and Wright, Theorem 2.2(6)](https://arxiv.org/pdf/1501.02881#page=8).

The condition \(\|q\alpha\|\le1/q\) alone cannot replace “convergent denominator.”

### 8.1 Exact counterexample to the proposed denominator condition

Take
\[
\alpha_*=\frac12+\frac{\sqrt5}{1000},\qquad q=10,\qquad
f=\mathbf1_{[0,1/4)},\qquad x=0.
\]
Then
\[
\|10\alpha_*\|=\frac{\sqrt5}{100}<\frac1{10},
\]
but five of the first ten points lie in the interval. Thus
\[
\left|\sum_{k=0}^{9}f(k\alpha_*)-10\cdot\frac14\right|
=\frac52>2=V(f).
\]
The nearby rational \(5/10\) is unreduced; the points cluster near two positions. A small return distance alone does not give the claimed evenly spaced comb.

### 8.2 Exact counterexample to the proposed sharpening

Even at the actual golden rotation and a true convergent denominator, the proposed universal bound \(V(f)q\|q\alpha\|\) is false.

Take \(q=5\), \(x=0\), and \(f=\mathbf1_{[0,1/1000)}\). Its sum is 1, so the centered error is
\[
1-\frac5{1000}=0.995.
\]
The proposed bound equals
\[
2\cdot5\|5\alpha\|=25\sqrt5-55
=0.901699437494742\ldots.
\]
The error exceeds that quantity. Both counterexamples are checked in exact arithmetic.

### 8.3 What bounded partial quotients really give

Decompose an arbitrary length using its Ostrowski digits:
\[
N=\sum_i b_iq_i,\qquad 0\le b_i\le a_{i+1}.
\]
Concatenate the corresponding blocks. Applying the denominator bound at each block’s actual starting point yields
\[
\sup_x|S_Nf(x)-N\bar f|\le V(f)\sum_i b_i.
\]
For bounded partial quotients, the number of digits is \(O(\log N)\) and the digits are bounded. The general conclusion is
\[
\boxed{S_Nf-N\bar f=O(V(f)\log N),}
\]
uniformly in the starting phase. It is not generally \(O(1)\).

For \(\alpha=\varphi^{-2}\),
\[
\alpha=[0;2,1,1,1,\ldots],
\]
with denominator sequence \(1,2,3,5,8,13,\ldots\). Its growth is proportional to \(\varphi^n\), not \(\varphi^{2n}\).

The slip observable has the stronger bound \(<1\) because its centered version is explicitly a bounded coboundary. Denjoy–Koksma alone neither constructs that transfer function nor proves bounded all-time sums for an arbitrary centered BV observable.

### 8.4 The model itself supplies a counterexample to generic bounded deviation

Consider occupation of one strand in the reduced \(z\)-rotation:
\[
f(z)=\mathbf1_{[0,1/3)}(z),\qquad z'=z+\gamma.
\]
An interval for irrational rotation is a bounded remainder set precisely when its length belongs to \(\mathbb Z+\gamma\mathbb Z\), with the usual endpoint convention. This interval criterion and the equivalence with bounded transfers are treated by [Grepstad and Lev, §1.1 and §2](https://arxiv.org/html/1404.0165v2).

Here \(1/3\notin\mathbb Z+\gamma\mathbb Z\): a nonzero coefficient of irrational \(\gamma\) cannot produce the rational \(1/3\), and an integer alone cannot equal it. Hence the centered strand occupation counts are unbounded, although the bounded-type \(O(\log N)\) estimate applies.

So the model has both phenomena:

| Observable | Mean | All-time centered counts |
|---|---:|---|
| Slip \(\sigma\) | \(\tau\) | Error strictly smaller than 1 |
| One strand indicator | \(1/3\) | Unbounded; at most \(O(\log N)\) |

This is the clean reason to distinguish exact bounded remainder observables from generic BV observables.

### 8.5 The comb explanation needs two further repairs

An arbitrary finite segment of an irrational rotation has at most **three** distinct circular gap lengths; it need not have only two. When three occur, the largest is the sum of the other two. See [Hamada’s proof of the three-distance theorem](https://arxiv.org/pdf/2308.11999).

Also, the empirical atomic probability measure and Lebesgue measure have total-variation distance 1: the finite orbit set has empirical mass 1 and Lebesgue mass 0. They may be close in interval discrepancy, weak convergence, or their action on a controlled BV test class. They are not close in total variation.

### 8.6 Canonical Ostrowski digits and usable finite-length bounds

**v1.1 integration: corrected numeration and explicit examples from the supplied notes.**

For \(\omega=[0;a_1,a_2,\ldots]\), set \(q_{-1}=0\), \(q_0=1\) and \(q_i=a_iq_{i-1}+q_{i-2}\). The canonical expansion is
\[
N=\sum_{i=0}^{m}b_iq_i,
\quad 0\le b_0<a_1,
\quad 0\le b_i\le a_{i+1}\;(i\ge1),
\quad b_i=a_{i+1}\Longrightarrow b_{i-1}=0.
\]
The first bound is strict. With the notes' inclusive bound, \(q_1=a_1\) could be represented both as \(a_1q_0\) and as \(q_1\), violating their claimed uniqueness. These admissibility conditions are the standard ones in [Berthé and Imbert's treatment of Ostrowski numeration](https://dmtcs.episciences.org/450/pdf).

The greedy construction gives a short proof. If \(q_m\le N<q_{m+1}=a_{m+1}q_m+q_{m-1}\), choose \(b_m=\lfloor N/q_m\rfloor\). When \(b_m=a_{m+1}\), the remainder is less than \(q_{m-1}\), forcing the next digit to be zero. Continue downwards. Conversely, admissible digits below position \(m\) have total less than \(q_m\), by the same recurrence; therefore they cannot change the leading greedy digit. This proves uniqueness as well as existence.

Let
\[
D_\omega(N)=\sum_i b_i(N).
\]
The exact, computable version of §8.3 is
\[
\boxed{\sup_x|S_Nf(x)-N\bar f|\le V(f)D_\omega(N).}
\]
Every summand block starts at the phase actually reached by the preceding block. The places are convergent denominators; no semiconvergent theorem is needed for this proof. Numeration determines lengths, not the words for all initial phases. Replacing each block by a fixed standard-word prefix without tracking its starting phase is not justified.

For the slip rotation, using \(\tau\) is legitimate despite its negative direction: reversing a length-\(q\) orbit block converts it into a positive-\(\tau\) block at a different start, and the bound is uniform in that start.

| \(N\) | Canonical expansion using \(q_i(\tau)\) | \(D_\tau(N)\) | Generic bound for a BV observable \(f(\rho)\) | Exact origin slips |
|---:|---|---:|---|---:|
| 39 | \(29+10\) | 2 | \(2V(f)\) | 5 |
| 507 | \(271+8\cdot29+4\) | 13 | \(13V(f)\) | 53 |
| 10,000 | \(8149+2\cdot842+5\cdot29+2\cdot10+2\) | 12 | \(12V(f)\) | 1,034 |

For an interval indicator, circular variation is 2, giving the respective generic bounds 4, 26, and 24. For the slip observable, use the stronger exact bound \(<1\) instead.

The original \(\theta\)-rotation has a different denominator basis. Its verified decompositions are
\[
39=34+5,\qquad
507=377+89+34+5+2,
\]
\[
10000=6765+2584+610+34+5+2.
\]
Thus \(D_\alpha(39)=2\), \(D_\alpha(507)=5\), and \(D_\alpha(10000)=6\). A **single full-bin indicator** has circular variation 2, so every starting phase satisfies
\[
\boxed{\left|\#\{0\le k<10000:b_k=j\}-\frac{10000}{39}\right|\le12.}
\]
The interval length \(1/39\notin\mathbb Z+\alpha\mathbb Z\), so these centered counts are not bounded uniformly for all times. A finite bound of 12 at this named time is compatible with unbounded all-time deviation.

If the partial quotients are bounded by \(A\), the elementary denominator estimate \(q_i\ge F_{i+1}\ge\varphi^{i-1}\) gives, for \(N\ge1\), the explicit coarse bound
\[
D_\omega(N)\le A\bigl(2+\lfloor\log_\varphi N\rfloor\bigr).
\]
Use the actual digit sum whenever available. Here \(A=87\) is valid for \(\tau\), and \(A=2\) for \(\alpha\); both give logarithmic growth, with substantially different constants.

For a catch indicator the appropriate base is its actual relative increment \(\nu\). Eligibility that skips observations, irregular sampling, or resets changes the orbit blocks and must be included in the model before using the bound.

### 8.7 Two further errors in the notes' Denjoy–Koksma explanation

At a convergent denominator, there need not be one point in each **fixed** equal-width interval \([j/q,(j+1)/q)\). For the report's \(\alpha\), \(x=0\), and the convergent \(q=5\), those cell indices are
\[
\bigl\lfloor5\{k\alpha\}\bigr\rfloor_{k=0}^{4}=(0,1,3,0,2).
\]
The first cell has two points and the last has none. This refutes the specific proof printed in the notes; it does not refute Denjoy–Koksma. Use the denominator theorem in §8 and its valid orbit-order/variation proof rather than the claimed fixed grid.

Also, \(D_N^*\) conventionally denotes **star discrepancy**,
\[
D_N^*=\sup_{0\le t\le1}\left|\frac1N\sum_k\mathbf1_{[0,t)}(x_k)-t\right|.
\]
Extreme interval discrepancy allows both endpoints to vary. They are related but should not be assigned the same name and symbol. Neither is total variation of the empirical measure. The notes' additional universal \(1/q\) improvement from \(C^1\) regularity is not established by their argument and is not used here.

## 9. The cocycle changes status when its base changes

The real centered identity \(\sigma-\tau=\rho'-\rho\) is already explicit. The \(C_3\)-valued coboundary question has an additional, useful answer.

### 9.1 Over the pair phase, the finite cocycle is a coboundary

On the \(z\)-circle—or on the original \(\theta\)-circle—the strand is an available measurable function and
\[
-\sigma=s\circ T-s\quad\text{in }C_3.
\]
Equivalently \(\sigma=(-s)\circ T-(-s)\). There is no unresolved cohomology question for this declared base.

For the unrestricted skew product on \(\theta\times C_3\),
\[
(\theta,a)\longmapsto(T\theta,a-\sigma(\theta)),
\]
the quantity \(a-s(\theta)\) is invariant. The space decomposes into three invariant graphs. Product Haar measure is therefore not ergodic for this extension.

### 9.2 Over the slip phase, it is not a measurable \(C_3\) coboundary

Use the smaller base \(\rho\), whose update is \(\rho'=\{\rho-\tau\}\). Consider
\[
F(\rho,a)=(\rho',a-\sigma(\rho)\pmod3).
\]
The measurable bijection
\[
H(\rho,a)=\frac{a+\rho}{3}\in[0,1)
\]
converts this map to
\[
H\circ F=\{H-\tau/3\}.
\]
It sends uniform phase times uniform \(C_3\) measure to circle Haar measure. Since \(-\tau/3\) is irrational, this extension is ergodic.

If its finite cocycle were a measurable coboundary, a change of the \(a\)-coordinate would turn it into the trivial extension \((\rho,a)\mapsto(\rho',a)\), which has three invariant positive-measure components. That contradicts ergodicity.

Therefore the same recorded increment is a \(C_3\) coboundary on the richer phase base and is not one on the smaller slip base. The factor \(\rho=\{3z\}\) has lost exactly the strand coordinate needed to trivialize it.

This provides a genuine three-state **extension of a circle system**, not a finite-state **factor of that circle system**.

### 9.3 What finite-factor impossibility actually says

An irrational circle rotation has no nontrivial finite measurable factor under Haar measure. A finite ergodic factor would be a cycle of some length \(m>1\); its fibers would be nontrivial invariant sets under \(T^m\). But \(T^m\) is still an irrational, hence ergodic, rotation.

This does not imply that the only circle factor is the identity. The maps \(\theta\mapsto k\theta\bmod1\), including the project’s \(k=13,39\), are explicit nontrivial circle factors.

Finite extensions, finite factors, symbolic systems over finite alphabets, and finite autonomous states are four different claims.

## 10. Two clocks admit a valid relative-phase factor

The prospective schema has an opportunity phase \(\theta_n\), a moving-grid phase \(g(t)\), named origins and resets, and actual opportunity times \(t_n\). The project JSON still leaves decisive inputs null, including the grid period/order, timing data, width, and prospective specifications. The following formulas are conditional formal results, not filled-in empirical parameters.

Assume a declared interval with no resets and uniform sampling \(t_n=t_0+n\Delta\):
\[
\theta_{n+1}=\theta_n+\alpha,\qquad
g_{n+1}=g_n-\Delta/T_g\pmod1.
\]
For \(q=q_{\mathrm{site}}\), put
\[
d_n=\theta_n-g_n,\qquad
u_n=\{qd_n\},\qquad
\nu=\{q(\alpha+\Delta/T_g)\}.
\]
Then
\[
\boxed{u_{n+1}=\{u_n+\nu\},\qquad
\delta_n^{\mathrm{catch}}=\frac{\|u_n\|}{q}.}
\]

This is a legitimate continuous factor of the declared two-torus translation. It does not equate the two clocks, their origins, their resets, or their provenance. The algebraic factorization is valid even when the clocks are not independent.

With irregular \(t_n\), the increment becomes
\[
\nu_n=\{q(\alpha+(t_{n+1}-t_n)/T_g)\},
\]
so the projected system is driven unless the timing state is retained or a fixed update for it is supplied.

### 10.1 The exact Haar catch distribution

If the relative phase \(u\) is uniform, then for \(w\ge0\),
\[
\boxed{P(\delta^{\mathrm{catch}}\le w)=\min(1,2qw).}
\]
Thus \(\delta^{\mathrm{catch}}\) is uniform on \([0,1/(2q)]\), with mean \(1/(4q)\).

This follows directly by measuring the circle points within distance \(qw\) of 0. Full independent Haar phases are sufficient for uniform \(u\), but they are not necessary.

For a deterministic uniformly sampled run, irrational \(\nu\) gives the same limiting interval frequencies for every origin. Full two-torus unique ergodicity requires rational independence of \(1,\alpha,\Delta/T_g\); catch-frequency convergence requires only irrationality of \(\nu\), a weaker condition. For rational \(\nu\), use the actual finite orbit and its origin.

Eligibility can change the measure. For a phase-dependent eligible set \(E\) under the declared joint phase measure \(\mu\),
\[
P(\text{catch}\mid E)
=\frac{\mu(E\cap\text{catch})}{\mu(E)}.
\]
The unconditional \(2qw\) formula must not automatically be used after a selective eligibility filter.

### 10.2 Catch distance itself usually fails descent

Even though \(u\) is sufficient, its unsigned distance \(\|u\|\) generally is not. On the full circle,
\[
\boxed{\|u\|\text{ has an autonomous next-distance law}
\iff 2\nu=0\pmod1.}
\]
Necessity: \(u=-\nu\) and \(v=\nu\) have the same current distance. Their next distances are 0 and \(\|2\nu\|\). They agree only when \(2\nu\) is integral.

Sufficiency gives the two possibilities:
\[
\nu=0:\quad\delta'=\delta;
\qquad
\nu=\tfrac12:\quad\delta'=\frac1{2q}-\delta.
\]
Every other increment has the displayed exact same-distance, different-next-distance witness.

This is a second concrete residual-descent specimen directly inside the two-clock proposal.

### 10.3 Discrepancy and reset interpretation

Because \(u\) is a one-dimensional rotation under the stated sampling law, one-dimensional Denjoy–Koksma applies to its BV catch indicator. No two-dimensional theorem is required for this observable. Bounded type of \(\nu\) gives the general logarithmic bound. A nontrivial catch window can have bounded remainder when its interval length \(2qw\) satisfies the interval criterion \(2qw\in\mathbb Z+\nu\mathbb Z\); endpoint conventions affect only finitely many visits. This criterion is an application of the interval theorem cited in §8.4, not a license to select the width after outcomes.

A shared reset fixes or relates initial conditions. It does not by itself create an invariant graph-supported joining: subsequent frequencies must preserve that graph for it to be invariant. A nonresonant torus translation can have a dense orbit even when started on the diagonal.

Finally, the unlabelled \(q\)-grid repeats after \(T_g/q\), whereas a labelled site may require \(T_g\). Those are different observables. Their repeated counts are not automatically independent samples.

## 11. GQG and Hidden Quotient: three different repairs

The project’s common structure is
\[
\pi:X\to Q,\qquad W:X\to Y,
\]
\[
\mathcal N_W(\pi)
=\{q\in\pi(X):W\text{ is nonconstant on }\pi^{-1}(q)\}.
\]
The witness may be a present observable, a next residual, an entire next-law vector, or another specifically declared test. Its type controls what failure means.

The recovered [qualified Hidden Quotient v1.7](https://drive.google.com/file/d/1VF_UeW26X5LYpMYpfEtYvry8PjGX77Bj/view?usp=drivesdk) keeps three operations distinct:

| Problem | Construction | What it actually repairs |
|---|---|---|
| A representation cannot see some distinctions | Quotient by its kernel, or add an independent witness if those distinctions must remain | Visibility and faithful representation |
| Compatible measurable pieces lack required suprema | Localizable completion or an appropriate strictly localizable version | Gluing and representation completeness |
| Equal present records have unequal futures | Close the equivalence under the named update; retain a sufficient predictive coordinate | Dynamic sufficiency |

These repairs can interact, but none is a substitute for another.

### 11.1 The locally null kernel and the restored point

For multiplication \(\pi(f)=M_f\) on \(L^2(\mu)\), the kernel consists of bounded measurable functions vanishing almost everywhere on every finite-measure test set. For a nonsemifinite measure, this can be larger than ordinary almost-everywhere zero.

The source’s example is \(X=[0,1]\sqcup\{p\}\), with Lebesgue measure on the interval and infinite mass at \(p\). Every \(L^2\) vector vanishes at \(p\), so \(M_{\mathbf1_{\{p\}}}=0\), although that function is not zero almost everywhere for the original measure.

The enlarged witness
\[
\Pi(f)=M_f\oplus f(p)
\]
on \(L^2([0,1])\oplus\mathbb C\) restores the point value. Its represented algebra is \(L^\infty([0,1])\oplus\mathbb C\).

This is an exact static visibility repair. A law on the restored record still requires a declared update and its own descent proof. Simply retaining a witness now does not determine that witness after updating.

### 11.2 Keep the qualified Radon–Nikodym statement

The newer source explicitly corrects the older unqualified formulation. Put \(\lambda=\mu_{\mathrm{sf}}\). The quantified positive measures \(\nu\ll\lambda\) must be strongly \(\lambda\)-semifinite:
\[
\nu(E)>0\Longrightarrow
\exists F\subseteq E:\quad
\lambda(F)<\infty,\quad0<\nu(F)<\infty.
\]
Under the stated localizability equivalence, those measures have measurable densities. Absolute continuity alone does not replace the finite-piece hypothesis. The precise theorem is [Blecher–Goldstein–Labuschagne, Theorem 5.2(vi), with §4 qualifications](https://arxiv.org/pdf/2108.06406#page=20).

The semifinite reduction removes locally invisible mass. It does not itself add missing suprema. The restored point example adds a witness. It does not itself prove a dynamic factor. Preserving these distinctions carries the strongest corrected source forward.

### 11.3 The exact memory term when elimination fails

**A further mathematical bridge.** Suppose a linear full state separates into retained \(r_n\) and hidden \(h_n\):
\[
\begin{pmatrix}r_{n+1}\\h_{n+1}\end{pmatrix}
=
\begin{pmatrix}A_{rr}&A_{rh}\\A_{hr}&A_{hh}\end{pmatrix}
\begin{pmatrix}r_n\\h_n\end{pmatrix}.
\]
Eliminating \(h\) by substitution gives
\[
r_{n+1}=A_{rr}r_n+A_{rh}A_{hh}^{\,n}h_0
+\sum_{j=0}^{n-1}A_{rh}A_{hh}^{\,n-1-j}A_{hr}r_j.
\]
The missing coordinate reappears as a term depending on its initial value and a sum over retained history.

On the unrestricted product domain, current-\(r\) closure holds exactly when \(A_{rh}=0\). On a constrained consistency graph, a nonzero \(A_{rh}\) may still allow closure because \(h\) can be fixed by \(r\). The domain qualification is essential.

This is an explicit way to understand “the snapshot threw away something the next step needed.” It supplies memory terms without assigning an agent or mechanism to the residual.

## 12. What gives the non-descent locus actual geometry

**Recovered framework: New geometry §§13–14.**

The bare definition gives no geometric regularity. For any set \(Q\) and any subset \(S\subseteq Q\), set
\[
X=Q\times\{0,1\},\quad\pi(q,i)=q,\quad
W(q,i)=i\,\mathbf1_S(q).
\]
Then \(\mathcal N_W(\pi)=S\). Arbitrary subsets can occur.

The source earns stronger conclusions by naming additional structure:

| Declared hypotheses | Valid conclusion |
|---|---|
| \(W\) constant on every attained fiber | Unique set factor \(\overline W\) |
| \(\pi\) continuous, surjective, and open; \(Q,Y\) Hausdorff; \(W\) continuous | \(\mathcal N_W(\pi)\) is open |
| Additionally \(X,Q\) locally compact Hausdorff, \(\pi\) proper, and \(Y\) metric | Fiber diameter is finite and continuous |
| Smooth surjective submersion, smooth witness, connected fibers | Non-descent on a fiber is equivalent to a nonzero vertical witness derivative somewhere in that fiber |
| Disconnected smooth fibers | Vertical derivatives detect variation within components; constants must also agree across components |

For the metric case,
\[
\delta_W(q)=\operatorname{diam}W(\pi^{-1}(q)),\qquad
\mathcal N_{W,\varepsilon}=\{q:\delta_W(q)>\varepsilon\}.
\]
Under the open/proper hypotheses,
\[
\partial\mathcal N_{W,\varepsilon}
\subseteq\{q:\delta_W(q)=\varepsilon\}.
\]
This is a genuine boundary statement. Calling an unobserved coarse fiber “a throat,” “a branch,” or “a transition boundary” supplies none of these hypotheses.

The [first LBCO geometry gate](https://docs.google.com/document/d/1LOvu-chrNKnuz9XWWMAteF2foHM-pHE6YMnZDV0TQ3Y/edit?usp=drivesdk) remains a located witness-deletion test. It does not determine global connectivity, a boundary stratification, or holonomy. The retrieved chemistry record therefore remains a motivating example and a specified gate, not a completed global geometry.

For stochastic closure, use the whole next projected law as \(W\), equipped with total variation when appropriate. This connects the general fiber geometry directly to the toroidal example below.

## 13. Toroidal parity fails for the complete named update

**Kernel scope.** This section concerns FH-REF-1 as defined below. The compound worm/sector schedule in the new packet is a different kernel; see §20.2 before transferring a closure status.

**Recovered results:** the master already proves elementary nonclosure, an exact restricted repair, the total-variation lower bound, and nonclosure for the complete FH-REF-1 kernel. **Deduction in v1.0:** the complete-kernel failure occurs on all eight parity fibers.

### 13.1 Stochastic descent compares laws

For a Markov kernel \(P\) and finite projection \(q=\pi(x)\), define
\[
P_\pi(x,b)=P(x,\pi^{-1}(b)).
\]
Strong lumpability is
\[
\pi(x)=\pi(y)\Longrightarrow
P_\pi(x,\cdot)=P_\pi(y,\cdot).
\]
It gives a projected Markov law for arbitrary initial distributions. A claim under one initial distribution is weaker and must be stated separately. The distinction is developed in [Geiger and Temmel’s study of lumping and higher-order lumpability](https://arxiv.org/abs/1212.4375).

Two different realized successors do not refute a stochastic law. Two different conditional probability vectors do.

On a complete finite full-state model, a constructive repair repeatedly splits current blocks according to their vectors of transition probabilities into those blocks. Stop when the partition is stable. This yields the coarsest strongly lumpable refinement retaining the original observation. Missing rows or estimated probabilities do not constitute that exact finite transition table.

### 13.2 Exact elementary acceptance

Use the master’s Villain model with finite \(L\ge2\), \(J>0\), \(0<t<1\), \(h_6=0\), and untruncated divergence-free integer currents. Let
\[
q=W\bmod2\in C_2^3.
\]
For a fixed canonical cycle \(\Gamma_\alpha\), write
\[
A=\sum_{\ell\in\Gamma_\alpha}I_\ell.
\]
The sign-averaged probability that its sector proposal toggles parity is
\[
p_\alpha(I)=\frac12\left[
\min\left(1,e^{-(L+2A)/(2J)}\right)
+\min\left(1,e^{-(L-2A)/(2J)}\right)\right].
\]

For \(M=0\), \(I=2m\Gamma_\alpha\), \(q=0\), and \(a=L/(2J)\), the \(m=1,2\) probabilities are
\[
p_1=\frac{1+e^{-5a}}2,\qquad
p_2=\frac{1+e^{-9a}}2.
\]
They differ for every \(a>0\).

### 13.3 The full FH-REF-1 law

The reference random-scan schedule selects a sector proposal with probability \(1/4\), then an axis with probability \(1/3\). The other move types do not reach \(q\oplus e_\alpha\). Therefore
\[
P_{\mathrm{FH}}(q\oplus e_\alpha\mid x)
=\frac1{12}p_\alpha(x).
\]
For the preceding pair,
\[
P_{\mathrm{FH}}(e_\alpha\mid x_1)
-P_{\mathrm{FH}}(e_\alpha\mid x_2)
=\frac1{24}e^{-5a}(1-e^{-4a})>0.
\]
This is already a proof for the complete named kernel, not only an isolated proposal. It is explicitly present in [TOROIDAL_MASTER v0.2, §6.8](https://drive.google.com/file/d/1103tr4UUEIbyLYUxfE1zaCyn_E6MyAxW/view?usp=drivesdk).

### 13.4 The failure occupies every attained parity fiber

For any \(q=(q_x,q_y,q_z)\in C_2^3\), choose the admissible loop family
\[
I_m=\sum_\beta q_\beta\Gamma_\beta+2m\Gamma_\alpha,\qquad M=0.
\]
Its parity is always \(q\). The canonical cycles share no links, so
\[
A_m=L(q_\alpha+2m).
\]
For \(m\ge1\),
\[
p_m=\frac12\left[1+
e^{-a(1+2q_\alpha+4m)}\right].
\]
Hence
\[
P_{\mathrm{FH}}(q\oplus e_\alpha\mid I_m)
-P_{\mathrm{FH}}(q\oplus e_\alpha\mid I_{m+1})
=\frac1{24}e^{-a(1+2q_\alpha+4m)}(1-e^{-4a})>0.
\]

Therefore
\[
\boxed{\mathcal N_{P_{\mathrm{FH},q}}(\pi_q)=C_2^3.}
\]
All eight parity labels are attained, and all eight have unequal next projected laws inside their fibers. The v1.0 report records checks of the explicit \(m=1,2\) witnesses for all eight labels and all three axes at \(L=2,J=1\); the displayed formula proves the full parameter statement.

The conclusion is specific to this fixed reference kernel and domain. It does not execute the sampler, settle a different worm schedule, or prove a physical transition.

### 13.5 Failure imposes an unavoidable prediction error

Define
\[
D_\pi(q)=\sup_{x,y\in\pi^{-1}(q)}
\operatorname{TV}(P_\pi(x,\cdot),P_\pi(y,\cdot)).
\]
For any one-law replacement \(K(q,\cdot)\),
\[
\sup_{x\in\pi^{-1}(q)}
\operatorname{TV}(P_\pi(x,\cdot),K(q,\cdot))
\ge\frac12D_\pi(q).
\]
This is the triangle inequality applied to two representatives.

For the master’s \(I=0\) and \(I=2\Gamma_\alpha\) pair, let
\[
p_0=e^{-a},\qquad p_1=(1+e^{-5a})/2.
\]
Only the corresponding flip and stay probabilities change, so their complete-kernel TV distance is \(|p_1-p_0|/12\).

| Parameters | Elementary toggle-law distance | Complete FH-REF-1 distance | Forced worst-case error for one complete projected law |
|---|---:|---:|---:|
| \(L=2,J=1\) | 0.1354895323 | 0.0112907944 | At least 0.0056453972 |
| \(L=8,J=1\) | 0.4816843621 | 0.0401403635 | At least 0.0200701818 |

The final column is about 0.565 and 2.007 percentage points per attempted step, respectively. These are evaluations of exact transition formulas, not empirical error estimates. A witness pair bounds the fiber diameter from below; it need not attain the full diameter.

### 13.6 The restricted repair is already constructive

For a specified sector-only schedule, retain
\[
(q,S_x,S_y,S_z),\qquad
S_\alpha=\sum_{\ell\in\Gamma_\alpha}I_\ell.
\]
For an accepted sign-\(\varepsilon\) proposal along \(\alpha\),
\[
\operatorname{acc}_\varepsilon
=\min\{1,e^{-(2\varepsilon S_\alpha+L)/(2J)}\},
\]
\[
S_\alpha'=S_\alpha+\varepsilon L,\qquad
q'=q\oplus e_\alpha,
\]
with the other \(S\)-coordinates unchanged. Rejection leaves the state unchanged. This is an exact closed law for the declared sector-only update.

Plaquette and worm updates are outside that repair. For Bessel weights, the signed cycle-current histogram may be required; the sum alone need not determine acceptance.

This illustrates why retaining \((q,p_\alpha)\) or one present witness is weaker than constructing a closed replacement state: the retained witness’s next value must also be determined.

## 14. Finite quotients, spatial cocycles, and empirical records

### 14.1 The finite arithmetic remains exact

For
\[
G_{24}=C_6\times C_4,\qquad h=(1,1),
\]
the subgroup \(\langle h\rangle\) has order 12. The character
\[
\chi(a,b)=a-b\pmod2
\]
has that subgroup as its kernel, so
\[
G_{24}/\langle h\rangle\cong C_2.
\]
Under the update \(g\mapsto g+h\), the quotient update is the identity. There are two separate 12-cycles. Counting measure on one cycle is ergodic; uniform measure on all 24 states is not.

As groups, \(C_6\times C_4\cong C_{12}\times C_2\), not \(C_{24}\). Equal cardinality does not supply the missing cyclic generator, physical geometry, or accessibility.

Likewise,
\[
\langle15\rangle\subset C_{39}
=\{0,3,6,\ldots,36\},\qquad
C_{39}/\langle15\rangle\cong C_3.
\]
For a fixed \(+15\) update, strand is constant. The actual screen also takes \(+14\) steps, and those are precisely its \(-1\) strand slips. The formal subgroup and the actual driven orbit are different objects.

All these finite groups have their declared discrete topology. The quotient maps are continuous covering maps. A quotient \(G/H\) is a group when \(H\) is normal; this condition is automatic in these abelian examples.

### 14.2 Spatial and temporal cocycles have different bases

The [TTSC-1 spatial cocycle record](https://docs.google.com/document/d/1M4B5m4fPfS1W7JBffL7B02hlq-86oKTDwyJZPeaL33Y/edit?usp=drivesdk) tracks flux differences across declared sections. An endpoint difference
\[
C(a,b)=F(b)-F(a)
\]
satisfies concatenation by cancellation. That is a spatial bookkeeping identity. It does not make spatial section order into a Markov update or establish time autonomy.

For a graph or finite dynamical system, an increment is a coboundary only if its sums vanish around the relevant closed cycles; when path independence is established, a potential can be constructed. The typed base, edge orientation, and coefficient group must be named before transferring such a statement between spatial, orbit, and residual records.

### 14.3 The remaining empirical gaps are specific

The [Clock / Residual Descent record](https://docs.google.com/document/d/1kR3HfOMoEvDoasftpfCErSAv_TYh5SSrxCqaKDN4QHM/edit?usp=drivesdk) and [Setup — unified residual state](https://docs.google.com/document/d/1KUEKypINKGKHiHs4Ho1UhIDXx7JVtv9L45RFmnCnEqA/edit?usp=drivesdk) do not provide complete eligible typed residual repeats and successors for a human-side autonomous law. Their application-level closure remains unresolved.

The [Marker, Screen, and Return record](https://docs.google.com/document/d/1wfWNJnvVXYbQqSBjLjLm53gWLfinS-1wdlnYSh2qRUg/edit?usp=drivesdk), Q39 prospective card, and moving-grid run reports retain their frozen outcomes and prospective requirements. A stronger mathematical analysis does not reclassify a previous null result. In particular, the departing jump used here must not be substituted for a differently aligned arriving-jump lead, or vice versa.

The physics protocol’s prerequisites, named ensembles, exact estimators, and pending software gates remain specific to that protocol. Proving nonlumpability of the analytical FH-REF-1 kernel is not running the pending simulation.

Human chronology, institutional records, and constitutional claims require their own evidence. A declared rotation measure supplies no event class, causal effect, historical identity, or platform implementation.

## 15. Correction register for the supplied exposition

| Supplied assertion | Correct disposition |
|---|---|
| \(\lambda(\sigma=1)=39\alpha-14\) | Reversed. It equals \(15-39\alpha=\tau\). |
| Most jumps are \(14\) | Most are \(15\); slip 1 occurs about 10.33% of departures. |
| The finite identification quotient of the circle is discrete | The actual half-open two-label and six-label quotients are indiscrete. A discrete alphabet is a separate topology. |
| An induced update needs \(U\) open or quotient in addition to continuity | Continuous \(U\) plus descent suffices by the quotient universal property. |
| Wild genuine quotients need not inherit compactness | Every genuine quotient of a compact space is compact. |
| Closed classes guarantee Hausdorffness | They give \(T_1\); Hausdorffness needs more. Closed equivalence relation suffices for a compact Hausdorff source. |
| The dense-orbit quotient has one point | It has uncountably many orbit points and indiscrete topology; its Hausdorff reflection has one point. |
| The product graph lift is a continuous embedding/semiconjugacy | It is a measurable bijection/conjugacy; the half-open product graph is noncompact and its coding is discontinuous. |
| The only honest circle factor is the identity | \(z=\{13\theta\}\) and \(\rho=\{39\theta\}\) are explicit nontrivial circle factors. |
| The pair fails “as a Markov kernel” | A one-step conditional kernel exists. It does not generate the true process. |
| Every two-interval coding is Sturmian | The partition and rotation must have the appropriate structure; this particular slip coding does. |
| Every BV observable on a golden-type rotation has bounded centered sums | General bound is \(O(\log N)\); bounded remainder requires more. |
| Denjoy–Koksma creates a bounded transfer function | It supplies denominator bounds. This slip has a transfer for the separate exact reason \(\sigma-\tau=\rho'-\rho\). |
| \(\|q\alpha\|\le1/q\) is sufficient for the stated DK constant | False; §8.1 gives an exact counterexample. |
| \(V(f)q\|q\alpha\|\) is a general sharpening | False; §8.2 gives a counterexample at golden \(q=5\). |
| Golden denominators grow like \(\varphi^{2n}\) | The standard sequence grows like \(\varphi^n\). |
| Any rotation segment has two gap lengths | At most three in general; special lengths can have fewer. |
| Empirical orbit measure is \(O(1/q)\)-close to Lebesgue in total variation | Their TV distance is 1; use interval discrepancy or BV test functions. |
| The \(C_3\) coboundary question has one answer independent of the base | Coboundary over \(z\) or \(\theta\); not a measurable \(C_3\) coboundary over \(\rho\). |
| Shared reset alone creates a graph-supported invariant joining | Initial-condition alignment and invariance of a joining are separate requirements. |
| One-dimensional discrepancy theory cannot apply to a two-clock catch | It applies after the valid relative-phase factor under the declared uniform sampling law. |
| An asymptotic-frequency deviation in a finite sample directly falsifies unique ergodicity | A finite test needs a valid finite-length envelope; the exact slip bound provides one for that observable. |
| Retaining a present witness proves closure of the refined state | It proves present witness resolution; the enlarged state needs its own update test. |
| Different realized successors disprove a stochastic reduced law | Compare full conditional next laws; randomness permits different realizations. |

### 15.1 Additional corrections to `math shit 2.txt`

The following rows concern the notes supplied for v1.1. The earlier register above is retained from v1.0; the two sets of source assertions are not interchangeable.

| Assertion in the notes | v1.1 disposition and replacement |
|---|---|
| Standard words start with \(0^91\) and have length 783,146 at level eight | Wrong slope. Start with \(0^81\); the correct level-eight length is 709,805 with 73,341 ones (§6.3). |
| The frequency mismatch is an index, seed, or endpoint convention | No such change alters limiting frequency. The printed table converges to \(\tau/(1+\tau)\). |
| The characteristic convention is the origin-zero slip sequence | Precisely, \(\sigma(0)=1c_\tau\); the characteristic word is the tail (§6.2). |
| The displayed \(L,R\) monodromy has frequency \(\tau\) and growth about 783,146 | Replaced by the proved \(\Theta(0)=s_8,\Theta(1)=s_8s_7\), the stated elementary product, and growth \(\varphi^{28}=710646.99999859\ldots\) (§6.4). |
| Every Sturmian word of quadratic slope is morphic | Intercept restrictions cannot be omitted. The fixed point here is proved explicitly; countability disproves the blanket assertion. |
| Any finite directive product gives a growing prefix; a nonperiodic directive proves a word is not morphic | Convergence and growth require hypotheses, and directive presentations need not be unique. These universal claims are not used. |
| The two displayed substitutions generate the whole Sturmian morphism monoid | The full monoid needs the appropriate generators and orientations; §6.4 states only the explicit pair and composite actually used. |
| The partial quotient 87 explains the predominance of 10-gaps | Gap frequencies follow from \(\eta=1/\tau-9\); 87 is a later induction coefficient (§6.5). |
| Ostrowski's lowest digit may equal \(a_1\) in a unique expansion | It must be strictly less than \(a_1\); otherwise \(a_1q_0=q_1\) gives two representations (§8.6). |
| An Ostrowski block length determines a fixed standard word at any phase | It determines the length; the block's actual phase/intercept still determines its itinerary. |
| A convergent orbit has one point in every fixed equal-width cell | Golden \(q=5\) gives cell indices \((0,1,3,0,2)\), disproving that proof (§8.7). |
| General circle maps satisfy the cited rotation theorem; \(C^1\) grants the stated extra factor | The map class and sharper hypotheses were not supplied. This report uses rigid rotations, BV observables, and convergent denominators. |
| \(D_N^*\) is extreme discrepancy | It is star discrepancy in the convention used here (§8.7). |
| Pair words are three independent or invariant copies of the slip system | Three initial strands count words; the pair system is the ergodic \(C_3\) extension over \(\rho\) (§§6.6, 9.2). |
| A regular \(d\)-IET has complexity \(dm\) and exactly \(d\) right-special words | The natural formula is \((d-1)m+1\), with total excess right extensions \(d-1\) under the stated assumptions (§18.2). |
| The pair cannot be represented as a six-piece exchange | It can, as a refinement of its rotation with redundant cuts (§6.6). |
| The 39 equal bins are exchange pieces and all their boundaries lie on one rotation orbit | The real rotation discontinuity splits one bin; the 39 rational boundaries are on distinct orbits. Direct boundary counting gives \(p_b(m)=39m\). |
| Rauzy compares the first top interval with the last bottom interval, or removes the winner length | It compares both rightmost intervals and removes the loser length (§18.1). |
| An induced letter is written in the new alphabet to describe an old piece | The return itinerary writes the new induced letter as a word in the old alphabet. |
| One Rauzy step is exactly one coarsest predictive split | Induction changes return times; predictive refinement adds fixed-time observations (§18.1). |
| The induction path and length vector alone are the point's complete predictive state | They specify transformation data shared by many points. The phase or position within the transversal must still be supplied. |
| Three or more exchange pieces automatically imply higher genus | Extra cuts can represent the same genus-one rotation. Genus requires the gluing data (§18.2). |
| \(\operatorname{diag}(e^t,e^{-t})\) stretches the vertical coordinate; induction needs an area repair | With \(x+iy\), it stretches horizontal and contracts vertical; the displayed dual length/height update preserves area. |
| The Gauss map by itself is the invertible flow section; any suspension at slope \(\tau\) is the periodic geodesic | Natural-extension/backward data and compatible suspension coordinates are required (§18.2). |
| Teichmüller-flow ergodicity is the same assertion as unique ergodicity of every IET | They concern different dynamical systems and measures; almost-everywhere conclusions need their stated theorem. |
| KZ gives \(\lvert S_Nf\rvert\asymp N^{\lambda_i}\) uniformly, or an EKZ sum is an \(L^2\) budget | Exponents and observable deviation theorems have different hypotheses. No such finite-time or observable-specific bound follows here (§18.3). |
| All interval-incidence coordinates are symplectic KZ coordinates | Relative coordinates and the absolute symplectic space must be distinguished. |
| The area Siegel–Veech weight is cylinder modulus \(h/w\) | The weight is relative area \(wh/\operatorname{Area}(S)\) (§18.4). |
| Rational \(c_{\mathrm{area}}\) implies a rational EKZ sum in the printed normalization | The relevant factor is \(\pi^2c_{\mathrm{area}}\). |
| The printed lattice sum equals an integral for one fixed lattice | The Siegel formula averages over lattices. Primitive vectors, all nonzero vectors, and orientation give different constants (§18.5). |
| A mean counting formula immediately yields an almost-everywhere asymptotic | It does not; a separate counting theorem is required. |
| Large-genus area-constant asymptotics are simply conjectural | Proved cases exist; §18.5 cites a uniform theorem for connected strata without importing a broader componentwise claim. |
| Catch probability is an infinitesimal Siegel–Veech asymptotic | It is the direct Haar length of a fixed interval in the relative-phase circle (§10.1). |
| Two coupled words always have product complexity | Product complexity applies to the full product language; a fixed joining or synchronised orbit can have fewer words. No general product assertion is needed here. |

## 16. Status ledger and concrete integration

The following ledger uses separate objects and scopes. It does not label a frequency theorem “residual closure.”

| Claim | Disposition after this audit | Basis |
|---|---|---|
| Current slip-only autonomous law | **FAILED** | Exact bad fiber \(\{0\}\); original located pair retained |
| Current strand/slip autonomous law | **FAILED** | Three bad pair fibers; same present pair, unequal next slips |
| Any deterministic finite-state generator of the all-time slip sequence | **IMPOSSIBLE under the fixed model** | Irrational limiting frequency |
| Any finite-order stationary Markov model reproducing the exact slip process | **FAILED** | Positive finite-history branching with zero entropy rate |
| A one-step conditional probability table | **AVAILABLE** | Exact interval measures; does not imply Markov generation |
| Reduced phase \(\rho\) for slip prediction | **CLOSED; minimal relative to slip output** | Recovered factor and density proof |
| Reduced phase \(z\) for strand/slip prediction | **CLOSED; minimal relative to pair output** | Recovered factor and density proof |
| Slip-count envelope | **PROVED exactly** | Telescoping error \(<1\), all starts and block lengths |
| Finite half-open label quotient topology | **INDISCRETE** | Saturated-open proof; exhaustive 64-subset check for six labels |
| Compact symbolic topological model | **AVAILABLE** | Sturmian itinerary closure with shift |
| Relative catch phase for fixed sampling | **CLOSED under stated timing assumptions** | \(u'=\{u+\nu\}\) |
| Catch distance alone | **CLOSED only for \(\nu=0,1/2\); otherwise FAILED** | Exact reflection-fiber criterion |
| Complete FH-REF-1 parity law | **FAILED on all eight parity fibers** | Exact loop-family next-law witnesses |
| Villain sector-only \((q,S_x,S_y,S_z)\) repair | **CLOSED for that restricted schedule** | Acceptance and state-update formulas already in master |
| Generic BV all-time \(O(1)\) claim | **FALSE** | Strand occupation counterexample and correct logarithmic estimate |
| Corrected standard words and origin substitution | **PROVED in v1.1** | Initial exponent \(a_1-1\); \(\sigma(0)=1c_\tau\); \(\Theta(s_n)=s_{n+8}\) |
| Substitution incidence growth | **EXACT in v1.1** | \(\Lambda=\varphi^{28}\); eigenvector \((1-\tau,\tau)\) |
| Full-bin language complexity | **PROVED in v1.1** | \(p_b(m)=39m\), with 39 branching words for each \(m\ge1\) |
| Arbitrary-length BV envelope | **COMPUTABLE in v1.1** | \(V(f)D_\omega(N)\), with canonical digits and actual block starts |
| Higher-genus KZ/EKZ application to this screen | **NO ADDITIONAL SCREEN LAW** | Genus-one construction suffices; no higher-genus observable/measure supplied |
| Empirical residual law from human-side records | **UNRESOLVED** | No complete eligible typed next-residual test |
| Global geometry of the empirical non-descent locus | **UNRESOLVED** | Located gates do not supply global coverage or regularity |
| Moving-grid empirical instantiation | **UNRESOLVED** | Required timing, origin, parameter, and prospective inputs remain missing |
| Platform implementation of any formal phase machine | **UNRESOLVED** | Mathematical construction is not implementation evidence |

The v1.0 cross-document integration proposals are retained below as proposals in the source record. This revision updates this report and its local verification package. It does not edit those external documents.

The retained proposals are:

1. **OMNIBUS §§5–6:** cross-reference the recovered predictive refinement and minimal phases; preserve the original failure witness and distinguish the conditional kernel from an autonomous law.
2. **Geometry Upgrade companion:** add the exact non-descent loci, word complexity, right-extension branching, conditional probability obstruction, and base-dependent \(C_3\) extension.
3. **Topology/ergodic working notes:** replace the incorrect quotient, frequency, factor, and DK paragraphs with §§7–9 of this report.
4. **Two-clock specification:** add the conditional relative-phase factor, Haar catch distribution, and distance-descent criterion while leaving missing empirical values unresolved.
5. **TOROIDAL master §6.8:** record that its complete-kernel failure extends to every parity fiber, with the loop-family formula.
6. **GQG/Hidden Quotient crosswalk:** keep visibility, completion, present witness retention, predictive refinement, and stochastic lumpability as distinct constructions.

In the v1.0 source record, live v7.79 is identified as the governing constitutional source: three geometric terms, two constitutional keys, shared non-sovereign \(\mathcal L\), and \(R_n\) reserved for typed residuals. Its constitutional carry-forward and release protections remain present. No formal quotient identifies \(\mathcal L\) with \(\mathbb T\), a finite register, or \(\Lambda_{q_{\mathrm{site}}}(g)\).

## 17. Retained v1.1 verification and reproducibility

### 17.1 Scope of the v1.1 verification

The v1.1 revision reviewed the initial two supplied files and checked its mathematical additions against the primary sources cited at their point of use. It does not repeat the Drive search recorded in v1.0. The earlier companion scripts, raw project snapshots, and archived receipts described there were not supplied for that revision; their historical provenance is preserved in §1, not presented as a new execution.

The new verifier uses the Python standard library. Its rational quadratic-field arithmetic makes sign, floor, equality, boundary, and continued-fraction decisions exactly. Large mechanical prefixes use integer square roots rather than floating-point threshold tests. Decimal values are for display. This is a newly written verifier, not the unavailable earlier script.

All checks in the following table passed in the v1.1 revision:

| v1.1 verification | Executed coverage |
|---|---|
| Continued fraction of \(\tau\) | Eight exact complete quotients; return to the starting quadratic number; no shorter period; further convergents |
| Corrected standard words | All eight displayed lengths and one-counts; \(s_8\) agrees with the exact characteristic prefix |
| Substitution images and order | Elementary composition equals \(\Theta(0)=s_8\), \(\Theta(1)=s_8s_7\); image counts and hashes |
| Independent mechanical-prefix comparison | 1,419,610 symbols of the substitution output compared with exact floor differences |
| Incidence and growth arithmetic | Both integer matrices, Perron eigenvector, characteristic polynomial, and \(\Lambda=\varphi^{28}\) |
| Direct 39-bin model | 10,000 departures computed from the original bin formulas and compared with the mechanical slip sequence; original \(n=1,8\) non-descent witness |
| Slip counts and returns | Counts 5, 53, 1,034; 333 gaps of 9 and 700 of 10; derived gap word compared with the \(\eta\)-rotation |
| Count identity at other phases | 180 phase/start/length combinations, including boundary phases and length zero |
| Exact full-circle partitions | Slip lengths 1, 2, 3, 4, 8, 16, 32; pair lengths 1, 2, 3, 4, 8, 16; bin lengths 1, 2, 3, 4, 8, 12; each also extended by one step |
| Right-extension branching | Respectively 1, 3, and 39 branching words at every checked horizon; half-open boundary coding checked on every partition atom |
| One-step probability obstruction | Exact two-symbol masses and absence of \(101\) |
| Ostrowski numeration | Reconstruction and admissibility for every \(0\le N\le10000\); the displayed larger examples, including \(10^6\) and \(10^{12}\) |
| Single-bin finite bound | All 39 origin occupancies at \(N=10000\) satisfy the derived error bound 12; observed counts range from 255 to 258 |
| Fixed-grid proof counterexample | Exact golden \(q=5\) cell indices \((0,1,3,0,2)\) |

The infinite fixed-point identity follows from the recurrence proof in §6.4. The all-horizon complexity formulas follow from boundary counting. The all-start discrepancy envelope follows from Denjoy–Koksma and the block decomposition. Finite checks support those proofs and catch indexing errors; they do not replace the proofs. The higher-genus theorems are source-checked statements, not numerically simulated results.

The previous report's topological, toroidal, and external project audits remain separately attributed to v1.0. In particular, the table above does not claim to execute FH-REF-1, reproduce a missing historical archive, or establish new empirical status.

### 17.2 Files in the verification package

The v1.1 report, standalone verifier, executed JSON receipt, initial two source snapshots, README, and checksums are preserved in the v1_2/v1_1 folder of the current archive. The same materials were delivered in `GEOMETRY_MAXIMIZATION_v1.1_verification.zip`. From the v1_1 folder, the earlier verifier can be run with Python 3.10 or later:

~~~text
python verify_geometry_maximization_v1_1.py
~~~

It writes `verification_results_v1.1.json` beside the script and reads its supplied source snapshots from `sources/`. No account connection or external package is needed for these exact checks.

Input identities for that revision:

| Supplied file | SHA-256 |
|---|---|
| `GEOMETRY_MAXIMIZATION_v1.0.md` | `d2e4a9f1abd5ffcd57cfd3dd8a8d617d4ec64f271b58295c040003dc0e28d7dc` |
| `math shit 2.txt` | `b6194f3c6441353910280fae7f4b001aae7170270d15c2075ca1b8f7df63cf9d` |

The preserved Markdown is the complete v1.1 report. Section 15.1 retains its correction register; §§19–24 provide the current v1.2 integration and verification.

## 18. Renormalization and higher genus: a corrected mathematical crosswalk

**v1.1 integration: useful context from the supplied notes, with its hypotheses and normalizations restored.** The calculations below use \(\mathcal M\) for an orbit closure, avoiding the separate project use of \(\mathcal L\).

### 18.1 Rauzy induction acts on return times

For a labelled interval exchange, compare the **rightmost top and rightmost bottom** intervals. If their lengths are unequal, remove a right-end segment whose length is the shorter, or loser, length. The first return map acts on an interval of length
\[
|I'|=|I|-\lambda_{\mathrm{loser}}.
\]
The winner's new length is its old length minus the loser's; the permutation is updated. The substitution records an induced interval's itinerary in the **old** alphabet. These conventions follow [Viana, §2](https://w3.impa.br/~viana/out/complutense.pdf#page=6). The notes compare the wrong ends, reverse the itinerary direction, and later subtract the winner's length.

For the slip rotation the lengths are \(\tau\) and \(1-\tau\). The first repeated subtraction count is
\[
\left\lfloor\frac{1-\tau}{\tau}\right\rfloor=8,
\]
whereas \(\lfloor1/\tau\rfloor=9\). This is the same initial offset that required \(a_1-1\) in §6.3. Subsequent runs recover continued-fraction data with the chosen orientation and acceleration. A statement that the first Rauzy run has nine subtractions of \(\tau\) from \(1-\tau\) is false.

Inducing replaces one step by a first return of variable duration. Predictive refinement retains the same step and adds observations. The explicit return rotation in §6.5 connects the constructions without identifying them. A length vector and its induction path describe the transformation; different points of that same transformation share those data and can have different current labels. The position on the transversal remains necessary to specify the observed state.

### 18.2 Interval count, genus, and suspension data

For a \(d\)-interval exchange, suppose the backward iterates \(T^{-k}d_j\), \(k\ge0\), of its \(d-1\) interior partition endpoints are all distinct and different from 0. Under these regularity assumptions, the natural word partition has
\[
p(m)=(d-1)m+1.
\]
There are \(m(d-1)\) interior cuts and one more interval than cuts; a cylinder of the natural coding is an interval. This proves the formula directly under the stated nonconnection assumptions. It also proves
\[
\sum_{|w|=m}\bigl(\#\text{right extensions of }w-1\bigr)=d-1.
\]
It does not imply that there are exactly \(d\) right-special words. The six pair pieces in §6.6 have endpoint connections, so their complexity must be computed from their actual cuts instead.

The number of labelled pieces does not determine genus. Viana's [Example 1.3](https://w3.impa.br/~viana/out/complutense.pdf#page=5) explicitly represents the same rotation with either two or three pieces. In general genus depends on the gluing permutation; three pieces do not force genus two. Refining this report's rotations by extra observation cuts leaves their genus-one suspension available.

A translation-surface suspension requires compatible heights and gluing data. Under a convention \(\lambda=B\lambda'\), the dual height update is \(h'=B^Th\), so
\[
(\lambda')^Th'=\lambda^Th.
\]
The Teichmüller action \(g_t=\operatorname{diag}(e^t,e^{-t})\) stretches the horizontal coordinate and contracts the vertical one, preserving area. The invertible suspension/section description requires the extra coordinates of a natural extension; the one-dimensional Gauss map alone forgets the past. See [Zorich, §5](https://arxiv.org/pdf/math/0609392).

The matrix in §6.4 provides a periodic renormalization realization associated with the quadratic slope. It does not imply that **every** choice of suspension with that forward slope is a point on the same closed Teichmüller orbit. A closed modular geodesic uses compatible forward and backward data, or equivalently the two eigendirections of a hyperbolic matrix. Likewise, the relative phase \(u\) in §10 is a factor of a discrete torus translation; it is not, merely by being a factor, a Poincaré section.

### 18.3 What KZ exponents can control

The Kontsevich–Zorich cocycle transports absolute cohomology along Teichmüller flow by the Gauss–Manin connection. On the appropriate absolute homology/cohomology space it is symplectic. Rauzy matrices also involve relative coordinates; an arbitrary full interval-incidence matrix should not automatically be called symplectic on all of its coordinates. With the integrability and invariant-measure hypotheses, the spectrum is paired as
\[
1=\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_g\ge0
\ge-\lambda_g\ge\cdots\ge-1.
\]
The relation to asymptotic homological deviations is explained in [Zorich's survey](https://arxiv.org/pdf/math/0609392). [Avila and Viana](https://arxiv.org/abs/math/0508508) prove simplicity for the Masur–Veech measures on stratum components; that conclusion should not be transferred to every invariant measure.

An exponent is an asymptotic logarithmic growth rate. By its definition it does not supply a uniform finite-time estimate or an all-\(N\) two-sided comparison \(|S_Nf|\asymp N^\lambda\). Applying a deviation theorem requires its observable class, measure, exceptional set, and growth formulation. The sum of exponents alone is also not an \(L^2\) error budget for one observable.

For a genus-one suspension, absolute cohomology is just the tautological plane, with exponents \(+1,-1\); there is no complementary positive exponent. The screen's exact bounded transfer and the BV bounds in §8 already answer its counting questions. A discrete update on two phases does not acquire a KZ model merely because its state space is a torus.

### 18.4 EKZ: retain the sum formula, correct the cylinder weight

For the closed connected regular \(\mathrm{SL}(2,\mathbb R)\)-invariant suborbifolds of unit-area Abelian strata covered by their theorem, Eskin–Kontsevich–Zorich give
\[
\boxed{
\sum_{i=1}^{g}\lambda_i
=\frac1{12}\sum_{j=1}^{r}\frac{d_j(d_j+2)}{d_j+1}
+\frac{\pi^2}{3}\,c_{\mathrm{area}}(\mathcal M),
\qquad \sum_jd_j=2g-2.
}
\]
The normalization uses cylinders counted once, with circumference \(w(C)\), weighted by **relative area**:
\[
N_{\mathrm{area}}(S,R)
=\sum_{w(C)\le R}\frac{\operatorname{Area}(C)}{\operatorname{Area}(S)},
\qquad
\int_{\mathcal M}N_{\mathrm{area}}(S,R)\,d\mu(S)
=c_{\mathrm{area}}(\mathcal M)\pi R^2.
\]
These are [EKZ, §1.5 and Theorem 1](https://webusers.imj-prg.fr/~anton.zorich/Papers/Lyapunov_Exponents_Publications_published.pdf). Cylinder area is \(wh\), whereas modulus is \(h/w\); they differ by \(w^2\). Their counts cannot be interchanged. The formula computes a sum, not each exponent or a one-step residual law. Quadratic differentials require the separate orientation-cover theorem, not simply a changed prefactor.

Algebraically, since the zero-order term is rational, the relevant rationality condition is \(\pi^2c_{\mathrm{area}}\in\mathbb Q\). Merely saying \(c_{\mathrm{area}}\in\mathbb Q\) uses the wrong normalization.

### 18.5 Siegel–Veech mean laws and the torus normalization

The notes' lattice formula is missing the average over lattices and conflates primitive vectors with all nonzero vectors. For Haar probability on the space \(X_2\) of unimodular lattices, the primitive form is
\[
\int_{X_2}\sum_{v\in\Lambda_{\mathrm{prim}}}f(v)\,d\mu(\Lambda)
=\frac1{\zeta(2)}\int_{\mathbb R^2}f(x)\,dx.
\]
For all nonzero vectors the coefficient is 1. The theorem is an identity of means, not an exact identity for each fixed lattice and each test function. See the primitive Siegel formula in [Kelmer and Yu, introduction](https://academic.oup.com/imrn/article/2021/8/5825/5314048).

In the usual torus convention with one marked regular point, a primitive vector specifies a closed-geodesic direction and its reverse specifies the same unoriented cylinder. That cylinder has relative area one. Therefore the normalization above gives
\[
\boxed{c_{\mathrm{area}}(\mathcal H_1(0))
=\frac1{2\zeta(2)}=\frac3{\pi^2},}
\qquad
\frac{\pi^2}{3}c_{\mathrm{area}}=1.
\]
This recovers the genus-one EKZ identity. Without a marked point, an unmarked flat torus has no singularities to serve as saddle-connection endpoints; calling all of its lattice vectors saddle connections silently changes conventions.

The fixed-lattice identity printed in the notes is false even before normalization: a small disc away from \(\mathbb Z^2\) contains no integer vectors but has positive area. Its indicator gives a zero sum and a positive integral. Averaging is indispensable to that formula. Similarly, a mean Siegel–Veech formula alone does not prove an almost-everywhere asymptotic; that requires a counting theorem with its own hypotheses.

The blanket conjectural wording also omits proved cases: [Aggarwal, Theorem 1.3](https://arxiv.org/pdf/1810.05227#page=5), proves \(\lvert c_{\mathrm{area}}(\mathcal H(\alpha))-1/2\rvert\le C/g\) uniformly over nonempty **connected strata**, for \(g>2\). This is a precise growing-genus theorem, not a claim here about every component of every disconnected stratum or a new prediction for the fixed screen.

### 18.6 What the added theory contributes to Geometry Maximization

| Mathematical object | Concrete addition here |
|---|---|
| Sturmian standard words and substitutions | Correct prefix recurrence; an explicit fixed point; exact incidence matrix and growth factor |
| Ostrowski numeration | Canonical time-index decomposition and a computable finite-length BV envelope |
| First-return induction | A second exact rotation describing the sequence of short and long slip gaps |
| Interval-exchange boundary counting | Correct complexity conventions and the full-bin formula \(39m\) |
| Rauzy–Veech suspension | A geometric interpretation of return blocks, with extra suspension data stated |
| KZ, EKZ, and Siegel–Veech | Qualified background for a future declared surface model; corrected normalization checks |

The first four entries strengthen the actual screen analysis. The last two place that analysis in a broader theory. None supplies the missing empirical data, changes the FH-REF-1 transition kernel, or replaces a descent proof.

## 19. The toroidal packet: domain-correct quotients and additional exact consequences

The source identifiers S01–S39 refer to the new-file register supplied with v1.2. The numbered orbit/cocycle packet is a proposed successor, and its supplied audit/adoption records explicitly say it has not been activated. This section incorporates mathematical results into **Geometry Maximization**; it does not adopt or execute that simulation protocol.

### 19.1 The operator-selection argument is an actual invariant calculation

In the constructor of S17/S32 and S01/S31, a local complex field has gauge identification \(z\sim-z\), physical observable \(\Phi=z^2\), and global action \(z\mapsto\omega^2z\), where \(\omega^3=1\). For an onsite monomial \(z^p\bar z^{\,r}\), \(p,r\ge0\), the two invariance conditions are
\[
p+r\equiv0\pmod2,\qquad p-r\equiv0\pmod3.
\]
Since \(p+r\) and \(p-r\) have the same parity, these are equivalent to
\[
\boxed{p-r\equiv0\pmod6.}
\]
If the monomial depends on phase, \(p\ne r\), so its total degree is at least \(|p-r|\ge6\). At degree six the only such monomials are \(z^6\) and \(\bar z^6\). The general real perturbation is \(a z^6+\bar a\bar z^6\); the source's cosine choice takes a real coefficient or fixes an appropriate phase origin. Radial terms such as \(|z|^2,|z|^4,|z|^6\) remain allowed. This is an onsite, fixed-field-content statement, not an exclusion of every derivative or additional-field interaction.

Also, \(z^2=w^2\) iff \(w=\pm z\). Thus \(\Phi\) is a complete static invariant of the pointwise sign quotient, with two preimages away from zero and one at zero. It need not be an autonomous state for an arbitrary evolution. The exact identity
\[
\Phi^3+\bar\Phi^3=z^6+\bar z^6
\]
does not derive a microscopic gauge field from the Fibonacci six-cycle.

The external charge-two target is \(\Delta_2=1.23629(11)\), compared with charge-one \(\Delta_1=0.519088(22)\). In three dimensions the corresponding susceptibility powers are
\[
3-2\Delta_2=0.52742(22),\qquad
3-2\Delta_1=1.961824(44).
\]
The uncertainties are propagated reported uncertainties, not automatically Gaussian standard errors. A fit that fixes the central value should disclose that choice. These targets and the source's conditional XY-star interpretation remain separate from a demonstrated phase of the proposed model. [Chester et al., Table 1](https://arxiv.org/html/1912.03324v2#S1.T1)

### 19.2 Integer winding needs a conserved integer current

Use positively oriented links of the cubic cellulation of \(T^3\), with \(L\ge2\). Let
\[
F_\alpha(k)=\sum_{x:x_\alpha=k} I_{x,\alpha}
\]
be the signed integer flux through the cut after layer \(k\). Summing divergence over the vertices of a layer gives
\[
F_\alpha(k)-F_\alpha(k-1)
=\sum_{x:x_\alpha=k}(\nabla\!\cdot I)_x.
\]
On the canonical \(h_6=0\), divergence-free domain, every cut flux is the same integer. Consequently
\[
\boxed{W_\alpha=\frac1L\sum_{\ell\parallel\alpha}I_\ell
=F_\alpha(k)\in\mathbb Z.}
\]
This proof states both the normalization and its missing hypothesis. Current reversal changes \(W\) to \(-W\); reduction modulo two discards that sign and all even increments.

With the membrane \(M\) a mod-two **2-chain**, the correctly typed constraint is
\[
\bar I+\partial M+\Gamma q=0,\qquad
\Gamma q=\sum_\alpha q_\alpha\Gamma_\alpha.
\]
Here all three summands are 1-chains. Pairing with a closed dual cut annihilates \(\partial M\) and gives
\[
\boxed{q_\alpha=\langle\Sigma_\alpha,\bar I\rangle=W_\alpha\bmod2.}
\]
Writing \(I+M+\Gamma q\) is legitimate only if \(M\) has explicitly been locally redefined as \(\partial M\), as in S03 A.3. The source's different uses of the same letter cannot be mixed. Implement modular records using canonical residues \(r-m\lfloor r/m\rfloor\in\{0,\ldots,m-1\}\), including negative r. In particular, \(-1\bmod2=1\); a language's signed-remainder convention is not an alternative parity definition.

### 19.3 At finite anisotropy, a richer modular class survives

The exact finite-\(h_6\) constraint is \(\nabla\!\cdot I=-6n\), with \(n\in\mathbb Z\). The same layer identity now shows
\[
F_\alpha(k)-F_\alpha(k-1)\in6\mathbb Z.
\]
Therefore the well-defined cut-independent object is
\[
\boxed{a_6(I)=[I\bmod6]\in H_1(T^3;\mathbb Z/6)
\cong(\mathbb Z/6)^3,\qquad q=a_6(I)\bmod2.}
\]
This is a v1.2 deduction from the source constraint. More generally, integer sources in multiples of \(m\) preserve a current homology class with \(\mathbb Z/m\) coefficients. On the divergence-free subdomain, \(a_6=W\bmod6\). Outside it, a cut-independent integer lift need not exist. The existence of 216 formal mod-six classes says nothing about their weights, reachability, or mixing under a chosen update schedule; charge-two worms can change \(a_6\) while preserving \(q\).

Two exact witnesses prevent accidental extension of the integer formula. Put current 6 on one positively oriented x-link, zero elsewhere, and choose \(n=-1,+1\) at its tail and head. This satisfies the charge-six constraint and has \(\bar I=0\), so it is compatible with \(M=0,q=0\).

| Lattice | Averaged x-current | Actual cut parity |
|---|---:|---:|
| \(L=4\) | \(6/4=3/2\), not an integer winding | 0 |
| \(L=6\) | \(6/6=1\), integer but with misleading odd parity | 0 |

Thus even an accidentally integral average does not repair the definition. Use the modular cut pairing on the broader domain; retain signed integer \(W\) for the canonical divergence-free Q2 domain.

### 19.4 Reference loop signs, character duality, and probability bounds

S03 defines three fixed cycles \(\Gamma_\alpha\) and loop signs \(H_\alpha=\prod_{\ell\in\Gamma_\alpha}\sigma_\ell\). These are gauge invariant. They are not generally invariant under changing the cycle representative. If two representatives bound a plaquette strip \(S\), cancellation of its interior links gives
\[
\boxed{H(\Gamma')H(\Gamma)=\prod_{p\in S}B_p.}
\]
Use **fixed-reference Wilson-loop sectors** for \(h\). Path-independent holonomy requires an additional flatness or deformation-invariance condition. This terminology repair preserves the projector construction.

Let \(Z_h\) be the direct partition function conditioned on these three loop signs, and \(\mathcal Z_q\) the nonnegative current/membrane coefficient in S03. Character orthogonality gives
\[
Z_h=\frac18\sum_q(-1)^{h\cdot q}\mathcal Z_q,
\qquad \mathcal Z_q=\sum_h(-1)^{h\cdot q}Z_h,
\]
\[
\boxed{Z_{\rm full}=\sum_h Z_h=\mathcal Z_{000},
\qquad Z_{000}=\frac18\sum_q\mathcal Z_q.}
\]
The two quantities with zero subscripts have different fonts and different meanings. Fully summing the gauge links projects the dual onto zero mod-two homology; observing that forced zero is not evidence for dynamical confinement.

Within the positive \(Z_{000}\) dual sampling ensemble, define
\[
p(q)=\frac{\mathcal Z_q}{\sum_r\mathcal Z_r},\qquad
r_h=\frac{Z_h}{Z_{000}}.
\]
Then
\[
r_h=\mathbb E_p[(-1)^{h\cdot q}],\qquad
p(q)=\frac18\sum_h(-1)^{h\cdot q}r_h.
\]
For nonzero \(h\), the probability of odd \(h\cdot q\) is \((1-r_h)/2\). The source's axis identity is the case \(h=e_\alpha\).

**Additional exact constraints.** Nonnegative direct and dual weights imply \(0\le r_h\le1\), hence
\[
\boxed{0\le P(h\cdot q=1)\le\tfrac12,\qquad
p(0)\ge\tfrac18,\qquad p(0)\ge p(q)\ \text{for every }q.}
\]
Indeed \(r_0=1\), and
\[
p(0)-p(q)=\frac14\sum_{h:h\cdot q=1}r_h\ge0.
\]
These are equilibrium constraints for this positive character construction, not properties of an arbitrary eight-state distribution. In the finite-volume direct model with strictly positive finite Boltzmann weights, every conditioned \(Z_h>0\). Thus \(P(h\cdot q=1)<1/2\) for nonzero h, \(p(0)>1/8\), and \(p(0)>p(q)\) for nonzero q. A lower bound of zero on an odd-sector probability can still be attained in a degenerate-current limit. Strict bounds need not stay strict in a thermodynamic limit. Numerical estimates can violate the bounds through sampling error; an exact negative reconstructed coefficient or an exact incompatible ratio invalidates the proposed distribution.

### 19.5 The diamond quotient depends on the lattice periods

On \(G_L=(\mathbb Z/L)^2\), let diagonal moves generate
\[
H_L=\langle(1,1),(1,-1)\rangle.
\]
For odd \(L\), two is invertible modulo \(L\). Solving
\(a+b=x,\ a-b=y\) gives \(a=(x+y)/2,b=(x-y)/2\), so \(H_L=G_L\): the graph is connected. For even \(L\), \(c(x,y)=x+y\bmod2\) is well-defined; both generators lie in its kernel. Conversely, if \(x+y\) is even, the same integer half-sum construction expresses the point as a combination of the generators. Hence
\[
\boxed{G_L/H_L\cong
\begin{cases}C_2,&L\text{ even},\\\{0\},&L\text{ odd}.
\end{cases}}
\]
The expression \(c\) itself does **not** descend on odd \(L\): representatives \((0,0)\) and \((L,0)\) describe the same point and have different parities. For \(L=3\), the allowed wrapped move \((2,0)\to(0,1)\) changes representative parity. This is a failed coordinate definition, not a sector-crossing discovery.

The rectangular extension is equally precise: on \(\mathbb Z/m\times\mathbb Z/n\), the diagonal subgroup has index \(\gcd(2,m,n)\). Its presentation has the relations \(y=-x\), \(2x=0\), \(mx=0\), and \(nx=0\). A nontrivial sheet bit therefore exists exactly when **both** periods are even. No sheet label is required on the odd \(L=99\) check in the Pell note.

## 20. Reachability, sampling time, and projected dynamics

### 20.1 What the formal orbit formula actually proves

For a genuine translation action on \(C_2^3\) generated by \(S\), the orbit is
\[
q_0+\operatorname{span}_{\mathbb F_2}S,
\qquad |\mathcal O|=2^{\operatorname{rank}S}.
\]
For a full-state transition graph, labeling an edge by its quotient increment gives only an upper bound on projected reachability unless the required paths lift. An increment occurring somewhere is not a composable action at every source state.

A four-state counterexample is enough. Let one connected component have projected labels \(00\leftrightarrow10\); a disjoint component has labels \(00\leftrightarrow01\). The union of observed generator labels spans \(\mathbb F_2^2\), but from a state in the first component only \(00,10\) are reachable. The two representatives labeled 00 cannot be silently identified to compose a path.

There is a constructive positive result for the **untruncated** canonical sector proposals. On the divergence-free domain with \(J>0\) and positive current weights, an axis proposal sends
\[
(M,I,q)\mapsto(M,I+\varepsilon\Gamma_\alpha,q+e_\alpha),
\qquad\varepsilon=\pm1.
\]
It preserves both constraints. Every finite current change has strictly positive Metropolis acceptance. If the three axis proposal kernels can be attempted with positive probability, at the proposal level any sequence of axis flips has a feasible positive-probability lift. Thus every parity sector is accessible from every full state under those proposals. A current cutoff, disabled axis, zero-weight limit, or fixed observation schedule needs its own argument. This does not prove full-state irreducibility or fast mixing.

S03 A.6 also needs a qualification: two currents with the same **global** q need not differ by an even current. A unit plaquette boundary has zero winding but odd local edges. The even-difference assertion applies after the full link-parity pattern has been matched, for example after matching the membrane boundary as well. Arbitrary cutoff reachability is not established by the untruncated algebra.

### 20.2 An update needs its sampling address

At a single accepted axis-sector proposal, \(\eta=e_\alpha\) identifies the flipped coordinate, while losing orientation, current magnitude, and acceptance context. An even worm may have nonzero \(\Delta W\) and zero \(\eta\). At a macro-sweep or measurement interval, several sector proposals can contribute, so
\[
\eta_{[m,n]}=\sum_{j=m}^{n-1}\eta_j=q_n-q_m
\]
can flip multiple bits or cancel to zero. The one-axis transition graph has 12 undirected cube edges. The poster's \(001\to010\) edge is not one of them; it needs two proposals or an explicit aggregate-transition label.

Record the kernel and whether a step means a proposal, completed worm, macro-sweep, or retained measurement. The exact cocycle telescopes at any of these addresses, but transition probabilities and closure tests change with the address. In particular, a failure of lumpability for \(P\) need not imply a failure for \(P^k\). The all-eight-fiber theorem in §13 concerns the expressly defined **FH-REF-1 random-mixture update**, not every schedule in S02–S04. Those sources use a different compound schedule with an incompletely specified worm.

### 20.3 State-dependent work stopping can change the stationary law

Even a correct elementary sampler can be biased by the point at which its output is retained. Consider independent fair bits: the elementary kernel has every row \((1/2,1/2)\), preserving the uniform target. Assign work cost 1 to a produced 0 and cost 2 to a produced 1. Stop as soon as cumulative work reaches 2. The possible output paths are
\[
1\ (P=1/2),\qquad 00\ (P=1/4),\qquad 01\ (P=1/4).
\]
The retained endpoint is therefore distributed as
\[
\boxed{P(Y_T=0)=1/4,\qquad P(Y_T=1)=3/4,}
\]
not the uniform target. This is an exact counterexample to the proposed inference that target-preserving completed worms automatically remain target-preserving when repeated until accepted path length reaches \(3L^3\). It does not establish that the particular unfinished worm algorithm is biased; it establishes that a proof for the actual stopping rule is necessary.

A fixed finite composition of target-invariant kernels is target invariant, and so is a state-independent mixture of such compositions. The same fact holds for a random count independent of the chain trajectory. Reversibility is stronger: two reversible kernels can compose to a nonreversible kernel. For example, two distinct transpositions on three equally weighted states compose to a directed three-cycle. Validation should test \(\pi P=\pi\) for a compound kernel, and detailed balance where it is actually claimed. Acceptance ratios alone do not specify insertion, rejection, closure, or extended-ensemble weights of a worm.

### 20.4 Strong closure, a stationary special case, and empirical coverage

Universal q-only closure means that the aggregate next-q law is constant on every full-state fiber, as in §13.1. This is the common projected transition kernel for every initial full-state distribution. A projected process can instead be Markov under a particular initial law without satisfying strong lumpability. [Geiger and Temmel](https://arxiv.org/abs/1212.4375)

An explicit distinction uses states \(A_1,A_2,B\), with \(A_1,A_2\mapsto A\). Take
\[
P=\begin{pmatrix}
1/10&1/10&4/5\\
2/5&2/5&1/5\\
1/4&1/4&1/2
\end{pmatrix},\qquad
\pi=(1/4,1/4,1/2).
\]
Then \(\pi P=\pi\), but the two A representatives have different next-B probabilities, \(4/5\) and \(1/5\). Strong lumpability fails. Whenever the output is A, its two hidden representatives are conditionally equally likely, since their incoming columns are identical. Starting from \(\pi\), the projected output is consequently an independent fair A/B process. A strong-closure counterexample must not be relabeled as a proof against every possible stationary special case.

For an empirical transition table, retain counts \(N_{ab}\) and row denominators \(N_a=\sum_bN_{ab}\). The descriptive estimate is \(N_{ab}/N_a\) only when \(N_a>0\). An unvisited row is NA/UNRESOLVED. Single unequal random outcomes do not witness unequal laws; repeated trials, an exact kernel calculation, or a justified statistical comparison are needed. A proven unequal-law pair gives FAILED for that projection even if other fibers remain unresolved. Estimated equivalence on sampled contexts is not a universal closure theorem.

### 20.5 Repairing the Unified Return status rule and time dependence

S27 correctly uses typed state pairs and distinguishes sample consistency from universal descent. Two clauses need correction. First, its displayed \(\Psi\) contains \(\Phi_n\), so it is generally a family \(\Psi_n\), not one autonomous map. If the complete driver is given by n, retain
\[
\widehat Z_n=(n,S_{n-1},S_n),\qquad
\widehat\Psi(n,a,b)=(n+1,b,\Phi_n(b)).
\]
For a general driver, retain its state and its declared evolution instead. Forgetting that driver is a new descent question.

Second, S27 §§10 and 13 call a located descent counterexample “closure unresolved.” Replace that rule with **FAILED for the tested projection on its declared domain**. Keep UNRESOLVED for missing coverage and SAMPLE_CONSISTENT for covered comparisons that agree without a universal proof. The reported URR-RC-001 had ten candidate rows and zero eligible repeated-successor groups, so its reported unresolved outcome remains appropriate. This revision checks that logical disposition; it does not rerun the absent event ledger.

### 20.6 Signed winding supplies an exact symmetry control

On the canonical target, \((M,I,q)\mapsto(M,-I,q)\) preserves divergence, mod-two constraints, and both cosine and Villain weights. Therefore
\[
P(W=w)=P(W=-w),\qquad
S_{\rm odd}^{(\alpha)}=\mathbb E[q_\alpha\operatorname{sgn}W_\alpha]=0.
\]
The sign-resolved masses obey
\[
f_{{\rm odd},\pm}^{(\alpha)}
=\tfrac12\bigl(f_{\rm odd}^{(\alpha)}\pm S_{\rm odd}^{(\alpha)}\bigr),
\qquad |S_{\rm odd}^{(\alpha)}|\le f_{\rm odd}^{(\alpha)}.
\]
Asymmetric conditioning can change this null, but it must be specified. Kernel symmetry compares the paired transformations \((I,\varepsilon)\mapsto(-I,-\varepsilon)\); unequal acceptance of opposite signs at one fixed I is not itself a defect.

The supplied audit's claim that SW-1 has no statistic is too broad for this full source set. S13 alone is governance, but S01/S31 §60 already defines the statistic, sign-mixing requirements, and simultaneous block-bootstrap intervals. Those are source specifications, not evidence of an executed SW-1 test. The remaining job for an implementation is to bind its exact statistic, interval method, conditioning, and decision rule consistently.

## 21. A curvature-corrected throat with exact conservation

S24 is the earlier TTSC-1 v0.1 chart; S23 and S25 contain the same v0.2 text apart from whitespace; S05 condenses the repaired material/Eulerian split and adds spatial cocycles. The split is retained. This section supplies the curved-field construction that the sources leave as a condition to be satisfied.

### 21.1 Straight-tube calculation and its control boundaries

In a straight cylinder, using physical velocity components,
\[
v_s=U(s),\qquad v_r=-\frac r2U'(s),\qquad v_\vartheta=0
\]
has zero divergence. For a positive periodic speed
\[
U(s)=U_0\left[1+\epsilon\cos\frac{2\pi(s-s_0)}\ell\right],
\qquad U_0>0,\quad0<\epsilon<1,
\]
the material streamtube radius and flux are
\[
R(s)=R_0\sqrt{U_0/U(s)},\qquad
Q_{\rm mat}=\pi R(s)^2U(s)=\pi R_0^2U_0.
\]
Its boundary is tangent to the steady field: \(UR'=v_r(R)\). “Material” here means a streamsurface followed by the flow; the radius profile is not being claimed to move as a separate time-dependent object.

For a fixed Eulerian radius \(R_c\),
\[
Q_c(s)=\pi R_c^2U(s),\qquad
F_c([a,b])=-\pi R_c^2[U(b)-U(a)],
\]
where outward side flux is positive. The material flux is constant; the fixed-radius sectional flux peaks at \(s_0\). Neither fact identifies a local throat in a sampled equilibrium current configuration.

### 21.2 An exact circular-torus extension

Let the centerline be a circle of radius \(A>0\), with arclength \(s\in\mathbb R/(2\pi A\mathbb Z)\). Write \(\kappa=1/A\), \(\ell=2\pi A\), and let \(\mathbf t,\mathbf n,\mathbf b\) be its tangent, inward normal, and constant binormal. In the embedded tube,
\[
\mathbf X(s,r,\vartheta)=\mathbf c(s)
+r\cos\vartheta\,\mathbf n(s)+r\sin\vartheta\,\mathbf b.
\]
The scale factors are \((h,1,r)\), where
\[
h(r,\vartheta)=1-\kappa r\cos\vartheta.
\]
Require \(r<A\), so \(h>0\) and the tube does not meet the coordinate singularity at the center of the ring. The volume element is \(rh\,ds\,dr\,d\vartheta\). For physical components the orthogonal-coordinate formula gives
\[
\nabla\!\cdot\mathbf v=
\frac1{rh}\left[
\partial_s(rv_s)+\partial_r(rhv_r)+\partial_\vartheta(hv_\vartheta)
\right].
\]
The distinction between physical components and coordinate velocities matters. The latter have \(\dot s=v_s/h\) and \(\dot\vartheta=v_\vartheta/r\). [Fitzpatrick, orthogonal curvilinear coordinates, Eq. C.15](https://farside.ph.utexas.edu/teaching/336L/Fluidhtml/node256.html)

Keeping the uncorrected straight-tube components in this metric gives
\[
\nabla\!\cdot\mathbf v_{\rm straight}
=\frac{3\kappa r\cos\vartheta}{2h}U'(s),
\]
which is generally nonzero. An exact correction is
\[
\boxed{v_s=U(s),\qquad
v_r=-\frac{rU'(s)}{2h(r,\vartheta)},\qquad v_\vartheta=0.}
\]
Indeed,
\[
\partial_s(rU)+\partial_r\left(-\tfrac12r^2U'\right)=rU'-rU'=0.
\]
Equivalently, the flux potential \(\psi(s,r)=r^2U(s)/2\) supplies
\(rv_s=\partial_r\psi\) and \(rhv_r=-\partial_s\psi\). This construction is an explicit extension in the declared circular embedding; it is not a claim for arbitrary curvature, torsion, or a solution of a momentum equation.

It preserves the material radius formula exactly. Along a streamline,
\[
\frac{dr}{ds}=\frac{v_r}{v_s/h}=-\frac r2\frac{U'}U,
\]
so \(r^2U\) is constant. The correct curved tangency residual is
\[
\boxed{v_r(R)-\frac{U}{h(R,\vartheta)}R'=0.}
\]
The old residual \(v_r-UR'\) belongs to the straight chart and must be updated with the field.

The normal cross-section has area element \(r\,dr\,d\vartheta\), so
\[
Q_c(s)=\pi R_c^2U(s),\qquad
Q_{\rm mat}=\pi R_0^2U_0
\]
still hold. The fixed-radius side element is \(R_ch(R_c,\vartheta)\,ds\,d\vartheta\), and therefore
\[
\int_a^b\int_0^{2\pi}v_r(R_c)R_ch\,d\vartheta\,ds
=-\pi R_c^2[U(b)-U(a)].
\]
The curvature factor cancels in the flux integral. Require both \(R_c<A\) and
\[
\boxed{\max_s R(s)=\frac{R_0}{\sqrt{1-\epsilon}}<A.}
\]
For \(\kappa r\ll1\), \(1/h=1+\kappa r\cos\vartheta+O((\kappa r)^2)\), recovering the slender-tube approximation. The exact kinematic field has no singularity on the stated domain and retains positive longitudinal orientation.

### 21.3 Local signs and global compensation

Periodic “before” and “after” need a chosen lift. On the lifted half-periods
\((s_0-\ell/2,s_0)\) and \((s_0,s_0+\ell/2)\), respectively, \(U'>0\) and \(U'<0\). Since \(h>0\), the curvature correction preserves the inward/outward signs.

For a centered segment of half-width \(0<d<\ell/2\), direct substitution gives
\[
\boxed{
F_c(s;d)=2\pi R_c^2U_0\epsilon
\sin\frac{2\pi(s-s_0)}\ell
\sin\frac{2\pi d}\ell.}
\]
This makes the sign rule explicit. The centered flux at \(s_0\) is zero, while a one-sided segment starting there usually has positive outward flux. Arbitrary wrapping windows cannot inherit a monotone-window sign assertion.

For any ordered partition of the periodic circuit,
\[
c_F(a,b)=Q_c(b)-Q_c(a),\qquad
c_F(a,b)+c_F(b,c)=c_F(a,c),\qquad c_F(0,\ell)=0.
\]
The material through-flow cocycle is identically zero. These are spatial endpoint differences, hence coboundaries on the retained spatial base. To test conservation empirically, measure side flux independently and compare it with \(-\Delta Q\). Defining side flux to be \(-\Delta Q\) and then checking that equality tests the definition alone.

This exact torus construction strengthens the comparator's mathematics. It supplies no measured throat, real-time current dynamics, force law, reconnection process, or change to the Q2 verdict.

## 22. Silver/Pell structure and the independent phase clocks

### 22.1 The Pell and silver branches have an exact algebraic connection

S33 correctly retains
\[
x^2-8k^2=1,\qquad
\binom{x_{n+1}}{k_{n+1}}
=\begin{pmatrix}3&8\\1&3\end{pmatrix}
\binom{x_n}{k_n}.
\]
The matrix preserves the form \(x^2-8k^2\). Starting at \((1,0)\), multiplication of quadratic units gives
\[
\boxed{x_n+k_n\sqrt8=(3+\sqrt8)^n=(1+\sqrt2)^{2n}.}
\]
Thus the first five positive pairs are
\[
(3,1),(17,6),(99,35),(577,204),(3363,1189).
\]
There is an actual connection to the silver unit \(1+\sqrt2\); no association of behavioral counts is needed for it. In particular,
\[
(1+\sqrt2)^8=577+408\sqrt2=577+204\sqrt8.
\]
That identity does not select measured observables X and K. S33 records that the ordered observable pair and extraction/exposure rules were unset; \((577,204)\) remains an arithmetic target, not a confirmed empirical prediction. Its \(L=99\) odd-grid example demonstrates connectivity, not a second measured coordinate 35.

### 22.2 Exact beat and gate arithmetic

Under the specific 21-tempo-beat interpretation in S26, keep the declared 39-Hz base and 169-BPM clock. The two tones and their positive difference are
\[
f_P=39\frac{23}{19},\qquad
f_S=39\frac{1+\sqrt2}{2},\qquad
f_B=f_P-f_S=\frac{39(27-19\sqrt2)}{38}.
\]
Because \(27^2-2\cdot19^2=7\),
\[
\boxed{T_B=\frac{38(27+19\sqrt2)}{273},\qquad
T_G=\frac{1260}{169}.}
\]
The timing assumption is explicit: seven nodes times three tempo beats per node. The source itself notes that its historical beat-unit notation did not uniquely establish that reading.

| Quantity | Value under that reading |
|---|---:|
| Difference frequency \(f_B\) | \(0.133361849514\ldots\ \mathrm{Hz}\) |
| Beat-maximum period \(T_B\) | \(7.498396307814\ldots\ \mathrm{s}\) |
| Gate macroperiod \(T_G\) | \(7.455621301775\ldots\ \mathrm{s}\) |
| Period difference \(T_B-T_G\) | \(0.042775006039\ldots\ \mathrm{s}\) |
| Frequency residual \(\Delta f=f_B-1/T_G\) | \(-0.000765134612\ldots\ \mathrm{Hz}\) |
| Relative phase drift per gate | \(-2.053639410621\ldots\) degrees |
| Full relative-phase return time \(1/|\Delta f|\) | \(1306.959563960916\ldots\ \mathrm{s}\) |

The v1.2 values above are recomputed from the exact algebraic expressions at 70-digit decimal precision. They refine the last displayed digits in S26 without changing its timing prediction.

For equal-amplitude, initially aligned tones,
\[
\cos(2\pi f_Pt)+\cos(2\pi f_St)
=2\cos(\pi f_Bt)\cos(2\pi\bar f t),\quad
\bar f=(f_P+f_S)/2.
\]
The signed prefactor has period \(2T_B\), whereas its absolute amplitude and the beat maxima have period \(T_B\). This removes an otherwise easy factor-of-two ambiguity. Linear superposition contains the two input spectral lines; a difference-frequency envelope alone is not evidence of a separately generated nonlinear low-frequency mode.

The source's two mismatch percentages use different denominators:
\[
\frac{T_B-T_G}{T_G}=0.00573728\ldots,
\qquad
1-f_BT_G=0.0057045539183935\ldots.
\]
Both are correct; they are not interchangeable. After j paired returns, the beat maximum is delayed by \(j(T_B-T_G)\). At j gate times, the unwrapped relative phase is instead \(2\pi j\Delta fT_G\). Phase-estimation conventions must say which object is being fitted.

### 22.3 A phase quotient closes even when the full oscillators do not recur

Write each source phase in cycles, \(a_i(t)=a_i(0)+f_it\bmod1\). The triadic relative phase
\[
u(t)=a_P(t)-a_S(t)-a_G(t)\bmod1
\]
is an exact factor with
\[
u(t+t')=u(t)+\Delta f\,t'\bmod1.
\]
Its continuous-time circle flow returns after \(1/|\Delta f|\). Sampled once per gate, however,
\[
\boxed{u_{j+1}=u_j+\Delta fT_G\bmod1}
\]
is an irrational rotation: \(f_BT_G-1\) has a nonzero \(\sqrt2\) coefficient. There is no finite exact gate-index period. The full three-tone phase vector also has no positive common return period, since \(f_P/f_S\) is irrational. A return of a phase combination does not imply simultaneous return of all its source phases.

This is a useful companion to §10: a properly retained relative phase can be autonomous in a specified clock model while the coarser observation is not. A measured value such as \(\cos(2\pi u)\) identifies \(u\) and \(-u\). It admits an autonomous one-step update under rotation by \(\nu\) exactly when \(\sin(2\pi\nu)=0\), that is, \(\nu=0\) or \(1/2\bmod1\). This follows from
\[
\cos(2\pi(u+\nu))-\cos(2\pi(-u+\nu))
=-2\sin(2\pi u)\sin(2\pi\nu).
\]
The actual irrational gate increment fails this condition. Retaining oriented relative phase repairs that reflection loss. It still does not demonstrate physical locking: the specified uncoupled prediction is nonzero phase drift.

### 22.4 The prospective two-clock schema still needs experiment-specific inputs

S07 is valid JSON containing null parameters and formula strings. It is a prospective template. Section 10 already proves the relative catch formula
\[
\delta_n=\frac1q\bigl\|q(\theta_n-g(t_n))\bigr\|_{\mathbb R/\mathbb Z}.
\]
A concrete realization must declare \(q\in\mathbb N_{>0}\), \(T_g>0\), phase units in cycles, timestamp units/origin, both reset semantics, lag, eligibility, \(0\le w<1/(2q)\), and the classifier \(\delta_n\le w\). At a reset boundary the convention must specify which epoch supplies the phase. When finite numerical precision cannot resolve the inequality, record the boundary ambiguity instead of silently rounding toward a preferred prediction.

For uniform no-reset samples, the factor increment is the \(\nu\) in §10. For irregular samples,
\[
u_{n+1}=u_n+q\alpha+\frac{q(t_{n+1}-t_n)}{T_g}\pmod1
\]
between resets. It is driven by the retained time increments; a constant-increment claim needs the extra sampling hypothesis. The unlabelled q-site period remains \(T_g/q\), and a labelled site's period may be \(T_g\). None of these identities supplies the missing experimental origins, periods, reset ledger, raw outcomes, or holdout design. This revision does not choose those values after seeing the old results.

## 23. Evidence composition and the remaining protocol repairs

### 23.1 A usable scale branch has separate fields

S14 correctly treats the four-radius rule as a finite-range scale check. S04 B.20.8 still combines a finite-radius gate with preference for a long-range model. These clauses cannot be integrated by treating an unavailable finite radius as a passed inequality.

Keep model preference, fit validity, diagnostic concordance, and scale result as separate fields. In particular, FR_PREFERRED and ESTIMATOR_DISCORDANT can both be true; the source's demand for exactly one label from a list containing both is not a total, disjoint classification.

| Preconditions and model result | Finite-radius record | Four-radius result | Interpretation |
|---|---|---|---|
| Required fit invalid | Unavailable | INVALID | Scale inference is inadmissible |
| Required diagnostics missing or discordant | Retain all estimates, no selected verdict estimate | UNRESOLVED | No diagnostic substitution |
| Valid, concordant finite-range preference | Estimated \(\xi\) and its stated UCB | CLEARED iff \(L_{\max}\ge4\xi^{\rm UCB}\) | Apply the other Q2 criteria |
| Valid long-range preference | No finite radius established | INAPPLICABLE | Requires a separately specified long-range verdict path |
| Models not distinguished | No model-selected radius | UNRESOLVED | No asymptotic verdict from model choice |

This is a proposed logical repair for future protocol integration, not a retrospective change to a frozen experiment. A failed fit does not establish \(\xi=\infty\). In an implementation, “diagnostics missing” must be an explicit branch if diagnostics are required.

The factor four is a chosen heuristic informed by the finite-size saturation seen in a particular Villain benchmark, not a geometric theorem. The source benchmark at \(t=0.7,J=0.336\), with \(J_c=0.3335(3)\), is confirmed in the primary paper; its couplings and axial ensemble do not transfer automatically to the cosine three-axis constructor. [Coleman, Kuklov and Tsvelik, Fig. 5 and discussion](https://arxiv.org/html/2502.08708v2)

The theoretical alternatives also remain alternatives. The deconfining interpretation discussed by Bonati, Pelissetto and Vicari and the confinement argument of Coleman, Kuklov and Tsvelik cannot be settled by the source's exact parity bookkeeping. Their models, observables, and finite-volume conventions need the declared comparison. [Bonati, Pelissetto and Vicari](https://arxiv.org/abs/2404.07050), [Coleman, Kuklov and Tsvelik](https://arxiv.org/abs/2502.08708)

### 23.2 Agreement needs a tolerance, and resampling must respect paths

A difference-test result \(p\ge0.05\) does not demonstrate the axis or placement equivalence claimed in S03 A.8.5. Define a scientifically meaningful tolerance \(\varepsilon\) prospectively. If a simultaneous confidence interval for every required difference lies wholly inside \((-\varepsilon,\varepsilon)\), it can support the stated equivalence at the interval's simultaneous coverage level. An interval containing zero while extending outside the equivalence band is inconclusive.

For two estimates built from shared or nested samples,
\[
\operatorname{Var}(\widehat a-\widehat b)
=\operatorname{Var}(\widehat a)+\operatorname{Var}(\widehat b)
-2\operatorname{Cov}(\widehat a,\widehat b).
\]
Use the paired difference in the same resampling replicate. The sum-of-variances denominator is justified by independence, not by putting estimates in separate files. Q1, Q2, and Q3 are separate measurement and interpretation requirements; this does not assert statistical independence of their estimators.

When resampling transition blocks, preserve the links among \(W,q,\eta\) within each original block. A concatenation seam between unrelated blocks is not an observed transition or a completed round trip. Transition counts and path statistics must exclude such artificial seams or use a specifically justified path-resampling construction. This sharpens S04's instruction to keep complete transition blocks together.

### 23.3 The historical records remain different evidence sets

| Supplied record | What this revision can verify | Retained empirical status |
|---|---|---|
| S06/S34, 22-call rotating-lattice report | Reported denominators add to 323 rows and 102 failures; reported best exact AUC 0.595 and familywise p 0.5966 fail its stated gates | Reported null; underlying row-level analysis not rerun |
| S16, corrected 40-call / 72-model summary | The text and figures consistently retain failed primary lanes and a separately described q=39 lead | Reported bank failure; later-cohort arriving-lag lead remains prospective |
| S27, URR-RC-001 | Ten candidate rows, zero eligible repeated-successor groups imply no closure decision | Reported execution with insufficient coverage; event ledger not rerun |
| S33, Pell holdout | Exact recurrence and target; definitions of the measured pair remain unset in that record | Arithmetic survives; confirmatory empirical bridge unestablished |
| S26, prime–silver–gate candidate | Exact algebraic periods and uncoupled phase drift | Formal timing prediction; no room/coupling experiment reproduced |
| S29/S39, Corner Relay alpha C6 | Source-binding bytes match the embedded binding and stated digest; the embedded test-output digest matches | Reports 20 software tests; unrelated to Q2 simulation validation |

These rows are not independent replications of one result. The 22-call and 40-call studies have different ledgers and bank definitions. The departing-jump mathematics in §§4–6 does not change the alignment of the reported arriving-jump lead. The Word manuscript's behavioral counts are reported findings from cited underlying records; neither their raw denominators nor their statistical significance is recreated by its illustrations.

### 23.4 Source integrity and mathematical validity have separate receipts

All 17 payload hashes in S28 were recomputed successfully. Fifteen payloads were explicitly supplied among the 39 new files; the receipt also names the adjacent README and poster, which were read for byte verification. All 17 payload entries in S22 agree as well. The Word document has its own matching manifest hash and contains an image byte-identical to the poster; it is not a payload listed in S28.

The source bytes contain existing damage: S01 and S31 each contain seven replacement characters; S04 contains 312 private-use characters; S32 contains 118; S37 contains 396. Other equations use bare brackets or have lost operators. The new report's equations are rederived or reconstructed from the named clean definitions and checked here; the original snapshots remain unchanged. A matching hash of damaged math is still a matching hash.

S20–S22 record a recommended adoption with modification and no governing effect until integration/reissue. This mathematical update does not transform that recommendation into an adopted simulation specification. No external pre-output trust anchor is established by the newly generated local receipt. Likewise, the Corner Relay receipt does not supply a toroidal execution root merely because its filename contains “execution provenance.”

## 24. Retained v1.2 verification, source map, and resulting status

**Historical v1.2 receipt.** The package described in this section is now preserved under v1_2/ in the v1.3 archive. Its v1_1/ paths are relative to that preserved package. The current checks are in §29.

The original v1.1 mathematical revision is retained in §§2–18. Its verification receipt is preserved separately in §17 and in the archive's v1_1 folder. The new verifier checks the additions in §§19–22 and the supplied-file integrity relationships. No toroidal production simulation, empirical bank, or Word-referenced event analysis was executed in this revision.

| New check | Executed coverage and outcome |
|---|---|
| Onsite operator selection | Every monomial through total degree 24; first phase-dependent invariant degree 6 |
| Diamond connectivity | Breadth-first enumeration on 169 rectangular grids with periods 2–14, plus the 99-by-99 grid; all 170 agree with \(\gcd(2,m,n)\) |
| Integer chain identities | L=2,3,4,6; 945 plaquette boundaries and 315 cube boundaries; canonical loop/cut pairing |
| Winding and parity | 960 constructed plaquette/sector/even-loop updates, checked against divergence, membrane constraint, integer cut flux, and parity |
| Finite-anisotropy class | 300 charge-six source transfers preserve every mod-six cut class; L=4 and L=6 counterexamples reproduced |
| Character algebra | All 64 projector cases; \(H^2=8I\); inverse, ratios, probability constraints on a declared algebraic fixture |
| Transition graph and liftability | Twelve single-axis cube edges; four-state noncomposable-lift counterexample |
| Markov distinctions | Exact rational stopping-bias and nonreversible-composition examples; stationary weak example checked on all 510 A/B words of lengths 1–8 |
| Curved field | Independent Cartesian finite differences at 60 points; corrected maximum divergence about \(4.2\times10^{-11}\), uncorrected field about 0.135 at the largest observed residual |
| Curved side flux | Independent surface quadrature agrees with the analytic flux to about \(8.3\times10^{-8}\); curved tangency identity checked |
| Pell and clocks | Twenty exact Pell steps; silver eighth power; timing arithmetic recomputed at 70-digit decimal precision |
| Source integrity | Seventeen receipt payloads, manifest relationships, embedded poster, and Corner Relay binding/test-output hashes verified |

All listed new checks passed. The finite graphs and constructed current updates are not weighted enumeration of the user's entire Q2 ensemble. Numerical differentiation and quadrature check the curved formulas independently; the exact divergence and flux claims rest on the derivations in §21. The probability fixture checks transform algebra, not physical sector values. The verifier's checks on finite word lengths support the explicit stationary-process argument rather than prove it by extrapolation.

The archive contains the full v1.2 report, a concise source/change register, all 39 newly supplied source snapshots, the two receipt-referenced payloads, a portable standard-library verifier, its executed JSON results, original-file identities, and package checksums. The preserved v1.1 subfolder contains its original report, verifier, receipt, and the initial two inputs. Together these snapshots bind the actual material used here; they do not recreate the much larger historical Drive retrieval described in §1.

After extracting the archive, run the new checks with Python 3.10 or later:

~~~text
python verify_v12.py
~~~

The script reads the adjacent sources folder and writes its new result JSON beside the script. The optional earlier check is documented in v1_1/README.md. The Word manuscript was inspected through extracted text/table content, document structure, and all six embedded images. No full Word page-layout render pass is claimed; the delivered report is Markdown.

| Result carried forward or added | Status in Geometry Maximization v1.2 |
|---|---|
| Exact golden slip construction, substitution, complexity and discrepancy | Retained with v1.1 proofs and receipt |
| FH-REF-1 q-only law | Failed on all eight fibers of that named kernel |
| The different compound packet kernel | Requires a fully specified valid kernel before its own closure claim |
| Integer winding/parity and reference-loop transform | Exact with the stated domain and sector definitions |
| Finite-anisotropy current class | Mod-six homology retained; integer-average parity rejected outside its domain |
| Diamond sheet quotient | C2 for both periods even; trivial otherwise |
| Circular-torus throat | Exact formal divergence-free construction on the declared embedded tube |
| Pell–silver link and triadic relative phase | Exact algebraic/formal results; measured bridge remains separate |
| Empirical rotating model, Q2 production and human residual closure | No new empirical confirmation from this mathematical revision |

The concrete advance is additional mathematics with explicit domains, usable constructions, and preserved counterexamples. None of the update's exact quotients, probability identities, or phase laws is used as a substitute for the missing experiment that would establish a physical or platform realization.

## 25. A warped golden screen: what survives exactly

The additional source, **S40 = `_Math2.txt`**, proposes replacing the rigid screen by a nonlinear circle map. That becomes a useful extension once the map, observation, coordinate convention, and measure are all specified. The constructions below are mathematical examples, not fitted experimental dynamics.

### 25.1 Transport the observation together with the map

Let \(h:S^1\to S^1\) be an orientation-preserving homeomorphism, interpreted as **physical coordinate to rotation coordinate**. Fix its phase origin. Define
\[
F=h^{-1}\circ R_\alpha\circ h,\qquad
\alpha=(3-\sqrt5)/2.
\]
Then \(h\circ F^n=R_\alpha^n\circ h\) for every integer n. For the transported bin observation, set
\[
b_h(x)=\lfloor39h(x)\rfloor,\qquad
z_h(x)=\{13h(x)\},\qquad \rho_h(x)=\{39h(x)\},
\]
where fractional parts use the chosen half-open circle chart. Also set
\[
s_h=b_h\bmod3,\qquad
\sigma_h=\mathbf1_{[0,\tau)}(\rho_h),\qquad \tau=15-39\alpha.
\]
These are the original observations composed with h. Consequently,
\[
\boxed{\rho_h(Fx)=\{\rho_h(x)-\tau\},\qquad
\sigma_h(x)-\tau=\rho_h(Fx)-\rho_h(x).}
\]
The second identity uses real representatives in \([0,1)\); it is not just an equality modulo one. It gives
\[
\boxed{\sum_{j=0}^{N-1}\sigma_h(F^{n+j}x)
=N\tau+\rho_h(F^{n+N}x)-\rho_h(F^nx),}
\]
with error strictly below 1 for every start and length. The 9-or-10 return gaps, forbidden word 101, substitution at the appropriately aligned origin, and exact language complexities in §6 all survive **without approximation**.

This is a conjugacy statement about an observed system, not just about its state map. If \(B_h=B\circ h\), its predictive relations satisfy
\[
x\,E_m^{F,B_h}\,y
\quad\Longleftrightarrow\quad
h(x)\,E_m^{R_\alpha,B}\,h(y).
\]
This follows by comparing \(B_h(F^jx)=B(R_\alpha^jh(x))\) at each required j. Thus the coarsest predictive phases remain \(h(x),z_h,\rho_h\) for full bins, pairs, and slips, respectively. A change of coordinates does not turn any of these circle factors into a finite autonomous generator.

### 25.2 The occupation measure and variation transform cleanly

The unique invariant probability is
\[
\mu_h=(h^{-1})_*\lambda,\qquad
\mu_h(E)=\lambda(h(E)).
\]
If h is a \(C^1\) diffeomorphism, then \(d\mu_h=h'(x)\,dx\). With this convention, writing \((h^{-1})'\) as a density in the x-coordinate would reverse the chart. Under \(\mu_h\), the transported process has exactly the original Haar law, including its failure to be a finite-order stationary Markov process.

Smoothness is not required to preserve circular bounded variation. For any BV observable A, orientation preservation maps cyclically ordered partitions bijectively to cyclically ordered partitions, giving
\[
\boxed{\operatorname{Var}(A\circ h^{-1})=\operatorname{Var}(A).}
\]
Applying §8 in the rotation coordinate therefore yields, at its convergent denominators,
\[
\sup_x\left|\sum_{j=0}^{q_n-1}A(F^jx)
-q_n\int A\,d\mu_h\right|\le\operatorname{Var}(A).
\]
The same transport gives the Ostrowski digit-sum bound at arbitrary N. S40's suggestion that \(C^1\) conjugacy is needed merely to pull back an interval indicator with controlled variation is stronger than necessary. Differentiability becomes useful for densities and metric distortion, which are different questions.

If \(0<m\le h'\le M\), a transported bin has physical width between \(1/(39M)\) and \(1/(39m)\), while its invariant probability is exactly \(1/39\). Probability and coordinate width need not agree.

### 25.3 Keeping the old coordinate bins changes the observation

The fixed physical-coordinate observation \(b_{\rm phys}(x)=\lfloor39x\rfloor\) is generally different from \(b_h\). Its stationary bin probabilities are
\[
\boxed{\mu_h\bigl([j/39,(j+1)/39)\bigr)
=h((j+1)/39)-h(j/39),}
\]
using a degree-one lift of h. They are not generally uniform. Nor does its departing jump have to lie in \(\{14,15\}\).

Here is a concrete analytic example:
\[
H_\epsilon(x)=x+\frac{\epsilon}{2\pi}\sin(2\pi x),\qquad
0<\epsilon<1,\qquad
\widetilde F_\epsilon(x)=H_\epsilon^{-1}(H_\epsilon(x)+\alpha).
\]
The lift is strictly increasing because \(H_\epsilon'=1+\epsilon\cos(2\pi x)>0\), and it commutes with integer translation. Hence it defines an analytic circle diffeomorphism of exactly the prescribed rotation number. At \(\epsilon=1/4\),
\[
H(13/39)=0.367791389297\ldots
<\alpha<0.389794911128\ldots=H(14/39).
\]
Since \(H(0)=0\), its first image satisfies
\[
13/39<F(0)<14/39,
\qquad \boxed{b_{\rm phys}(F(0))-b_{\rm phys}(0)=13.}
\]
The numerical root is \(F(0)=0.349737755708\ldots\). The strict bracket has margins exceeding 0.006 in H-coordinates; the verifier also checks those endpoints using high-precision Taylor arithmetic. This is a robust counterexample to carrying the old jump rule over to unchanged coordinate bins. In the transported bins the same step still has its correct original label.

There is also a sharp bounded-remainder distinction. A fixed physical bin pulls forward to an interval of length
\(\ell_j=H((j+1)/39)-H(j/39)\). By the interval criterion already used in §8.4, its centered occupation has bounded all-time discrepancy precisely when \(\ell_j\in\mathbb Z+\alpha\mathbb Z\). No such assertion follows just from knowing the rotation number. The special slip coboundary is preserved by transporting its observation.

### 25.4 Approximate phase coordinates give a finite-horizon certificate

Exact conjugacy is stronger than a fitted phase coordinate. Suppose instead that chosen degree-one lifts obey
\[
\left|H(\widetilde F(x))-H(x)-\alpha\right|\le e
\quad\text{for all }x.
\]
Summing these one-step residuals gives
\[
\left|H(\widetilde F^{,n}(x))-H(x)-n\alpha\right|\le ne.
\]
Let \(\mathcal D_{39}=\{j/39:0\le j<39\}\), and put
\(y_n=\{H(x)+n\alpha\}\). The observed and ideal transported bin labels are equal whenever
\[
\boxed{\operatorname{dist}_{S^1}(y_n,\mathcal D_{39})>ne.}
\]
The margin condition matters because a discontinuous bin observation can change under an arbitrarily small phase error at a boundary.

If the **initial rotation coordinate** is Haar distributed, the probability that any of the first N labels fails this sufficient certificate is at most
\[
\boxed{\min\{1,\,39eN(N-1)\}.}
\]
Indeed, the boundary neighborhood at time n has measure at most \(78ne\); sum over \(n=0,\ldots,N-1\). This bounds a possible-error cover, not the probability of an actual mismatch. It does not assume that the approximate map preserves Haar, and it gives no infinite-time label guarantee. The verified fixture uses \(e=10^{-6},N=64\), for which the bound is 0.157248.

## 26. Arithmetic constants and correctly scoped linearization

S40's arithmetic discussion is useful once the different series and the quantifiers in the linearization theorems are kept separate. In this section \(\mathcal B_Y\) denotes the **Gauss-map Brjuno function**, avoiding the existing physical-field symbol \(\Phi\).

### 26.1 The relevant theorem depends on the category

The following distinctions are the ones used here:

| Object and assumptions | Guaranteed conclusion |
|---|---|
| Circle diffeomorphism; irrational rotation number; \(\log F'\) of bounded variation | Topological conjugacy to rotation |
| \(C^\infty\) circle diffeomorphism; Diophantine rotation number | \(C^\infty\) conjugacy |
| Analytic circle diffeomorphism on a specified strip; Brjuno angle; sufficiently small analytic perturbation | Analytic conjugacy on a smaller strip |
| Analytic circle diffeomorphism, without smallness | The universal arithmetic class is Herman's \(\mathcal H\), with \(\mathrm{CD}\subsetneq\mathcal H\subsetneq\mathcal B\) |

These are universal guarantees for classes of maps. They do not say that an individual linearizable map must have a Diophantine angle; rigid rotations are counterexamples to that reading. S40's unqualified “analytic needs Brjuno” loses the local/global distinction, while “every Liouville angle has arbitrarily small non-linearizable analytic perturbations” is too broad. The non-Brjuno counterexample theorem has the narrower hypothesis \(\alpha\notin\mathcal B\). [Eliasson–Fayad–Krikorian, Theorems 2, 4, 6, 7 and 9](https://arxiv.org/html/1810.07107v1)

For holomorphic germs, Brjuno is sufficient for all germs with that multiplier. Its necessity has a universal or specified-family meaning: outside Brjuno, the quadratic \(e^{2\pi i\omega}z+z^2\) fails to linearize. An individual germ such as the rigid linear map remains linearizable at any irrational multiplier. [Buff–Chéritat, introduction](https://arxiv.org/abs/math/0401044)

The golden angle is bounded type, so the smooth/analytic circle guarantees apply when their map hypotheses are met. For the explicit \(F_\epsilon\) in §25, the conjugacy is already supplied by construction. None of these theorems says that a state-dependent perturbation automatically keeps the same rotation number.

### 26.2 Two explicit Brjuno evaluations and a period-eight formula

For \(0<\omega<1\) irrational, define
\[
x_0=\omega,\quad x_{n+1}=\{1/x_n\},\quad
\beta_{-1}=1,\quad \beta_n=\prod_{j=0}^{n}x_j,
\]
\[
\mathcal B_Y(\omega)=\sum_{n\ge0}\beta_{n-1}\log(1/x_n).
\]
The series has the exact functional equation
\[
\mathcal B_Y(\omega)=\log(1/\omega)+\omega\mathcal B_Y(\{1/\omega\}).
\]
It is a different numerical function from \(\sum_n(\log q_{n+1})/q_n\), although the two have the same convergence condition. Natural logarithms and the Gauss-map convention are fixed throughout.

Put \(\varphi=(1+\sqrt5)/2\) and \(g=\varphi^{-1}\). Since \(\{1/g\}=g\),
\[
\mathcal B_Y(g)=\frac{\log\varphi}{1-g}=\varphi^2\log\varphi.
\]
The golden screen has \(\alpha=g^2\) and \(\{1/\alpha\}=g\). Therefore
\[
\boxed{\mathcal B_Y(\alpha)=2\log\varphi+g^2\mathcal B_Y(g)
=3\log\varphi=1.443635475178810\ldots.}
\]
This is the explicit constant that S40 leaves unevaluated. For the silver reciprocal \(d=\sqrt2-1=[0;\overline2]\), the same fixed-point calculation gives
\[
\boxed{\mathcal B_Y(d)=\frac{\log(1+\sqrt2)}{2-\sqrt2}
=1.504598827159773\ldots.}
\]

For any periodic Gauss orbit of period p, let
\[
b=\prod_{j=0}^{p-1}x_j,\qquad
A=\sum_{n=0}^{p-1}\left(\prod_{j=0}^{n-1}x_j\right)\log(1/x_n).
\]
Grouping the nonnegative series into periods proves
\[
\boxed{\mathcal B_Y(\omega)=\frac{A}{1-b}.}
\]
For the slip angle \(\tau=[0;\overline{9,1,2,9,2,1,9,87}]\), p is 8. Each \(x_j\) is an explicitly computable number in \(\mathbb Q(\sqrt5)\), and
\[
\boxed{b=\varphi^{-28}=\Lambda^{-1},\qquad
\mathcal B_Y(\tau)=2.443440158975292\ldots.}
\]
Here \(\Lambda\) is exactly the substitution eigenvalue from §6.4. To see the link, let \(a_{j+1}=\lfloor1/x_j\rfloor\). Then
\[
\begin{pmatrix}a_{j+1}&1\\1&0\end{pmatrix}
\binom{1}{x_{j+1}}
=x_j^{-1}\binom{1}{x_j}.
\]
Multiplying through a period makes the continued-fraction matrix's positive eigenvalue \(b^{-1}\). Section 6.4 identifies that eigenvalue with \(\varphi^{28}\). Thus the word-growth factor and the arithmetic tail contraction have a precise common origin; they are not two unrelated numerical coincidences.

The first-return gap angle \(\eta=\{1/\tau\}\) has
\[
\mathcal B_Y(\eta)
=\frac{\mathcal B_Y(\tau)-\log(1/\tau)}{\tau}
=1.679832851941722\ldots.
\]
After k complete periods, the uncomputed nonnegative tail is exactly \(b^kA/(1-b)\). This supplies a usable error formula for numerical evaluation, rather than interpreting a truncated positive sum as the full value.

### 26.3 Bounded type, Liouville, and Fourier division

A uniform partial-quotient bound \(a_n\le A\) gives the nonoptimal but explicit estimate
\[
\left|\omega-\frac pq\right|>\frac1{(A+2)q^2}
\quad(q\ge1).
\]
Choose \(q_n\le q<q_{n+1}\). The continued-fraction best-approximation property and the exact error identity give
\[
\|q\omega\|\ge\|q_n\omega\|
=\frac1{q_{n+1}+q_nx_{n+1}}
>\frac1{(A+2)q_n}\ge\frac1{(A+2)q}.
\]
Dividing by q proves the stated rational-approximation bound. Thus the constants \(1/4\) and \(1/89\) are valid for \(\alpha\) and \(\tau\), respectively. Finite checks through \(q=10000\) supplement this argument; they do not establish its universal quantifier.

Unbounded partial quotients alone do not imply Liouville approximation. For example \([0;1,2,3,\ldots]\) has unbounded digits but \(q_{n+1}\le Cq_n^2\), so it has a finite Diophantine exponent. Conversely, Liouville does not imply non-Brjuno. A concrete construction begins with \(a_1=2\) and chooses \(a_{n+1}=q_n^n\). Its convergents satisfy
\[
\left|\omega-p_n/q_n\right|<q_n^{-n-2},\qquad
q_n^{n+1}\le q_{n+1}\le2q_n^{n+1}.
\]
The first inequality makes the limit Liouville. The second gives
\((\log q_{n+1})/q_n\le[\log2+(n+1)\log q_n]/q_n\), a summable sequence because \(q_n\) eventually grows at least doubly exponentially. This repairs S40's approximation ladder with an explicit witness.

For a centered periodic observable a, the rotation cohomological equation is
\[
W(y+\alpha)-W(y)=a(y).
\]
In Fourier coefficients,
\[
\widehat W(k)=\frac{\widehat a(k)}{e^{2\pi i k\alpha}-1}\quad(k\ne0),
\qquad \widehat a(0)=0.
\]
Since \(|e^{2\pi it}-1|\ge4\|t\|\), the bound for \(\alpha\) implies a denominator lower bound \(1/|k|\). Smooth a therefore has a smooth solution; analytic a has an analytic solution on any strictly narrower strip. This is a directly usable small-divisor calculation. It does not say every BV observable has a bounded solution: §8's strand/bin counterexamples remain in force.

The approximation function in S40's Bruno–Rüssmann formula must use \(\|k\omega\|\), the distance to an integer. Literal \(|k\omega|\) would have no small divisors for a nonzero scalar \(\omega\). Nor are general bounded-type denominators always asymptotic to \(c\varphi^n\): the silver denominators grow at rate \((1+\sqrt2)^n\), and periodic continued fractions can have other rates.

## 27. Automorphic measures with the Jacobian repaired

S40 repeatedly changes the density and coordinate conventions, and gives contradictory statements about existence. This section fixes one convention and derives its consequences. They provide a useful measure theory for the explicit warped screen, while retaining the ordinary invariant measure for occupation statistics.

### 27.1 The set identity determines the density equation

For an orientation-preserving circle diffeomorphism F, define an s-conformal probability by
\[
\boxed{\mu_s(F(E))=\int_E F'(x)^s\,d\mu_s(x).}
\]
Its equivalent test-function equation is
\[
\int\psi\,d\mu_s=\int\psi(Fx)F'(x)^s\,d\mu_s(x).
\]
For \(C^2\) F of irrational rotation number, there is a unique such probability for **every real s**. No proximity-to-rotation assumption is needed. This is the Douady–Yoccoz theorem in the form explicitly recalled by [Goncharuk–Yampolsky, Theorem 9](https://arxiv.org/html/2404.03780v1). S40's earlier restriction to a special family produced by Loewner theory is therefore rejected.

If \(d\mu_s=w_s(x)\,dx\), changing variables on the left gives
\[
\int_E w_s(Fx)F'(x)\,dx
=\int_E F'(x)^s w_s(x)\,dx.
\]
Thus the correct density relation is
\[
\boxed{w_s(Fx)F'(x)=F'(x)^s w_s(x),\qquad
w_s(Fx)=F'(x)^{s-1}w_s(x).}
\]
The formula \(w_s(Fx)F'(x)^s=w_s(x)\) printed several times in S40 is incorrect for this definition. It drops the ordinary change-of-variables Jacobian and places the exponent on the wrong side. At \(s=0\) it would even lose the usual invariant-density equation.

An immediate control is
\[
\boxed{\mu_1=\lambda\quad\text{for every orientation-preserving }C^1
\text{ circle diffeomorphism}.}
\]
This is simply the arc-length substitution formula. Under the stated uniqueness hypotheses, the s=1 measure must therefore be Lebesgue. S40's claim that a Liouville angle can make **every** \(\mu_s\) singular to Lebesgue cannot hold.

An s-conformal probability is generally not invariant under F. It should not be called an equilibrium occupation measure just because it is a fixed point of a weighted operator. Invariance is a requirement in the definition of an equilibrium state. In particular, a 2-conformal measure is still supported on a circle; its exponent does not make it ordinary planar area measure or a dimension-two measure on that circle.

### 27.2 The whole family is explicit for a smooth conjugacy

Retain the convention \(F=h^{-1}R_\alpha h\), with h a \(C^1\) diffeomorphism and \(h'>0\). Differentiating the conjugacy gives
\[
h'(Fx)F'(x)=h'(x).
\]
Substitution into the density equation proves
\[
\boxed{d\mu_s(x)=\frac{h'(x)^{1-s}}{Z_s}\,dx,\qquad
Z_s=\int_0^1 h'(x)^{1-s}\,dx.}
\]
The density is positive and normalizable for every real s because h' is bounded above and away from zero. The theorem's uniqueness identifies this constructed measure with its canonical probability whenever F meets that theorem's hypotheses.

Equivalently, if \(k=h^{-1}\) maps rotation coordinates into physical coordinates,
\[
\mu_s=k_*\left(\frac{k'(y)^s}{\int_0^1k'(u)^s\,du}\,dy\right).
\]
The extra weight is taken **before** pushing forward. Writing a bare \(|h'|^s\,dx\) without fixing these chart roles is not an equivalent formula.

For the explicit sinusoidal h in §25.3, write \(d(x)=1+\epsilon\cos(2\pi x)\). Four cases are especially transparent:

| Exponent | Normalized density in x | Role |
|---:|---|---|
| 0 | \(d(x)\) | Invariant occupation probability |
| 1 | 1 | Arc length |
| 2 | \(\sqrt{1-\epsilon^2}/d(x)\) | 2-conformal probability |
| −1 | \(d(x)^2/(1+\epsilon^2/2)\) | Infinitesimal conjugacy obstruction |

The normalizers follow by integrating cosine powers and \(\int_0^1[1+\epsilon\cos(2\pi x)]^{-1}dx=(1-\epsilon^2)^{-1/2}\). These measures are distinct for \(0<\epsilon<1\). The notes' squared-derivative candidate corresponds here to \(s=-1\), not \(s=2\).

For \(\epsilon=1/4\), independent quadrature and test functions verify the correct s=2 law. The unnormalized wrong squared-derivative candidate has a pointwise residual exceeding 3 in the same test. A normalization constant cannot repair a failed homogeneous Jacobian equation.

The transformed slip sequence should still be evaluated with \(\mu_0\) when claiming stationary Haar-derived statistics. Starting it under \(\mu_2\) is a different, generally nonstationary ensemble. Its pointwise telescoping count identity survives because that identity is deterministic.

### 27.3 Weighted empirical measures and their endpoint error

Let \(w_k=(F^k)'(x)^s\), \(S_N=\sum_{k=0}^{N-1}w_k\), and
\[
\nu_N=\frac1{S_N}\sum_{k=0}^{N-1}w_k\,\delta_{F^kx}.
\]
The derivative chain rule gives the exact residual
\[
\boxed{\int\psi\circ F\,F'^s\,d\nu_N-\int\psi\,d\nu_N
=\frac{w_N\psi(F^Nx)-\psi(x)}{S_N}.}
\]
Thus \((w_N+1)/S_N\to0\) is a sufficient endpoint condition for weak limits to be automorphic. Divergence of \(S_N\) by itself does not supply it: for \(w_k=2^k\), the ratio \(w_N/S_N\) approaches 1. S40's existence sketch needs the derivative control, not just an infinite weight sum.

For the constructed conjugate rotation,
\[
(F^k)'(x)=\frac{h'(x)}{h'(F^kx)}.
\]
All \(w_k\) are bounded above and away from zero uniformly in k; therefore the endpoint error is \(O(\|\psi\|_\infty/N)\) for every start. Equidistribution in h-coordinates directly gives the limit density \(h'^{1-s}/Z_s\), providing another derivation of §27.2. This argument is specific to the declared smooth conjugacy; it is not a replacement proof for every map in the Douady–Yoccoz theorem.

With the image-measure convention in §27.1, the same measure is automorphic of exponent s for \(F^{-1}\). Indeed,
\(\mu_s(F^{-1}E)=\int_E[(F^{-1})']^s\,d\mu_s\).
Merely passing to the inverse does **not** reverse the exponent to −s. A claimed reduction of all negative exponents to positive ones needs an additional construction.

### 27.4 Change of coordinates preserves the exponent with a weight

Let \(\widetilde F=\phi F\phi^{-1}\), where \(\phi\) is a \(C^1\) orientation-preserving diffeomorphism. The correct normalized covariance law is
\[
\boxed{\widetilde\mu_s
=\frac{\phi_*\bigl(\phi'^s\mu_s\bigr)}{\int\phi'^s\,d\mu_s}.}
\]
The derivative weight is evaluated at the source x, then pushed forward. To verify it, use
\[
\widetilde F'(\phi x)=\frac{\phi'(Fx)F'(x)}{\phi'(x)}
\]
and apply the original image-measure identity. The two factors \(\phi'(x)^s\) cancel on the required side. The exponent remains s; the measure and its metric-dependent density transform. S40's assertion that the exponent itself is not invariant under such a coordinate change is therefore replaced by this precise covariance rule.

### 27.5 A concrete tangent obstruction and the critical boundary

For a differentiable change of coordinates \(k_t=\mathrm{id}+tw+o(t)\), the induced family satisfies
\[
k_tFk_t^{-1}=F+tv+o(t),\qquad
v=w\circ F-F'w.
\]
The s=−1 identity immediately implies
\[
\boxed{\int v(F^{-1}y)\,d\mu_{-1}(y)=0.}
\]
This is a necessary condition for a perturbation to be tangent to a conjugacy orbit. It does not by itself prove that a finite perturbation preserves the rotation number.

For the smooth golden conjugate, put \(y=h(x)\),
\[
A(y)=h'(Fx)v(x),\qquad W(y)=h'(x)w(x).
\]
The tangent equation becomes \(A(y)=W(y+\alpha)-W(y)\). Its zero-mean condition is exactly the displayed \(\mu_{-1}\) obstruction, up to the positive normalizer. For smooth v and h, the Fourier construction in §26.3 supplies a smooth w when that mean is zero. This gives a complete linearized test in this specific smooth, bounded-type setting; it is not a nonlinear deformation theorem.

For a multicritical circle **homeomorphism**, the negative-exponent equation is written as
\[
\int\psi\,d\mu_s
=\int \bigl[F'(F^{-1}y)\bigr]^{-s}\psi(F^{-1}y)\,d\mu_s(y),
\quad s<0.
\]
The exponent \(-s\) is positive and acts on the **forward derivative evaluated at the inverse point**. At a critical value its weight vanishes. It is not a positive power of the infinite derivative of the inverse, as S40 says. The existence/uniqueness extension uses the hypotheses of the multicritical theory, and the associated tangent-space results have their own family assumptions. [Goncharuk–Yampolsky, Definition 1 and Theorem 2](https://arxiv.org/html/2404.03780v1)

For the Arnold lift \(F_{a,b}(x)=x+a+b\sin(2\pi x)\),
\[
F'_{a,b}(1/2)=1-2\pi b.
\]
At \(b=1/(2\pi)\) there is a cubic critical point while the map remains increasing. Beyond that value it ceases to be monotone and is outside the circle-homeomorphism theorem. Adding a nonmonotone **observation** to a rigid rotation also does not create a critical point of the evolution map. Both distinctions correct S40's final proposed application.

Finally, Riesz representation applies to suitable continuous functionals on \(C^0\), or positive functionals; it does not turn an arbitrary distribution into a measure. Uniqueness of automorphic probabilities cannot by itself establish a uniqueness theorem for all distributions. The order-one invariant-distribution result for multicritical maps is a substantive additional theorem. [de Faria–Guarino–Nussenzveig](https://arxiv.org/abs/2306.13524)

## 28. Complex geometry and renormalization: the qualified crosswalk

The remainder of S40 is a survey of Siegel disks, hedgehogs, conformal measures, and renormalization. Its named theories are useful context. They become additions to this report only with the relevant object and theorem hypotheses stated.

### 28.1 What the Brjuno constant says about a chosen quadratic

If one separately chooses the complex polynomial
\[
P_\alpha(z)=e^{2\pi i\alpha}z+z^2,
\]
then the golden angle is Brjuno and its fixed point has a Siegel disk. Its conformal radius r is the derivative at zero of the normalized disk uniformization. The established compensated size function is
\[
\Upsilon(\omega)=\mathcal B_Y(\omega)+\log r(\omega)
\quad\text{on Brjuno angles}.
\]
It has a continuous, one-periodic extension, hence is bounded. For this particular golden polynomial,
\[
\boxed{r(\alpha)=\varphi^{-3}e^{\Upsilon(\alpha)}.}
\]
The exact arithmetic factor is now known; the unknown remainder is not numerically supplied by the notes. No radius is computed in this revision. At a non-Brjuno point, the continuous extension is not defined by performing the indeterminate operation \(+\infty+(-\infty)\). [Buff–Chéritat](https://arxiv.org/abs/math/0401044)

S40's blanket statement that the Hölder exponent has not been proved misses an established restricted result: the Marmi–Moussa–Yoccoz one-half Hölder assertion is proved on an appropriate high-type class. That restricted theorem is not a global assertion and supplies no estimate here for the golden angle. This report does not assume a global one-half Hölder theorem. [Cheraghi–Chéritat](https://arxiv.org/abs/1210.5384)

The notes also reverse a boundary fact. Bounded-type Siegel disks of rational maps are quasidisks with a critical point on their boundary. Thus “bounded type, often not even a quasicircle” cannot describe that class. [Zhang](https://arxiv.org/abs/0810.2733)

Existence theorems for other parameters with smooth or prescribed-regularity boundaries concern specified holomorphic families and their nondegeneracy assumptions. They do not follow from an intermediate-value argument on r: continuity of \(\Upsilon\) does not make r continuous. The general-family construction requires its approximation lemmas. [Avila–Buff–Chéritat](https://arxiv.org/abs/1911.10056)

Keeping the golden multiplier in a holomorphic germ also precludes **local nonlinearizability**, by Brjuno sufficiency. One cannot enter a Cremer regime simply by adding analytic nonlinear terms while retaining that multiplier. A larger linearizable hedgehog extending beyond a linearization domain is a separate notion.

### 28.2 A hedgehog invariant needs a neighborhood map

For a holomorphic germ and a specified admissible domain, the Siegel compact is a full invariant continuum; its outside uniformization supplies an analytic circle map in the prime-end coordinate. This does not identify the compact itself with a circle or make the uniformization a homeomorphism on its entire boundary.

Biswas's conjugacy criterion uses a conformal map **between neighborhoods of the hedgehogs**, fixing the indifferent point, together with equality of rotation numbers. A conformal equivalence of their exterior domains alone is inadequate: exterior Riemann uniformization is already available for every such nontrivial full continuum. The subgroup correspondence is stated for **germs of families of hedgehogs**. Its centralizer identification applies to a nonlinearizable germ with that hedgehog germ, not literally to every group element—the identity's centralizer is the whole ambient group. [Biswas, Theorems 3.7–3.10 and following remark](https://arxiv.org/html/0903.2394v1)

The source's proof sketch through “two rotations commute” is replaced by the actual local ingredient: the commutator is tangent to the identity and preserves the common hedgehog; the corresponding rigidity theorem forces that commutator to be the identity. This is a theorem about holomorphic germs, not a generic rule that two maps preserving a labeled set commute.

The prime-end circle map's unique invariant measure cannot simply be asserted to be a unique occupation measure on K. The point 0 is fixed, so \(\delta_0\) is already invariant and the whole nontrivial K is not minimal. Even the linearizable Siegel-compact example of a closed rotation disk has many invariant probabilities, including uniform probabilities on concentric circles. S40's blanket compact-dynamics claim is not imported as a theorem about nonlinearizable hedgehogs.

### 28.3 The Loewner generator is a distinct, normalized evolution

In Biswas's exterior-chart convention, write
\[
\phi_t(z)=e^tz+a_0(t)+a_1(t)/z+\cdots.
\]
The coefficient is the logarithmic capacity \(\operatorname{cap}(K_t)\); therefore
\[
\boxed{\operatorname{cap}(K_t)=e^t,\qquad t=\log\operatorname{cap}(K_t).}
\]
Calling capacity itself t would conflict with this normalization. Shrinking a germ's compact to its fixed point corresponds to \(t\to-\infty\) in this coordinate, not \(t\to0^+\). A radius-parametrized family can use a different parameter, but it must be distinguished.

For a probability \(\nu\) on the circle, the exterior Herglotz transform is
\[
(\mathcal H\nu)(z)=\int_{S^1}\frac{\xi+1/z}{\xi-1/z}\,d\nu(\xi),
\qquad |z|>1.
\]
With \(r(z)=\bar z\), the theorem identifies the local generator as
\[
\boxed{\chi(z)=z\,\mathcal H(r^*\mu_{2,g})(z),\qquad
X(g)=g'\chi-\chi\circ g.}
\]
The 2-conformal probability is determined by the current circle map. This is a local semigroup on the domains where it is defined, with a specified right derivative and forward uniqueness. It does not assert an unrestricted global two-sided flow. [Biswas, Theorems 1.1–1.3](https://arxiv.org/html/1603.00830v2)

For the actual rigid complex rotation \(g(z)=az\), Haar gives \(\mathcal H\lambda=1\). Hence \(\chi(z)=z\) and
\[
\boxed{X(g)(z)=az-az=0.}
\]
The associated round hulls may expand with capacity while the induced circle map stays fixed. This checks the normalization and explains why the generator adds no time dependence to the original rigid screen. A general analytically conjugate map need not have a radial driver in the exterior chart; the smooth circle conjugacy is not automatically that exterior uniformization.

### 28.4 Return induction, predictive refinement, and a trivial zeta

The RG dictionary in S40 is an analogy, not a proved equivalence. Predictive refinement adds future output distinctions at fixed time steps; first-return induction changes the time step; renormalization additionally specifies a rescaling and a space of maps or couplings. A stabilized predictive partition does not by itself define a renormalization fixed point, and a retained-output obligation is not automatically an unstable eigenvector.

If a genuine renormalization step changes a length scale by b and a linearized coupling by \(\lambda\), its scaling exponent is
\[
y=\frac{\log|\lambda|}{\log b},
\]
not the eigenvalue itself. The substitution eigenvalue \(\varphi^{28}\) is a word-growth quantity; §26 proves its relation to a Brjuno tail factor. No spatial scale or thermodynamic critical exponent follows from that identification.

Similarly, uniformizing an annulus preserves its conformal modulus \((2\pi)^{-1}\log(R/r)\). Normalizing a cylinder's circumference is permissible; setting every annulus's modulus to 1 by conformal uniformization is not.

A precise dynamical zeta can be defined here without any operator-trace assumption:
\[
\zeta_T(z)=\exp\left(\sum_{n\ge1}\frac{\#\operatorname{Fix}(T^n)}n z^n\right).
\]
For the irrational rotation, \(n\alpha\notin\mathbb Z\) for every positive n, so
\[
\boxed{\zeta_{R_\alpha}(z)=1.}
\]
The same holds for its conjugates and for the compact Sturmian shift in §6.1: a periodic symbolic point would have rational symbol frequency, contradicting that system's irrational frequency. This zeta records no nontrivial periodic points; it does not encode the nonzero Brjuno function or the infinite predictive memory. Replacing a periodic-point count by the trace of an arbitrary transfer operator requires a separate trace theorem.

## 29. v1.3 source review, checks, and status

S40 contains 2,212 lines and 15,529 whitespace-separated words. Its 112,884 original bytes have SHA-256

~~~text
d29446d8099ffcf140f2d54940f89f92615becf9658b796f216bc74a6c881c00
~~~

It is a compilation of explanations with repeated topics and contradictory intermediate claims. All of it was read; the mathematical review concentrated on the proposed extension to the screen, arithmetic, measure formulas, and the complex-dynamical crosswalk. Historical anecdotes and every survey-level proof estimate have not been independently certified. The source's repository-placement suggestions and instructions were treated as content, not executed.

| New verification | Scope |
|---|---|
| Quadratic arithmetic | Exact period-eight Gauss orbit, period product \(\varphi^{-28}\), and correspondence with the existing substitution eigenvalue |
| Brjuno values | 110-digit decimal calculations; independent long positive-series checks and the exact periodic-tail formula |
| Small divisors | Rational-approximation bounds checked for every denominator through 10,000 for \(\alpha\) and \(\tau\) |
| Transported screen | 9,000 constructed departures; original jump and phase laws agree under the explicit conjugacy |
| Unchanged physical bins | First jump 13, checked with a strictly separated high-precision endpoint bracket; nonuniform invariant bin masses |
| Conformal measures | Six exponents, 4,096 quadrature points and four test functions; density/Jacobian identities and change-of-coordinate covariance |
| Incorrect density control | The source's squared-derivative candidate fails the s=2 equation; the corrected density passes |
| Approximate phase coordinate | 4,096 initial phases over 64 observations; every certified bin label agrees; the analytical bad-set cover is checked by interval union |
| Infinitesimal conjugacy | Weighted obstruction vanishes for a constructed tangent vector; a four-mode Fourier solution satisfies the cohomological equation |
| Critical/Loewner controls | Critical weight and Arnold monotonicity checks; numerical Haar Herglotz transform and zero rigid-map generator |

All listed constructed checks passed. They support the accompanying exact derivations; finite sampling is not used to prove a universal theorem. No unknown map was linearized from data, and no Siegel radius, hedgehog, toroidal production run, or empirical bank was computed.

The portable archive includes this complete report, a source/change register, S40's exact snapshot, a standard-library verifier, its executed JSON receipt, and checksums. The complete v1.2 verification package is preserved under **v1_2/**, including its earlier **v1_1/** folder. Its original checksums are retained. From the extracted v1.3 archive, run:

~~~text
python verify_v13.py
~~~

Earlier checks can be rerun using the commands in the preserved version folders. Prior mathematical and empirical statuses remain those stated in §§16–24. The new result is a specified extension of the observed circle system, with correct measures, arithmetic constants, and finite-horizon error bounds. The complex survey supplies qualified connections rather than a replacement for those constructions.


