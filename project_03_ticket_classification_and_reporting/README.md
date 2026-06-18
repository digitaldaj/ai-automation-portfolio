# Project 03: Ticket Classification and Reporting

## Purpose

This project demonstrates deterministic classification logic for operational tickets. It uses rule precedence to keep reporting categories stable and explainable.

## Business problem

When one ticket contains multiple keywords, simple keyword matching can misclassify the issue. For example, a request mentioning both "payment" and "unlock" may be counted under the wrong category if precedence is not documented.

## Solution approach

1. Load synthetic ticket data.
2. Apply category rules in a defined order.
3. Add explanation text for each classification.
4. Produce a classified ticket file.
5. Produce a summary by month and category.

## Run the demo

```bash
python3 project_03_ticket_classification_and_reporting/src/classify_tickets.py
```

## Skills demonstrated

- Python classification logic
- SQL-style rule documentation
- KPI integrity thinking
- Audit-ready explanations
- Reporting summary generation
- Data validation design
