import unittest

from helpers import valid_payload

from bbi_ai_readiness.reporting import render_markdown
from bbi_ai_readiness.scoring import score_assessment


class ReportingTests(unittest.TestCase):
    def test_render_markdown_includes_core_fields(self):
        result = score_assessment(valid_payload(4))
        report = render_markdown(result, "Sample Assessment")
        self.assertIn("# Sample Assessment", report)
        self.assertIn("Overall score", report)
        self.assertIn("Readiness band", report)
        self.assertIn("Business value", report)
        self.assertIn("Limitations", report)

    def test_render_markdown_lists_warnings_when_present(self):
        payload = valid_payload(5)
        payload["dimensions"]["human_oversight"]["score"] = 1
        result = score_assessment(payload)
        report = render_markdown(result, "Warned Assessment")
        self.assertIn("## Warnings", report)
        self.assertTrue(any("prevents READY" in line for line in report.splitlines()))
