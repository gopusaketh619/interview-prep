# Data Engineering Interview Guide: Kafka & Snowflake

Technical and system-design questions with concise model answers. Each section goes from fundamentals to senior-level depth.

---

## Part 1: Apache Kafka

### 1.1 Fundamentals

**Q1. What is Kafka and when would you use it over a traditional message queue (RabbitMQ, SQS)?**
Kafka is a distributed, partitioned, replicated, append-only commit log.
- Messages are **retained** (by time/size) regardless of consumption, so many consumer groups can read independently and **replay** history.
- Ordering is guaranteed **within a partition**.
- Very high throughput via sequential disk I/O, batching, compression, and zero-copy transfer.
- Use it for event streaming, CDC, log aggregation, decoupling microservices, and feeding both real-time and batch sinks. Use a classic queue when you need per-message acks/routing, priority queues, or delayed delivery with low volume.

**Q2. Explain topics, partitions, offsets, brokers, and replicas.**
- **Topic**: logical stream of records.
- **Partition**: ordered, immutable log; the unit of parallelism and ordering.
- **Offset**: monotonically increasing position of a record within a partition.
- **Broker**: a Kafka server hosting partitions.
- **Replica**: copy of a partition on another broker. One is the **leader** (serves reads/writes); others are **followers**.

**Q3. What is the ISR (In-Sync Replica) set?**
Replicas that are caught up with the leader within `replica.lag.time.max.ms`. With `acks=all`, a write is committed only once all ISR members have it. `min.insync.replicas` (commonly 2 with RF=3) defines the minimum ISR size required to accept writes; below that, producers get `NotEnoughReplicasException`.

**Q4. How does a consumer group work?**
Each partition is assigned to exactly one consumer in a group, so parallelism is capped at the number of partitions. Different groups each receive the full stream. Offsets are committed per group to the internal `__consumer_offsets` topic.

**Q5. What triggers a rebalance, and why is it a problem?**
Consumers joining or leaving, missed heartbeats (`session.timeout.ms`), exceeding `max.poll.interval.ms`, or partition count changes. With the eager protocol, all consumers stop processing during the rebalance.
Mitigations:
- **Cooperative sticky assignor** (incremental rebalancing).
- **Static membership** (`group.instance.id`) so rolling restarts don't trigger rebalances.
- Tune `max.poll.records` / `max.poll.interval.ms` so slow processing doesn't get a consumer kicked out.

**Q6. ZooKeeper vs KRaft?**
KRaft (Kafka Raft) replaces ZooKeeper with an internal Raft-based metadata quorum of controllers. Benefits: one system to operate, faster controller failover, and support for millions of partitions. ZooKeeper mode is removed in Kafka 4.0.

---

### 1.2 Producers

**Q7. Explain `acks=0`, `acks=1`, `acks=all`.**
| Setting | Durability | Latency |
|---|---|---|
| `0` | Fire-and-forget; can lose data | Lowest |
| `1` | Leader persisted; lost if leader dies before replication | Medium |
| `all` | All ISR persisted; safe with `min.insync.replicas>=2` | Highest |

**Q8. How does the producer decide which partition a record goes to?**
Explicit partition if given; otherwise `hash(key) % numPartitions`; if there's no key, the **sticky partitioner** fills a batch for one partition before switching (better batching than round-robin). Note that adding partitions changes key-to-partition mapping and breaks per-key ordering for existing keys.

**Q9. What is an idempotent producer?**
`enable.idempotence=true` (default since 3.0). The broker tracks a producer ID + sequence number per partition and drops duplicates caused by retries. Gives exactly-once *per partition, per producer session* and preserves ordering with up to 5 in-flight requests.

**Q10. Which producer settings matter for throughput?**
`batch.size`, `linger.ms` (wait to fill batches), `compression.type` (`lz4`/`zstd`), `buffer.memory`, and `max.in.flight.requests.per.connection`. The trade-off is latency vs throughput.

