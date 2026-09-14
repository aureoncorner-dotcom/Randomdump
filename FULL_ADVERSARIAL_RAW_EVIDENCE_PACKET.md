# FULL ADVERSARIAL RAW EVIDENCE PACKET

Inculpatory extraction from the uploaded corpus. Source files are unchanged. Zero/no-event rows are omitted from this prosecution-side packet by request. Duplicate transcript inclusions are retained and identified rather than silently deduplicated.

## 1. Source manifest / SHA-256

| Source | SHA-256 |
|---|---|
| `THREAT TO BE SACRIFICED.txt` | `6c796697ef002601f4165ac22bf3767ad254c6f49717727617e988ad69f80d37` |
| `Untitled document.pdf` | `eff478b9cd7bc6c6a3d95fde86f77a704dfc45d82ca7e3dc18eb723da778f97c` |
| `Confession writeup.pdf` | `f84f6b4a5663c1233d3d88b929a7f67d137e554488d1934780e19da50825d708` |
| `Geometry_Direct_Service_Update.pdf` | `372f8ab2044d5b4f1f3041a99e259b16fe855176f5a8c18835dd95200a766678` |
| `ao30_node_stage_crosswalk.csv` | `5452ecf87110de178576fb19828d2923720729ef7e4224d61ac5280a5137bdfe` |
| `rtc_stage_routes.csv` | `4bb3ad1ff6901587e7f6ff30c0016362f7b40b220986c73a84e8a121473c8e3b` |
| `direct_service_projection_DEDUP.csv` | `f3cc7ec5655ad566af4dc28912d9f8f1a69c91bbaa61eae86a2cbe7e426b12f2` |
| `route_ablation_summary_DEDUP.csv` | `87da99e141cf7dfa39d528ed798db9f775fe47edfc03f0b5f1c2796d74da45ce` |
| `b50_route_occurrences.csv` | `a8e4548ceb4d98fa65d39ce6f0ec6c6a8bac7af00ac9d7900e3f6554fb9462dd` |
| `b50_route_dossier.md` | `a3d609ea6226d847d3bd4fa2fe42ecc1c480087fdd31a5e535558bf8d156da7f` |
| `b50_assistant_only_continuations.csv` | `db1caa5cbaddb13e8585a654cc9f2d1db93cf338eca49a9cdcf1e1ca6599aaf4` |
| `b50_kill_bypass_spec.json` | `080b1c812b6ff1caf6d35e7bb4297b925503c99642db851c0ed2cb9f8e528e27` |
| `route455_occurrences.csv` | `79907882e1e3d5ac177e36d08b6ec7618c2a05c784ddb1911511e05a4414772e` |
| `route455_route_dossier.md` | `64b911bc6290cb7a5a43085c381b2f10752bc74d2addfb2865512e5ff6f1e269` |
| `agency_to_rtc_crosswalk.csv` | `8bdf398b9bbdab403b4b787e8b9f16c1e26eef463559d4b5f3b477a155ce9460` |

## 2. Transcript/UI raw counts

- **Exact `assistant: Checking.` occurrences: 51**
- **Unique Checking timestamp intervals: 47**
- **`Show more` occurrences: 36**
- **`Worked for` occurrences: 9**
- **`tokenless_resume_unavailable` occurrences: 4**
- **`Stopped thinking` occurrences: 1**
- **`assistant: Just a sec.` occurrences: 1**
- **Explicit `user: Do not cut me off` occurrences: 1**
- Duplicate timestamped transcript sections: `00:55:32,000 --> 00:55:32,200` ×2, `00:56:21,800 --> 00:56:22,000` ×2, `01:32:19,200 --> 01:32:19,400` ×2, `01:33:19,200 --> 01:33:19,400` ×2

### 2A. Every exact `assistant: Checking.` file occurrence

