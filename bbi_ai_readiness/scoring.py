from __future__ import annotations

from dataclasses import dataclass
from typing import Any

DIMENSIONS: dict[str, dict[str, Any]] = {
    "business_value": {"weight": 0.20, "critical": True, "label": "Business value"},
    "data_readiness": {"weight": 0.20, "critical": True, "label": "Data readiness"},
    "human_oversight": {"weight": 0.15, "critical": True, "label": "Human oversight"},
    "risk_governance": {"weight": 0.15, "critical": True, "label": "Risk and governance"},
    "delivery_readiness": {"weight": 0.15, "critical": False, "label": "Delivery readiness"},
    "evidence_quality": {"weight": 0.15, "critical": True, "label": "Evidence quality"},
}


@dataclass(frozen=True)
class DiagnosticResult:
    overall_score: float
    readiness_band: str
    recommendation: str
    dimension_results: list[dict[str, Any]]
    warnings: list[str]


def _validate_score(value: Any, dimension: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{dimension}.score must be an integer from 0 to 5")
    if value < 0 or value > 5:
        raise ValueError(f"{dimension}.score must be between 0 and 5")
    return value


def _base_band(score: float) -> str:
    if score >= 85:
        return "READY"
    if score >= 70:
        return "CONDITIONAL"
    if score >= 50:
        return "DISCOVERY"
    return "NOT READY"


def _recommendation(band: str) -> str:
    return {
        "READY": (
            "Prepare a bounded implementation plan with named owners, controls, "
            "success measures, and verification."
        ),
        "CONDITIONAL": ("Proceed only after named gaps are resolved or explicitly constrained."),
        "DISCOVERY": ("Limit work to discovery, evidence collection, or prototype validation."),
        "NOT READY": (
            "Do not begin implementation. Resolve foundational business, data, "
            "oversight, governance, or evidence gaps first."
        ),
    }[band]


def score_assessment(payload: dict[str, Any]) -> DiagnosticResult:
    assessment = payload.get("dimensions")
    if not isinstance(assessment, dict):
        raise ValueError("The assessment must contain a 'dimensions' object")

    dimension_results: list[dict[str, Any]] = []
    warnings: list[str] = []
    weighted_total = 0.0
    critical_floor_triggered = False

    for key, config in DIMENSIONS.items():
        entry = assessment.get(key)
        if not isinstance(entry, dict):
            raise ValueError(f"Missing dimension: {key}")

        score = _validate_score(entry.get("score"), key)
        evidence = entry.get("evidence", [])
        notes = entry.get("notes", "")

        if not isinstance(evidence, list) or not all(
            isinstance(item, str) and item.strip() for item in evidence
        ):
            raise ValueError(f"{key}.evidence must be a list of non-empty strings")

        normalized = score * 20.0
        contribution = normalized * float(config["weight"])
        weighted_total += contribution

        if len(evidence) == 0:
            warnings.append(f"{config['label']}: no evidence supplied")

        if bool(config["critical"]) and score < 2:
            critical_floor_triggered = True
            warnings.append(f"{config['label']}: critical score below 2 prevents READY status")

        dimension_results.append(
            {
                "key": key,
                "label": config["label"],
                "score": score,
                "normalized_score": normalized,
                "weight": config["weight"],
                "weighted_contribution": contribution,
                "critical": config["critical"],
                "evidence_count": len(evidence),
                "evidence": evidence,
                "notes": notes if isinstance(notes, str) else str(notes),
            }
        )

    overall = round(weighted_total, 1)
    band = _base_band(overall)

    if critical_floor_triggered and band == "READY":
        band = "CONDITIONAL"

    if sum(item["evidence_count"] for item in dimension_results) == 0:
        band = "NOT READY"
        warnings.append("No supporting evidence was supplied for any dimension")

    return DiagnosticResult(
        overall_score=overall,
        readiness_band=band,
        recommendation=_recommendation(band),
        dimension_results=dimension_results,
        warnings=warnings,
    )