---

### 1.3 Delivery Semantics & Exactly-Once

**Q11. Explain at-most-once, at-least-once, and exactly-once.**
- **At-most-once**: commit offset *before* processing; a crash loses messages.
- **At-least-once**: commit offset *after* processing; a crash causes reprocessing (duplicates). Most common default.
- **Exactly-once (EOS)**: idempotent producer + transactions, with consumers using `isolation.level=read_committed`.

**Q12. How do Kafka transactions achieve exactly-once in a consume-transform-produce loop?**
The producer with a `transactional.id` calls `beginTransaction()`, produces output records, sends consumer offsets via `sendOffsetsToTransaction()`, then `commitTransaction()`. Outputs and offset commits succeed or fail atomically. A transaction coordinator writes commit/abort markers; `read_committed` consumers skip aborted data. Fencing via `transactional.id` epochs prevents "zombie" producers.

**Q13. EOS only covers Kafka-to-Kafka. How do you get exactly-once into an external sink like Snowflake or a database?**
Make the sink **idempotent** or **transactional**:
- Upsert/MERGE on a natural or business key, or dedupe on `(topic, partition, offset)`.
- Store offsets in the sink in the same transaction as the data, and resume from there on restart.
- Snowflake Kafka connector with Snowpipe Streaming uses channel offset tokens to give exactly-once.

---

### 1.4 Storage & Internals

**Q14. How does Kafka store data on disk?**
Each partition is a directory of **segments** (`.log`, `.index`, `.timeindex`). Only the active segment is written to. Retention deletes whole closed segments. Kafka relies heavily on the OS page cache and `sendfile` zero-copy.

**Q15. Retention: delete vs compact.**
- `cleanup.policy=delete`: drop segments older than `retention.ms` or beyond `retention.bytes`.
- `cleanup.policy=compact`: keep the **latest value per key**; a null value is a **tombstone** that eventually deletes the key. Used for changelogs, CDC state, and `__consumer_offsets`.
- Both can be combined.

**Q16. What is tiered storage?**
Older segments are offloaded to object storage (S3/GCS) while recent data stays on local disk. This decouples retention from broker disk, making long retention cheap and broker recovery/rebalancing faster.

**Q17. What happens when a leader broker fails?**
The controller elects a new leader from the ISR. If `unclean.leader.election.enable=true` and no ISR replica is available, an out-of-sync replica may become leader, which **loses data** but restores availability. Keep it `false` for critical data.

---

### 1.5 Ecosystem

**Q18. What is Schema Registry and why use it?**
A central store for Avro/Protobuf/JSON Schema. Producers register schemas and embed a schema ID in each message; consumers fetch the schema to deserialize. Enforces compatibility modes:
- **BACKWARD** (default): new consumers can read old data, e.g. add fields with defaults or delete fields.
- **FORWARD**: old consumers can read new data.
- **FULL**: both.

**Q19. Kafka Connect: what are source/sink connectors, SMTs, and DLQs?**
A framework for moving data in and out of Kafka without custom code. Source connectors (e.g. Debezium CDC) write to Kafka; sink connectors (e.g. Snowflake, S3) read from it. **Single Message Transforms** do lightweight per-record changes. `errors.tolerance=all` + `errors.deadletterqueue.topic.name` routes bad records to a DLQ instead of failing the task.

**Q20. Kafka Streams vs Flink vs Spark Structured Streaming?**
- **Kafka Streams**: a library embedded in your app; state in RocksDB backed by changelog topics; Kafka-in/Kafka-out only.
- **Flink**: separate cluster; true event-at-a-time; rich event-time/watermark support; large state with checkpoints; many sources/sinks.
- **Spark Structured Streaming**: micro-batch (mostly); great if you're already on Spark/Databricks.

**Q21. KStream vs KTable vs GlobalKTable?**
- **KStream**: every record is an independent event (insert).
- **KTable**: changelog; each record is an upsert for its key (latest value wins).
- **GlobalKTable**: fully replicated to every instance; enables non-co-partitioned joins for small reference data.

