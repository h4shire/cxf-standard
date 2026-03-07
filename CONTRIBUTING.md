# Contributing to CXF

Thank you for contributing to CXF.

CXF is a standards-oriented project. The highest-value contributions are those that improve clarity, interoperability, reject behavior, evidence semantics, and long-term verifiability.

## Before you contribute

Please read:

- `README.md`
- `spec/cxf-1.0.md`
- relevant files under `cddl/`
- relevant registry and governance documents

## Core design rule

Before proposing a change, align it with this rule:

**Keep the root of trust small. Keep extension paths explicit. Avoid second truths.**

## Good contribution areas

Examples of especially useful contributions:

- parser and verifier implementations
- CDDL corrections
- positive and negative test vectors
- malformed corpus additions
- interoperability reports
- registry proposals
- reason-code review
- governance artifact review
- editorial clarifications
- fuzzing and reject-path coverage
- security analysis

## Contribution workflow

1. Open an issue describing the problem or proposal.
2. Reference the affected specification section, schema, registry entry, or test artifact.
3. Provide concrete examples, failing cases, or proposed text where possible.
4. Prefer small, reviewable changes over broad conceptual rewrites.
5. Open a pull request linked to the issue.

## Pull request expectations

A good pull request should:

- explain the problem being solved
- describe the affected artifacts
- include tests or corpus changes where relevant
- avoid unrelated formatting churn
- preserve deterministic and machine-verifiable behavior

## Normative changes

If your change affects normative behavior, also include, where relevant:

- updated CDDL
- updated registry artifacts
- positive and negative tests
- updated interop expectations
- changelog entry or editorial note

## Non-normative contributions

Non-normative improvements are also welcome, including:

- documentation improvements
- examples
- implementation notes
- onboarding material
- FAQ clarifications

## Reviews

Reviews will prioritize:

- technical correctness
- interoperability impact
- reject-path clarity
- long-term stability
- consistency with existing governance and evidence rules

## Conduct

By participating in this project, you agree to follow `CODE_OF_CONDUCT.md`.