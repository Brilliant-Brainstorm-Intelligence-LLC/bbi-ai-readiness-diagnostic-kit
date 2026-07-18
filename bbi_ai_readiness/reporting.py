from __future__ import annotations

from .scoring import DiagnosticResult


def render_markdown(result: DiagnosticResult, title: str) -> str:
    lines = [
        f"# {title}",
        "",
        f"**Overall score:** {result.overall_score:.1f} / 100",
        "",
        f"**Readiness band:** `{result.readiness_band}`",
        "",
        f"**Recommendation:** {result.recommendation}",
        "",
        "## Dimension results",
        "",
        "| Dimension | Score | Weight | Evidence |",
        "|---|---:|---:|---:|",
    ]

    for item in result.dimension_results:
        lines.append(
            f"| {item['label']} | {item['normalized_score']:.0f}/100 "
            f"| {item['weight']:.0%} | {item['evidence_count']} |"
        )

    lines.extend(["", "## Warnings", ""])
    if result.warnings:
        lines.extend(f"- {warning}" for warning in result.warnings)
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Evidence and notes",
            "",
        ]
    )

    for item in result.dimension_results:
        lines.extend([f"### {item['label']}", ""])
        if item["evidence"]:
            lines.extend(f"- {evidence}" for evidence in item["evidence"])
        else:
            lines.append("- No evidence supplied")
        if item["notes"]:
            lines.extend(["", f"**Notes:** {item['notes']}"])
        lines.append("")

    lines.extend(
        [
            "## Limitations",
            "",
            "This report is a decision aid. It is not a certification, guarantee, "
            "compliance determination, or substitute for professional review.",
            "",
        ]
    )

    return "\n".join(lines)