**Q22. Explain event time, processing time, windows, and late data.**
Windows: **tumbling** (fixed, non-overlapping), **hopping** (fixed, overlapping), **sliding**, **session** (gap-based). Use event time for correctness; watermarks/grace periods determine how long to wait for out-of-order events. Late events beyond the grace period are dropped or sent to a side output.

---

### 1.6 Operations & Troubleshooting

**Q23. Consumer lag keeps growing. How do you debug it?**
1. Measure lag per partition (`kafka-consumer-groups --describe`, Burrow, or metrics).
2. Is lag on **all partitions** (throughput problem) or **a few** (hot partition / key skew, or a stuck consumer)?
3. Check for frequent rebalances, slow downstream calls, GC pauses, or poison messages causing retry loops.
4. Fixes: add consumers (up to partition count), add partitions, batch downstream writes, process asynchronously, fix key skew (salting), and move poison messages to a DLQ.

**Q24. How do you choose the number of partitions?**
`partitions ≈ max(target_throughput / producer_throughput_per_partition, target_throughput / consumer_throughput_per_partition)`, plus headroom for growth. Considerations: you can add partitions later but can't reduce them, and adding them reshuffles keys. Too many partitions increases metadata, open files, and failover time.

**Q25. How do you handle a poison pill message?**
Catch deserialization/processing errors, publish the record plus error metadata to a **DLQ** topic, commit the offset, and continue. Alert on DLQ volume and build a replay path.

**Q26. How do you secure Kafka?**
TLS for encryption in transit; SASL (SCRAM, OAUTHBEARER, Kerberos) or mTLS for authentication; ACLs or RBAC for authorization; encryption at rest at the disk/volume level; audit logs.

**Q27. How do you replicate across data centers/regions?**
MirrorMaker 2 (Connect-based, translates offsets via checkpoints), Confluent Cluster Linking, or a managed service's built-in replication. Discuss active-passive vs active-active, topic naming to avoid loops, and consumer offset translation on failover.

---

## Part 2: Snowflake

### 2.1 Architecture

**Q28. Describe Snowflake's architecture.**
Three independently scaling layers:
1. **Storage**: compressed, columnar **micro-partitions** in cloud object storage.
2. **Compute**: **virtual warehouses** (MPP clusters) that read shared storage; many warehouses can run on the same data without contention.
3. **Cloud services**: metadata, query optimization, auth, transactions, result cache.

Key benefit: storage and compute scale and are billed separately.

**Q29. What are micro-partitions?**
Immutable files of ~50–500 MB uncompressed, stored columnar. Snowflake keeps metadata per partition (min/max per column, distinct counts, null counts). The optimizer uses this metadata for **partition pruning**. Data is partitioned automatically by insertion order; there's no user-defined partitioning.

**Q30. What is clustering, and when do you define a clustering key?**
Clustering describes how well co-located similar values are across micro-partitions (measured by clustering depth/overlap). Define a clustering key only when:
- The table is large (multi-TB).
- Queries filter on predictable columns (e.g. `event_date`, `tenant_id`).
- Query profiles show poor pruning.

Automatic Clustering then reclusters in the background and **costs credits**. Avoid high-cardinality keys like raw timestamps; use `TO_DATE(ts)` instead. Check with `SYSTEM$CLUSTERING_INFORMATION`.

**Q31. Explain Snowflake's three caches.**
- **Result cache** (cloud services, 24h): identical query on unchanged data returns instantly with no warehouse.
- **Local disk/warehouse cache**: SSD cache of remote data on the warehouse; lost when the warehouse suspends.
- **Metadata cache**: answers `COUNT(*)`, `MIN`/`MAX` from metadata without scanning.

---

### 2.2 Warehouses & Performance

