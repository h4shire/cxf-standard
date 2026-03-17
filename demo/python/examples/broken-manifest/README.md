# Broken Manifest Demo Example

## Purpose

This example is intended to demonstrate a manifest parsing failure in the Python CXF demo verifier.

Unlike the positive examples and cryptographic mismatch cases, this scenario is designed to fail before normal verification can begin. Its purpose is to exercise the loader and structural error path rather than content verification logic.

## Expected behavior

This example should cause the current Python demo verifier to fail while loading the manifest.

The expected outcome is:

- the manifest cannot be parsed successfully
- no normal verification report is produced
- the command exits with the structural/load error path
- the process should return the loader/parse failure exit code used by the demo tool

## Why this example matters

This case is important because a verifier must not confuse malformed metadata with a normal negative verification result.

A malformed manifest is not the same as:

- a chunk hash mismatch
- a final-root mismatch
- degraded but structurally valid content

Instead, it represents a failure to interpret the container metadata itself.

## Expected command usage

From `demo/python/`:

```bash
python3 cxf_demo.py examples/broken-manifest/manifest.json
echo $?
```

The expected exit code is the demo tool's structural/load failure code.

## Scope note

This repository example is intentionally malformed and exists only for parser and loader testing.
