
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from lib.manifest import load_manifest
from lib.verifier import verify_manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="CXF Python demo verifier")
    parser.add_argument("manifest", help="Path to a demo manifest (.json or .cbor)")
    parser.add_argument("--out", help="Optional path to write the JSON verifier report")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    manifest = load_manifest(manifest_path)
    report = verify_manifest(manifest_path, manifest)
    report_dict = report.to_dict()

    output = json.dumps(report_dict, indent=2)
    print(output)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