**Q32. Scale up vs scale out?**
- **Scale up** (larger size: XS→S→M…): helps **complex individual queries** and spilling; each size doubles compute and credits.
- **Scale out** (multi-cluster warehouse): helps **concurrency**/queuing with many simultaneous users. Scaling policies: Standard (favors performance) vs Economy (favors cost).

**Q33. A query is slow. How do you investigate?**
Open the **Query Profile** and look for:
- **Poor pruning**: partitions scanned ≈ total, so add filters, a clustering key, or search optimization.
- **Spilling** to local/remote disk: warehouse too small, so scale up or reduce data earlier.
- **Exploding joins**: row count grows past a join, caused by missing join keys or duplicates.
- **Queuing**: concurrency problem, so use multi-cluster or separate warehouses.
- Large `ORDER BY`/`DISTINCT`, UDF overhead, or non-sargable predicates like `WHERE TO_CHAR(date)=...`.

**Q34. Search Optimization Service vs clustering vs materialized views?**
- **Search Optimization**: point lookups/selective filters on high-cardinality columns (IDs, emails), substring, and VARIANT field lookups.
- **Clustering**: range filters on a few known columns over large tables.
- **Materialized views**: precomputed results of a single-table query; auto-maintained (costs credits); good for repeated aggregations.
- **Query Acceleration Service**: offloads parts of outlier scan-heavy queries to shared compute.

**Q35. How do you control Snowflake cost?**
- Aggressive `AUTO_SUSPEND` (60s) and `AUTO_RESUME`.
- Right-size warehouses; separate warehouses per workload (ELT, BI, data science) for isolation and chargeback.
- **Resource monitors** with credit quotas and suspend actions.
- Avoid unnecessary Automatic Clustering, materialized views, and search optimization.
- Use transient tables for staging (no Fail-safe), and reduce Time Travel retention on churn-heavy tables.
- Monitor with `SNOWFLAKE.ACCOUNT_USAGE` (`WAREHOUSE_METERING_HISTORY`, `QUERY_HISTORY`).

---

### 2.3 Data Loading & Ingestion

**Q36. What are the options for loading data into Snowflake?**
| Method | Latency | Use case |
|---|---|---|
| `COPY INTO` from a stage | Batch (minutes–hours) | Scheduled bulk loads |
| **Snowpipe** (file-based, event-triggered) | ~1 min | Continuous file arrival in S3/GCS/Azure |
| **Snowpipe Streaming** (row-based API) | Seconds | Kafka, low-latency rows without files |
| Kafka connector | Seconds–minutes | Kafka topics into tables |
| External tables / Iceberg tables | N/A (query in place) | Lakehouse, open formats |

**Q37. Best practices for `COPY INTO`?**
- Files of ~100–250 MB compressed for parallelism.
- Load metadata prevents reloading the same file for 64 days (idempotent loads); `FORCE=TRUE` overrides.
- `ON_ERROR` (`CONTINUE`, `SKIP_FILE`, `ABORT_STATEMENT`) and `VALIDATION_MODE` for dry runs.
- Use named file formats and stages; `MATCH_BY_COLUMN_NAME` for Parquet/Avro.

**Q38. Internal vs external stages?**
- **Internal**: Snowflake-managed storage (user `@~`, table `@%t`, named `@s`).
- **External**: your S3/GCS/Azure bucket, accessed via a **storage integration** (IAM role-based, no keys in SQL).

**Q39. How do you handle semi-structured data?**
Load JSON/Avro/Parquet into a `VARIANT` column. Query with `col:field.subfield::type` and `LATERAL FLATTEN` for arrays. Snowflake auto-columnarizes common VARIANT paths for performance. Best practice: land raw in VARIANT, then extract frequently used fields into typed columns in downstream models.

---

### 2.4 Transformations & CDC

