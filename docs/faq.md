# FAQ

## Is CXF a replacement for existing forensic container formats?

CXF is intended as a modern, deterministic, cryptographically verifiable evidence container format for long-term interoperability and validation.

## Is discovery metadata authoritative?

No. Discovery artifacts are never equal to the root of trust.

## Are receipts stored inside the immutable container core?

No. Receipts are external append-only evidence artifacts.

## Does CXF allow silent fallbacks?

No. Unknown critical structures and malformed mandatory semantics must be rejected.
