# Demo Example: Minimal Valid

This directory contains the first runnable example for the CXF Python demo prototype.

## Files

- `manifest.json`  
  A simple demo manifest used by the prototype verifier.

- `chunks/chunk-0000.bin`  
  The first demo chunk.

- `chunks/chunk-0001.bin`  
  The second demo chunk.

- `expected-report.json`  
  A compact expectation file describing the intended high-level verification result.

## Run

From `demo/python/`:

```bash
python3 cxf_demo.py examples/minimal-valid/manifest.json
```

## Intent

This is not a full CXF container bitstream example. It is a practical prototype fixture for validating the first demo verifier logic against stable test data.
