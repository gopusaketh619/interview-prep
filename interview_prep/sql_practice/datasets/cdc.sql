-- Change data capture domain: an append-only update log, an I/U/D change log, and daily snapshots.
-- Traps: same updated_at with different ingest times, a late-arriving older record, exact duplicate
-- rows, a change log stored out of LSN order, delete-then-reinsert, and a tier that changes and
-- later changes back (A -> B -> A must be three SCD2 versions, not two).

CREATE TABLE customer_updates (
    customer_id INTEGER NOT NULL,
    email       VARCHAR NOT NULL,
    updated_at  TIMESTAMP NOT NULL,
    ingested_at TIMESTAMP NOT NULL
);

INSERT INTO customer_updates VALUES
    (1, 'a1@x.com', '2025-01-01 10:00:00', '2025-01-01 10:05:00'),
    (1, 'a2@x.com', '2025-01-03 09:00:00', '2025-01-03 09:01:00'),
    (1, 'a3@x.com', '2025-01-03 09:00:00', '2025-01-03 09:30:00'),
    (2, 'b1@x.com', '2025-01-02 08:00:00', '2025-01-02 08:01:00'),
    (2, 'b0@x.com', '2025-01-01 08:00:00', '2025-01-04 00:00:00'),
    (3, 'c1@x.com', '2025-01-05 12:00:00', '2025-01-05 12:00:00'),
    (3, 'c1@x.com', '2025-01-05 12:00:00', '2025-01-05 12:00:00');

CREATE TABLE cdc_log (
    lsn         INTEGER PRIMARY KEY,
    op          VARCHAR NOT NULL,   -- 'I' insert | 'U' update (full row image) | 'D' delete
    customer_id INTEGER NOT NULL,
    email       VARCHAR,
    tier        VARCHAR,
    op_ts       TIMESTAMP NOT NULL
);

INSERT INTO cdc_log VALUES
    (6,  'U', 12, 'x12new@a.com', 'bronze', '2025-01-01 10:05:00'),
    (1,  'I', 10, 'x10@a.com',    'bronze', '2025-01-01 10:00:00'),
    (3,  'U', 10, 'x10@a.com',    'gold',   '2025-01-01 10:02:00'),
    (2,  'I', 11, 'x11@a.com',    'silver', '2025-01-01 10:01:00'),
    (10, 'U', 10, 'x10b@a.com',   'gold',   '2025-01-01 10:09:00'),
    (5,  'D', 11, NULL,           NULL,     '2025-01-01 10:04:00'),
    (4,  'I', 12, 'x12@a.com',    'bronze', '2025-01-01 10:03:00'),
    (8,  'D', 13, NULL,           NULL,     '2025-01-01 10:07:00'),
    (7,  'I', 13, 'x13@a.com',    'silver', '2025-01-01 10:06:00'),
    (9,  'I', 13, 'x13b@a.com',   'gold',   '2025-01-01 10:08:00');

CREATE TABLE customer_snapshots (
    snapshot_date DATE NOT NULL,
    customer_id   INTEGER NOT NULL,
    tier          VARCHAR NOT NULL
);

INSERT INTO customer_snapshots VALUES
    ('2025-01-01', 1, 'bronze'), ('2025-01-02', 1, 'bronze'), ('2025-01-03', 1, 'silver'),
    ('2025-01-04', 1, 'silver'), ('2025-01-05', 1, 'bronze'), ('2025-01-06', 1, 'bronze'),
    ('2025-01-01', 2, 'gold'),   ('2025-01-02', 2, 'gold'),   ('2025-01-03', 2, 'gold'),
    ('2025-01-04', 2, 'gold'),   ('2025-01-05', 2, 'gold'),   ('2025-01-06', 2, 'gold'),
    ('2025-01-03', 3, 'silver'), ('2025-01-04', 3, 'silver'), ('2025-01-05', 3, 'silver'),
    ('2025-01-06', 3, 'gold');
