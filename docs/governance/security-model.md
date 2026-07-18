# Security Model

This document describes security controls implemented for the BBI AI Readiness Diagnostic Kit.

## Threat boundary

This repository is a public, dependency-light Python toolkit. It does not connect to private BBIOS systems, does not call external AI services, and must not contain secrets, client data, or private operating records.

## Implemented controls

- GitHub secret scanning: enabled
- Secret scanning push protection: enabled
- Dependabot version updates for GitHub Actions: configured via `.github/dependabot.yml`
- Dependabot security updates: enabled for the repository when available on the current plan
- CodeQL analysis workflow: enabled for Python
- OpenSSF Scorecard workflow: enabled for repository health signals
- Minimum workflow permissions: CI defaults to `contents: read`
- CODEOWNERS for security-sensitive paths
- Public issue guidance requiring removal of secrets and private data before filing

## Development quality gates (implemented)

- Ruff linting and formatting checks
- Static typing with mypy
- Pytest execution of the test suite with coverage reporting
- CLI integration exercise against the fictional sample assessment
- Documentation presence checks for required governance and proof files

## Planned controls (not yet enforced)

- Mandatory signed commits
- Mandatory signed release tags
- Package attestations / provenance for published artifacts
- Independent security reviewer approval on every pull request

## Reporting

See [`SECURITY.md`](../../SECURITY.md) for vulnerability reporting expectations.
