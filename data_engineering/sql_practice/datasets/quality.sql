-- Raw landing tables with no constraints enforced, used for data quality checks.
-- Traps: duplicate primary keys, NULL emails, orphan foreign keys, NULL foreign keys
-- (not the same thing as orphans), and negative amounts.

CREATE TABLE dq_customers (
    customer_id INTEGER,
    email       VARCHAR,
    country     VARCHAR
);

INSERT INTO dq_customers VALUES
    (1, 'a@x.com',  'US'),
    (2, NULL,       'US'),
    (3, 'c@x.com',  NULL),
    (3, 'c2@x.com', 'UK'),
    (4, 'd@x.com',  'IN'),
    (5, NULL,       'IN'),
    (5, NULL,       'IN');

CREATE TABLE dq_orders (
    order_id    INTEGER,
    customer_id INTEGER,
    amount      DECIMAL(10, 2)
);

INSERT INTO dq_orders VALUES
    (100, 1,    50),
    (101, 2,    20),
    (102, 9,    30),
    (103, NULL, 10),
    (104, 4,    -5),
    (105, 8,    15);
