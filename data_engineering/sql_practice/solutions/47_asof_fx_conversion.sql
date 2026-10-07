-- 47. Point-in-time FX conversion (as-of join): reference solution
--
-- Approach (portable): LEFT JOIN every earlier-or-equal rate for the same currency, then keep the
--           latest one per order with ROW_NUMBER. Orders with no rate survive as a single NULL row.
-- Traps:
--   * `<` instead of `<=` misses order 2, placed exactly when the 1.12 EUR rate took effect.
--   * Forgetting the currency condition applies GBP rates to EUR orders.
--   * An INNER JOIN silently drops order 5 (before the first GBP rate). Losing rows is worse
--     than a NULL you can alert on.
-- Native as-of joins (faster; no fan-out):
--   DuckDB:    FROM intl_orders o ASOF LEFT JOIN fx_rates r
--                ON o.currency = r.currency AND o.order_ts >= r.effective_ts
--   Snowflake: FROM intl_orders o ASOF JOIN fx_rates r
--                MATCH_CONDITION (o.order_ts >= r.effective_ts) ON o.currency = r.currency
-- Alternative with SCD2-style ranges: LEAD(effective_ts) gives valid_to, then a range join.

SELECT o.order_id, o.currency, o.amount, r.rate_to_usd,
       ROUND(o.amount * r.rate_to_usd, 2) AS amount_usd
FROM intl_orders o
LEFT JOIN fx_rates r
       ON r.currency = o.currency
      AND r.effective_ts <= o.order_ts
QUALIFY ROW_NUMBER() OVER (PARTITION BY o.order_id ORDER BY r.effective_ts DESC) = 1;
