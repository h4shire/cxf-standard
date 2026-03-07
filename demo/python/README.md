# CXF Python Demo Prototype

This directory contains a small Python prototype for experimenting with core CXF verification concepts.

The goal of this prototype is not to provide a complete CXF implementation. Instead, it provides a lightweight starting point for:

- loading a manifest from JSON or CBOR
- computing SHA3-256 chunk hashes
- deriving a simple Merkle-style final root from chunk hashes
- comparing the derived root with the expected root in the manifest
- producing a small demo verifier output as JSON

## Scope

This prototype is intentionally limited.

It currently focuses on:

- manifest loading
- chunk hashing
- final-root derivation
- basic report generation

It does **not** yet implement:

- full CXF bitstream parsing
- COSE signing
- receipt generation
- BridgeAuditTrail handling
- DigestSunsetDecisionRecord handling
- LTR-1 to LTR-4 validation
- discovery sidecar validation

## Files

- `cxf_demo.py` — command-line entry point
- `requirements.txt` — Python dependency list

## Manifest format used by this prototype

The prototype accepts a JSON or CBOR manifest with a structure similar to the following:

```json
{
  "bitstream_version": "1.0",
  "active_profile_ids": ["sha3-256", "demo-merkle"],
  "logical_size": 12345,
  "chunk_count": 2,
  "expected_final_root": "<hex sha3-256 digest>",
  "chunks": [
    {
      "chunk_id": 0,
      "path": "chunk0.bin"
    },
    {
      "chunk_id": 1,
      "path": "chunk1.bin"
    }
  ]
}
```

Notes:

- `expected_final_root` is optional. If omitted, the prototype will still compute and display the derived root.
- Chunk paths are resolved relative to the manifest file.
- The demo Merkle procedure is deterministic and SHA3-256-based.

## Demo Merkle rule

This prototype uses a simple deterministic Merkle-style rule for demonstration:

- hash each chunk with SHA3-256
- if a level has an odd number of nodes, duplicate the last node
- parent hash = `SHA3-256(left || right)`
- continue until one root remains

This rule is intentionally simple and should be treated as a prototype mechanism, not as a final normative CXF implementation unless and until it is explicitly aligned with the final specification language.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Verify a manifest

```bash
python cxf_demo.py verify path/to/manifest.json
```

### Write verifier output to a file

```bash
python cxf_demo.py verify path/to/manifest.json --output verifier-output.json
```

### Pretty-print only

```bash
python cxf_demo.py verify path/to/manifest.json --pretty
```

## Example verifier output

The prototype produces a small JSON report with fields such as:

- `tool_identity`
- `build_identity`
- `manifest_path`
- `manifest_hash_sha3_256`
- `derived_final_root`
- `expected_final_root`
- `root_match`
- `verification_events`
- `summary`

This is a demo-oriented output format intended to help shape later work on a fuller verifier-output implementation.

## Intended next steps

The natural follow-up steps for this prototype are:

1. add canonical sample manifests and chunk files under `examples/`
2. support standardized CXF verifier-output field naming more closely
3. add CBOR output mode
4. add COSE signing for attested demo reports
5. evolve the prototype into a stronger reference implementation, likely in Rust
