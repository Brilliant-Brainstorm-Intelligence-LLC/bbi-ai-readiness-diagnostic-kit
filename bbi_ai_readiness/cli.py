from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .reporting import render_markdown
from .scoring import score_assessment


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Score an evidence-first AI readiness assessment."
    )
    parser.add_argument("assessment", type=Path, help="Path to an assessment JSON file")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        payload = json.loads(args.assessment.read_text(encoding="utf-8"))
        result = score_assessment(payload)
        title = payload.get("assessment_title", "AI Readiness Diagnostic")
        report = render_markdown(result, str(title))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.output:
        args.output.write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(f"Overall score: {result.overall_score:.1f} / 100")
        print(f"Readiness band: {result.readiness_band}")
        print(f"Recommendation: {result.recommendation}")
        if result.warnings:
            print("Warnings:")
            for warning in result.warnings:
                print(f"- {warning}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
