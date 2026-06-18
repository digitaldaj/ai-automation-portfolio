# Automation Prioritization Scoring Model

Each use case receives a 1 to 5 score across six dimensions.

| Dimension | Meaning |
|---|---|
| Volume impact | How many records, users, or interactions are affected |
| Manual effort | How repetitive or time-consuming the work is |
| Compliance risk | Whether errors create business, audit, or customer risk |
| Data readiness | Whether required data is structured and accessible |
| Implementation complexity | How difficult the solution is to build and maintain |
| Stakeholder alignment | Whether business owners are aligned and available |

Implementation complexity is weighted negatively because high complexity can reduce near-term feasibility.

## Recommendation thresholds

| Score | Recommendation |
|---:|---|
| 3.5 or higher | Prioritize for discovery |
| 2.5 to 3.49 | Hold for refinement |
| Below 2.5 | Do not prioritize now |
