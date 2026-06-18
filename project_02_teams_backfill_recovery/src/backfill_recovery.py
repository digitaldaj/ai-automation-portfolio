"""Recover missing tracker fields from synthetic Teams-style message exports.

This demo intentionally uses only Python standard-library modules and synthetic data.
"""

from __future__ import annotations

import csv
import html
import re
from pathlib import Path
from typing import Dict, Iterable, List

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "outputs"


def read_csv(path: Path) -> List[dict]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_csv(path: Path, rows: Iterable[dict], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def clean_html(raw_html: str) -> str:
    """Convert simple HTML content into readable plain text."""
    no_tags = re.sub(r"<[^>]+>", " ", raw_html or "")
    decoded = html.unescape(no_tags)
    return re.sub(r"\s+", " ", decoded).strip()


def build_message_lookup(messages: List[dict]) -> Dict[str, dict]:
    """Create a message lookup, excluding threaded replies."""
    lookup = {}
    for message in messages:
        is_reply = str(message.get("is_reply", "")).strip().lower() == "true"
        if is_reply:
            continue
        lookup[message["message_id"]] = message
    return lookup


def recover_tracker_rows(tracker_rows: List[dict], messages: List[dict]) -> List[dict]:
    lookup = build_message_lookup(messages)
    recovered_rows = []

    for row in tracker_rows:
        message = lookup.get(row["message_id"])
        updated = dict(row)

        if not message:
            updated["recovery_status"] = "No matching source message"
            recovered_rows.append(updated)
            continue

        updated["sender_name"] = row.get("sender_name") or message.get("sender_name", "")
        updated["manager_email"] = row.get("manager_email") or message.get("manager_email") or "manager_unavailable"
        updated["content"] = row.get("content") or clean_html(message.get("body_html", ""))
        updated["logged_at"] = row.get("logged_at") or message.get("sent_at", "")
        updated["recovery_status"] = "Recovered"
        recovered_rows.append(updated)

    return recovered_rows


def main() -> None:
    messages = read_csv(DATA_DIR / "sample_teams_messages.csv")
    tracker_rows = read_csv(DATA_DIR / "sample_missing_tracker_rows.csv")
    recovered = recover_tracker_rows(tracker_rows, messages)

    output_path = OUTPUT_DIR / "recovered_tracker_rows.csv"
    fieldnames = ["tracker_id", "message_id", "logged_at", "sender_name", "manager_email", "content", "recovery_status"]
    write_csv(output_path, recovered, fieldnames)

    recovered_count = sum(1 for row in recovered if row["recovery_status"] == "Recovered")
    unmatched_count = sum(1 for row in recovered if row["recovery_status"] != "Recovered")
    print(f"Recovered rows: {recovered_count}")
    print(f"Unmatched rows: {unmatched_count}")
    print(f"Output written to: {output_path}")


if __name__ == "__main__":
    main()
