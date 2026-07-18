# Architecture

```text
Assessment JSON
      |
      v
Schema and score validation
      |
      v
Weighted dimension scoring
      |
      +--> Critical-floor checks
      |
      +--> Evidence warnings
      |
      v
Readiness band and recommendation
      |
      v
Console summary or Markdown report
```

The v0.1 implementation uses only the Python standard library at runtime.

## Boundaries

- No model calls
- No private connectors
- No automated approval
- No live compliance determination
- No hidden reasoning capture
- No persistence of assessment data
