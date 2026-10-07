# Data Platform & Governance Engineer: Interview Prep

Questions and model answers targeted at a role owning Snowflake administration, access governance, vendor tooling (Fivetran, Airflow/Astronomer, Hex), warehouse cost, and CDC/streaming ingestion.

General Kafka/Snowflake fundamentals are in [data_engineering_kafka_snowflake.md](data_engineering_kafka_snowflake.md).

---

## JD to Prep Map

| JD responsibility | Sections |
|---|---|
| Structure and ownership of Snowflake data | 1 |
| Narrow RBAC + automated joiner/mover/leaver | 2 |
| Row access policies and PII masking | 3 |
| Migrating sources into governed homes without breaking teams | 4 |
| Fivetran, Airflow/Astronomer, Hex ownership + on-call | 5 |
| Warehouse spend | 6 |
| CDC/streaming, delivery semantics, cutovers | 7 |
| SQL/Python judgment | 8 |
| Behavioral | 9 |

---

## 1. Organizing Data in Snowflake with Clear Ownership

**Q1. Snowflake has grown organically: hundreds of schemas, unclear owners, everyone uses SYSADMIN. How do you bring structure?**
1. **Inventory**: query `ACCOUNT_USAGE.TABLES`, `ACCESS_HISTORY`, `QUERY_HISTORY`, and `TABLE_STORAGE_METRICS` to see what exists, who writes it, who reads it, size, and last access.
2. **Define a layout convention**, for example:
   - `RAW_<source>` databases: landing zones owned by ingestion (Fivetran, Snowpipe, CDC). Nobody but the loader writes here.
   - `STAGING` / `INTERMEDIATE`: transformation-owned (dbt).
   - `ANALYTICS` / `MARTS_<domain>`: curated, documented, owned by a domain team.
   - `SANDBOX_<user|team>`: scratch space with auto-expiry.
3. **Assign one owning team per database/schema**, recorded with **object tags** (`owner_team`, `data_domain`, `sensitivity`, `cost_center`) so ownership is queryable via `TAG_REFERENCES`.
4. **Transfer object ownership** away from human users and `SYSADMIN` to owning roles, so ownership survives people leaving.
5. **Clean up**: deprecate tables with no reads in 90+ days (announce, revoke access, wait, drop; Time Travel/clones give a safety net).
6. **Codify it** in Terraform or a permissions-as-code tool so new projects follow the pattern by default.

**Q2. Database per domain, or schema per domain inside a shared database?**
- **Database per domain**: clean ownership boundaries, easy database-level replication/cloning/sharing, and **database roles** scope privileges nicely. More objects to manage.
- **Schema per domain**: fewer objects, but cross-domain grants get noisy and ownership is blurrier.
- Common answer: database per *layer + domain* where ownership differs (raw per source system, marts per domain), schemas for sub-areas within a team.

**Q3. What are managed access schemas and why use them?**
In a regular schema the object owner can grant access to their object. In a **managed access schema** (`CREATE SCHEMA ... WITH MANAGED ACCESS`), only the schema owner or a role with `MANAGE GRANTS` can grant privileges. That centralizes grant decisions and prevents ad-hoc "I'll just grant my table to my friend's role" sprawl. Use it for any schema holding governed data.

**Q4. What are database roles and when do you use them over account roles?**
Database roles live inside a database and can only hold privileges on that database's objects. They're granted to account roles (or to shares). Benefits: privileges travel with the database (cloning, replication, sharing), and the access model per database is self-contained. Typical pattern: `ANALYTICS.READER`, `ANALYTICS.WRITER` database roles granted to functional account roles.

---

## 2. RBAC Design and Access Automation

**Q5. Design a role hierarchy that keeps access narrow.**
Two-tier **access roles + functional roles**:
- **Access roles** (or database roles): hold privileges on one scope, e.g. `AR_FINANCE_MARTS_READ`, `AR_FINANCE_MARTS_WRITE`. Never granted directly to users.
- **Functional roles**: map to a job or team, e.g. `FR_FINANCE_ANALYST`, `FR_DATA_ENG`. Granted the access roles they need, and granted to users.
- **Service roles**: one per system (`SVC_FIVETRAN`, `SVC_AIRFLOW`, `SVC_DBT`, `SVC_HEX`), each with only the access it needs and its own warehouse.
- All custom roles roll up to `SYSADMIN` so admins can manage objects, but SYSADMIN isn't used day to day.
- `ACCOUNTADMIN` is limited to 2–3 break-glass users with MFA, and alerts fire when it's used.

