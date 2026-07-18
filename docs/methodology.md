# Methodology

The diagnostic evaluates whether a specific AI use case has enough business clarity, data, oversight, governance, delivery capacity, and evidence to justify the next investment.

## Scoring

Each dimension receives a score from 0 to 5:

- 0 — Unknown or absent
- 1 — Materially inadequate
- 2 — Partially defined, with major gaps
- 3 — Adequate for bounded discovery or prototype work
- 4 — Strong, with manageable gaps
- 5 — Verified and implementation-ready within stated boundaries

Scores are normalized to 100 and combined using explicit weights.

## Critical-floor rule

Business value, data readiness, human oversight, risk/governance, and evidence quality are critical. A critical dimension below 2 prevents a `READY` result regardless of the weighted total.

## Evidence discipline

A score without supporting evidence is weak. The tool reports missing-evidence warnings and forces `NOT READY` when no dimension includes evidence.

The method intentionally separates:

- source fact,
- observed condition,
- assumption,
- recommendation,
- missing evidence.
