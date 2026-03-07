# Minimal Valid Demo Example

This directory contains the first runnable example set for the Python CXF demo verifier.

## Included files

- `manifest.json`  
  A simple JSON manifest used by the prototype.
- `chunks/`  
  The demo chunk payloads.
- `expected-report.json`  
  A sample expected-style output for comparison and inspection.

## Usage

From `demo/python/` run:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json
```

Or write the output to a file:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json --out examples/minimal-valid/generated-report.json
```

## Note

This example is intentionally small and is meant only to demonstrate the first end-to-end verification path of the Python prototype.
