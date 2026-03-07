# Signed-Valid Discovery Sidecar

## Purpose

This example describes a realistic discovery-style sidecar corresponding to a standard signed-valid CXF container.

It is intended to demonstrate how a richer projection artifact may support indexing, triage, and workflow integration while still remaining strictly outside the root of trust.

## Reference object

This sidecar corresponds to:

- `examples/sample-containers/signed-valid-container.md`

## Expected sidecar characteristics

This example assumes:

- a valid CXF container with a deterministic authoritative manifest
- a sidecar that is derived from that container
- no independent evidentiary authority
- no replacement of verifier outputs or receipts
- no override of manifest semantics
- support for indexing and operational tooling

## Expected sidecar semantics

A sidecar in this case may carry:

- core deterministic projection fields
- profile identifiers useful for workflow routing
- values suitable for quick inspection or cataloging
- a defined integrity binding for the sidecar content itself, where the sidecar model provides one

It may be helpful for:

- repository indexing
- case-management integration
- preview-oriented workflows
- operational filtering and search

It must not be treated as:

- a substitute for verifier output
- a substitute for receipts
- a policy carrier
- a source of evidentiary truth independent of the container

## Typical interpretation

This example should be understood as:

- an operational projection
- a sidecar suitable for system integration
- a workflow aid
- a non-authoritative derivative of container truth

If its values diverge from the container, the sidecar is wrong, not the container.

## Why this example matters

This is the most practical sidecar example because it models the likely operational use case for discovery-style projections in real forensic environments, while preserving the strict CXF trust boundary.

## Interpretation note

This example is intentionally useful but constrained. It should help implementers understand that sidecars may be rich enough to be operationally valuable while still never becoming part of the root of trust.