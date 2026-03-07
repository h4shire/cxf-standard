# Signed Valid Basic Receipt

## Purpose

This example describes a realistic basic receipt corresponding to a normal signed evidentiary CXF container under CXF 1.0.

It is intended to represent the standard receipt case that most implementations should support as part of ordinary exchange, verification, and audit workflows.

## Reference objects

This receipt corresponds to:

- `examples/sample-containers/signed-valid-container.md`
- `examples/sample-reports/signed-valid-report.md`

## Expected receipt characteristics

This example assumes:

- a valid CXF 1.0 container
- a deterministic authoritative manifest
- a valid SHA3-256-based verification path
- a valid final root
- a successful standardized verifier output
- no bridge profile usage
- no recovery-specific reconstruction evidence
- suitability for inter-laboratory exchange and audit

## Expected receipt semantics

A basic receipt for this case should bind to:

- the authoritative manifest hash
- the final root of the verified container
- the relevant receipt issuer identity
- the signing context for the receipt
- any predecessor receipt if the receipt is not the first in the chain

The receipt should function as a signed evidence-layer object that confirms the verified state of the referenced container at the time of issuance.

## Typical interpretation

This example should be understood as:

- a standard evidentiary receipt
- a signed extension of the verification chain
- a compact artifact suitable for later review and exchange
- a stable reference point for receipt verification across tools

It should not be interpreted as changing the authority of the original container. The manifest and signed core structures remain the root of trust.

## Why this example matters

This is the most practically important receipt example because it provides the likely baseline for:

- common receipt generation implementations
- sample receipt verification logic
- audit demonstrations
- interoperability exercises
- documentation of normal evidentiary workflows

## Interpretation note

This example should be treated as the default conceptual model for a successful CXF 1.0 basic receipt in a normal verification scenario.