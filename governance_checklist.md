# Governance Checklist

## Before deployment

- [ ] Business owner approved requirements.
- [ ] Required fields identified.
- [ ] Reporting fields confirmed stable.
- [ ] Test list created.
- [ ] Flow tested with complete and incomplete records.
- [ ] Error handling tested.
- [ ] Rollback approach documented.
- [ ] User communication drafted.

## After deployment

- [ ] Confirm production list permissions.
- [ ] Validate notification routing.
- [ ] Compare sample reporting output before and after change.
- [ ] Monitor failed flow runs.
- [ ] Collect user feedback after first week.
- [ ] Document enhancement requests separately from defects.

## Responsible automation considerations

- Avoid over-automation of ambiguous decisions.
- Require human validation for compliance-sensitive steps.
- Keep audit fields visible and protected.
- Make status logic explainable to non-technical users.