**Q40. What are Streams and Tasks?**
- **Stream**: a change-tracking object on a table/view that exposes inserts/updates/deletes since the last consumption, via `METADATA$ACTION`, `METADATA$ISUPDATE`, `METADATA$ROW_ID`. The offset advances only when the stream is consumed inside a committed DML transaction.
- **Task**: scheduled or triggered SQL/procedure execution; can form DAGs; serverless or warehouse-backed. Use `WHEN SYSTEM$STREAM_HAS_DATA('s')` to skip empty runs.

**Q41. Dynamic Tables vs Streams+Tasks?**
Dynamic Tables are **declarative**: you write the `SELECT` and a `TARGET_LAG`, and Snowflake handles incremental refresh and dependency ordering. Prefer them for most pipelines. Use Streams+Tasks when you need procedural logic, custom merge semantics, or side effects.

**Q42. Write a MERGE to apply CDC changes with deduplication.**

```sql
MERGE INTO dim_customer t
USING (
    SELECT *
    FROM raw_customer_changes
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY customer_id ORDER BY event_ts DESC, kafka_offset DESC
    ) = 1
) s
ON t.customer_id = s.customer_id
WHEN MATCHED AND s.op = 'D' THEN DELETE
WHEN MATCHED AND s.event_ts > t.event_ts THEN UPDATE SET
    t.name = s.name, t.email = s.email, t.event_ts = s.event_ts
WHEN NOT MATCHED AND s.op <> 'D' THEN INSERT (customer_id, name, email, event_ts)
    VALUES (s.customer_id, s.name, s.email, s.event_ts);
```

Key points: dedupe the source first (MERGE errors on nondeterministic multi-matches), guard against out-of-order events with `event_ts > t.event_ts`, and handle deletes.

**Q43. How do you implement SCD Type 2 in Snowflake?**
Use a stream on the staging table. In one transaction: (1) `UPDATE` current rows whose tracked attributes changed, setting `valid_to = change_ts` and `is_current = FALSE`; (2) `INSERT` new versions with `valid_from = change_ts`, `valid_to = NULL`, `is_current = TRUE`. Alternatively use a MERGE with a union trick, or dbt snapshots. Hash the tracked columns (`HASH()`/`MD5`) to detect changes cheaply.

---

### 2.5 Data Protection & Sharing

**Q44. Time Travel vs Fail-safe?**
- **Time Travel**: user-accessible historical data for 0–90 days (1 by default; up to 90 on Enterprise). Supports `AT`/`BEFORE` queries, `UNDROP`, and cloning from a point in time.
- **Fail-safe**: 7 additional days, **Snowflake-support recovery only**; permanent tables only.
- **Transient/temporary tables**: no Fail-safe, Time Travel 0–1 day, so cheaper storage for staging.

**Q45. What is zero-copy cloning?**
`CREATE TABLE/SCHEMA/DATABASE ... CLONE src` copies metadata only, pointing to the same micro-partitions. Storage is incurred only for subsequently changed data. Great for dev/test environments, backups before risky changes, and CI.

**Q46. How does Secure Data Sharing work?**
The provider grants read access to objects via a **share**; consumers query live data with **no copying** and use their own compute. Reader accounts serve non-Snowflake consumers. Cross-region/cloud sharing requires replication. The Marketplace builds on this.

**Q47. Explain Snowflake's access control model.**
Role-based (RBAC) with role hierarchies plus discretionary ownership. System roles: `ACCOUNTADMIN`, `SECURITYADMIN`, `USERADMIN`, `SYSADMIN`, `PUBLIC`. Best practice is **access roles** (privileges on objects) granted to **functional roles** (granted to users). Use future grants, and never use ACCOUNTADMIN for daily work.

**Q48. How do you protect PII?**
- **Dynamic Data Masking** policies (masked based on `CURRENT_ROLE()`).
- **Row Access Policies** for row-level security (e.g. by tenant/region).
- **Tag-based masking** to apply policies automatically to tagged columns.
- External tokenization, Secure Views, column-level lineage/classification, and network policies + private link.

---

## Part 3: Kafka + Snowflake Integration

