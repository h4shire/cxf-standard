
from __future__ import annotations

import argparse
import json
from pathlib import Path

from lib.compare import compare_reports, load_expected_report
from lib.manifest import load_manifest
from lib.verifier import verify_manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="CXF Python demo verifier")
    parser.add_argument("manifest", help="Path to a JSON or CBOR manifest")
    parser.add_argument("--out", help="Write generated report JSON to this file")
    parser.add_argument("--expect", help="Compare the generated report against an expected JSON report")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print JSON output")
    parser.add_argument("--strict", action="store_true", help="Fail with exit code 3 when --expect comparison differs")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest)

    try:
        manifest, manifest_raw = load_manifest(manifest_path)
        report = verify_manifest(manifest, manifest_raw, manifest_path)
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 2

    payload = report.to_dict()
    indent = 2 if args.pretty or args.out else 2
    text = json.dumps(payload, indent=indent)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text + "\n", encoding="utf-8")

    mismatches = []
    if args.expect:
        try:
            expected = load_expected_report(args.expect)
            mismatches = compare_reports(payload, expected)
        except Exception as exc:
            print(f"ERROR: expectation handling failed: {exc}")
            return 2

    print(text)

    if mismatches:
        print("\nExpectation mismatches:")
        for item in mismatches:
            print(f"- {item}")
        if args.strict:
            return 3

    verification_state = payload["summary"]["verification_state"]
    return 0 if verification_state == "verified" else 1


if __name__ == "__main__":
    raise SystemExit(main())