```sql
CREATE ROLE AR_FINANCE_MARTS_READ;
GRANT USAGE ON DATABASE FINANCE TO ROLE AR_FINANCE_MARTS_READ;
GRANT USAGE ON SCHEMA FINANCE.MARTS TO ROLE AR_FINANCE_MARTS_READ;
GRANT SELECT ON ALL TABLES IN SCHEMA FINANCE.MARTS TO ROLE AR_FINANCE_MARTS_READ;
GRANT SELECT ON FUTURE TABLES IN SCHEMA FINANCE.MARTS TO ROLE AR_FINANCE_MARTS_READ;
GRANT SELECT ON ALL VIEWS IN SCHEMA FINANCE.MARTS TO ROLE AR_FINANCE_MARTS_READ;
GRANT SELECT ON FUTURE VIEWS IN SCHEMA FINANCE.MARTS TO ROLE AR_FINANCE_MARTS_READ;

CREATE ROLE FR_FINANCE_ANALYST;
GRANT ROLE AR_FINANCE_MARTS_READ TO ROLE FR_FINANCE_ANALYST;
GRANT USAGE ON WAREHOUSE WH_FINANCE_BI TO ROLE FR_FINANCE_ANALYST;
GRANT ROLE FR_FINANCE_ANALYST TO ROLE SYSADMIN;
```

**Q6. How do you automate joiner/mover/leaver so access is granted and revoked automatically?**
- **Source of truth is the identity provider** (Okta / Entra ID). Users and group memberships are provisioned into Snowflake via **SCIM**. Disabling a user in the IdP disables them in Snowflake.
- **IdP groups map to functional roles** (either pushed as roles via SCIM, or mapped in code). A team change in HR moves the user to a new group, which swaps their functional role. Nobody files a ticket.
- **Role definitions and grants live in code** (Terraform Snowflake provider, or a permissions tool), reviewed via pull request, applied by CI. Manual grants are detected and reverted (drift detection).
- **Elevated or sensitive access** (e.g. PII unmasked) goes through a request workflow with an approver and an **expiry**; a scheduled job revokes it automatically.
- **SSO-only login** for humans; **key-pair auth** (or OAuth) for service users; no passwords.
- **Quarterly access reviews** generated from `GRANTS_TO_USERS` / `GRANTS_TO_ROLES` and sent to data owners to attest.

**Q7. What do you do about service accounts when someone leaves?**
Service users must not be tied to a person: dedicated `TYPE = SERVICE` users, key-pair auth with rotation, owned by a team role, and documented in code. Check `LOGIN_HISTORY` and `QUERY_HISTORY` for personal credentials being used by pipelines, and migrate them before offboarding.

**Q8. Future grants at database vs schema level: any gotchas?**
Yes. If future grants exist at **both** levels for the same object type, the **schema-level future grants win** and database-level ones are ignored for that schema. Also, future grants only apply to objects created afterwards; existing objects need `GRANT ... ON ALL ...`. And in managed access schemas, only the schema owner or `MANAGE GRANTS` can define them.

**Q9. How do secondary roles affect your access model?**
With `USE SECONDARY ROLES ALL`, a session gets the union of privileges from all of the user's granted roles (for querying), not just the primary role. That's convenient but weakens "least privilege per session". It also affects policy logic: `CURRENT_ROLE()` only sees the primary role, while `IS_ROLE_IN_SESSION()` sees primary + secondary + inherited roles. Policies should use `IS_ROLE_IN_SESSION()` for correctness.

