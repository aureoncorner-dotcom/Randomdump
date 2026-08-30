# Audit Addendum E-01 – E-11

## Defect register against *The Clock as a Bifurcation Machine*

**Addendum version:** A-1.0
**Issued:** 2026-08-28T23:04:05−04:00 (America/New_York, UTC−04:00)
**Status:** open defect register; five entries blocking
**License:** CC0 1.0 Universal — Public Domain

### Parent of record

| Field | Value |
|---|---|
| Filename | `CLOCK_AS_BIFURCATION_MACHINE_CONSOLIDATED_NOTE_v0_1.md` |
| Declared version in header | 0.1.1 |
| Declared date in header | 2026-08-29 (unqualified; see E-11) |
| Size | 39409 bytes |
| SHA-256 | `fcc25e1f7dadfcb78edc694d4d1e9b350b4c17cb15c5e7fcb3c97d3ae30c2479` |

The parent file is **not modified** by this addendum. All repairs land in v0.2.

**Byte convention.** Offsets are zero-indexed, inclusive, over the parent file's raw bytes (UTF-8, LF line endings), verified against the SHA-256 above. Any edit to the parent invalidates every offset in this register.

### Status semantics

| Status | Meaning |
|---|---|
| **BLOCKING** | No confirmation run may be evaluated, and no clock verdict may be issued, until the entry is resolved. A run already in flight is demoted to exploratory. |
| Non-blocking | Must be resolved before the v0.2 freeze. Does not invalidate a run in progress. |

### Provenance of two entries

E-01 and E-05 supersede an earlier audit formulation that was itself defective. The superseded claims are recorded inside those entries so the correction is auditable rather than silent.

---

## E-01 — BLOCKING — The winding register is undefined at the clock's operating point

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §3.4 signed winding vs parity | 7888–8772 | 272–300 |
| §3.4 boxed \(W_\alpha\) definition | 7985–8040 | 278 |
| §3.5 finite anisotropy | 8773–9280 | 301–318 |
| §3.5 boxed \((\nabla\!\cdot I)_i=-6n_i\) | 8906–8956 | 306 |
| §8 \(V_{\rm tooth}\) | 16989–17058 | 646 |
| §9.1 state box | 17259–17379 | 663 |
| §12 tooth-removal row | 21881–22027 | 847 |
| §12 slip-ledger row | 22416–22549 | 851 |
| §15.1 authoritative register box | 28577–28734 | 1077 |

**Defect.** §3.4 conditions the signed winding on \(h_6=0\). §3.5 establishes that at finite anisotropy the integer current is leaky, \((\nabla\!\cdot I)_i=-6n_i\). But D1 operates at \(\kappa_3\neq0\): §8 introduces the tooth potential and §12 sets \(\kappa_3=0\) as the *null*. The operating regime is therefore the finite-\(h_6\) regime, where §9.1 and §15.1 carry \(W\) as a register coordinate whose defining conservation law does not hold, while §12 demands a signed \(\Delta W\) per slip and §3.4 states that parity cannot supply sign. The register is caught between its own two theorems.

**Superseded claim.** An earlier formulation proposed retaining \(W\bmod 6\) on the averaged winding. That is wrong: at finite \(h_6\) the averaged quantity

\[
W_\alpha=\frac1L\sum_k F_{\alpha,k}
\]

need not remain an integer, because the cuts no longer agree.

**Required repair.** Work with cut flux rather than an average. For the dual cut \(\Sigma_{\alpha,k}\),

\[
F_{\alpha,k}
=
\sum_{\ell\pitchfork\Sigma_{\alpha,k}} I_\ell,
\qquad
F_{\alpha,k+1}-F_{\alpha,k}
=
-6\sum_{i\in\text{slab}}n_i,
\]

so the cut-independent invariant is

\[
\boxed{r_\alpha=F_{\alpha,k}\bmod6.}
\]

The Chinese-remainder split \(\mathbb Z_6\cong\mathbb Z_2\times\mathbb Z_3\) gives

\[
q_\alpha^{(2)}=r_\alpha\bmod2,
\qquad
c_\alpha^{(3)}=r_\alpha\bmod3.
\]

This recovers what parity alone discards — \(r_\alpha\) distinguishes \(+1\) from \(-1\) for unit winding — but it is not a full signed record: it aliases \(|W|\ge3\) and cannot separate \(0\) from \(\pm6\).

