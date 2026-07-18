def valid_payload(score: int = 4):
    return {
        "dimensions": {
            "business_value": {"score": score, "evidence": ["evidence"]},
            "data_readiness": {"score": score, "evidence": ["evidence"]},
            "human_oversight": {"score": score, "evidence": ["evidence"]},
            "risk_governance": {"score": score, "evidence": ["evidence"]},
            "delivery_readiness": {"score": score, "evidence": ["evidence"]},
            "evidence_quality": {"score": score, "evidence": ["evidence"]},
        }
    }
