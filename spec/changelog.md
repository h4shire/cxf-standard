# CXF Changelog

## Version 1.0

Initial public 1.0 release of the Canonical eXchange Format for Digital Evidence.

### Core highlights

- Deterministic CBOR manifest as the sole authoritative metadata source
- Linear TLV-based container structure with strict reject behavior
- SHA3-256 as the normative verification digest
- Signed verifier output for standardized evidence reporting
- Basic receipt path for append-only evidence continuity
- Strict separation between immutable core content and external evidence artifacts

### Governance highlights

- Registry-driven digest lifecycle model
- Signed governance artifacts for digest sunset decisions and bridge profile audits
- Interoperability-first release model with coverage expectations

### Out of scope for 1.0

- Discovery sidecar standardization
- Advanced conformance claims
- Extended recovery evidence profiles beyond the initial LTR-4 path
- Additional candidate performance digest suites