D1 must therefore carry **one** of:

- **(a)** raw flux at a declared reference cut \(k^\*\), \(F_{\alpha,k^\*}\), together with \(r_\alpha\); or
- **(b)** a separately constructed real-time phase winding \(\mathcal W_\alpha(t)\), with its own definition, gauge audit, and \(h_6\to0\) limit.

Neither may inherit the symbol or the interpretation of the equilibrium \(W\). Withdraw the averaged \(W_\alpha\) as a register coordinate; retain it only as a derived VIEW quantity flagged valid at \(h_6=0\).

**Verification.** On a run with \(n_i\neq0\): confirm \(r_\alpha\) is identical across all \(L\) cuts while \(F_{\alpha,k}\) is not; confirm the §12 slip ledger records oriented events under the chosen construction; confirm agreement with the frozen \(h_6=0\) result in the limit.

---

## E-02 — BLOCKING — No gap policy; drift, diffusion, stability, and tick numbering are undefined across dropouts

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §10.1 forward-tick box | 18740–18888 | 729 |
| §10.2 amplitude collapse | 18988–19222 | 746–755 |
| §11.1 \(\omega\) definition | 19925–20018 | 776 |
| §11.2 \(D_\Theta\) definition | 20128–20242 | 791 |
| §11.4 tick regularity | 20639–21145 | 817–835 |
| §19 preregistration | 34299–35570 | 1255–1291 |

**Defect.** §10.2 correctly forbids unwrapping through \(R_\Phi<R_{\min}\). §11.1 and §11.2 then define \(\omega\) and \(D_\Theta\) as \(T\to\infty\) limits on \(\widetilde\Theta_\Phi\), which is undefined on invalid intervals, and §11.4 requests Allan deviation on the same record. Ordinary Allan deviation is not defined on a gapped series. Separately, §10.1's monotone infimum silently skips amplitude-invalid crossings: the index \(n\) advances by one regardless of how much physical phase elapsed during the dropout, so \(n\) ceases to track phase advance, and the definition is monotone in \(n\) by construction and therefore structurally cannot represent the duplicated or skipped crossings §11.4 asks the experimenter to report. Finally, censoring low-\(R_\Phi\) segments is selection on a variable correlated with the outcome — the RAW/VIEW contamination §19 exists to prevent.

**Required repair — metrics.** Report unconditionally, and before any drift statistic:

\[
A=\frac{T_{\rm valid}}{T_{\rm total}},
\qquad
\nu_{\rm op}=\frac{N_{\rm valid\ ticks}}{T_{\rm total}}.
\]

Report drift and diffusion **only** as within-segment conditional quantities on maximal valid segments, accompanied by the segment-length distribution. Phase advance across a dropout is **UNKNOWN** — not stitched, not interpolated, not renumbered. Replace ordinary Allan deviation with a declared gap-aware stability statistic, or restrict it to segments exceeding a preregistered minimum length.

**Required repair — event detection.** Replace the monotone infimum with a two-stage detector:

1. **Generate** candidate crossings from the raw trajectory with no validity filter.
2. **Code** each candidate as `valid`, `invalid-amplitude`, `recrossing`, `duplicate`, or `unknown`.

The tick counter becomes a derived VIEW quantity computed from the coded event list. It is no longer the definition of the event. This is what makes §11.4's requested counts representable at all.

**Add to §19.** Gap policy; minimum valid-segment length; the within-segment estimator for drift and diffusion; the gap-aware stability statistic; the event-coding rule.

---

## E-03 — Derived parity is carried as an independent state coordinate

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §9.1 state box | 17259–17379 | 663 |
| §9.1 "\(q\) is derived parity" | 17648–17704 | 689 |
| §9.2 Markov-completeness warning | 18070–18561 | 707–718 |
| §15.1 register box | 28577–28734 | 1077 |

**Defect.** The parity residue is a deterministic function of the winding record, is labelled as such in prose, and is nonetheless listed inside the state vector whose successor kernel §9.2 discusses. That placement invites precisely the confusion §3.4 warns against.