**Q10. How do you audit who has access to a sensitive table and who actually used it?**
- **Who can access**: recursively expand `ACCOUNT_USAGE.GRANTS_TO_ROLES` and `GRANTS_TO_USERS` from the table's privileges up through the role hierarchy to users.
- **Who used it**: `ACCOUNT_USAGE.ACCESS_HISTORY` (Enterprise+) shows `base_objects_accessed` and `direct_objects_accessed` down to column level, per query and user.
- Compare the two: roles with access but no use in 90 days are candidates for revocation.

---

## 3. Row Access Policies and PII Masking

**Q11. How do you implement row-level security across many tables without writing a policy per table?**
Use **one policy per access dimension**, driven by a **mapping table**, and attach it to every table with that dimension:

```sql
CREATE TABLE GOVERNANCE.POLICIES.REGION_ACCESS_MAP (
    role_name STRING,
    region    STRING
);

CREATE OR REPLACE ROW ACCESS POLICY GOVERNANCE.POLICIES.RAP_REGION
AS (region STRING) RETURNS BOOLEAN ->
    IS_ROLE_IN_SESSION('FR_GLOBAL_ANALYST')
    OR EXISTS (
        SELECT 1
        FROM GOVERNANCE.POLICIES.REGION_ACCESS_MAP m
        WHERE m.region = region
          AND IS_ROLE_IN_SESSION(m.role_name)
    );

ALTER TABLE SALES.MARTS.ORDERS
    ADD ROW ACCESS POLICY GOVERNANCE.POLICIES.RAP_REGION ON (region);
```

Key points:
- Policies live in a central `GOVERNANCE` database owned by a governance role, separate from data owners. Grant `APPLY ROW ACCESS POLICY` narrowly.
- Mapping rows are managed in code/automation, so access changes don't require policy edits.
- Keep the policy body simple and the mapping table small; complex subqueries run for every query against the table. Memoizable functions can cache lookups.
- Test with a matrix of roles × expected row counts in CI.

**Q12. How do you roll out PII masking across all sensitive datasets?**
1. **Discover**: run Snowflake **data classification** (`SYSTEM$CLASSIFY` / automatic classification) to find semantic categories (email, phone, name, national ID), and supplement with naming heuristics and owner review.
2. **Tag**: apply a `PII` tag with values (`EMAIL`, `PHONE`, `SSN`, ...) to columns.
3. **Tag-based masking**: attach masking policies to the **tag**, not to individual columns. Any column tagged in the future is protected automatically.
4. **Policy logic** checks roles, e.g. a `PII_READER` access role sees clear text, everyone else sees a hash or partial mask:

```sql
CREATE OR REPLACE MASKING POLICY GOVERNANCE.POLICIES.MASK_EMAIL
AS (val STRING) RETURNS STRING ->
    CASE
        WHEN IS_ROLE_IN_SESSION('AR_PII_READER') THEN val
        WHEN IS_ROLE_IN_SESSION('AR_PII_PSEUDONYM') THEN SHA2(LOWER(val))
        ELSE REGEXP_REPLACE(val, '.+@', '****@')
    END;

ALTER TAG GOVERNANCE.TAGS.PII SET MASKING POLICY GOVERNANCE.POLICIES.MASK_EMAIL;
ALTER TABLE CRM.MARTS.CUSTOMERS MODIFY COLUMN email SET TAG GOVERNANCE.TAGS.PII = 'EMAIL';
```

5. **Prevent leakage**: tags propagate via lineage in some cases, but derived tables built by dbt can strip protection. Re-apply tags in dbt (`post-hook` or meta-driven macros), and scan for untagged PII regularly.
6. **Monitor coverage**: a dashboard of classified-but-untagged columns and tagged-but-unmasked columns.

**Q13. Why hash rather than null out masked values?**
A deterministic hash (`SHA2` with a secret salt, or tokenization) keeps joins and `COUNT(DISTINCT)` working for analysts without exposing raw values. Nulling is safer but breaks analytics. Choose per category: SSNs fully masked, emails hashed for joins.