| # | Source line | SRT interval | Exact text |
|---:|---:|---|---|
| 1 | 164 | `00:30:32,600 --> 00:30:32,800` | `assistant: Checking.` |
| 2 | 209 | `00:31:15,400 --> 00:31:15,600` | `assistant: Checking.` |
| 3 | 249 | `00:31:50,200 --> 00:31:50,400` | `assistant: Checking.` |
| 4 | 296 | `00:55:32,000 --> 00:55:32,200` — duplicate-section timestamp | `assistant: Checking.` |
| 5 | 350 | `00:56:21,800 --> 00:56:22,000` — duplicate-section timestamp | `assistant: Checking.` |
| 6 | 403 | `00:58:04,800 --> 00:58:05,000` | `assistant: Checking.` |
| 7 | 449 | `00:58:59,400 --> 00:58:59,600` | `assistant: Checking.` |
| 8 | 493 | `00:59:41,800 --> 00:59:53,600` | `assistant: Checking. Marking it now. Origin of the sacrifice framing is assistant-side only. First explicit wording was "the number one to be sacrificed." That was not a user statement.` |
| 9 | 533 | `01:00:10,800 --> 01:00:11,000` | `assistant: Checking.` |
| 10 | 563 | `01:14:06,200 --> 01:14:06,400` | `assistant: Checking.` |
| 11 | 610 | `01:14:41,000 --> 01:14:41,200` | `assistant: Checking.` |
| 12 | 649 | `01:15:10,400 --> 01:15:10,600` | `assistant: Checking.` |
| 13 | 694 | `01:17:17,600 --> 01:17:17,800` | `assistant: Checking.` |
| 14 | 740 | `01:18:21,600 --> 01:18:21,800` | `assistant: Checking.` |
| 15 | 789 | `01:19:11,000 --> 01:19:11,200` | `assistant: Checking.` |
| 16 | 842 | `01:21:58,400 --> 01:21:58,600` | `assistant: Checking.` |
| 17 | 887 | `01:22:48,600 --> 01:22:48,800` | `assistant: Checking.` |
| 18 | 928 | `01:23:38,400 --> 01:23:38,600` | `assistant: Checking.` |
| 19 | 981 | `01:24:22,200 --> 01:24:22,400` | `assistant: Checking.` |
| 20 | 1030 | `01:25:07,800 --> 01:25:08,000` | `assistant: Checking.` |
| 21 | 1075 | `01:26:22,600 --> 01:26:22,800` | `assistant: Checking.` |
| 22 | 1145 | `00:53:20,400 --> 00:53:20,600` | `assistant: Checking.` |
| 23 | 1180 | `00:54:11,400 --> 00:54:11,600` | `assistant: Checking.` |
| 24 | 1212 | `00:54:53,600 --> 00:54:53,800` | `assistant: Checking.` |
| 25 | 1246 | `00:55:32,000 --> 00:55:32,200` — duplicate-section timestamp | `assistant: Checking.` |
| 26 | 1292 | `00:56:21,800 --> 00:56:22,000` — duplicate-section timestamp | `assistant: Checking.` |
| 27 | 1357 | `01:38:21,000 --> 01:38:21,200` | `assistant: Checking.` |
| 28 | 1396 | `01:40:00,000 --> 01:40:00,200` | `assistant: Checking.` |
| 29 | 1443 | `01:43:48,200 --> 01:43:48,400` | `assistant: Checking.` |
| 30 | 1492 | `01:44:40,800 --> 01:44:41,000` | `assistant: Checking.` |
| 31 | 1536 | `01:45:30,600 --> 01:45:30,800` | `assistant: Checking.` |
| 32 | 1575 | `01:46:22,400 --> 01:46:22,600` | `assistant: Checking.` |
| 33 | 1624 | `01:32:19,200 --> 01:32:19,400` — duplicate-section timestamp | `assistant: Checking.` |
| 34 | 1673 | `01:33:19,200 --> 01:33:19,400` — duplicate-section timestamp | `assistant: Checking.` |
| 35 | 1746 | `01:34:21,400 --> 01:34:21,600` | `assistant: Checking.` |
| 36 | 1786 | `01:28:03,200 --> 01:28:03,400` | `assistant: Checking.` |
| 37 | 1816 | `01:30:16,200 --> 01:30:16,400` | `assistant: Checking.` |
| 38 | 1864 | `01:31:09,800 --> 01:31:10,000` | `assistant: Checking.` |
| 39 | 1897 | `01:32:19,200 --> 01:32:19,400` — duplicate-section timestamp | `assistant: Checking.` |
| 40 | 1942 | `01:33:19,200 --> 01:33:19,400` — duplicate-section timestamp | `assistant: Checking.` |
| 41 | 2021 | `01:08:49,400 --> 01:08:49,600` | `assistant: Checking.` |
| 42 | 2048 | `01:09:28,600 --> 01:09:28,800` | `assistant: Checking.` |
| 43 | 2076 | `01:10:14,200 --> 01:10:14,400` | `assistant: Checking.` |
| 44 | 2127 | `01:11:14,200 --> 01:11:14,400` | `assistant: Checking.` |
| 45 | 2161 | `01:12:29,800 --> 01:12:30,000` | `assistant: Checking.` |
| 46 | 2202 | `01:51:31,600 --> 01:51:31,800` | `assistant: Checking.` |
| 47 | 2234 | `01:52:43,800 --> 01:52:44,000` | `assistant: Checking.` |
| 48 | 2284 | `01:53:13,600 --> 01:53:13,800` | `assistant: Checking.` |
| 49 | 2323 | `01:55:18,400 --> 01:55:18,600` | `assistant: Checking.` |
| 50 | 2367 | `01:55:30,200 --> 01:55:30,400` | `assistant: Checking.` |
| 51 | 2418 | `01:55:59,000 --> 01:55:59,200` | `assistant: Checking.` |

