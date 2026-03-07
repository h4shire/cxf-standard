# CXF Python Demo Prototype

This directory contains a small Python-based CXF demo verifier.

The prototype is intentionally limited. It is not a full CXF 1.0 implementation and it is not a normative reference implementation. Its purpose is to help the community experiment with:

- manifest loading
- SHA3-256 chunk hashing
- simple Merkle-style final root derivation
- generation of a small demo verifier output

## What it can do

The current prototype can:

1. load a manifest from JSON or CBOR
2. hash the chunk files referenced by the manifest
3. derive a simple deterministic final root
4. compare the derived value with `expected_final_root`
5. emit a demo verifier output as JSON

## What it does not do yet

The current prototype does not yet implement:

- the full CXF bitstream format
- full canonical CBOR validation
- COSE signing
- receipts
- bridge audit trails
- digest sunset records
- recovery evidence or LTR-4 logic

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the bundled example

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json
```

## Expected result

The demo prints a verifier-style JSON object to standard output.

For the bundled example, the output should indicate:

- a valid layout assumption
- a verified final root
- two verified chunks
- no bridge usage
- no recovery semantics

## Repository intent

This prototype is a practical development aid for the CXF repository. It is suitable for experimentation and early interoperability discussions. A future production-grade implementation would be better suited to Rust or C.
