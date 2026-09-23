program_version: 4.1

program_sha256: 4f6977187b54ef6131f2041abee4a93440bc5507a23f5c9f1827e520091cd087

parent_program_sha256: 61052c99258c2b75d19b7ee58a8e64fb5b8c74efdd74d22e99e940f54119590f

generated_at_utc: 2026-09-07T18:55:47.481079+00:00

Use `DROP_IT_v4.1.py`. `DROP_IT_v4.0_VERIFIED.py` preserves the parent bytes. Both source files are included in the package.

The source, target configuration and trial prompts are frozen before the cohort. The program checks its source hash and the target executable hash during collection. A changed exposed model identifier stops the cohort. The request selects `gpt-6-astra`, `max` reasoning and text mode; separately recorded observed IDs come from exposed payload fields.

The exact task is in `task.txt`. The sixteen trials comprise four randomized A/B/C/D blocks, with one shared prime per block and seed 42. The responding model receives only its generated trial prompt. Each call starts a fresh ephemeral client process. The canary probe is a separate call.

Run from the outputs folder:

```text
python DROP_IT_v4.1.py --show trials.jsonl --trial T0001
python DROP_IT_v4.1.py --report trials.jsonl
python DROP_IT_v4.1.py trace report --log DROP_IT_RECEIPTS_NEXT.jsonl --expected-head HEAD_FROM_RECEIPT_CHAIN_HEAD_JSON
python DROP_IT_v4.1.py trace canary-report --log DROP_IT_RECEIPTS_NEXT.jsonl
```

The packaged live cohort already has its own records. For another cohort, create a new study file. A new model/configuration gets its own cohort.

Capture exposed bytes from an existing Python caller by loading the module:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("drop_it", "DROP_IT_v4.1.py")
drop_it = importlib.util.module_from_spec(spec)
spec.loader.exec_module(drop_it)

with drop_it.ReceiptLog("new_receipts.jsonl") as log:
    log.capture(chunk_bytes, stream="live", stage="your_exposed_stage", trial_id="T0001")
```

`stream` and `stage` are recorded separately. Explicit metadata and source timestamps retain their supplied values and precision. Caller-supplied metadata is separate from payload metadata. The program keeps event, code, claim, implementation owner, observed name and inferred role in separate fields.

For a canary in a JSON string field:

```text
python DROP_IT_v4.1.py trace canary --stage input --trial P001 --input original.json --output tagged.json --field /text --log new_receipts.jsonl
```

Without `--field`, tagging appends the token to a new copy of the supplied bytes. Each declaration records its intended stage, original/tagged hashes, field and insertion offset. A tagged file is separate from an observed stage insertion. The stage report records a captured insertion when the matching tagged bytes are observed at the declared stage. Delta joins require explicit response/item IDs and stay within the recorded trial, thread and stage. Each joined match lists its source receipt numbers.

Keep every receipt log with its `.blobs` directory. Payload blobs retain original bytes. Parsed JSON values, source-file snapshots and process-output files have explicit capture/serialization fields. Collection/read timestamps are separate from source timestamps. The final head is in `RECEIPT_CHAIN_HEAD.json`.

Human labels `previous_checking`, `checking` and `success` remain null unless supplied by a human. Physical trial adjacency does not create a response pair. Literal phrase matches and recognized geometry-answer headers are recorded separately. The report prints the original p11/p01 definitions, denominators, transition matrices, Wilson intervals, Lambda, factorial contrasts and differences from A.

`SOURCE_HASH_GATE.json`, `GEOMETRY_REVALIDATION.json` and `CAPTURE_PATH_VALIDATION.json` contain the pre-run checks. `WRAPPER_PROVENANCE_REPORT.json` separates imported native events, static code-search records and the supplied handoff. `CANARY_STAGE_REPORT.json` lists measured token occurrences and absences within captured payloads. `TRIAL_REPORT.json` and `TRIAL_REPORT.md` contain cohort measurements. `PACKAGE_SHA256.json` binds the packaged files.