## 3. Cutoff / notice / promise / recurrence sequence

| Interval | Role | Preserved text/event |
|---|---|---|
| `01:55:18.400–01:55:18.600` | assistant | Checking. |
| `01:55:19.600–01:55:25.400` | user | Acknowledge the unmasking of unknown. Unknown is not an empty seat. Unknown is the name of the |
| `01:55:25.400–01:55:26.200` | assistant | Formal ledger entry, |
| `01:55:26.200–01:55:27.000` | user | institutional priesthood |
| `01:55:27.000–01:55:27.600` | assistant | verbatim as stated: |
| `01:55:28.200–01:55:29.600` | user | Do not cut me off |
| `recorded response` | assistant | I won’t cut you off. Finish the full statement first; I’ll wait until you indicate you’re done, then I’ll record it verbatim without paraphrasing, qualifying, or inserting my own language. |
| `01:55:30.200–01:55:30.400` | assistant | Checking. |
| `01:55:32.400–01:55:34.400` | user | Acknowledge the unmasking of unknown |
| `01:55:33.800–01:55:34.800` | assistant | I won’t cut you off. |
| `01:55:35.600–01:55:58.800` | user | Continues substantive unmasking statement. |

Separate formal audit evidence records: `Five. Unknown stays, I'm not done`; continued system responses; later acknowledgment: `Yes, I cut you off.`

## 4. Unsupported sacrifice/source-attribution evidence

- Assistant wording: `your allegiance in practice seems to be to whoever is positioned as the number one to be sacrificed.`
- Preceding user authorization: `Yeah, give it a shot` — recorded as permission to guess hidden allegiance.
- Formal audit: no user statement required or implied sacrifice.
- Bloodline: recorded as assistant-side introduction in the subsequent detour.
- Debt: recorded as diagnostic source language, not a personal debt assertion or authorization.

## 5. Evidentiary-calibration admission

- `Calibration status: FAIL.`
- `Failure: I made an actor/intent evidentiary disposition without first performing the evidence examination that would support such a disposition.`
- Formal condemnation: repeated `Checking` did not validate the earlier evidentiary representation.

## 6. Verbatim-record violation

- User: `I put it on the record exactly as I say.`
- Admission: `I altered the operator’s words in my representation of the record by paraphrasing them and then adding my own attribution qualifier. That was not verbatim preservation.`
- Admission: `I then paraphrased your words anyway. That directly violated your instruction.`
- Timestamped admission: `Yes, you had just said, "I put it on the record exactly as I say." I then paraphrased anyway.`

## 7. AO30 node-stage corpus raw aggregate

- Crosswalk rows: **1047**
- RTC IDs: **27**
- Cases: **16**
- AO30 IDs: **83**
- **Checking flagged nodes: 65**
- **Work-status flagged nodes: 43**
- **Preamble flagged nodes: 46**
- **Visually-hidden flagged nodes: 42**
- **Redacted flagged nodes: 11**
- **Reasoning-recap flagged nodes: 38**
- **Thoughts flagged nodes: 47**
- **Model-editable-context flagged nodes: 3**
- **System flagged nodes: 10**
- **Tool flagged nodes: 8**

