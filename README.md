# AI Automation Portfolio

A public-safe portfolio demonstrating business-to-technology translation, workflow automation design, data validation, responsible AI guardrails, and operational reporting logic.

> Confidentiality note: This portfolio uses only synthetic data, generic workflow names, and public-safe examples. It does not include customer data, internal URLs, proprietary process details, credentials, or company-owned files.

## Positioning

I am building toward roles in AI enablement, enterprise automation, business systems analysis, data analysis, and solution architecture. My current experience sits at the intersection of operations, process improvement, workflow design, reporting integrity, and responsible use of AI tools.

This repository is designed to show how I think through problems:

1. Translate business pain points into automation or AI use cases.
2. Define data, workflow, and governance requirements.
3. Build small working prototypes using synthetic data.
4. Document architecture decisions, risks, and adoption needs.
5. Create outputs that business and technical stakeholders can both understand.

## Portfolio projects

| Project | What it demonstrates | Relevant skills |
|---|---|---|
| 01 - Power Platform Solution Design | SharePoint/List schema design, workflow governance, Dev/Prod thinking, manager visibility UX | Solution design, Power Automate logic, governance, documentation |
| 02 - Teams Backfill Recovery | Data recovery logic for missing tracker fields using synthetic Teams-style messages | Python, data normalization, data quality, automation recovery pattern |
| 03 - Ticket Classification and Reporting | Deterministic classification with precedence rules and KPI validation | Python, SQL, reporting logic, data validation, audit readiness |
| 04 - Responsible AI Assistant Guardrails | Guardrail test cases, risk register, and response evaluation framework | GenAI governance, prompt testing, responsible AI, explainability |
| 05 - Automation Use Case Intake | Prioritization model for automation opportunities | Business analysis, scoring logic, stakeholder communication, roadmap thinking |

## How to run the demos locally

```bash
python3 project_02_teams_backfill_recovery/src/backfill_recovery.py
python3 project_03_ticket_classification_and_reporting/src/classify_tickets.py
python3 project_04_responsible_ai_assistant_guardrails/src/evaluate_guardrails.py
python3 project_05_automation_use_case_intake/src/prioritize_use_cases.py
```

Or run everything:

```bash
bash scripts/run_all_demos.sh
```

Run tests:

```bash
python3 -m unittest discover
```

## What to review first

For a leader or mentor reviewing this portfolio, start here:

1. `docs/portfolio_walkthrough.md`
2. `project_01_power_platform_solution_design/README.md`
3. `project_02_teams_backfill_recovery/README.md`
4. `project_04_responsible_ai_assistant_guardrails/README.md`

## Skills represented

- Workflow automation design
- Power Platform solution thinking
- SharePoint/List schema planning
- Dev/Prod deployment awareness
- Data validation and quality controls
- KPI classification logic
- Responsible AI guardrails
- Documentation for technical and non-technical stakeholders
- Python scripting using standard libraries
- SQL-style classification logic
- Automation intake and roadmap prioritization
