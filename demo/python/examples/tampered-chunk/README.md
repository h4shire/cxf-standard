# Tampered Chunk Example

## Purpose

This example represents the first negative verification case for the Python CXF demo verifier.

It demonstrates a container whose overall structure remains valid, but where one chunk on disk no longer matches the digest recorded in the manifest. The example is intended to show how the verifier should distinguish between structural validity and verification failure.

## Expected behavior

A verifier run against this example should produce a result in which:

- the container layout remains structurally valid
- one chunk is reported as mismatched
- the calculated final root no longer matches the expected final root
- the overall verification state is failed
- the content state is no longer fully verified

## Why this example matters

This is the first negative-path example in the demo set. It shows that CXF verification is not limited to happy-path success cases and that a verifier must report digest mismatches explicitly and deterministically.

## Reference semantics

This example is designed to model a simple tampering scenario:

- the manifest remains unchanged
- one chunk file is modified after the manifest was created
- the verifier detects the mismatch without treating the container as structurally malformed

## Files in this example

- `manifest.json` contains the expected chunk digests and expected final root
- `chunks/chunk-0000.bin` still matches the manifest
- `chunks/chunk-0001.bin` has been intentionally altered
- `expected-report.json` describes the expected high-level verifier outcome