**Required repair.** Move the parity residue to the recorded VIEW/register layer. The Markov state carries independent coordinates only. Under E-01 the register layer holds \(F_{\alpha,k^\*}\) or \(\mathcal W_\alpha\) as the independent record, with \(r_\alpha\), \(q_\alpha^{(2)}\), and \(c_\alpha^{(3)}\) flagged derived.

---

## E-04 — BLOCKING — \(\theta_{\rm ref}\) is undeclared; the reported quality is relative, not intrinsic

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §11.3 \(Q_{\rm clk}\) definition | 20479–20524 | 809 |
| §14.1 \(\chi_{\rm obs}=\chi-\theta_{\rm ref}\) | 26463–26502 | 990 |
| §17 crosswalk table | 31878–32875 | 1221–1236 |
| §19 preregistration | 34299–35570 | 1255–1291 |

**Defect.** §14.1 makes the hand observable by referring it to \(\theta_{\rm ref}\) — correctly, since a fully quotiented global rotation would remove the hand. But \(\theta_{\rm ref}\) is given no dynamics, no drift budget, no diffusion, no calibration, and no entry in §19. Every reported \(\omega\) and \(D_\Theta\) is consequently a two-oscillator difference, and \(Q_{\rm clk}\) as defined is a relative quality that the reference can either flatter or degrade.

**Required repair.** State the composition explicitly:

\[
\omega_{\rm obs}
=
\omega_{\rm clk}-\omega_{\rm ref},
\qquad
D_{\rm obs}
=
D_{\rm clk}+D_{\rm ref}-2D_{\rm cross}.
\]

Report

\[
Q_{\rm rel}=\frac{|\omega_{\rm obs}|}{2D_{\rm obs}}
\]

and label it as such. Intrinsic \(Q_{\rm clk}\) may be claimed only after reference drift, reference diffusion, the cross-covariance \(D_{\rm cross}\), and the calibration procedure are frozen and the cross term is measured or bounded. Add \(\theta_{\rm ref}\) and its full budget to §19.

---

## E-05 — BLOCKING — The drive-reversal null names no symmetry

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §12 drive-reversal row | 21377–21546 | 843 |
| §13.3 finite triad (lag, delay, feedback) | 25113–25896 | 932–961 |
| §16 fixed / swept coupling and feedback | 30749–31872 | 1183–1218 |

**Defect.** §12 requires \(\omega(-\tau)\approx-\omega(\tau)\) "for a symmetric model" without naming the symmetry, while §13.3 and §16 explicitly admit phase lag, delay, forcing, and feedback. The null hypothesis of the reversal test is therefore not stated.

**Superseded claim.** An earlier formulation asserted that lag, delay, or feedback each break the reflection. That over-claims. Phase lag generally does break it; delay and feedback may preserve or break it depending on the exact kernel.

**Required repair.** Declare the involution \(\mathcal R\) and require full equivariance of the D1 law:

\[
\boxed{
F(\mathcal RX;-\tau)
=
D\mathcal R\,F(X;\tau),
}
\]

with an \(\mathcal R\)-reflected initial-condition ensemble and an \(\mathcal R\)-invariant noise law. The audit is performed term by term on the declared law, not inferred from the presence or absence of memory.

**Constructive note.** For the schematic §8 rotor, take \(\mathcal R:(\Theta_\Phi,\Omega_\Phi)\mapsto(2\Theta_*-\Theta_\Phi,-\Omega_\Phi)\). The tooth potential is even about \(\Theta_*\), and the inertial and damping terms are both \(\mathcal R\)-odd, so the reduced rotor is equivariant provided the noise law is symmetric. **This does not discharge the audit.** It must be run on the full state including the gauge-link partner \(\mathcal E\) and the vison/flux configuration \(\mathcal V\), which is exactly where a chirality-carrying term would sit without appearing in the reduced equation.

Only after the audit passes may §12 demand \(\omega(-\tau)=-\omega(\tau)\). If it fails, asymmetric response is a *prediction of the declared model*, not a falsifier of it. The existing pinning/depinning carve-out is retained.

---

## E-06 — Adler time normalization, and a symbol collision

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §13.2 Adler locking | 24003–25112 | 892–931 |
| §13.2 normalized form | 24175–24199 | 905 |
| §8 drive torque \(\tau_i(t)\) | 16312–17133 | 618–652 |

