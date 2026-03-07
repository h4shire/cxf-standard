# Recovery Reference Receipt

## Purpose

This example describes a receipt-oriented reference case for a recovery-aware CXF scenario.

Its role is to show how receipt logic may relate to a container and a recovery-informed verification context without moving reconstruction semantics into the core container or collapsing recovery evidence into the receipt itself.

## Reference objects

This receipt corresponds to:

- `examples/sample-containers/recovery-reference-container.md`
- `examples/sample-reports/recovery-reference-report.md`

## Expected receipt characteristics

This example assumes:

- a valid CXF 1.0 container
- an authoritative deterministic manifest
- a stable final root for the original container
- a verification context that includes recovery-related interpretation
- recovery evidence stored externally to the core container
- no rewriting of the original root-of-trust model

## Expected receipt semantics

A receipt in this scenario should still bind to:

- the authoritative manifest hash
- the final root of the original container
- the signing context of the receipt
- the identity of the receipt issuer
- the appropriate predecessor relation if part of a receipt chain

Where recovery evidence is relevant, the receipt may refer to that broader verification context, but it should not absorb or replace the recovery evidence artifact itself.

## Typical interpretation

This example should be understood as:

- a receipt that remains anchored to the original container identity
- a signed artifact that may coexist with recovery-oriented evidence
- a layered evidence object that preserves separation of concerns
- a bridge between verified container state and later recovery-aware review

It should not be interpreted as a recovery artifact in itself. Recovery evidence remains a separate evidentiary layer.

## Why this example matters

This example is important because it demonstrates one of the key CXF design principles:

- receipts remain compact evidence-chain objects
- recovery evidence remains external
- the original container remains authoritative
- complex post-verification evidence can be layered without distorting the core container meaning

## Interpretation note

This example should be used as a conceptual basis for later long-term and recovery-oriented examples, including future LTR and recovery-evidence relationships beyond the basic receipt path.