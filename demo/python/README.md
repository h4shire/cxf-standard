# CXF Python Demo Prototype

This directory contains a small Python prototype for demonstrating core CXF verification concepts.

## Scope

This prototype is intentionally limited. It is **not** a full CXF 1.0 reference implementation and it does **not** produce a finalized signed verifier artifact. Its purpose is to support repository examples, implementation discussion, and early validation experiments.

## Current capabilities

The prototype can currently:

- load a demo manifest from JSON
- derive a deterministic manifest hash
- hash chunk files using SHA3-256
- derive a simple deterministic Merkle-style final root
- compare the calculated root with the expected root in the manifest
- emit a local demo verifier report as JSON
- optionally write the report to disk with `--out`

## Repository layout

```text
demo/python/
├── README.md
├── requirements.txt
├── cxf_demo.py
├── lib/
│   ├── __init__.py
│   ├── hashing.py
│   ├── manifest.py
│   ├── model.py
│   └── verifier.py
└── examples/
    └── minimal-valid/
        ├── README.md
        ├── manifest.json
        ├── expected-report.json
        └── chunks/
            ├── chunk-0000.bin
            └── chunk-0001.bin
```

## Quick start

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the demo verifier:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json
```

Write the verifier output to a file:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json --out report.json
```

## Notes

- `manifest_hash` is now derived from a canonical JSON encoding used by this demo prototype.
- The report format is still a local development artifact (`demo-v1`) and must not be confused with the final normative CXF 1.0 signed verifier output.
- The Merkle-style final-root logic in this prototype is intentionally simple and exists only to support repository examples and incremental implementation work.

## Next likely steps

- add a second example set such as `signed-valid`
- add malformed and negative test examples
- introduce CBOR manifest loading
- introduce schema-aware report generation
- later add proper COSE-based signing for standardized outputs
