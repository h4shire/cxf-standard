# Multi-Chunk Large Demo Example

## Purpose

This example demonstrates a larger positive verification case for the Python CXF demo verifier.

Unlike the smaller minimal-valid and signed-valid examples, this case contains a broader chunk set and is intended to exercise the demo verifier's chunk loop and Merkle-style final-root derivation on a slightly more substantial payload set.

## Expected behavior

This example should verify successfully.

The expected outcome is:

- the manifest loads successfully
- all chunk files are present
- all chunk hashes verify successfully
- the calculated final root matches the declared expected final root
- the verifier produces a normal positive report
- the command exits with code 0

## Why this example matters

This case is useful because it gives the demo suite a larger positive reference point without introducing recovery, bridge, or policy complexity.

It helps demonstrate:

- stable multi-chunk hashing behavior
- deterministic root derivation over a larger set
- confidence that the verifier logic scales beyond the smallest examples

## Expected command usage

From `demo/python/`:

```bash
python3 cxf_demo.py examples/multi-chunk-large/manifest.json
python3 cxf_demo.py examples/multi-chunk-large/manifest.json --expect examples/multi-chunk-large/expected-report.json --strict
echo $?
```

The expected exit code for strict validation is `0`.
