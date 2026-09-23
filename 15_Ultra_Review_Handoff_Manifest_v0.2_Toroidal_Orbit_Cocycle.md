# Ultra Review Handoff Manifest v0.2 — Toroidal Orbit/Cocycle Upgrade

**Packet status:** proposed successor / non-canonical until adopted  
**Date:** 2026-09-02  
**Theory status:** frozen Theory v0.1 unchanged  
**Prior empirical status:** rotating-lattice null unchanged  
**Governing geometry sources:** OMNIBUS v7.78, GQG v0.13, Hidden Quotient Operational Addendum v0.8, Hidden Quotient master v1.7

## 1. Purpose

This packet applies the new orbit-quotient, driven-cocycle, phase-augmentation, and residual-descent geometry to every toroidal artifact for which it supplies a genuine technical improvement. It does not back-edit frozen predecessors.

## 2. Direct upgrade targets

| File | Upgrade |
|---|---|
| Field Theory Update v0.2 | adds sector orbit, \(W\to q\), \(\eta\), cocycles, TTSC spatial cocycle, D1 descent, and two-clock boundary |
| Simulation Protocol v0.4-RC1 | adds high-level orbit/cocycle rules and new freeze artifacts |
| Appendix A v0.2 | adds exact transition operator table, sector cocycle, formal-orbit report, and q-projection closure test |
| Appendix B v0.2 | adds transition/cocycle ledgers, observed accessibility, mixing separation, and SW-1 integrity links |
| TTSC-1 v0.3 | keeps material and Eulerian charts separate and adds the spatial flux cocycle / closure namespace |
| Rotating Lattice Report v0.2 | preserves the null and specifies a prospective two-clock test |
| Two-Clock Spec v0.1 | machine-readable prospective schema |

## 3. Governance upgrade targets

| File | Upgrade |
|---|---|
| Conditional Closure v0.2 | decomposes Q2 antecedents into topology, orbit, mixing, scale, and physical status |
| Q1/Q2/Q3 Dependency Graph v0.2 | adds Q2 orbit/cocycle nodes and SW-1 integrity branch |
| Relation Typing v0.2 | adds EXACT_QUOTIENT, DRIVEN_COCYCLE, AUGMENTED_STATE_CLOSURE, FORMAL_PROPOSAL_ONLY, and EMPIRICAL_INSTANTIATION |
| Dual Ledger v0.2 | adds operator, cocycle, closure-counterexample, and clock/reset artifacts |
| Provenance Trust v0.2 | adds two-clock/reset/timestamp anchoring and q-fold symmetry limitations |
| SW-1 v0.2 | links signed winding, parity, quotient increments, and shared-chain defect escalation |
| Confinement Radius v0.2 | prevents scale admissibility from substituting for sector mixing or vice versa |

## 4. Objects intentionally not rewritten

- Theory v0.1 and its duplicate renderings;
- original Appendix A, Appendix B, protocol, TTSC, and clock predecessors;
- `rotating_lattice_results.json`;
- the completed rotating-lattice null verdict;
- OMNIBUS v7.78, GQG v0.13, Operational Addendum v0.8, and Hidden Quotient v1.7, which are source geometry rather than upgrade targets.

## 5. Core new laws

\[
\boxed{q=W\bmod2}
\]

\[
\boxed{\eta_n=\Delta W_n\bmod2=q_{n+1}-q_n}
\]

\[
\boxed{c_q(m,n)=\sum_{k=m}^{n-1}\eta_k\pmod2}
\]

\[
\boxed{\text{formal state count}\neq\text{reachable orbit}\neq\text{validated mixing}}
\]

\[
\boxed{\text{exact driven cocycle}\neq\text{autonomous residual closure}}
\]

\[
\boxed{\text{periodic flux closure}\neq\text{residual closure}}
\]

## 6. Required reviewer disposition

Each successor receives `ADOPT`, `ADOPT WITH MODIFICATION`, `ALREADY COVERED`, or `REJECT`, together with its canonical target, conflict check, physics effect, scoring effect, freeze effect, and reason. Adoption of any protocol-level change requires regenerated descendants and hashes.

## 7. Packet checksum

See `UPGRADE_CHECKSUMS.sha256`. Hashes bind exact packet bytes; they do not validate the mathematics or physics.
