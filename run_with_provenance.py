"""Run the C6 tests and emit a hash-bound execution provenance record."""

from __future__ import annotations

import hashlib
import json
import platform
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from reference_trace import write_reference_trace


ROOT = Path(__file__).resolve().parent
HASHED_FILES = (
    "corner_relay.py",
    "test_corner_relay.py",
    "run_with_provenance.py",
    "reference_trace.py",
    "README.md",
    "C6_RESULT.md",
    "FROZEN_PACKET.txt",
    "source_binding.json",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source_binding = json.loads((ROOT / "source_binding.json").read_text(encoding="utf-8"))
    observed_packet_hash = sha256_file(ROOT / "FROZEN_PACKET.txt")
    expected_packet_hash = source_binding["frozen_packet_sha256"]
    source_binding_ok = observed_packet_hash == expected_packet_hash
    started_wall = time.monotonic()
    started_utc = datetime.now(timezone.utc)
    command = [sys.executable, "-m", "unittest", "-v", "test_corner_relay.py"]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    finished_utc = datetime.now(timezone.utc)
    duration = time.monotonic() - started_wall
    match = re.search(r"Ran\s+(\d+)\s+tests?", completed.stdout)
    test_count = int(match.group(1)) if match else None
    trace_hash = write_reference_trace(ROOT / "reference_trace.json")
    hashes = {name: sha256_file(ROOT / name) for name in HASHED_FILES}
    hashes["reference_trace.json"] = sha256_file(ROOT / "reference_trace.json")
    effective_return_code = completed.returncode if source_binding_ok else 2
    provenance = {
        "schema": "corner-relay-alpha/execution-provenance/v1",
        "artifact_id": "Corner-Relay-alpha-C6-reference-v0.1",
        "track": "Python 3 code plus tests",
        "execution_status": "PASS" if effective_return_code == 0 else "FAIL",
        "return_code": effective_return_code,
        "test_return_code": completed.returncode,
        "tests_run": test_count,
        "command": "python -m unittest -v test_corner_relay.py",
        "started_utc": started_utc.isoformat(),
        "finished_utc": finished_utc.isoformat(),
        "duration_seconds": round(duration, 6),
        "runtime": {
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "executable": sys.executable,
        },
        "artifact_file_sha256": hashes,
        "test_output_sha256": hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest(),
        "test_output": completed.stdout,
        "reference_trace_sha256": trace_hash,
        "source_binding": source_binding,
        "source_binding_verification": {
            "status": "PASS" if source_binding_ok else "FAIL",
            "expected_frozen_packet_sha256": expected_packet_hash,
            "observed_frozen_packet_sha256": observed_packet_hash,
        },
        "claim_boundary": (
            "This execution establishes only that this artifact passed its declared tests "
            "in the recorded environment. It does not identify a hidden source or mechanism."
        ),
    }
    output_path = ROOT / "execution_provenance.json"
    output_path.write_text(
        json.dumps(provenance, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(completed.stdout, end="")
    print(f"\nexecution_provenance={output_path.name}")
    print(f"execution_provenance_sha256={sha256_file(output_path)}")
    print(f"reference_trace_sha256={trace_hash}")
    return effective_return_code


if __name__ == "__main__":
    raise SystemExit(main())