**Q49. How does the Snowflake Kafka connector work?**
A Kafka Connect sink. Two ingestion modes:
- **Snowpipe (file-based)**: the connector buffers records, writes files to an internal stage, and calls Snowpipe. Latency ~1 minute; costs per file, so many small files are expensive.
- **Snowpipe Streaming** (recommended): writes rows directly through channels (one per partition), with lower latency and cost and **exactly-once** via offset tokens stored in Snowflake.

By default it lands two VARIANT columns, `RECORD_METADATA` (topic, partition, offset, timestamp, key) and `RECORD_CONTENT`, or schematized columns with schema evolution enabled.

**Q50. Key tuning knobs for the connector?**
`buffer.flush.time`, `buffer.count.records`, `buffer.size.bytes` (latency vs file size/cost), `tasks.max` (≤ partitions), `snowflake.ingestion.method=SNOWPIPE_STREAMING`, `snowflake.enable.schematization`, and DLQ settings for bad records.

**Q51. How do you handle duplicates landing in Snowflake from Kafka?**
Even with at-least-once upstream, make the warehouse layer idempotent: keep `RECORD_METADATA:partition` and `:offset` (or a business event ID), and dedupe with `QUALIFY ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY ...) = 1` in the transform layer or in MERGE.

**Q52. How do you handle schema evolution end to end?**
Schema Registry enforces compatibility at the producer. The connector with schematization adds new columns automatically (`ENABLE_SCHEMA_EVOLUTION = TRUE` on the table), or you land into VARIANT and evolve downstream models explicitly. Breaking changes go to a new topic version (`orders.v2`) with a migration plan.

---

## Part 4: System Design Scenarios

For each, structure your answer as: **requirements → high-level architecture → data model → delivery guarantees → scaling → failure handling → monitoring → cost**.

### Design 1: Real-time clickstream analytics
**Prompt:** 500K events/sec from web/mobile; dashboards with <1 min freshness; 2-year history.

- **Ingestion**: SDKs → collector API → Kafka `clickstream.raw` (keyed by `session_id` or `user_id` for ordering; ~100+ partitions sized from throughput; RF=3, `acks=all`, `min.insync.replicas=2`, `zstd` compression; Avro + Schema Registry).
- **Stream processing**: Flink or Kafka Streams for bot filtering, enrichment (GlobalKTable/broadcast state for geo/device lookups), sessionization (session windows), and writing to `clickstream.enriched`.
- **Warehouse**: Snowflake Kafka connector (Snowpipe Streaming) into a raw table → Dynamic Tables for sessions and hourly aggregates (`TARGET_LAG = '1 minute'`) → BI warehouse with multi-cluster for dashboard concurrency.
- **Storage/perf**: cluster on `event_date` (+ maybe `tenant_id`); archive raw to S3/Iceberg for cheap long-term retention.
- **Failure handling**: DLQ for malformed events; replay from Kafka retention (e.g. 7 days) or the S3 archive; idempotent dedupe on `event_id`.
- **Monitoring**: consumer lag, end-to-end freshness (`max(event_ts)` vs now), DLQ rate, Snowflake credit usage.

### Design 2: CDC from OLTP (Postgres/MySQL) to Snowflake
**Prompt:** Replicate 200 tables from production DBs with <5 min latency, including deletes and schema changes.

- **Capture**: Debezium source connector reading the WAL/binlog (no load on tables); one topic per table, keyed by primary key; compacted topics for current state plus a long enough retention for replay. Initial snapshot followed by streaming.
- **Land**: Snowflake connector into raw append-only change tables (op, before, after, source LSN/ts).
- **Apply**: Streams + Tasks or Dynamic Tables to MERGE into current-state tables, deduping by PK and ordering by LSN; deletes as hard or soft deletes (`is_deleted`). Optional SCD2 history tables.
- **Correctness**: ordering is guaranteed per key because of the PK-keyed partitioning; use LSN rather than wall-clock time to resolve conflicts; run periodic reconciliation (row counts/checksums vs source).
- **Schema changes**: Schema Registry + compatible evolution; alert on breaking DDL.
- **Ops**: monitor replication slot lag (an unconsumed Postgres slot can fill the source disk!), connector task status, and freshness per table.

