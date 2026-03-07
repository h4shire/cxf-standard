# Signed-Valid Python Demo Example

This directory contains a runnable `signed-valid` example for the CXF Python demo verifier.

## Purpose

This example is more realistic than the `minimal-valid` example and is intended to represent a standard verification case for a valid evidentiary container model. It uses three chunks, a deterministic manifest, and a precomputed expected final root.

## Included files

- `manifest.json` — the demo manifest used by the Python verifier
- `expected-report.json` — the expected summary values for a successful run
- `chunks/` — three input chunks referenced by the manifest

## How to run

From `demo/python/`:

```bash
python3 cxf_demo.py examples/signed-valid/manifest.json
```

To also write a report file:

```bash
python3 cxf_demo.py examples/signed-valid/manifest.json --out examples/signed-valid/generated-report.json
```

## Expected outcome

A successful run should produce:

- a valid layout result
- a verified final root
- three verified chunks
- zero mismatches

## Scope note

This is a repository demo artifact for the Python prototype. It complements the English documentation in `examples/sample-containers/` and `examples/sample-reports/`, but it is not itself a normative CXF artifact.
