import unittest

from helpers import valid_payload

from bbi_ai_readiness.scoring import score_assessment


class ScoringTests(unittest.TestCase):
    def test_high_scores_are_ready(self):
        result = score_assessment(valid_payload(5))
        self.assertEqual(result.overall_score, 100.0)
        self.assertEqual(result.readiness_band, "READY")

    def test_critical_floor_prevents_ready(self):
        payload = valid_payload(5)
        payload["dimensions"]["human_oversight"]["score"] = 1
        result = score_assessment(payload)
        self.assertNotEqual(result.readiness_band, "READY")
        self.assertTrue(any("prevents READY" in item for item in result.warnings))

    def test_no_evidence_forces_not_ready(self):
        payload = valid_payload(5)
        for entry in payload["dimensions"].values():
            entry["evidence"] = []
        result = score_assessment(payload)
        self.assertEqual(result.readiness_band, "NOT READY")

    def test_missing_dimension_fails(self):
        payload = valid_payload()
        del payload["dimensions"]["data_readiness"]
        with self.assertRaises(ValueError):
            score_assessment(payload)

    def test_invalid_score_fails(self):
        payload = valid_payload()
        payload["dimensions"]["business_value"]["score"] = 6
        with self.assertRaises(ValueError):
            score_assessment(payload)


if __name__ == "__main__":
    unittest.main()