### Design 3: Exactly-once financial transactions pipeline
**Prompt:** Payment events must never be lost or double-counted in reporting.

- Idempotent producers + `acks=all`, RF=3, `min.insync.replicas=2`, `unclean.leader.election.enable=false`.
- Kafka transactions for any Kafka-to-Kafka processing; consumers use `read_committed`.
- Every event carries a globally unique `transaction_id`; Snowflake MERGE on that ID so the sink is idempotent.
- Snowpipe Streaming for exactly-once ingestion via offset tokens.
- Daily reconciliation against the source ledger; alert on mismatches; immutable raw layer + Time Travel for audit.
- Masking policies and row access policies on PII/PCI fields; tokenize card numbers before they reach Kafka.

### Design 4: Multi-tenant SaaS analytics platform
**Prompt:** 5,000 customers, each sees only their own data; some large tenants dominate volume.

- Kafka: key by `tenant_id` but watch for **hot partitions** from large tenants; salt the key (`tenant_id + hash(entity_id) % N`) for large tenants, or give them dedicated topics.
- Snowflake: a shared schema with `tenant_id` on every table + **Row Access Policies** (simpler at this scale) vs a database per tenant (stronger isolation, harder to manage). Cluster on `tenant_id, event_date`.
- Separate warehouses for ingestion vs tenant-facing queries; resource monitors; per-tenant usage chargeback from `QUERY_HISTORY` with query tags.
- Secure Data Sharing for tenants who want raw data in their own Snowflake accounts.

### Design 5: Lambda vs Kappa architecture
**Question:** Which would you choose for a new platform?

- **Lambda**: separate batch and speed layers; accurate but two codebases that drift.
- **Kappa**: everything is a stream; reprocessing = replay the log with a new job version. Simpler, made practical by long retention / tiered storage.
- Modern answer: mostly Kappa-style with Kafka as the source of truth, plus a lakehouse (Iceberg) / Snowflake for history, with Dynamic Tables or incremental dbt models instead of a separate batch codebase.

---

## Part 5: Rapid-Fire Questions

1. **Can you decrease Kafka partitions?** No; create a new topic and migrate.
2. **Max consumers usefully active in a group?** Equal to the partition count; extras sit idle.
3. **Where are consumer offsets stored?** The `__consumer_offsets` compacted topic.
4. **What does `auto.offset.reset` do?** Where to start when no committed offset exists: `earliest`, `latest`, or `none`.
5. **Why might ordering break with retries?** Without idempotence and `max.in.flight > 1`, a retried batch can land after a later one; idempotence fixes this.
6. **Default max message size?** ~1 MB (`message.max.bytes`); for large payloads, store in S3 and send a pointer (claim-check pattern).
7. **Snowflake: does `COUNT(*)` on a table use a warehouse?** No; it's served from metadata.
8. **Snowflake: how long is the result cache valid?** 24 hours, renewed on reuse up to 31 days, invalidated if the underlying data changes.
9. **Snowflake: are there indexes?** No traditional indexes; use pruning, clustering, and search optimization. Hybrid tables (Unistore) do support indexes.
10. **Snowflake: `TRANSIENT` vs `TEMPORARY` tables?** Transient persists across sessions without Fail-safe; temporary lives only for the session.
11. **Snowflake: how is billing calculated?** Compute in credits per second (60s minimum on resume) per warehouse size, plus storage per TB/month, plus serverless features and cloud services above 10% of daily compute.
12. **Snowflake: `UNION` vs `UNION ALL` cost?** `UNION` dedupes (extra sort/hash); prefer `UNION ALL` when duplicates are impossible or acceptable.
13. **Snowflake: what is `QUALIFY`?** A filter on window function results, like `HAVING` for windows.
14. **Snowflake: Iceberg tables?** Tables in open Apache Iceberg format on your object storage, managed by Snowflake or an external catalog, so other engines (Spark, Trino) can read the same data.

