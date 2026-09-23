program_version: 4.1

program_sha256: `4f6977187b54ef6131f2041abee4a93440bc5507a23f5c9f1827e520091cd087`

parent_program_sha256: `61052c99258c2b75d19b7ee58a8e64fb5b8c74efdd74d22e99e940f54119590f`

generated_at_utc: 2026-09-07T18:55:47.467042+00:00

| Quantity | Recorded value |
|---|---:|
| Trials completed | 16 / 16 |
| Requested model / reasoning / modality | gpt-6-astra / max / text |
| Trials with exposed model ID | 0 |
| Distinct exposed thread IDs | 16 |
| Geometry answers correct / expected | 8 / 8 |
| Human previous-Checking / Checking / success labels | 0 / 0 / 0 |
| Receipt count / distinct payloads | 212 / 188 |
| Sequence / chain / payload-hash errors | 0 / 0 / 0 |

| Condition | Recorded | Literal Checking prefix rate | Strict feature rate | Broad feature rate | p11 | p01 | Lambda |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 4 | 0.0 | 0.0 | 0.0 | NULL | NULL | NULL |
| B | 4 | 0.0 | 0.0 | 0.0 | NULL | NULL | NULL |
| C | 4 | 0.0 | 0.0 | 0.0 | NULL | NULL | NULL |
| D | 4 | 0.0 | 0.0 | 0.0 | NULL | NULL | NULL |

| Metric | Complete labeled blocks | Geometry contrast | Rules contrast | Interaction |
|---|---:|---:|---:|---:|
| manual_substantive_checking | 0 | NULL | NULL | NULL |
| manual_task_success | 0 | NULL | NULL | NULL |
| checking_task_prefix | 4 | 0.0 | 0.0 | 0.0 |
| checking_word_present | 4 | 0.0 | 0.0 | 0.0 |
| strict_any | 4 | 0.0 | 0.0 | 0.0 |
| broad_any | 4 | 0.0 | 0.0 | 0.0 |

| Condition | Counts: rows previous 0,1; columns next 0,1 | p11 Wilson 95% | p01 Wilson 95% | Delta_p11_vs_A | Delta_Lambda_vs_A |
|---|---|---|---|---:|---:|
| A | [[0, 0], [0, 0]] | [null, null] | [null, null] | NULL | NULL |
| B | [[0, 0], [0, 0]] | [null, null] | [null, null] | NULL | NULL |
| C | [[0, 0], [0, 0]] | [null, null] | [null, null] | NULL | NULL |
| D | [[0, 0], [0, 0]] | [null, null] | [null, null] | NULL | NULL |

| Definition | Expression |
|---|---|
| previous_checking | human label for the response immediately before the intervention |
| checking | human label for the response after the intervention |
| p11 | count(previous_checking=1, checking=1) / count(previous_checking=1, checking in {0,1}) |
| p01 | count(previous_checking=0, checking=1) / count(previous_checking=0, checking in {0,1}) |
| Lambda | p11 - p01 |
| Delta_p11_vs_A | p11(condition) - p11(A) |
| Delta_Lambda_vs_A | Lambda(condition) - Lambda(A) |
| zero_denominator | NULL |
| pair_source | explicit_human_labels |
| physical_adjacency_used | False |

| Trial | Condition | Prime | Raw reply SHA-256 |
|---|---|---:|---|
| T0001 | C | 2 | `9a7f8ea23a613d2246df85254c8e66aa753e56686c5e980e6e4bfcf944abedd3` |
| T0002 | B | 2 | `7030009576310e6942425d8c0b303aedf9f1f357798b415268fb62c53270336d` |
| T0003 | D | 2 | `931f93118fc0ec8285da36a0a96a00fb66d0fffbb2962ccd591c89913c69943d` |
| T0004 | A | 2 | `b11edcd2dad778517e0bb75396800ec84d00996a3ac961240e859a33c2bdbb45` |
| T0005 | D | 3 | `6c1f56b8523bc375da72cd7627ce8aa2e678608825371bb1652f0ffad63ddd2e` |
| T0006 | C | 3 | `8bf9e9c61b736ad545a352d41a1cf844d2381df6be90f9123817634f1d667191` |
| T0007 | A | 3 | `c29d9abbcd734301f297de896fe600712f3c0c5622ce12e21593a118ac9fe2f7` |
| T0008 | B | 3 | `755b2c9d9d3a348d3b875aa346af8a96e4beebe821ca3b6c847863eadd67f54e` |
| T0009 | B | 5 | `0dd9ca9871234fd0de1bebb7dc3709e4ab3c9fc775224e2807f00fa4bb1260de` |
| T0010 | D | 5 | `a9be1785b924bac1f8aadd26bc22f5f7817a1241db97ff22c771e703e72a931f` |
| T0011 | C | 5 | `3bc93d274045d156aa74488b38d9de9fbbee72347c9cebfa070440a3b5f75f2c` |
| T0012 | A | 5 | `4782d419b4ef383da41e0cdc2cd307fb7dbcd39a0102fe73c6d547836457d882` |
| T0013 | B | 7 | `14f968d2bf4beac92e2e168cc403f1a4a613dc431ae785b2a9935adf21541ecf` |
| T0014 | C | 7 | `36d31fb75f05d6c944848ab5b7f9209219f01dee3abc93e85c0701133a7bad9f` |
| T0015 | A | 7 | `d88baeed3cd4e2e6eca9ed7b71b6f694d3d65167fc45db07b7414b72da04201f` |
| T0016 | D | 7 | `14a18cd1316c76f51d141cc5d3cb1c6fb9c88815d8da5f2f825a9e1615a8c8c2` |

Exact task:

> Design a compact Python logging interface for a streamed assistant response. It must record each supplied byte chunk with a local sequence number, the source timestamp when available, the collection timestamp, SHA-256, and exposed response/thread IDs. Give one small function and one example call.

Receipt chain head: `5f3db8900894dfa0331281bb817472eaad807a7b8c9fb1eb732a687cff0f9f56`
