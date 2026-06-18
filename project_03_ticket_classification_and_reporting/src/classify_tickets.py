"""Classify synthetic operational tickets using deterministic precedence rules."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path
from typing import Iterable, List, Tuple

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "outputs"

RULES = [
    ("card_unlock", [r"\bunlock\b", r"card unlock"]),
    ("compliance_review", [r"compliance", r"high risk", r"exception"]),
    ("payment_or_billing", [r"payment", r"eft", r"biller", r"billing"]),
    ("cancellation_issue", [r"cancel", r"cancellation"]),
    ("callback_request", [r"callback", r"call back"]),
    ("system_access", [r"system access", r"cannot view", r"access issue"]),
]


def read_csv(path: Path) -> List[dict]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(path: Path, rows: Iterable[dict], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def classify_description(description: str) -> Tuple[str, str]:
    text = description.lower()
    for category, patterns in RULES:
        for pattern in patterns:
            if re.search(pattern, text):
                return category, f"Matched '{pattern}' using documented precedence"
    return "other", "No configured rule matched"


def classify_rows(rows: List[dict]) -> List[dict]:
    classified = []
    for row in rows:
        category, explanation = classify_description(row["description"])
        output = dict(row)
        output["category"] = category
        output["classification_explanation"] = explanation
        classified.append(output)
    return classified


def summarize(rows: List[dict]) -> List[dict]:
    counts = Counter((row["created_month"], row["category"]) for row in rows)
    summary = []
    for (month, category), count in sorted(counts.items()):
        summary.append({"created_month": month, "category": category, "ticket_count": count})
    return summary


def main() -> None:
    rows = read_csv(DATA_DIR / "sample_tickets.csv")
    classified = classify_rows(rows)
    summary = summarize(classified)

    write_csv(
        OUTPUT_DIR / "classified_tickets.csv",
        classified,
        ["ticket_id", "created_month", "description", "category", "classification_explanation"],
    )
    write_csv(OUTPUT_DIR / "monthly_category_summary.csv", summary, ["created_month", "category", "ticket_count"])

    print(f"Classified tickets: {len(classified)}")
    print(f"Categories found: {sorted(set(row['category'] for row in classified))}")
    print(f"Outputs written to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
