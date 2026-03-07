# Minimal Basic Receipt

## Purpose

This example describes the simplest useful receipt relationship for a valid CXF 1.0 container.

It is intended to show how a basic receipt may bind to a container in a minimal, non-complex scenario without introducing bridge usage, long-term receipt chains, or recovery-oriented evidence.

## Reference objects

This receipt corresponds to:

- `examples/sample-containers/minimal-valid-container.md`
- `examples/sample-reports/minimal-valid-report.md`

## Expected receipt characteristics

This example assumes:

- a valid CXF 1.0 container
- a deterministic manifest
- a valid final root
- a successful verification result
- no bridge profile usage
- no recovery evidence
- no extended long-term receipt chain

## Expected receipt semantics

A basic receipt for this case should bind to:

- the authoritative manifest hash
- the validated final root
- the relevant verification context
- the identity of the receipt issuer or signing context
- the predecessor receipt relation only if a chain exists

In the minimal case, the receipt should serve as a compact signed acknowledgment that the referenced container state was verified and recorded.

## Typical interpretation

This example should be understood as:

- a first-layer receipt
- a compact evidence extension
- a signed binding to the verified container state
- a non-destructive addition to the overall evidence chain

It should not be interpreted as a replacement for the container, the manifest, or the verifier report.

## Why this example matters

This is the simplest receipt example in the repository and establishes the baseline for:

- receipt generation logic
- receipt verification logic
- positive interoperability testing
- explanation of the difference between a container and a receipt

## Interpretation note

This example is intentionally minimal. It demonstrates the role of a receipt under ideal conditions and should be used as the first reference point before considering more complex receipt chains or recovery-related scenarios.