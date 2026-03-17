#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

EXAMPLES = [
    {
        "name": "minimal-valid",
        "manifest": "examples/minimal-valid/manifest.json",
        "expect": "examples/minimal-valid/expected-report.json",
        "expected_exit": 0,
        "description": "Minimal positive reference case",
    },
    {
        "name": "signed-valid",
        "manifest": "examples/signed-valid/manifest.json",
        "expect": "examples/signed-valid/expected-report.json",
        "expected_exit": 0,
        "description": "Realistic positive signed-valid case",
    },
    {
        "name": "tampered-chunk",
        "manifest": "examples/tampered-chunk/manifest.json",
        "expect": "examples/tampered-chunk/expected-report.json",
        "expected_exit": 1,
        "description": "Chunk mismatch and final-root failure",
    },
    {
        "name": "wrong-final-root",
        "manifest": "examples/wrong-final-root/manifest.json",
        "expect": "examples/wrong-final-root/expected-report.json",
        "expected_exit": 1,
        "description": "All chunks verify but declared final root is wrong",
    },
    {
        "name": "missing-chunk",
        "manifest": "examples/missing-chunk/manifest.json",
        "expect": "examples/missing-chunk/expected-report.json",
        "expected_exit": 1,
        "description": "Manifest references a missing chunk file",
    },
    {
        "name": "broken-manifest",
        "manifest": "examples/broken-manifest/manifest.json",
        "expect": None,
        "expected_exit": 2,
        "description": "Manifest parse / load failure",
    },
    {
        "name": "cbor-manifest-valid",
        "manifest": "examples/cbor-manifest-valid/manifest.cbor",
        "expect": "examples/cbor-manifest-valid/expected-report.json",
        "expected_exit": 0,
        "description": "Positive CBOR manifest example",
    },
    {
        "name": "multi-chunk-large",
        "manifest": "examples/multi-chunk-large/manifest.json",
        "expect": "examples/multi-chunk-large/expected-report.json",
        "expected_exit": 0,
        "description": "Larger positive multi-chunk example",
    },
]


def color(text: str, code: str, enabled: bool) -> str:
    if not enabled:
        return text
    return f"\033[{code}m{text}\033[0m"


def run_case(case: dict, python_cmd: str, strict: bool, use_color: bool) -> int:
    cmd = [python_cmd, "cxf_demo.py", case["manifest"]]
    if strict and case["expect"]:
        cmd.extend(["--expect", case["expect"], "--strict"])

    print(color(f"\n==> {case['name']}", "1;34", use_color))
    print(f"    {case['description']}")
    print("    " + " ".join(cmd))

    completed = subprocess.run(cmd)
    actual = completed.returncode
    expected = case["expected_exit"]

    if actual == expected:
        print(color(f"    PASS (exit {actual})", "1;32", use_color))
        return 0

    print(color(f"    FAIL (expected exit {expected}, got {actual})", "1;31", use_color))
    return 1


def main() -> int:
    root = Path(__file__).resolve().parent
    python_cmd = sys.executable
    strict = True
    use_color = sys.stdout.isatty()

    failures = 0
    print(color("CXF Python Demo Example Runner", "1;36", use_color))
    print(f"Working directory: {root}")
    print(f"Python executable: {python_cmd}")

    for case in EXAMPLES:
        failures += run_case(case, python_cmd, strict=strict, use_color=use_color)

    total = len(EXAMPLES)
    passed = total - failures
    print(color("\nSummary", "1;36", use_color))
    print(f"  Passed: {passed}")
    print(f"  Failed: {failures}")
    print(f"  Total : {total}")

    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
