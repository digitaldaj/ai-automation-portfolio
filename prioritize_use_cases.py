"""Prioritize automation use cases using a simple weighted scoring model."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "outputs"

WEIGHTS = {
    "volume_impact": 0.25,
    "manual_effort": 0.20,
    "compliance_risk": 0.20,
    "data_readiness": 0.20,
    "stakeholder_alignment": 0.15,
    "implementation_complexity": -0.15,
}


def read_csv(path: Path) -> List[dict]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(path: Path, rows: Iterable[dict], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def score_use_case(row: dict) -> float:
    score = 0.0
    for field, weight in WEIGHTS.items():
        score += int(row[field]) * weight
    return round(score, 2)


def recommendation(score: float) -> str:
    if score >= 3.5:
        return "Prioritize for discovery"
    if score >= 2.5:
        return "Hold for refinement"
    return "Do not prioritize now"


def prioritize(rows: List[dict]) -> List[dict]:
    output = []
    for row in rows:
        score = score_use_case(row)
        item = dict(row)
        item["priority_score"] = score
        item["recommendation"] = recommendation(score)
        output.append(item)
    return sorted(output, key=lambda item: item["priority_score"], reverse=True)


def main() -> None:
    rows = read_csv(DATA_DIR / "sample_use_cases.csv")
    prioritized = prioritize(rows)
    output_path = OUTPUT_DIR / "prioritized_use_cases.csv"
    fieldnames = list(prioritized[0].keys())
    write_csv(output_path, prioritized, fieldnames)

    print(f"Use cases scored: {len(prioritized)}")
    print("Top recommendation:", prioritized[0]["title"])
    print(f"Output written to: {output_path}")


if __name__ == "__main__":
    main()
