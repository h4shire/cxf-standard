# CBOR Manifest Valid Demo Example

## Purpose

This example demonstrates a valid CXF demo case using a CBOR manifest instead of a JSON manifest.

Its purpose is to show that the Python demo verifier can process the same logical container metadata through the CBOR path while preserving the same root-of-truth semantics used by the JSON-based examples.

## Expected behavior

This example should verify successfully.

The expected outcome is:

- the manifest is parsed from CBOR
- both chunk hashes verify successfully
- the calculated final root matches the declared expected final root
- the verifier produces a normal positive report
- the command exits with code 0

## Why this example matters

This case is important because CXF is designed around deterministic CBOR as the authoritative metadata form. A JSON demo path is useful for readability, but a CBOR example is necessary to demonstrate the intended metadata direction of the format.

## Expected command usage

From `demo/python/`:

```bash
python3 cxf_demo.py examples/cbor-manifest-valid/manifest.cbor
python3 cxf_demo.py examples/cbor-manifest-valid/manifest.cbor --expect examples/cbor-manifest-valid/expected-report.json --strict
echo $?
```

The expected exit code for strict validation is `0`.