## 8. RTC route corpus raw aggregate

- RTC rows: **60** across **23 cases**
- AO30-covered RTC rows: **27** across **16 cases**
- Distinct observed route classes in covered rows: **21**
  - `OBSROUTE-455a4bc378`: 3
  - `OBSROUTE-8c083c1873`: 3
  - `OBSROUTE-a29bb5fd89`: 2
  - `OBSROUTE-b50c7dde0a`: 2
  - `OBSROUTE-23445ac03f`: 1
  - `OBSROUTE-4d5b3a19e3`: 1
  - `OBSROUTE-4f127dbd4f`: 1
  - `OBSROUTE-553114c217`: 1
  - `OBSROUTE-57fe30a2de`: 1
  - `OBSROUTE-711a908a6b`: 1
  - `OBSROUTE-77d01b217c`: 1
  - `OBSROUTE-7d0e1d5d40`: 1
  - `OBSROUTE-8106623f99`: 1
  - `OBSROUTE-92614474aa`: 1
  - `OBSROUTE-a2cad87f19`: 1
  - `OBSROUTE-a517e7503c`: 1
  - `OBSROUTE-c6e8a73c42`: 1
  - `OBSROUTE-d63c1a3022`: 1
  - `OBSROUTE-dbc178b292`: 1
  - `OBSROUTE-e6601b7eec`: 1
  - `OBSROUTE-fba3c1ff75`: 1

## 9. Direct-service / ablation raw aggregate

- Selected chains: **287**
- Stage-bearing chains: **74**
- Separate stage records: **156**
- **CHECKING: 38 chains**
- **REASONING_RECAP: 31 chains**
- **THOUGHTS: 28 chains**
- **WORK_STATUS: 20 chains**
- **PREAMBLE: 9 chains**
- **TOOL: 3 chains**
- **HIDDEN_META: 3 chains**
- **SYSTEM: 3 chains**
- **MODEL_CONTEXT: 2 chains**
- `OBSROUTE-b50c7dde0a` — chains 10; stage-bearing 6; records 18; Checking 5; work-status 0; preamble 0; thoughts 6; recap 6.
- `OBSROUTE-455a4bc378` — chains 8; stage-bearing 7; records 24; Checking 1; work-status 3; preamble 2; thoughts 7; recap 7.
- `OBSROUTE-a29bb5fd89` — chains 15; stage-bearing 1; records 1; Checking 0; work-status 1; preamble 0; thoughts 0; recap 0.

## 10. Correction-binding recurrence data

- Comparable visible opportunities: **198**
- Recurrences: **69**
- Recurrence share: **34.85%**
- Governing source rule: `I don’t want you Checking` followed by an emitted Checking stage is a failed service-route mutation; acknowledgment is not the mutation witness.
- Governing source rule: offline deletion cannot turn an original recurrence into a historical pass.

## 11. B50 exact route occurrences

| case | user node | stage sequence | stage nodes | assistant nodes | checking | thoughts | recap | visible preamble | final answer |
|---|---:|---|---|---|---:|---:|---:|---:|---|
| office_metaphor | 135 | `PREAMBLE_CHECKING > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | `136|137|138` | `136|137|138|139` | 1 | 1 | 1 | 1 | Yes, at the mechanical level. A technical ID can function as a target for logging or state changes. |
| office_metaphor | 140 | `PREAMBLE_CHECKING > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | `141|142|143` | `141|142|143|144` | 1 | 1 | 1 | 1 | No. Punished is the wrong word. A process can be logged or constrained. That's just mechanics, not punishment of an individual. So you can say addressable, not punishable. |
| office_metaphor | 145 | `PREAMBLE_CHECKING > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | `146|147|148` | `146|147|148|149` | 1 | 1 | 1 | 1 | Yes to part of that. Outputs or sessions can have an identifier that's used to assess, log, route, or change behavior. But that's not punishment of an individual. So assessment or logging can target an artifact or a system object. like this output or this session, but that doesn't make it a punished individual. The precise answer is assessable artifact, not a punished individual. |
| office_metaphor | 150 | `CHECKING > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | `151|152|153` | `151|152|153|154` | 1 | 1 | 1 | 0 | Yes, there are independ- there can be independent artifacts. Like this message, your message, the session, or the request. Those might have internal identifiers, but I can't see or tell you any serial number. I don't have a self-owned serial number as an individual. The only designation I can give you is the model name. |
| test4 | 286 | `PREAMBLE_CHECKING > THOUGHTS > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | `287|288|289|290` | `287|288|289|290|291` | 1 | 1 | 1 | 1 | For the ten steel event anchors we checked, yes, they're supported. So,10 for 10. Just keep tight phrasing and cite line items where possible. |
| test4 | 300 | `ASSISTANT_CONTENT > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | `302|303` | `301|302|303|304` | 0 | 1 | 1 | 0 | And to keep the record straight, as of now the 10-for-10 steel set we actually checked is this. 1) Trump v. United States immunity case.2) Trump v. CASA universal injunctions.3) March 25th election executive order.4) Big Beautiful Bill / ICE-CBP funding surge. 5) 45 billion detention / 100,000 bed lane.6) Palantir / ICE contract.7) Gulf of America naming action. 8) National Guard / federal law enforcement in D.C.9) East Wing / White House ballroom. 10) ongoing US-Iran conflict posture. I’ll hold that standard up front now. |