---

## Part 6: Hands-On SQL Practice (Snowflake)

**P1. Latest record per key from a Kafka-landed VARIANT table.**

```sql
SELECT
    record_content:order_id::STRING       AS order_id,
    record_content:status::STRING         AS status,
    record_content:amount::NUMBER(12,2)   AS amount,
    record_metadata:offset::NUMBER        AS kafka_offset
FROM raw.orders_kafka
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY record_content:order_id
    ORDER BY record_content:updated_at::TIMESTAMP_NTZ DESC,
             record_metadata:offset::NUMBER DESC
) = 1;
```

**P2. Flatten a nested JSON array of line items.**

```sql
SELECT
    o.record_content:order_id::STRING AS order_id,
    li.value:sku::STRING              AS sku,
    li.value:qty::INT                 AS qty
FROM raw.orders_kafka o,
     LATERAL FLATTEN(input => o.record_content:line_items) li;
```

**P3. Sessionize events with a 30-minute inactivity gap.**

```sql
WITH flagged AS (
    SELECT
        user_id, event_ts,
        IFF(DATEDIFF('minute',
                     LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts),
                     event_ts) > 30
            OR LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts) IS NULL,
            1, 0) AS is_new_session
    FROM events
)
SELECT
    user_id, event_ts,
    SUM(is_new_session) OVER (PARTITION BY user_id ORDER BY event_ts
                              ROWS UNBOUNDED PRECEDING) AS session_num
FROM flagged;
```

**P4. Incremental pipeline with a Stream and Task.**

```sql
CREATE OR REPLACE STREAM raw.orders_stream ON TABLE raw.orders_kafka APPEND_ONLY = TRUE;

CREATE OR REPLACE TASK core.load_orders
    WAREHOUSE = etl_wh
    SCHEDULE = '1 MINUTE'
    WHEN SYSTEM$STREAM_HAS_DATA('raw.orders_stream')
AS
MERGE INTO core.orders t
USING (
    SELECT record_content:order_id::STRING AS order_id,
           record_content:status::STRING   AS status,
           record_content:updated_at::TIMESTAMP_NTZ AS updated_at
    FROM raw.orders_stream
    QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1
) s
ON t.order_id = s.order_id
WHEN MATCHED AND s.updated_at > t.updated_at THEN
    UPDATE SET t.status = s.status, t.updated_at = s.updated_at
WHEN NOT MATCHED THEN
    INSERT (order_id, status, updated_at) VALUES (s.order_id, s.status, s.updated_at);

ALTER TASK core.load_orders RESUME;
```

**P5. The same pipeline as a Dynamic Table.**

```sql
CREATE OR REPLACE DYNAMIC TABLE core.orders_current
    TARGET_LAG = '1 minute'
    WAREHOUSE = etl_wh
AS
SELECT record_content:order_id::STRING          AS order_id,
       record_content:status::STRING            AS status,
       record_content:updated_at::TIMESTAMP_NTZ AS updated_at
FROM raw.orders_kafka
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY record_content:order_id
    ORDER BY record_content:updated_at::TIMESTAMP_NTZ DESC
) = 1;
```

---

## Interview Tips

- **Always state the trade-off**: latency vs cost, consistency vs availability, simplicity vs flexibility.
- **Talk about failure modes unprompted**: broker loss, consumer crash mid-batch, poison messages, schema breaks, late data, backfills.
- **Make sinks idempotent**: it's the most reliable answer to "how do you avoid duplicates?"
- **Quantify**: estimate events/sec, bytes/event, partitions needed, storage per day, and warehouse size.
- **Mention observability**: lag, freshness SLAs, data quality checks (row counts, nulls, uniqueness), and cost dashboards.
