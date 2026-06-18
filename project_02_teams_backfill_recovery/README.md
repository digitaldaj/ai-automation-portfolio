# Project 02: Teams Backfill Recovery

## Purpose

This project demonstrates a data recovery pattern for an automation defect where tracker rows were logged without key fields such as sender, timestamp, content, or manager.

The example uses synthetic Teams-style message data and synthetic tracker rows.

## Business problem

When automation writes incomplete records, teams can lose visibility into historical volume, ownership, and reporting details. A recovery process needs to rebuild the missing data without duplicating records or creating mismatched rows.

## Solution approach

1. Load synthetic Teams-style messages.
2. Load tracker rows with missing fields.
3. Match records by message ID.
4. Filter out threaded replies.
5. Normalize sender, timestamp, content, and manager fields.
6. Convert HTML message bodies into readable text.
7. Write a recovered tracker output.

## Run the demo

```bash
python3 project_02_teams_backfill_recovery/src/backfill_recovery.py
```

Output:

```text
project_02_teams_backfill_recovery/outputs/recovered_tracker_rows.csv
```

## Skills demonstrated

- Python data transformation
- Backfill and remediation logic
- Data normalization
- HTML cleaning
- One-to-one record matching
- Reporting recovery pattern
- Automation defect analysis
