# Recovery Reference Sidecar

## Purpose

This example describes a discovery-style sidecar corresponding to a recovery-aware CXF reference container.

Its role is to illustrate how a sidecar may support workflow visibility in a recovery-related context without becoming a recovery artifact, a verifier report, or a receipt.

## Reference object

This sidecar corresponds to:

- `examples/sample-containers/recovery-reference-container.md`

## Expected sidecar characteristics

This example assumes:

- a valid CXF container with recovery-relevant context
- a non-authoritative projection role
- no direct evidentiary replacement of recovery evidence
- no rewriting of the original manifest or final root
- no absorption of verifier or receipt semantics into the sidecar

## Expected sidecar semantics

A sidecar in this case may help with:

- workflow discovery
- indexing of recovery-related processing context
- preview-level operational categorization
- tool routing or queueing logic

It may contain derived values that indicate that the referenced container is associated with recovery-aware workflows, but it must not serve as the evidence artifact proving recovery or reconstruction correctness.

That role belongs to separate evidence and report layers.

## Typical interpretation

This example should be understood as:

- a support artifact for workflow awareness
- a projection that may mention recovery-related context
- a non-authoritative operational companion
- a convenience layer that remains below the trust boundary

It must not be interpreted as:

- proof of reconstruction success
- a replacement for recovery evidence
- a replacement for verifier output
- a substitute for receipts or long-term evidence artifacts

## Why this example matters

This example is important because recovery-related workflows are exactly where convenience metadata can be mistakenly elevated into evidentiary truth. CXF’s design avoids that by keeping recovery evidence and discovery projections clearly separate.

## Interpretation note

This example should be used to reinforce a core CXF design principle: useful workflow metadata may exist outside the container, but evidence authority remains anchored in the container and the proper signed evidence artifacts.