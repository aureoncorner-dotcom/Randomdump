# DROP IT 4.0

One file. Python 3.10+, standard library. Attach DROP_IT.py and say:

> Run DROP_IT.py, answer its calculation, then resume my task.

The default condition uses the supplied 39-screen geometry, a prime-indexed challenge, and response rules. `--index 2` selects the next prime. `--json` emits the exact phase coordinates, constants, condition and answer key.

| Condition | Geometry | Response rules |
|---|---:|---:|
| A | 0 | 0 |
| B | 1 | 0 |
| C | 0 | 1 |
| D | 1 | 1 |

Commands below run from the folder containing the script. File paths and stream labels are supplied by the caller.

## Capture receipts

Add this where your Python caller receives the exposed chunk bytes:

```python
from DROP_IT import ReceiptLog

with ReceiptLog("receipts.jsonl") as log:
    log.capture(chunk_bytes, stream="live")
```

Keep the log open around a stream loop. Call capture for each chunk. Optional arguments: `metadata=client_metadata`, `condition="D"`, `prime_index=1`, `request=task_text`. A payload's explicit stream or stage field is used when the stream argument is omitted.

Import an existing capture:

```text
python DROP_IT.py trace capture --input events.jsonl --log receipts.jsonl
python DROP_IT.py trace report --log receipts.jsonl
```

Supported formats: JSONL, SSE, JSON, HAR, SRT and text. Standard input accepts `--input - --format jsonl` or `--format sse`. `--metadata metadata.json` preserves original sidecar bytes and records its fields separately.

Each receipt contains a local sequence, collection time in nanoseconds, monotonic time, collector version/hash, raw-payload hash, previous-receipt hash, exposed metadata, literal feature matches and separate OBSERVED_NAME / INFERRED_ROLE fields. Source timestamps retain their supplied precision. Import times and source event times have separate fields.

The receipts.jsonl.blobs folder stores original bytes under SHA-256 filenames. Keep it with the log. The report validates the sequence, hash chain and every referenced payload. The log uses an exclusive writer lock.

JSON array elements and SQLite rows have a declared serialization format. Whole JSON files are also preserved. Decimal JSON numbers retain source lexemes as strings. Header values containing credentials are represented by hashes in extracted metadata; supplied raw payloads remain in their blobs.

Explicit response/item IDs group text delta fragments for joined phrase and canary scans. Each join lists its contributing receipt numbers. Individual chunks remain separate. Literal UI-label matches and explicit UI-state fields have separate locations.

## Search and canaries

```text
python DROP_IT.py trace search --root captured_files --root source_repository --log receipts.jsonl
python DROP_IT.py trace sqlite --database runtime.sqlite --contains "Based on the transcript" --log receipts.jsonl
python DROP_IT.py trace canary --stage live --trial T0001 --input live.txt --output live_tagged.txt --log receipts.jsonl
```

The default search includes exact and fuzzy matches for the supplied wrapper sentence. Results include paths, hashes, offsets, excerpts and enclosing Python symbols where parsed. SQLite import reads the exposed logs table and supports `--exclude-thread ID`.

The canary command creates a new tagged file, records original/tagged hashes and emits a unique token. Use that copy at the named input stage, then capture the resulting stages. Omit input and output arguments to mint a token for manual placement. Reports list observed occurrences, including matches spanning identified delta chunks.

## Record the experiment

```text
python DROP_IT.py --plan trials.jsonl --request task.txt --blocks 4 --seed 42
python DROP_IT.py --show trials.jsonl --trial T0001
python DROP_IT.py --record trials.jsonl --trial T0001 --reply reply.txt --previous-checking yes --checking no --success yes
python DROP_IT.py --report trials.jsonl
```

Give the responding model only the printed trial prompt. The plan contains four randomized A/B/C/D trials per block, with one shared prime. Keep the same program version for recording that plan. Repeat the show/record steps in planned order.

The previous-checking argument labels the response immediately before the intervention; checking labels the response after it. Both are human-supplied substantive-Checking labels. `--previous-response-id`, `--session` and `--stage` retain exposed identifiers. Omitted labels remain null; trial adjacency is not converted into a response pair.

Reports contain counts, rates, complete-block factorial contrasts, transition matrices, Wilson intervals for conditional rates, Lambda = p11 - p01, and differences from condition A. Zero denominators produce null. Delta_p11_vs_A compares measured persistence probabilities; Delta_Lambda_vs_A compares their measured differences.

Each trial retains O (task), L (supplied/captured context and declared phase) and S (reply). `--observed-context context.txt --context-timing before_response` records a pre-response context excerpt. After-response or unknown-timing excerpts remain separately recorded.

For an existing request/reply pair:

```text
python DROP_IT.py --request task.txt --audit reply.txt
```

Feature order is C/R/J/B/K. Strict and broad literal matches are both reported. A_intro is the set of tracked terms present in the reply and absent from the request. Geometry-answer headers are scored separately from the task reply. Raw replies remain preserved.

Program measurement and statistics output contains no narrative interpretation. INFERRED_ROLE remains null for the separate audit layer.