**Defect.** The overdot denotes \(d/dt\) in \(\dot\beta=\Delta\omega-K\sin\beta\) and \(d/d(Kt)\) in \(\dot\beta=g-\sin\beta\). In a note this strict about symbol reuse, the rescaling must be written. Additionally, \(\tau\) already denotes the D1 drive torque in §8 and §12, so it cannot be reused for normalized time.

**Required repair.** Introduce a distinct normalized-time symbol, e.g.

\[
\varsigma=Kt,
\qquad
\frac{d\beta}{d\varsigma}=g-\sin\beta,
\]

and state the rescaling in the same sentence that introduces \(g=\Delta\omega/K\).

---

## E-07 — BLOCKING — The battery has no verdict rule

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §5.3 multiplicity requirement | 12724–12900 | 461 |
| §12 kill tests and controls | 21151–23005 | 838–857 |
| §18 bifurcation witnesses | 32881–34293 | 1239–1252 |
| §19 preregistration | 34299–35570 | 1255–1291 |

**Defect.** §5.3 demands multiplicity correction before constant-proximity claims may be read as evidence. §12 then lists twelve tests and §18 seven mechanism classifications with no family-wise error control and no rule for combining outcomes. "Passes" has no definition at battery level. The standard the note imposes on the numeric sidecar is not applied to the note's own inference.

**Required repair.** Partition the battery into three kinds and treat each on its own terms:

1. **Deterministic validation gates** — gauge transform, integrator refinement, amplitude gate. Pass/fail; no error rate applies; must be declared as gates rather than reported as hypothesis tests.
2. **Stochastic hypothesis families** — drive-off null, drive reversal, hysteresis sweep, tooth removal, perturb-and-release, phase-lock scan, projected-state memory. Declare the family membership, the correction procedure, and \(\alpha\) before unblinding.
3. **Model selection and classification** — §18. Declare the classifier, the full competing-mechanism set, and the selection criterion. This is not a hypothesis test and must not be reported as one.

Add the combination rule to §19 so that a battery-level verdict exists at all.

---

## E-08 — The checkerboard grid family is contaminated and partly degenerate

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §4 diamond chart and even-grid fracture | 9790–10815 | 341–392 |
| §4 grid series \(\{2,4,6,12,24\}\) | 10417–10571 | 388 |
| §4 \(L=99\) holdout sentence | 10574–10809 | 390 |
| §5.1 Pell independence rule | 11504–11645 | 436 |

**Defect.** §5.1 states the rule: the Pell pair is evidentiary only if \((99,35)\) or its recurrence is fixed independently of seeing the approximation. §4 then selects \(L=99\) — the Pell numerator — as the odd-grid holdout for the checkerboard mechanism. Every odd \(L\) falsifies \(\gcd(2,L)=1\) equally well, so the choice imports a sidecar-selected integer into the falsification design and entangles two lanes the note otherwise keeps apart. Separately, \(L=2\) is a degenerate member of \(\{2,4,6,12,24\}\): the index-two result holds, but the generators \((1,1)\) and \((1,-1)\) coincide mod 2, so it is not an independent instance of the mechanism.

**Required repair.** Select the grid family algorithmically and preregister it: a parity-balanced set of even and odd \(L\) spanning the size range, with the selection rule frozen before any run. Retain \(L=99\) as exploratory rather than confirmatory. Label \(L=2\) degenerate wherever the series appears.

---

## E-09 — The throat control tests an object D1 does not contain

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §6.3 frozen repair and scope sentence | 14802–14947 | 553 |
| §12 flat/no-throat control row | 22029–22159 | 848 |

**Defect.** No equation in the note couples \(U(s)\) or \(R(s)\) to \(z\), \(\Phi\), the register, or the rotor law. §6.3 concedes the throat is a spatial construction pending a declared transport law. §12 nonetheless prescribes a flat/no-throat control whose positive witness — "throat signature" — has no operational definition in D1.

**Required repair.** Either remove the row from the D1 battery, or declare a separate coupled model (call it **D1-T**) with an explicit constructor linking throat geometry to the D1 state, and give the signature an operational definition before the control is run. An undefined control must not be carried into a preregistration.

---

## E-10 — \(Q_4\times C_6\) performs no inferential work

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| §1 evidence-lane table, source row | 3308–3374 | 53 |
| §5.2 constants table, 24 row | 12050–12126 | 446 |
| §20 claim ledger | 35576–37520 | 1294–1331 |

