# CXF Python Demo Verifier

This directory contains a small Python prototype for demonstrating selected CXF verification flows.

The prototype is intentionally limited. It is **not** a full CXF 1.0 implementation and it is **not** a normative reference implementation. Its purpose is to support repository examples, demonstrate verifier behavior, and provide a lightweight local test harness for early CXF artifacts.

## Current capabilities

The demo currently supports:

- loading a JSON or CBOR-style manifest
- deriving a manifest hash from the manifest bytes
- hashing referenced chunk files with SHA3-256
- deriving a simple Merkle-style final root
- generating a JSON verifier-style report
- writing the generated report to disk
- comparing the generated report against an expected report
- returning stable exit codes for use in local validation and CI-style checks

## Exit codes

The CLI uses the following exit codes:

- `0` — verification completed successfully and the resulting verification state is `verified`
- `1` — verification completed but the resulting verification state is not `verified`
- `2` — loading, parsing, path, or structural execution error
- `3` — expectation mismatch when `--expect` is used

## Usage

Run a basic verification:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json
```

Write the generated report to a file:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json \
  --out examples/minimal-valid/generated-report.json
```

Pretty-print the report:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json --pretty
```

Compare the generated report with an expected report:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json \
  --expect examples/minimal-valid/expected-report.json
```

Strict mode treats any expectation mismatch as an explicit failure condition:

```bash
python3 cxf_demo.py examples/tampered-chunk/manifest.json \
  --expect examples/tampered-chunk/expected-report.json \
  --strict
```

## Notes

- This prototype uses a simplified Merkle-style derivation suitable for repository demonstration.
- The standardized CXF verifier output is expected to be signed; this demo currently produces an unsigned JSON report for development and testing purposes.
- The examples in `examples/` are intentionally small and readable so they can be inspected and understood without special tooling.
