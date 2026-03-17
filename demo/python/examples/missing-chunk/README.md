# Missing Chunk Demo Example

## Purpose

This example demonstrates a verification failure caused by a required chunk file being absent.

Unlike the tampered-content case, the chunk hash itself cannot be checked because the referenced file is missing. The demo verifier should represent this as an explicit missing-artifact condition rather than a normal chunk mismatch.

## Expected behavior

A run against this example should show:

- a structurally valid manifest
- one verified chunk
- one missing chunk
- a failed verification state
- degraded content state
- an explicit `chunk_missing` event
- a container-level failure event caused by missing required data

## Reference usage

From `demo/python/`:

```bash
python3 cxf_demo.py examples/missing-chunk/manifest.json
python3 cxf_demo.py examples/missing-chunk/manifest.json --expect examples/missing-chunk/expected-report.json --strict
```
