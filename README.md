# CXF — Canonical eXchange Format for Digital Evidence

[![Specification](https://img.shields.io/badge/specification-1.0-blue.svg)](#specification-status)
[![Schemas](https://img.shields.io/badge/CDDL-normative-green.svg)](#repository-layout)
[![Interop](https://img.shields.io/badge/interop-required-orange.svg)](#governance-and-interoperability)
[![Status](https://img.shields.io/badge/status-stable%20core-success.svg)](#current-status)
[![License](https://img.shields.io/badge/license-TBD-lightgrey.svg)](#license)

CXF is an open, deterministic, cryptographically verifiable container format for digital evidence.

It is designed for long-term forensic preservation, reproducible verification, and interoperable evidence exchange across tools, laboratories, archives, and jurisdictions. CXF combines a small, stable core with carefully separated extension paths for encryption, recovery, receipts, and governance.

---

## Table of contents

- [Why CXF exists](#why-cxf-exists)
- [Core principles](#core-principles)
- [What CXF includes](#what-cxf-includes)
- [What CXF does not do](#what-cxf-does-not-do)
- [Specification status](#specification-status)
- [Quick start](#quick-start)
- [Repository layout](#repository-layout)
- [Governance and interoperability](#governance-and-interoperability)
- [How to cite CXF](#how-to-cite-cxf)
- [Roadmap](#roadmap)
- [Who CXF is for](#who-cxf-is-for)
- [Contributing](#contributing)
- [Project philosophy](#project-philosophy)
- [Community and contact](#community-and-contact)
- [License](#license)

---

## Why CXF exists

Digital evidence containers are expected to outlive the software that created them.

That means a format must do more than store bytes. It must remain understandable, verifiable, and defensible many years later, including in court-facing, regulated, and adversarial environments.

CXF was created to address recurring problems in existing evidence workflows:

- ambiguous metadata semantics,
- silent parser divergence across implementations,
- unclear separation between convenience metadata and authoritative evidence data,
- weak long-term validation paths,
- poor machine-verifiable governance and interoperability testing.

CXF addresses these through deterministic serialization, strict reject behavior, explicit evidence semantics, and a design that keeps the root of trust small and stable.

---

## Core principles

### One source of truth

The authoritative evidence state is derived from the canonical manifest and signed core structures only.

Sidecars, discovery artifacts, mirrors, local catalog metadata, and convenience projections are never equal to the root of trust.

### Determinism over convenience

CXF uses deterministic CBOR for authoritative metadata and a linear TLV-based container structure. The format is intentionally strict about duplicate keys, reserved fields, canonical encodings, and reject behavior.

### Small core, extensible ecosystem

The 1.0 core is intentionally narrow. Useful but non-fundamental capabilities — such as discovery sidecars, advanced recovery evidence, or long-term preservation extensions — are kept outside the immutable container core.

### No silent fallbacks

Unknown critical structures, malformed canonical encodings, invalid reserved fields, and unsupported mandatory semantics must be rejected.

### Long-term verifiability

CXF separates immutable evidence content from append-only evidence artifacts such as receipts, attestations, audit trails, migration records, and recovery evidence.

---

## What CXF includes

CXF 1.0 is centered around:

- a linear TLV-based bitstream,
- a deterministic CBOR manifest,
- SHA3-256 as the normative verification digest,
- explicit structural, verification, and content state semantics,
- strict reject rules for malformed or unsafe inputs,
- external evidence artifacts for receipts, recovery, and governance,
- machine-readable registries, schemas, and interoperability materials.

### Cryptographic model

CXF treats cryptography as part of evidence semantics, not just transport.

- **SHA3-256** is the normative verification digest.
- **SHA-256** remains available only as a reporting/interoperability path under a controlled lifecycle model.
- **BLAKE3** may be considered only as a constrained future candidate path for performance-sensitive chunk/Merkle workflows, never as a replacement for the normative evidence path.
- Encryption uses explicit key separation and profile-based wrapping.
- Transitional bridge mechanisms are tightly constrained and governed.

### Evidence model

CXF distinguishes between:

- structural validity,
- verification outcome,
- content condition.

These are modeled separately so that tools can express states precisely and consistently across implementations.

### Long-term preservation model

CXF supports append-only evidence artifacts outside the immutable core, including:

- basic receipts,
- timestamp receipts,
- countersignature and attestation receipts,
- migration and preservation records,
- recovery evidence records,
- registry and governance audit artifacts.

---

## What CXF does not do

CXF is not:

- a general-purpose archive format,
- a vendor-specific wrapper,
- a convenience metadata dump,
- a substitute for legal or organizational trust policy,
- a “kitchen sink” format that forces every workflow into the immutable core.

It provides a technically rigorous substrate for evidence handling, preservation, validation, and exchange.

---

## Specification status

### Current status

**CXF 1.0 defines the stable core.**

The core is intentionally conservative:

- small enough to implement consistently,
- strong enough for long-term evidence integrity,
- strict enough to prevent silent divergence.

### Stability model

The project follows a “stable core, explicit extensions” philosophy:

- the root of trust stays narrow,
- optional profiles and evidence artifacts evolve outside the core,
- registry and interoperability artifacts carry much of the ecosystem evolution.

### Current status

- **Core specification:** Stable for 1.0
- **Manifest schema:** Normative
- **Basic receipt schema:** Normative
- **Verifier output:** Standardized evidence artifact
- **Discovery sidecar:** Outside the 1.0 core
- **Advanced recovery and long-term extensions:** Extension paths, separately governed

---

## Quick start

### Read the spec

Start here:

- `spec/cxf-1.0.md`
- `cddl/manifest.cddl`
- `cddl/basic-receipt.cddl`
- `cddl/verifier-output.cddl`

### Validate against the registry

Implementations should load the signed registry artifacts before enabling profile-specific behavior.

Planned location:

- `registry/registry-v1.cbor`

### Run the interoperability corpus

Before claiming support, implementations should pass the positive and negative corpus and compare output behavior against the published interoperability report.

Planned locations:

- `tests/positive/`
- `tests/negative/`
- `interop/interop-report-v1.md`

### Minimal implementation order

Recommended implementation order:

1. TLV parser
2. Deterministic manifest handling
3. Core verifier
4. Verifier-output generation
5. Basic receipt support
6. Optional encryption, recovery, and extended evidence artifacts

---

## Repository layout

A recommended repository layout for CXF looks like this:

```text
.
├── README.md
├── spec/
│   ├── cxf-1.0.md
│   ├── executive-summary.md
│   └── changelog.md
├── cddl/
│   ├── manifest.cddl
│   ├── basic-receipt.cddl
│   ├── verifier-output.cddl
│   ├── ltr/
│   └── extensions/
├── registry/
│   ├── registry-v1.cbor
│   ├── profiles/
│   ├── reason-codes/
│   ├── lifecycle/
│   └── governance/
├── tests/
│   ├── positive/
│   ├── negative/
│   ├── malformed/
│   └── corpus-index.json
├── examples/
│   ├── sample-containers/
│   ├── sample-receipts/
│   ├── sample-reports/
│   └── sample-sidecars/
├── interop/
│   ├── interop-report-v1.md
│   └── coverage-matrix/
├── governance/
│   ├── process.md
│   ├── review-model.md
│   ├── registry-policy.md
│   └── oversight/
└── docs/
    ├── getting-started.md
    ├── implementation-notes.md
    └── faq.md
```

---

## Governance and interoperability

CXF treats governance as machine-verifiable wherever possible.

This includes:

- signed registries,
- explicit profile states,
- lifecycle transitions,
- signed governance artifacts,
- public test corpora,
- interoperability reporting,
- coverage-based conformance evidence.

### Why this matters

A standard should not rely on vague process language alone. Critical lifecycle decisions should be represented through explicit artifacts that can be reviewed, archived, and verified.

### Interop principle

Independent implementations should converge on the same results for:

- valid inputs,
- malformed inputs,
- reject cases,
- verification outcomes,
- evidence state reporting.

### Interoperability minimums

The project expects public evidence of:

- independent parser and verifier behavior,
- reason-code consistency,
- reject-path consistency,
- coverage of normative positive and negative rules.

### Planned project links

Replace these placeholders once the public project is live:

- **Specification:** `https://github.com/<org>/cxf/tree/main/spec`
- **Registry:** `https://github.com/<org>/cxf/tree/main/registry`
- **Schemas:** `https://github.com/<org>/cxf/tree/main/cddl`
- **Test corpus:** `https://github.com/<org>/cxf/tree/main/tests`
- **Interop reports:** `https://github.com/<org>/cxf/tree/main/interop`
- **Issues:** `https://github.com/<org>/cxf/issues`
- **Discussions:** `https://github.com/<org>/cxf/discussions`

---

## How to cite CXF

Until a formal citation file is published, use a citation in this form:

```text
CXF Project. CXF 1.0 — Canonical eXchange Format for Digital Evidence.
Version 1.0. <Project Organization>, 2026.
Repository: https://github.com/<org>/cxf
```

Suggested BibTeX template:

```bibtex
@misc{cxf10,
  title        = {CXF 1.0: Canonical eXchange Format for Digital Evidence},
  author       = {{CXF Project}},
  year         = {2026},
  howpublished = {GitHub repository},
  note         = {Version 1.0}
}
```

---

## Roadmap

### Stable in 1.0

- deterministic manifest model,
- linear TLV core,
- normative verifier-output artifact,
- signed governance and registry direction,
- basic receipt path,
- strict reject semantics,
- interoperability-first release model.

### Expected post-1.0 work

- advanced long-term receipt profiles,
- extended recovery evidence profiles,
- discovery sidecar schema publication,
- richer conformance claims,
- additional governance tooling,
- expanded registry lifecycle automation,
- optional future candidate paths evaluated under strict interoperability and evidence constraints.

### Non-goals for 1.x

- broadening the root of trust,
- moving convenience metadata into the core,
- weakening reject behavior for compatibility,
- introducing alternate normative evidence digests without full governance and interoperability review.

---

## Who CXF is for

CXF is intended for:

- forensic laboratories,
- law enforcement and judicial workflows,
- public-sector archives,
- evidence platform vendors,
- independent tool developers,
- standards groups,
- open-source forensic communities,
- long-term preservation and audit environments.

---

## Contributing

Contributions are welcome, especially in these areas:

- parser and verifier implementations,
- CDDL review,
- positive and negative test vectors,
- malformed corpus contributions,
- interoperability reports,
- registry proposals,
- editorial clarifications,
- security analysis,
- reject-path and fuzzing coverage.

Before opening large proposals, align them with the core design rule:

**Keep the root of trust small. Keep extension paths explicit. Avoid second truths.**

### Suggested workflow

1. Open an issue describing the problem or proposal.
2. Reference the affected spec section, schema, registry entry, or test artifact.
3. Include concrete examples or draft text where possible.
4. Prefer small, reviewable changes over large conceptual rewrites.

### Contribution priorities

The highest-value contributions for a standards repository are usually:

- interoperable implementations,
- edge-case test vectors,
- reject-path validation,
- schema corrections,
- lifecycle and governance artifact review.

---

## Project philosophy

CXF is built on a simple premise:

> Digital evidence should still be verifiable, understandable, and defensible long after the original tools are gone.

That requires more than efficient storage. It requires semantic discipline, deterministic structure, explicit evidence handling, and testable interoperability.

CXF is designed to provide exactly that.

---

## Community and contact

A public project benefits from explicit, visible points of coordination.

Planned channels:

- GitHub Issues for defect reports and concrete proposals
- GitHub Discussions for design discussion and community questions
- Registry change process for profile, lifecycle, and reason-code evolution
- Interop publication workflow for implementation evidence

Suggested placeholders:

- **Mailing list:** `cxf-community@<domain>`
- **Security contact:** `security@<domain>`
- **Registry contact:** `registry@<domain>`
- **Interop coordination:** `interop@<domain>`

---

## License

**TBD**

Until a final license is selected, treat repository contents according to the project’s published contribution and governance rules.

---

## Closing note

CXF is not trying to be the biggest evidence format.
It is trying to be one of the clearest, strictest, and most durable.

That is the standard required for digital evidence that must remain trustworthy across tools, institutions, and decades.
