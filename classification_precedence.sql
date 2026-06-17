-- SQL-style example of documented classification precedence.
-- This is generic and uses synthetic field names.

SELECT
    ticket_id,
    created_month,
    description,
    CASE
        WHEN LOWER(description) LIKE '%unlock%' THEN 'card_unlock'
        WHEN LOWER(description) LIKE '%compliance%'
          OR LOWER(description) LIKE '%high risk%'
          OR LOWER(description) LIKE '%exception%' THEN 'compliance_review'
        WHEN LOWER(description) LIKE '%payment%'
          OR LOWER(description) LIKE '%eft%'
          OR LOWER(description) LIKE '%biller%'
          OR LOWER(description) LIKE '%billing%' THEN 'payment_or_billing'
        WHEN LOWER(description) LIKE '%cancel%' THEN 'cancellation_issue'
        WHEN LOWER(description) LIKE '%callback%'
          OR LOWER(description) LIKE '%call back%' THEN 'callback_request'
        WHEN LOWER(description) LIKE '%system access%'
          OR LOWER(description) LIKE '%cannot view%'
          OR LOWER(description) LIKE '%access issue%' THEN 'system_access'
        ELSE 'other'
    END AS category
FROM synthetic_ticket_table;
