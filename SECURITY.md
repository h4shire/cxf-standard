# Security Policy

## Reporting a vulnerability

Please report suspected vulnerabilities or security-relevant ambiguities privately to:

- `security@cxf-standard.org`

Do **not** report undisclosed vulnerabilities through public GitHub issues or discussions.

## What to include

Please include, where possible:

- affected component, document, schema, registry entry, or artifact
- version or commit reference
- clear reproduction steps
- expected behavior
- actual behavior
- security impact assessment
- proof-of-concept material, if available
- any suggested mitigations

## Scope

Security-relevant reports may include, for example:

- cryptographic ambiguity
- verification bypass
- canonicalization ambiguity
- parser divergence with security impact
- registry or lifecycle manipulation risk
- signature validation weaknesses
- malformed input acceptance where rejection is required
- discovery, receipt, or verifier-output confusion that could create a second source of truth

## Disclosure process

The project will acknowledge receipt as soon as reasonably possible.

After triage, the project will aim to:

1. confirm whether the issue is in scope,
2. assess severity and affected artifacts,
3. coordinate remediation or clarifying changes,
4. prepare a public advisory or changelog entry when appropriate.

## Preferred handling

Please practice coordinated disclosure.

Do not publish exploit details before the project has had a reasonable opportunity to assess and address the issue.

## security.txt

A machine-readable disclosure file is published at:

`https://cxf-standard.org/.well-known/security.txt`