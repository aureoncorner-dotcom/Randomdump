---
schema: simulation-protocol-a10-artifact-v1
artifact_id: A10-02
title: Frozen geometry specification
status: NOT_RUN
evidence_state: SCAFFOLD_ONLY
protocol_document_id: 1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE
protocol_revision_id: AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA
H_AppA: PENDING
H_AppB: PENDING
geometry_schema_sha256: PENDING_AFTER_COMPLETION
content_sha256: PENDING_AFTER_COMPLETION
completed_at_utc: PENDING
---

# Frozen geometry

- Lattice: `Lambda_L=(Z/LZ)^3`, coordinates `0,...,L-1`, addition modulo `L`.
- Positive link orientation: `+x,+y,+z`; code ordering and endianness: PENDING.
- `Gamma_x={((x,0,0),+x):0<=x<L}`.
- `Gamma_y={((0,y,0),+y):0<=y<L}`.
- `Gamma_z={((0,0,z),+z):0<=z<L}`.
- Ordered tuple: `(Gamma_x,Gamma_y,Gamma_z)` with base point `(0,0,0)`.
- `Sigma_alpha`: dual noncontractible cut orthogonal to `Gamma_alpha`, oriented so `<Sigma_alpha,Gamma_beta>=delta_alpha,beta mod 2`.
- Sector label order: `q=(q_x,q_y,q_z)` in lexicographic bit order `000,001,010,011,100,101,110,111`.
- Holonomy label order: the same bit order for `h=(h_x,h_y,h_z)`.

# Static provenance reconciliation — 2026-09-03

| Field | Recovered value |
| --- | --- |
| artifact Drive ID | `16ud7RWtzS-LLD9MC8xDNkHQ13Pgb7YjU` |
| artifact parent folder ID | `1l2BZjibcCHBJnep5rSnQaLmmNQ3yRlXl` |
| artifact created/observed modified | `2026-09-01T07:27:49.743Z` / `2026-09-01T07:27:49.743Z` before this reconciliation |
| canonical protocol Drive ID | `1HVlQsTPnvAiYPqbS1Lb9UjZkak5jMlbpS0gSeUbAwrE` |
| canonical protocol tab/revision | `t.0` / `AIroW36-rin9_MPmG0KG_r32bCYMKyhWo7Nc-bEuQ5RfahXZHNlwKtVOPFcxiasQzbKdMurbiXTr0TiqXDV8tA` |
| public repository pointer | `https://github.com/aureoncorner-dotcom/Relational_poop_geometrics` |
| observed immutable public snapshot | `26738b66617cab34698daa3b16b8773478ba9283` |
| public protocol mirror at snapshot | `theory_v0.3.md` |

These pointers ground the specification's document lineage only. No implementation geometry schema, ordering/endian binding, seam-map binding, or machine-exact test artifact was found. All implementation bindings, hashes, tests, and freeze fields remain pending/unrun.

# Required implementation bindings

| Binding | Code symbol/file | Frozen value/hash |
| --- | --- | --- |
| site index | PENDING | PENDING |
| oriented-link index | PENDING | PENDING |
| plaquette index/orientation | PENDING | PENDING |
| dual-cut incidence | PENDING | PENDING |
| cycle incidence | PENDING | PENDING |
| seam map `T_alpha` | PENDING | PENDING |

# Predetermined placement checks

Validate the canonical tuple and its complete translations by `r_x=(floor(L/2),0,0)`, `r_y=(0,floor(L/2),0)`, and `r_z=(0,0,floor(L/2))`. These are checks, not selectable replacements.

# Pass rule

Set `status: FROZEN` only after the implementation bindings contain no `PENDING`, their files hash successfully, and machine-exact tests establish `partial^2=0`, the intersection matrix is the 3-by-3 identity over `Z_2`, and `q_alpha=W_alpha mod 2` for every enumerated state. A changed base point, rerouted cycle, reordered axis, selected translation, or hash mismatch is `FAIL — GEOMETRY NOT FROZEN` and blocks `H_Execution`.
