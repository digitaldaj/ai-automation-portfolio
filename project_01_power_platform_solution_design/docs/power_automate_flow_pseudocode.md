# Power Automate Style Flow Pseudocode

## Trigger

When a new item is created or modified in the structured intake list.

## Logic

```text
IF request_type is blank OR priority is blank OR customer_impact is blank:
    Set review_status = "Incomplete"
    Send reminder to submitter
    Stop flow

IF review_status = "Pending Review":
    Notify review group in Teams-style channel
    Add timestamp to last_updated

IF review_validated = "Validated" AND manager_action_status is blank:
    Set manager_action_status = "Ready for Manager Review"
    Notify manager group

IF review_validated = "Not Validated":
    Set manager_action_status = "Hold for Clarification"
    Notify submitter with required clarification fields

Always:
    Preserve month field for reporting
    Append change summary to audit log
```

## Design principles

- Avoid silent defaults on validation fields.
- Keep reporting fields stable.
- Send notifications only when action is needed.
- Use test list before production deployment.
- Keep business-facing messages plain and specific.