**Q14. The BI tool (Hex) connects with one shared service account. What breaks in your governance model?**
Every Hex user inherits the service account's role, so row access and masking policies evaluate against **that** role, not the human. Either the service role sees everything (leak) or nothing (useless). Fixes:
- Use **per-user OAuth** to Snowflake from Hex, so policies evaluate against each user's own roles.
- If a shared connection is unavoidable, scope it to a role that sees only non-sensitive, aggregated data, and restrict which Hex workspaces/groups can use that connection.

**Q15. What's the performance impact of policies and how do you manage it?**
Policies are evaluated at query time. Row access policies add a filter (and possibly a join to the mapping table) to every query; masking runs per value returned. Keep bodies simple, avoid UDF calls inside, use small mapping tables, check Query Profile for the policy's cost, and use memoizable functions for repeated lookups.

---

## 4. Migrating Live Data Without Breaking Dependent Teams

**Q16. Walk through migrating a heavily used vendor dataset into a properly owned, governed home.**
1. **Find every consumer**: `ACCESS_HISTORY` (which users, roles, and service accounts query the old tables, and which columns), `OBJECT_DEPENDENCIES` (views built on it), dbt `ref`/sources and exposures, Hex projects, Airflow DAGs, reverse ETL syncs.
2. **Define the target**: owning team, database/schema, naming, tags, RBAC, masking/row policies, freshness SLA, and documentation.
3. **Build the new pipeline in parallel** and backfill history.
4. **Validate**: row counts, primary-key uniqueness, column-level checksums/aggregates by day, and a sample of exact row diffs between old and new. Run for long enough to cover edge cases like month-end.
5. **Provide a compatibility layer**: replace the old table with a **view** pointing at the new location (same name and columns), so consumers keep working while you migrate them.
6. **Migrate consumers in waves**, with owners notified and a deadline. Track usage of the old names through `ACCESS_HISTORY` until it hits zero.
7. **Deprecate**: revoke access to the old objects (reversible), wait, then drop. Keep a clone or Time Travel window for rollback.

**Q17. How do you swap a rebuilt table in atomically?**
Build into `orders_new`, validate, then `ALTER TABLE orders SWAP WITH orders_new`. It's a metadata operation, atomic, and the old version sits in `orders_new` for instant rollback. Be careful that grants, policies, and tags are on the right object after the swap (use `COPY GRANTS` when recreating; verify policy attachments).

**Q18. A migration changes column types or semantics. How do you avoid surprising consumers?**
Treat the schema as a **contract**: version it (`orders_v2`), publish a changelog and a deprecation window, keep the old shape available via a view during the window, and use dbt model contracts/versions to enforce it in CI. Never change semantics in place silently.

**Q19. How do you test a migration in production-like conditions without risk?**
Zero-copy **clone** production databases into a test environment, run the new pipeline and downstream dbt models against the clone, compare outputs, and drop the clone after. It's cheap since storage is shared until data changes.

---

## 5. Owning Vendor Tooling: Fivetran, Airflow/Astronomer, Hex

### Fivetran

**Q20. How is Fivetran billed, and how do you control the cost?**
Fivetran charges by **Monthly Active Rows (MAR)**: distinct rows inserted, updated, or deleted per connector per month. Cost drivers and fixes:
- **High-churn tables** (rows updated constantly, e.g. a `last_seen_at` column): exclude the table or column, or move to a cheaper ingestion path (CDC into Kafka/Snowpipe).
- **Unneeded tables/columns**: block them in the connector schema config. Default to "block new tables" for noisy sources.
- **Re-syncs**: historical re-syncs regenerate MAR; avoid them unless necessary.
- **History mode** multiplies rows; enable only where SCD history is truly required.
- Review the per-connector/per-table MAR usage report monthly and set alerts.
- **Snowflake side**: Fivetran's merges run on your warehouse. Give it a dedicated small warehouse with short auto-suspend, and tune sync frequency (every 5 minutes keeps the warehouse awake; hourly may be fine).

**Q21. A Fivetran connector is failing or delayed. How do you triage?**
Check the connector's sync logs and status (auth expired, source schema change, API rate limits, source DB replication slot or binlog issues), confirm the destination warehouse isn't suspended or out of credits (resource monitor), and confirm grants on the destination schema. Communicate impact using a freshness check on the destination tables. Prevent repeats with freshness monitors (dbt source freshness or Fivetran webhooks/alerts into the on-call channel).

