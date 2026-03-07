# Signed Valid Verifier Report

## Purpose

This example describes the expected verifier-report semantics for a realistic signed evidentiary CXF container.

It is intended to represent the normal, exchange-ready verification case for CXF 1.0 and should be treated as the primary example for common evidence workflows.

## Reference object

This report corresponds to:

- `examples/sample-containers/signed-valid-container.md`

## Expected verification characteristics

This report assumes:

- a valid CXF 1.0 container layout
- a deterministic manifest encoded as canonical CBOR
- correct SHA3-256 verification behavior
- a valid final root
- no bridge profile usage
- no recovery evidence required
- suitability for later receipt generation
- suitability for inter-laboratory exchange

## Expected report semantics

A verifier output for this case should indicate that:

- the container structure is valid
- the manifest is authoritative and internally consistent
- the final root has been validated
- the content is verified without reconstruction
- no bridge-related transition profile was used
- no discovery mismatch or integrity failure is present
- the report itself is represented as a standardized signed verifier artifact

## Typical result profile

A typical summary for this case would express:

- **structural state:** valid
- **verification state:** verified
- **content state:** verified and readable

Typical verification events would include:

- manifest accepted
- chunk verification completed successfully
- final root confirmed
- no recovery-related events
- no governance anomaly events
- no sidecar divergence events

## Why this example matters

This is the most practically important report example because it serves as the likely baseline for:

- production verifier implementations
- sample basic receipts
- interoperability reports
- review and audit workflows
- evidence exchange scenarios

## Interpretation note

This example should be used as the default human-readable reference for what a normal successful CXF 1.0 verifier report looks like conceptually.