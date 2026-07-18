import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from helpers import valid_payload

from bbi_ai_readiness.cli import main


class CliTests(unittest.TestCase):
    def test_cli_prints_console_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            assessment = Path(tmp) / "assessment.json"
            assessment.write_text(json.dumps(valid_payload(4)), encoding="utf-8")
            stdout = io.StringIO()
            with mock.patch("sys.argv", ["bbi-ai-readiness", str(assessment)]):
                with mock.patch("sys.stdout", stdout):
                    code = main()
            self.assertEqual(code, 0)
            printed = stdout.getvalue()
            self.assertIn("Overall score", printed)
            self.assertIn("Readiness band", printed)

    def test_cli_writes_markdown_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            assessment = Path(tmp) / "assessment.json"
            output = Path(tmp) / "report.md"
            payload = {"assessment_title": "CLI Sample", **valid_payload(4)}
            assessment.write_text(json.dumps(payload), encoding="utf-8")
            with mock.patch(
                "sys.argv",
                ["bbi-ai-readiness", str(assessment), "--output", str(output)],
            ):
                code = main()
            self.assertEqual(code, 0)
            self.assertTrue(output.exists())
            content = output.read_text(encoding="utf-8")
            self.assertIn("# CLI Sample", content)
            self.assertIn("Overall score", content)

    def test_cli_returns_error_for_invalid_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            assessment = Path(tmp) / "bad.json"
            assessment.write_text("{not-json", encoding="utf-8")
            with mock.patch("sys.argv", ["bbi-ai-readiness", str(assessment)]):
                with mock.patch("sys.stderr", io.StringIO()):
                    code = main()
            self.assertEqual(code, 1)