**Defect.** \(Q_4\times C_6\) appears in the evidence-lane table as established source mathematics, contributes the integer 24 to the constants table, and is then disowned in §20. It is never connected to F0, D0, or D1.

**Required repair.** Relabel as provenance-only motivation in §1 and §5.2, matching the §20 disposition. In a note whose purpose is demarcation, an unused object sitting in an evidence table is itself a demarcation liability.

---

## E-11 — Version, date, and file-naming hygiene

**Parent bytes**

| Passage | Bytes | Lines |
|---|---|---|
| Front matter | 0–946 | 1–14 |
| Version and date lines | 98–138 | 5 |

**Defect.** The filename encodes `v0_1`, the header declares 0.1.1, and the date `2026-08-29` carries no timezone and is in the future relative to this addendum's issue timestamp.

**Required repair.** No in-place repair of the parent. Emit v0.2 under a filename matching its declared version, with a timezone-qualified timestamp, and record this addendum together with the parent SHA-256 in its provenance block. The mismatched v0.1/0.1.1 artifact is retained unmodified as the parent of record.

---

## Disposition summary

| ID | Entry | Status | Primary parent sections |
|---|---|---|---|
| E-01 | Winding register undefined at finite \(h_6\) | **BLOCKING** | §3.4, §3.5, §9.1, §12, §15.1 |
| E-02 | No gap policy for metrics or tick coding | **BLOCKING** | §10.1, §10.2, §11.1–11.4, §19 |
| E-03 | Derived parity in the Markov state | Non-blocking | §9.1, §9.2, §15.1 |
| E-04 | \(\theta_{\rm ref}\) undeclared; \(Q\) is relative | **BLOCKING** | §11.3, §14.1, §17, §19 |
| E-05 | Reversal null lacks equivariance audit | **BLOCKING** | §12, §13.3, §16 |
| E-06 | Adler normalization and \(\tau\) collision | Non-blocking | §8, §13.2 |
| E-07 | Battery verdict undefined | **BLOCKING** | §5.3, §12, §18, §19 |
| E-08 | Grid family contaminated / degenerate | Non-blocking | §4, §5.1 |
| E-09 | Throat control out of D1 scope | Non-blocking | §6.3, §12 |
| E-10 | \(Q_4\times C_6\) does no work | Non-blocking | §1, §5.2, §20 |
| E-11 | Version, date, filename | Non-blocking | front matter |

---

## Effect on the v0.2 rewrite

Sections requiring substantive rewriting rather than annotation: **§3.4, §9.1, §10.1, §11.1–11.4, §12, §15.1, §19.**

Consequential edits the entries force elsewhere:

- **§17 crosswalk.** The "signed history" and "parity register" rows must be restated under E-01. The gauge-clock column no longer reads \(W\in\mathbb Z^3\) with \(q=W\bmod2\); it reads the declared construction (a) or (b) plus \(r_\alpha\in\mathbb Z_6\).
- **§20 claim ledger.** Add to *exact or established*: cut-independence of \(r_\alpha=F_{\alpha,k}\bmod6\) at finite \(h_6\), with the aliasing limitation stated in the same entry. The existing conditioned item — \(q_\alpha=W_\alpha\bmod2\) at \(h_6=0\) — remains true as written and is retained. Move \(Q_4\times C_6\) provenance out of the evidence lane per E-10.
- **§11.3.** The headline metric becomes \(Q_{\rm rel}\) until E-04 is discharged; the §18 "robust clock" row inherits that change.
- **Executive result.** Item 6 currently requires D1 to supply "a complete state" and "an amplitude-valid tick witness." Both are now qualified by E-01 and E-02 and should say so, rather than being read as already specified.

**Freeze order.** E-01 and E-02 must be resolved first: they change the register and the metrics, and E-04 and E-07 are written against those definitions. E-05 can be audited in parallel. The non-blocking entries are editorial once the four above are settled.

---

## Addendum provenance

Constructed by review of the parent file identified above, incorporating two corrections issued against an earlier audit draft: the cut-flux reformulation now in E-01, and the equivariance requirement now in E-05. Both superseded formulations are recorded in place. No source file was modified.
