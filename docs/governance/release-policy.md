# Release Policy

This document describes release controls implemented for the BBI AI Readiness Diagnostic Kit.

## Versioning (implemented)

- Releases use semantic version tags (`vMAJOR.MINOR.PATCH`).
- Release notes are stored under `docs/releases/`.
- `CHANGELOG.md` records user-visible changes.

## Release gate (implemented)

Before publishing a release:

1. `main` is green on CI for supported Python versions.
2. Local unit tests and CLI sample assessment succeed.
3. Public Proof Gate items relevant to the release are reviewed.
4. License remains Apache-2.0.
5. No private BBIOS, Nova, client, employer, or personal-financial material is present.

## Signing plan (planned, not yet enforced)

The following are planned controls and are **not** currently enforced as merge or release blockers:

- signed commits for release preparation commits,
- signed release tags,
- artifact attestations for published packages.

Until signing infrastructure and key custody are established, releases remain unsigned and this limitation is stated honestly.

## Package publishing (planned)

PyPI publishing and provenance attestations are roadmap items, not implemented controls in v0.1.x.
