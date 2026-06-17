# KPI Validation Plan

## Purpose

Classification rules should produce consistent, explainable reporting categories. This plan documents how to validate changes before using them in leadership reporting.

## Checks

1. Compare old category counts to new category counts.
2. Review tickets where category changed.
3. Confirm rule precedence with business owner.
4. Validate that multi-keyword tickets land in the intended category.
5. Confirm monthly summaries reconcile to the full ticket population.
6. Document rule changes in a change log.

## Example risk

If "payment" is evaluated before "unlock," an unlock-related request may be counted as a payment issue. Precedence rules should put the most specific category first.

## Approval criteria

- No duplicate tickets in output.
- Total ticket count matches source file.
- Category definitions are documented.
- Business owner agrees with precedence order.
