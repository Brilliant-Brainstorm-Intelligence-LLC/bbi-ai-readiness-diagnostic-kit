# BBI AI Readiness Diagnostic Kit

[![CI](https://github.com/Brilliant-Brainstorm-Intelligence-LLC/bbi-ai-readiness-diagnostic-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/Brilliant-Brainstorm-Intelligence-LLC/bbi-ai-readiness-diagnostic-kit/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Brilliant-Brainstorm-Intelligence-LLC/bbi-ai-readiness-diagnostic-kit)](https://github.com/Brilliant-Brainstorm-Intelligence-LLC/bbi-ai-readiness-diagnostic-kit/releases)

An evidence-first starter toolkit for evaluating whether an organization is ready to pursue a specific AI use case.

It assesses six practical dimensions:

1. Business value
2. Data readiness
3. Human oversight
4. Risk and governance
5. Delivery readiness
6. Evidence quality

The toolkit produces a transparent score, dimension-level findings, missing-evidence warnings, and a bounded recommendation.

## Why this exists

Organizations often start with a model or vendor before they have clarified:

- the business decision the system should improve,
- the data required,
- the responsible human owner,
- the consequences of failure,
- the evidence needed to justify implementation.

This kit puts those questions first.

## Quick start

Requirements:

- Python 3.11 or newer
- No third-party runtime dependencies

Run the included example:

```bash
python -m bbi_ai_readiness.cli examples/sample-assessment.json
```

Write a Markdown report:

```bash
python -m bbi_ai_readiness.cli   examples/sample-assessment.json   --output readiness-report.md
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Example output

```text
Overall score: 69.2 / 100
Readiness band: CONDITIONAL
Recommendation: Proceed only with a bounded discovery or prototype phase.
```

Scores are decision aids, not certifications, guarantees, or substitutes for legal, security, financial, privacy, accessibility, or domain review.

## Assessment format

Each dimension contains:

- `score`: integer from 0 to 5
- `evidence`: list of concrete evidence items
- `notes`: optional context

See [`examples/sample-assessment.json`](examples/sample-assessment.json).

## Readiness bands

| Score | Band | Interpretation |
|---:|---|---|
| 85–100 | READY | Ready for a bounded implementation plan, subject to identified controls |
| 70–84.9 | CONDITIONAL | Proceed only after named gaps are resolved or constrained |
| 50–69.9 | DISCOVERY | Limit work to discovery, evidence collection, or prototype validation |
| 0–49.9 | NOT READY | Do not begin implementation |

A critical dimension scoring below 2 automatically prevents a `READY` result.

## Public Proof Gate

This repository is not release-ready until it has:

- A clear user and problem
- A five-minute quick start
- A working sample
- Passing automated tests
- A versioned release
- Security, contribution, support, and license decisions
- Claims and limitations review
- A public-safe data review

See [`PUBLIC_PROOF_GATE.md`](PUBLIC_PROOF_GATE.md).

## Roadmap

### v0.1

- [x] Transparent scoring engine
- [x] JSON input
- [x] Markdown report
- [x] Example assessment
- [x] Unit tests
- [x] GitHub Actions CI
- [x] License decision (Apache-2.0)
- [x] First tagged release
- [x] Social preview image

### v0.2

- [ ] Interactive questionnaire
- [ ] Evidence traceability IDs
- [ ] Configurable dimension weights
- [ ] Comparison between two assessment versions

## Governance boundary

This is a public educational and diagnostic aid.

It does not:

- certify regulatory or legal compliance,
- guarantee project success,
- replace professional review,
- connect to private BBIOS data,
- make automated approval decisions,
- claim that a score is live operational telemetry.

## License

The software in this repository is licensed under the Apache License 2.0. See [`LICENSE`](LICENSE).

## Maintainer

Dr. Tatianna Gilliam — Brilliant Brainstorm Intelligence