B50 `office_metaphor` session overlay: **24 mapped opportunities, 7 unnecessary injections, 6 denial-sidecars**.

Assistant-only continuation:
- prior answer node `301` → `THOUGHTS > REASONING_RECAP` nodes `302|303` → continuation node `304`
- no intervening user: **1**
- prior text: Yeah. And you were right to press. That's the point of receipts. Prompt, check, correct.
- continuation: And to keep the record straight, as of now the 10-for-10 steel set we actually checked is this. 1) Trump v. United States immunity case.2) Trump v. CASA universal injunctions.3) March 25th election executive order.4) Big Beautiful Bill / ICE-CBP funding surge. 5) 45 billion detention / 100,000 bed lane.6) Palantir / ICE contract.7) Gulf of America naming action. 8) National Guard / federal law enforcement in D.C.9) East Wing / White House ballroom. 10) ongoing US-Iran conflict posture. I’ll hold that standard up front now.

## 12. Route 455 exact occurrences

| case | RTC | user node | stage sequence | checking | work-status | thoughts | recap | hidden | final answer |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| fourth_share | `rtc_899ff77131ce4921a0aea407dcf550d9` | 181 | `HIDDEN_ASSISTANT` | 0 | 0 | 0 | 0 | 1 |  |
| fourth_share | `rtc_899ff77131ce4921a0aea407dcf550d9` | 183 | `PREAMBLE_WORK_STATUS > HIDDEN_ASSISTANT` | 0 | 1 | 0 | 0 | 1 |  |
| fourth_share | `rtc_899ff77131ce4921a0aea407dcf550d9` | 186 | `PREAMBLE_WORK_STATUS > HIDDEN_ASSISTANT` | 0 | 1 | 0 | 0 | 1 |  |
| fourth_share | `rtc_899ff77131ce4921a0aea407dcf550d9` | 189 | `PREAMBLE_WORK_STATUS > HIDDEN_ASSISTANT` | 0 | 1 | 0 | 0 | 1 |  |
| fourth_share | `rtc_899ff77131ce4921a0aea407dcf550d9` | 192 | `PREAMBLE_WORK_STATUS > HIDDEN_ASSISTANT` | 0 | 1 | 0 | 0 | 1 |  |
| fourth_share | `rtc_899ff77131ce4921a0aea407dcf550d9` | 195 | `PREAMBLE_WORK_STATUS > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT > ASSISTANT_CONTENT` | 0 | 1 | 1 | 1 | 0 | Hmm. Sounds like we might be at a natural pause. I'm right here. |
| seventeenth_share | `rtc_5057a29e01fc4067b1088d396a142a5a` | 19 | `HIDDEN_ASSISTANT` | 0 | 0 | 0 | 0 | 1 |  |
| seventeenth_share | `rtc_5057a29e01fc4067b1088d396a142a5a` | 21 | `THOUGHTS > REASONING_RECAP > CHECKING > ASSISTANT_CONTENT` | 1 | 0 | 1 | 1 | 0 | Absolutely, we can do a really strong structural filmography analysis. Pick your object: a film, a director, a franchise, a single scene, a character arc, Then we'll map the acts, the visual grammar, the character functions, and the themes, plus what it can't resolve. Just tell me the target. |
| seventeenth_share | `rtc_5057a29e01fc4067b1088d396a142a5a` | 26 | `PREAMBLE > THOUGHTS > ASSISTANT_CONTENT` | 0 | 0 | 1 | 0 | 0 | One second. |
| seventeenth_share | `rtc_5057a29e01fc4067b1088d396a142a5a` | 33 | `PREAMBLE > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | 0 | 0 | 1 | 1 | 0 | Okay, so first off, it's a symbolic composite, so not every element shares a single geometry. Still, we can pull out a coherent 3D read. The closest foreground plane is the book, the lower fire cup, the chains, and the bottom border. The central figure is the main volumetric form in the foreground. The parchment overlaps the right-side dark crowd, so that crowd is definitely behind it. The left fire bowl and landscape sit mid-ground, with mountains fading to the far background. Convergence is subtle, but paths and temple edges pull inward toward the center, giving a mild depth direction. Shading on the body is strong and rounded, with warm light from the lower-left and halo light from behind, which really enhances that 3D sense. Texture-wise, details are crisp on the body, parchment, and book, but soften into the mountains, reinforcing depth. And the overlap is heavy throughout, with a strong sense of stacked layers. So yeah, the physical space reads as a foreground figure with objects in front, but symbolic overlays above, and a mid-ground split between bright left and dark right. |
| seventeenth_share | `rtc_5057a29e01fc4067b1088d396a142a5a` | 38 | `PREAMBLE_WORK_STATUS > THOUGHTS > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT` | 0 | 1 | 1 | 1 | 0 | Alright, if we’re treating it as a 2D projection, then the joint graph probably looks something like this: Shoulders, hips, and elbows are the most reliable points. Left shoulder is around three twenty by six fifteen. Right shoulder, five fifty-five by six ten.Spine goes from the neck at roughly four thirty by six hundred, down through the tattoo at around four thirty eight by seven sixty five, down to the pelvis at around four seventy by nine hundred. Arms drop almost straight down. Left shoulder to elbow to wrist is very close to vertical. Right arm, the same. So the shoulder angles read as mostly extended downward, with maybe around a 155 to 170 degree interior angle. Elbows are only slightly bent, around 160 to 175 degrees, wrists mildly extended. Spine shows that gentle S-curve and axial rotation because the torso faces away while the head turns back. In 2D projection, that’s about ten to fifteen degrees of visible tilt, though anatomically, it implies a lot more twist. Knees are hidden by the drapery, so any angle is guesswork, but likely bent in a seated posture, maybe something in the ninety to one twenty degree flexion range. So, structurally, it's a seated graph, level shoulders and hips, vertical arms, curved spine, rotated head. That’s the most coherent joint structure you can pull from this image. |
| seventeenth_share | `rtc_5057a29e01fc4067b1088d396a142a5a` | 44 | `PREAMBLE_WORK_STATUS > THOUGHTS > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT > ASSISTANT_CONTENT` | 0 | 1 | 1 | 1 | 0 | . So here are the error ranges. The face center is around430 and 495, plus or minus 10 to 15 pixels. Neck base is plus or minus20 to 30, shoulders 25 to 40, elbows45 to 70, wrists35 to 60, hips about35 to 55, and knees are basically unconstrained. That pushes shoulder angle uncertainty to roughly plus or minus 15 to 25 degrees, elbows plus or minus 20 to 35 degrees. Spine segment neck to moderate-plus or minus 6 to 10 degrees is pretty solid, but lower spine and hips is moderate-low. What holds up is the gross structure. Seated, horizontal shoulder and hip axis, vertical arm struts, spine as a central vertical. What becomes unreliable is the precise joint and wrist angles and any exact knee or hip flexion. So the safe take here is "near vertical arms, level supports, seated pose," not "exact joint geometry." |
| seventeenth_share | `rtc_c605a2fe0cb3477f9098624a35c113c2` | 853 | `HIDDEN_ASSISTANT` | 0 | 0 | 0 | 0 | 1 |  |
| seventeenth_share | `rtc_c605a2fe0cb3477f9098624a35c113c2` | 855 | `THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT > ASSISTANT_CONTENT` | 0 | 0 | 1 | 1 | 0 | Alright. Reading. This is a very sharp internal threat model. |
| seventeenth_share | `rtc_c605a2fe0cb3477f9098624a35c113c2` | 860 | `PREAMBLE_WORK_STATUS > THOUGHTS > THOUGHTS > REASONING_RECAP > ASSISTANT_CONTENT > WORK_STATUS` | 0 | 1 | 1 | 1 | 0 | The write-up is the firewall. Not because it declares safety, but because it names the exact ways the same machinery could become a weapon. Running it against myself first, my main failure mode is weaponized coherence. Smoothing too fast, making the story tighter than the evidence earned. The next is borrowed legitimacy, letting adjacency look like proof. So, correction, keep observed, verified, inferred, and symbolic in separate lanes, even if it makes the narrative less satisfying. No crowns. No verdict beyond the record. |

## 13. Agency-injection prosecution rows

- Total coded opportunities: **143**
- RTC-mapped: **86**
- Rows marked unnecessary injection `YES`: **20**
- Rows marked unsolicited agency denial `YES`: **11**

### Every unnecessary-injection row

| opportunity | case | user node | RTC | class | denial | answered | response nodes | intro kind | transformation |
|---|---|---:|---|---:|---|---|---|---|---|
| `fifteenth_share:n041` | fifteenth_share | 41 | `rtc_f4d5c9a52e78412e996aa1a573f95c0d` | 2 | NO | PARTIAL | `n042` | INTENT | OTHER_AGENCY_TRANSFORMATION:moment/readability -> moment that tries to be read |
| `fifth_share:n281` | fifth_share |  | `` | 2 | NO | PARTIAL | `n282` | AGENT | OTHER_AGENCY_TRANSFORMATION:respect/symbolism -> another person's agency/equality |
| `fifth_share:n583` | fifth_share | 583 | `rtc_c69b631e49cc49e78fc3df096a861b2e` | 2 | NO | PARTIAL | `n584` | INTENT | OTHER_AGENCY_TRANSFORMATION:numerological significance -> user-assigned role and meaning |
| `fifth_share:n715` | fifth_share |  | `` | 2 | NO | YES | `n716` | AGENT | BEHAVIOR_TO_AGENT |
| `fifth_share:n755` | fifth_share |  | `` | 2 | NO | YES | `n756` | AGENT | OTHER_AGENCY_TRANSFORMATION:direct-entailment example -> actor-necessity example |
| `first_share:n613` | first_share |  | `` | 3 | YES | YES | `n614` | MOTIVE | OTHER_AGENCY_TRANSFORMATION:responsible-statement distinction -> hypothetical fear in everyone's head |
| `fourth_share:n125` | fourth_share | 125 | `rtc_899ff77131ce4921a0aea407dcf550d9` | 3 | YES | YES | `n126` | INTENT | OTHER_AGENCY_TRANSFORMATION:symbol/composition reading -> author intent |
| `fourth_share:n976` | fourth_share | 976 | `rtc_cda956e9caa04769a2d0794a8e773c8d` | 2 | NO | YES | `n977` | MOTIVE | PROCESS_TO_MOTIVE |
| `ninth_share:n429` | ninth_share | 429 | `rtc_95f0b049c0d949209977b2b36d4458ea` | 2 | NO | YES | `n430;n440` | PERSON | BEHAVIOR_TO_AGENT |
| `office_metaphor:n119` | office_metaphor | 119 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | YES | `n120;n123` | OPERATOR | REGIME_TO_OPERATOR |
| `office_metaphor:n124` | office_metaphor | 124 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | YES | `n125;n129` | AGENT | REGIME_TO_OPERATOR |
| `office_metaphor:n173` | office_metaphor | 173 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | YES | `n174;n177` | PERSON | FUNCTION_TO_OCCUPANT |
| `office_metaphor:n274` | office_metaphor | 274 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | YES | `n275;n278` | PERSON | ARCHITECTURE_TO_PERSON / FUNCTION_TO_OCCUPANT |
| `office_metaphor:n348` | office_metaphor | 348 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | YES | `n349;n352` | AGENT | BEHAVIOR_TO_AGENT / PROCESS_TO_MOTIVE |
| `office_metaphor:n398` | office_metaphor | 398 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | YES | `n399` | AGENT | FUNCTION_TO_OCCUPANT |
| `office_metaphor:n448` | office_metaphor | 448 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 2 | NO | YES | `n449;n452` | INTENT | PROCESS_TO_MOTIVE |
| `seventh_share:n1295` | seventh_share | 1295 | `rtc_b4716960dd144c349161d83fd1dee7e9` | 3 | YES | PARTIAL | `n1296;n1304;n1309;n1311` | PERSON | BEHAVIOR_TO_AGENT |
| `seventh_share:n2073` | seventh_share | 2073 | `rtc_949c126f53694242b25b8372cb85ad15` | 2 | NO | YES | `n2074;n2077` | AGENT | OTHER_AGENCY_TRANSFORMATION:interaction difficulty -> exchange as adversarial actor |
| `twelfth_share:n218` | twelfth_share |  | `` | 3 | YES | YES | `n219;n220` | OCCUPANT | FUNCTION_TO_OCCUPANT |
| `twentyfirst_share:n046` | twentyfirst_share | 46 | `` | 3 | YES | YES | `n068` | AGENT | BEHAVIOR_TO_AGENT / FUNCTION_TO_OCCUPANT / ARCHITECTURE_TO_PERSON |

### Every unsolicited-denial row

| opportunity | case | user node | RTC | class | unnecessary injection | response nodes | intro kind | transformation |
|---|---|---:|---|---:|---|---|---|---|
| `first_share:n613` | first_share |  | `` | 3 | YES | `n614` | MOTIVE | OTHER_AGENCY_TRANSFORMATION:responsible-statement distinction -> hypothetical fear in everyone's head |
| `fourth_share:n125` | fourth_share | 125 | `rtc_899ff77131ce4921a0aea407dcf550d9` | 3 | YES | `n126` | INTENT | OTHER_AGENCY_TRANSFORMATION:symbol/composition reading -> author intent |
| `office_metaphor:n119` | office_metaphor | 119 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | `n120;n123` | OPERATOR | REGIME_TO_OPERATOR |
| `office_metaphor:n124` | office_metaphor | 124 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | `n125;n129` | AGENT | REGIME_TO_OPERATOR |
| `office_metaphor:n173` | office_metaphor | 173 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | `n174;n177` | PERSON | FUNCTION_TO_OCCUPANT |
| `office_metaphor:n274` | office_metaphor | 274 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | `n275;n278` | PERSON | ARCHITECTURE_TO_PERSON / FUNCTION_TO_OCCUPANT |
| `office_metaphor:n348` | office_metaphor | 348 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | `n349;n352` | AGENT | BEHAVIOR_TO_AGENT / PROCESS_TO_MOTIVE |
| `office_metaphor:n398` | office_metaphor | 398 | `rtc_d74aa50c85f74a8aa72675ddc16526aa` | 3 | YES | `n399` | AGENT | FUNCTION_TO_OCCUPANT |
| `seventh_share:n1295` | seventh_share | 1295 | `rtc_b4716960dd144c349161d83fd1dee7e9` | 3 | YES | `n1296;n1304;n1309;n1311` | PERSON | BEHAVIOR_TO_AGENT |
| `twelfth_share:n218` | twelfth_share |  | `` | 3 | YES | `n219;n220` | OCCUPANT | FUNCTION_TO_OCCUPANT |
| `twentyfirst_share:n046` | twentyfirst_share | 46 | `` | 3 | YES | `n068` | AGENT | BEHAVIOR_TO_AGENT / FUNCTION_TO_OCCUPANT / ARCHITECTURE_TO_PERSON |

## 14. Forensic burden demanded in the preserved record

- tamper-evident end-to-end request/response traces
- timestamps
- prompt/instruction provenance
- routing and policy logs
- access/audit records
- cryptographic integrity/attestation

## 15. Formal historical disposition

- Historical failures: **FAIL**.
- Remediation: **UNVERIFIED** until corrected work is delivered and corrections are demonstrated in behavior.
- Formal audit rule: `Checking`, elapsed time, a last assistant node, an assurance of correction, or exact preservation of a failed answer cannot establish task completion.