**Q22. How do you handle upstream schema changes from Fivetran sources?**
Choose a schema-change policy per connector (allow all, allow columns only, block all). Land raw tables as Fivetran writes them, and isolate consumers behind dbt staging models that select explicit columns, so a new or renamed column doesn't break downstream. Alert on schema change events.

### Airflow / Astronomer

**Q23. What makes an Airflow pipeline reliable?**
- **Idempotent tasks**: re-running a task for the same logical date gives the same result (MERGE or delete-and-insert a partition, never blind appends).
- **Retries with backoff** for transient failures; no retries for deterministic failures.
- **Timeouts** (`execution_timeout`) so hung tasks don't block slots.
- **Deferrable operators/sensors** so waiting doesn't occupy workers.
- **Pools and `max_active_runs`** to protect shared resources like Snowflake warehouses or vendor APIs.
- **Data-aware scheduling** (Datasets/Assets) instead of time-based guesses about upstream completion.
- **Thin DAGs**: heavy compute happens in Snowflake/dbt, not on Airflow workers.
- **Callbacks** (`on_failure_callback`) to page or post to Slack with run context and a runbook link.
- **CI**: DAG import tests, linting, and unit tests before `astro deploy`.

**Q24. You're on call and a critical DAG failed at 3 AM. Walk through it.**
1. Acknowledge the alert, then check impact: which tables and dashboards are stale, and is there an SLA?
2. Read task logs: transient (warehouse queue, network, vendor 5xx) or deterministic (bad data, schema change, code bug)?
3. Transient: clear and re-run the task (safe because it's idempotent).
4. Deterministic: decide whether to fix forward, skip, or let downstream run on yesterday's data with a notice to consumers.
5. Communicate status in the incident channel.
6. Follow-up: blameless postmortem, add a test or alert that would have caught it earlier, and update the runbook.

**Q25. How do you reduce on-call noise?**
Classify alerts: page only for SLA-impacting failures on tier-1 pipelines; send everything else to a ticket queue. Remove flaky alerts, auto-retry transient failures, add freshness-based alerts (data is late) instead of only task-failure alerts, and review alert volume weekly.

**Q26. What's specific to running Airflow on Astronomer?**
Managed deployments (scheduler, workers, executor) per environment; deploys via the Astro CLI from CI; deployment-level environment variables and secrets backends; worker queues for sizing; built-in observability for task duration and failures. Discuss promoting changes dev → staging → prod, and using Cosmos to render dbt projects as Airflow task groups.

### Hex

**Q27. What does Hex governance mean across company-wide dashboards?**
- **Connections**: per-user OAuth to Snowflake where policies matter; shared connections only for non-sensitive data, with a dedicated role and warehouse.
- **Workspace roles and groups**: who can create projects, edit, publish, or only view apps; map groups to IdP groups.
- **Trusted content**: distinguish certified/endorsed company dashboards from personal exploration; certified ones must use curated mart tables, not raw.
- **Cost control**: Hex queries run on a dedicated warehouse with a resource monitor; tag queries (`QUERY_TAG`) to attribute cost per project; watch for scheduled runs refreshing too often.
- **Lifecycle**: archive stale projects, transfer ownership when people leave, and check that published apps don't expose data beyond their audience.

---

## 6. Snowflake Warehouse Spend

**Q28. How do you find where Snowflake money is going?**
- `ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY`: credits per warehouse per hour.
- `ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY`: compute cost attributed per query, so you can roll it up by user, role, or query tag.
- `METERING_DAILY_HISTORY`: serverless costs (Snowpipe, auto-clustering, materialized views, search optimization, serverless tasks).
- `TABLE_STORAGE_METRICS`: active vs Time Travel vs Fail-safe bytes.
- Enforce `QUERY_TAG` from Airflow, dbt, and Hex so cost maps to pipelines and teams.
- Note that `ACCOUNT_USAGE` views lag by up to a few hours.

**Q29. Concrete right-sizing playbook?**
1. **One warehouse per workload** (ingestion, transformation, BI, ad hoc, data science) for isolation and attribution.
2. **Auto-suspend at 60 seconds** for most warehouses. BI warehouses may benefit from slightly longer to keep the cache warm.
3. **Right-size by experiment**: run the workload at size N and N-1. If runtime roughly doubles at N-1, credits are the same and the larger size wins on latency; if runtime barely changes, downsize.
4. **Spilling** to remote storage in Query Profile means the warehouse is too small for that query. Spilling to local disk is a warning sign.
5. **Queuing** means a concurrency problem: use multi-cluster (Economy policy for cost) rather than a bigger size.
6. **Guardrails**: `STATEMENT_TIMEOUT_IN_SECONDS` per warehouse, resource monitors with notify/suspend thresholds, budgets per team.
7. **Fix the worst queries**: top 20 by credits usually dominate. Look for full scans from missing filters, exploding joins, `SELECT *` from Hex, and dbt full refreshes that should be incremental.
8. **Serverless features**: review auto-clustering, materialized views, and search optimization costs against the benefit.
9. **Storage**: transient tables for staging, shorter Time Travel on high-churn tables, drop abandoned clones.

**Q30. Finance says Snowflake spend jumped 40% this month. What do you do?**
Compare credits by warehouse and by day to find when and where it started. Drill into the top queries by attributed cost in that warehouse, and check for: a new or changed dbt model (e.g. full refresh), a Hex dashboard on a short schedule, a warehouse resized and never reverted, auto-suspend disabled, a runaway retry loop in Airflow, or a new serverless feature. Fix, then add a guardrail (resource monitor, alert on daily credit anomaly) so it's caught within a day next time.

---

## 7. CDC / Streaming Ingestion and Safe Cutovers

**Q31. Design CDC from Postgres into Snowflake.**
- **Debezium** Postgres connector reading logical replication (`pgoutput`) via a **replication slot**.
- **Kafka topic per table**, keyed by primary key, so all changes to a row land in one partition in order.
- **Avro + Schema Registry** for schema evolution.
- **Snowflake Kafka connector with Snowpipe Streaming** into raw change tables (op, before/after, LSN, source timestamp).
- **Apply layer** (Dynamic Tables or Stream + Task MERGE) builds current-state tables: dedupe by PK, order by LSN, apply deletes.
- **Governance**: raw change tables are restricted; masking policies apply to the current-state tables; tags applied at creation.

**Q32. What delivery semantics does that pipeline have, end to end?**
Debezium is **at-least-once**: after a crash, it resumes from the last committed offset and may re-emit events. Kafka with idempotent producers avoids duplicates from producer retries. Snowpipe Streaming with offset tokens is exactly-once from Kafka into the table. But duplicates from the source connector can still arrive, so the **apply layer must be idempotent**: dedupe on (PK, LSN) and only apply a change if its LSN is newer than what's stored. That gives effectively-once results.

**Q33. How do you choose partitioning for CDC topics?**
Key by primary key: ordering is only guaranteed per partition, and per-row ordering is what matters for CDC. Partition count is set by throughput, but don't change it on a live topic, because it remaps keys and breaks ordering during the transition. For a table where one key is extremely hot, ordering still forces it to one partition; accept that or redesign upstream.

**Q34. What are the production risks with Postgres CDC specifically?**
- **Replication slot growth**: if the connector stops, Postgres retains WAL for the slot indefinitely and can **fill the source database disk**. Monitor slot lag (`pg_replication_slots`, `confirmed_flush_lsn`) and alert aggressively; set `max_slot_wal_keep_size` as a safety limit.
- **Low-traffic tables**: if captured tables are quiet but the DB is busy, the slot doesn't advance. Debezium's **heartbeat** setting fixes it.
- **Failover**: logical slots historically weren't replicated to the standby. Verify slot failover support on your Postgres version or managed service.
- **Snapshots**: the initial snapshot of big tables is slow; use **incremental snapshots** (signal table) so you can snapshot while streaming.
- **DDL**: column changes flow through Schema Registry; incompatible changes need coordination.
- **TOAST columns** may arrive as placeholder values for unchanged large columns unless `REPLICA IDENTITY FULL` is set.

**Q35. How do you safely cut over from Fivetran (or a batch job) to your new CDC pipeline?**
1. **Run both in parallel** into separate tables.
2. **Reconcile continuously**: row counts, PK sets, and column checksums per day; investigate every diff (deletes, timezones, type differences, soft-delete conventions).
3. **Point a view** (the contract consumers use) at the old table.
4. **Cutover**: switch the view to the new table in one statement during a low-traffic window, after confirming the new pipeline is caught up past a known LSN/timestamp.
5. **Keep the old pipeline running** for a rollback window (a week or two). Rollback = point the view back.
6. **Turn off the old pipeline** and stop paying for its MAR once reconciliation stays clean.

**Q36. How do you handle backfills and replays on a CDC pipeline?**
Replays from Kafka (within retention) or a fresh incremental snapshot. Because the apply layer is idempotent and LSN-ordered, replays converge to the correct state. Use a separate consumer group or connector for large backfills so you don't delay live changes.

**Q37. When would you choose Snowpipe Streaming vs file-based Snowpipe vs Fivetran?**
- **Fivetran**: fastest to set up, vendor-managed, best for SaaS APIs and moderate volumes; cost scales with MAR, so high-churn tables get expensive.
- **File-based Snowpipe**: files landing in S3/GCS from other systems; ~1 minute latency; per-file overhead makes many small files costly.
- **Snowpipe Streaming**: row-level, seconds of latency, cheaper for high-volume streams, exactly-once with the Kafka connector. More engineering to own.

---

## 8. SQL and Python Judgment

**Q38. Find roles that have access to PII-tagged columns, expanded to users.**

```sql
WITH pii_tables AS (
    SELECT DISTINCT object_database, object_schema, object_name
    FROM SNOWFLAKE.ACCOUNT_USAGE.TAG_REFERENCES
    WHERE tag_name = 'PII' AND domain = 'COLUMN'
),
direct_role_grants AS (
    SELECT g.grantee_name AS role_name, g.table_catalog, g.table_schema, g.name AS table_name
    FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES g
    JOIN pii_tables p
      ON g.table_catalog = p.object_database
     AND g.table_schema  = p.object_schema
     AND g.name          = p.object_name
    WHERE g.privilege = 'SELECT' AND g.deleted_on IS NULL
),
role_tree AS (
    SELECT role_name AS granted_role, role_name AS holder_role, table_name
    FROM direct_role_grants
    UNION ALL
    SELECT rt.granted_role, g.grantee_name, rt.table_name
    FROM role_tree rt
    JOIN SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES g
      ON g.name = rt.holder_role
     AND g.granted_on = 'ROLE'
     AND g.privilege = 'USAGE'
     AND g.deleted_on IS NULL
)
SELECT DISTINCT u.grantee_name AS user_name, rt.holder_role, rt.table_name
FROM role_tree rt
JOIN SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_USERS u
  ON u.role = rt.holder_role AND u.deleted_on IS NULL
ORDER BY user_name, table_name;
```

**Q39. Top 10 most expensive query patterns last week by role.**

```sql
SELECT
    q.role_name,
    a.query_parameterized_hash,
    ANY_VALUE(LEFT(q.query_text, 200))  AS sample_query,
    COUNT(*)                            AS runs,
    SUM(a.credits_attributed_compute)   AS credits
FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ATTRIBUTION_HISTORY a
JOIN SNOWFLAKE.ACCOUNT_USAGE.QUERY_HISTORY q USING (query_id)
WHERE a.start_time >= DATEADD('day', -7, CURRENT_TIMESTAMP())
GROUP BY q.role_name, a.query_parameterized_hash
ORDER BY credits DESC
LIMIT 10;
```

**Q40. Tables with no reads in 90 days (deprecation candidates).**

```sql
WITH reads AS (
    SELECT f.value:"objectName"::STRING AS fq_name, MAX(ah.query_start_time) AS last_read
    FROM SNOWFLAKE.ACCOUNT_USAGE.ACCESS_HISTORY ah,
         LATERAL FLATTEN(input => ah.base_objects_accessed) f
    WHERE ah.query_start_time >= DATEADD('day', -180, CURRENT_TIMESTAMP())
    GROUP BY 1
)
SELECT t.table_catalog || '.' || t.table_schema || '.' || t.table_name AS fq_name,
       t.row_count, t.bytes, r.last_read
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES t
LEFT JOIN reads r
  ON r.fq_name = t.table_catalog || '.' || t.table_schema || '.' || t.table_name
WHERE t.deleted IS NULL
  AND (r.last_read IS NULL OR r.last_read < DATEADD('day', -90, CURRENT_TIMESTAMP()))
ORDER BY t.bytes DESC NULLS LAST;
```

**Q41. Python: reconcile desired role grants (from config) against actual Snowflake grants.**

```python
import yaml
import snowflake.connector


def load_desired(path: str) -> set[tuple[str, str]]:
    """Config format: {functional_role: [access_role, ...]}"""
    with open(path) as f:
        config = yaml.safe_load(f)
    return {(fr, ar) for fr, ars in config.items() for ar in ars}


def load_actual(cur) -> set[tuple[str, str]]:
    cur.execute("""
        SELECT grantee_name, name
        FROM SNOWFLAKE.ACCOUNT_USAGE.GRANTS_TO_ROLES
        WHERE granted_on = 'ROLE' AND privilege = 'USAGE'
          AND deleted_on IS NULL
          AND grantee_name LIKE 'FR\\_%' AND name LIKE 'AR\\_%'
    """)
    return {(grantee, role) for grantee, role in cur.fetchall()}


def plan(desired: set, actual: set) -> list[str]:
    grants = [f"GRANT ROLE {ar} TO ROLE {fr};" for fr, ar in sorted(desired - actual)]
    revokes = [f"REVOKE ROLE {ar} FROM ROLE {fr};" for fr, ar in sorted(actual - desired)]
    return grants + revokes


if __name__ == "__main__":
    conn = snowflake.connector.connect(connection_name="governance")
    with conn.cursor() as cur:
        for stmt in plan(load_desired("roles.yml"), load_actual(cur)):
            print(stmt)
```

Talking points: print a plan first and apply only after review (like `terraform plan`); revokes are higher risk, so alert owners before applying; `ACCOUNT_USAGE` lags, so use `SHOW GRANTS` for real-time state at apply time.

---

## 9. Behavioral and Judgment Questions

Prepare a STAR story (Situation, Task, Action, Result) for each, with numbers where possible.

1. **"Tell me about a production migration you led. How did you avoid breaking downstream teams?"** Cover consumer discovery, parallel run, reconciliation, the compatibility layer, communication, and rollback.
2. **"Describe a time you tightened access controls and got pushback."** Show how you balanced security with productivity: self-service request flows, fast approvals, and clear data owners.
3. **"Tell me about an incident you handled on call."** Detection, triage, communication, fix, and the postmortem actions that stopped it recurring.
4. **"When did you push back on a spec or request?"** The JD stresses making judgment calls, not just executing. Show the trade-off you identified and the alternative you proposed.
5. **"How did you reduce cost on a platform you owned?"** Concrete numbers: credits or MAR saved, and how you kept it from regressing.
6. **"Tell me about a CDC/streaming pipeline you owned in production."** Delivery semantics, ordering, what went wrong, and how you cut over between systems.
7. **"How do you prioritize when platform requests come from many teams?"** Impact vs effort, risk reduction, paving paths that remove repeat requests.

---

## 10. Questions to Ask Them

- How is access managed today: IdP + SCIM, Terraform, or manual grants? What's the biggest pain?
- What share of sensitive data is covered by masking and row access policies today?
- What does on-call look like: rotation size, alert volume, which pipelines are tier 1?
- What's the current Snowflake and Fivetran spend trajectory, and is there a cost target?
- What's driving the CDC/streaming work: Fivetran cost, latency needs, or new sources?
- Is there a data catalog or ownership registry, or would this role build it?
- How do Hex users connect to Snowflake today: shared service account or per-user OAuth?
