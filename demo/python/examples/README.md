# CXF Python Demo Examples

This directory contains runnable example scenarios for the Python CXF demo verifier.

The examples are intentionally small, explicit, and easy to understand. Together they provide a compact local validation suite for the evolving demo implementation.

## Included examples

### Positive examples

- **minimal-valid**  
  Smallest useful positive reference case.

- **signed-valid**  
  More realistic positive verification example.

- **cbor-manifest-valid**  
  Positive example using a CBOR manifest.

- **multi-chunk-large**  
  Larger positive example with eight chunks.

### Negative examples

- **tampered-chunk**  
  One chunk has been modified and no longer matches its declared digest.

- **wrong-final-root**  
  All chunks verify successfully, but the declared expected final root is intentionally wrong.

- **missing-chunk**  
  The manifest references a required chunk file that is not present.

- **broken-manifest**  
  The manifest itself is malformed and cannot be parsed.

## Running all examples

From `demo/python/`:

```bash
python3 run_examples.py
```

The runner executes all example cases and checks that each one returns the expected exit code.

## Expected exit codes

The current Python demo verifier uses these exit codes:

- `0` — successful verification
- `1` — verification failure
- `2` — load / parse / structural runtime error
- `3` — expectation mismatch in strict mode

## Notes

These examples are designed for the Python demo prototype. They are repository-level runnable fixtures intended to support local development, quick verification checks, and future CI-style automation.
