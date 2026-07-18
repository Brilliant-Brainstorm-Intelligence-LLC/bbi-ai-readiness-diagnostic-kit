# Merge Policy

This document describes merge controls implemented for the BBI AI Readiness Diagnostic Kit.

## Branch protection (implemented)

The `main` branch is protected by a repository ruleset that:

- requires pull-request changes (no direct pushes to `main`),
- requires conversation resolution before merge,
- blocks force pushes,
- blocks branch deletion of the protected branch,
- requires the CI checks that exist in this repository to pass before merge.

## Review requirements (implemented for sole-maintainer phase)

While Dr. Tatianna Gilliam is the sole maintainer:

- an independent second-reviewer requirement is not enforced,
- CODEOWNERS identifies ownership for future team review,
- the maintainer remains accountable for Public Proof Gate review before merge.

When additional maintainers join the `maintainers` or `public-proof-reviewers` teams, review requirements should be raised without weakening CI gates.

## Required checks (implemented)

Merges to `main` require successful completion of the checks defined in `.github/workflows/ci.yml`, including quality gates and the Python version matrix.

## Out of scope for this phase

- Required independent human approval by a second person (deferred until staffing exists)
- Deployer environments and environment protection rules
