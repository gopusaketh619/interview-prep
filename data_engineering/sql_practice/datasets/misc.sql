-- Small classic interview tables (LeetCode/DataLemur style), one per pattern.

-- Bus queue: weight limit 1000, boarding by turn.
CREATE TABLE queue (
    person_id   INTEGER PRIMARY KEY,
    person_name VARCHAR NOT NULL,
    weight      INTEGER NOT NULL,
    turn        INTEGER NOT NULL
);
INSERT INTO queue VALUES
    (5, 'Alice', 250, 1), (4, 'Bob', 175, 5), (3, 'Alex', 350, 2),
    (6, 'John Cena', 400, 3), (1, 'Winston', 500, 6), (2, 'Marie', 200, 4);

-- Weather readings with a missing day (2025-01-04).
CREATE TABLE weather (
    id          INTEGER PRIMARY KEY,
    record_date DATE NOT NULL,
    temperature INTEGER NOT NULL
);
INSERT INTO weather VALUES
    (1, '2025-01-01', 10), (2, '2025-01-02', 25), (3, '2025-01-03', 20),
    (4, '2025-01-05', 30), (5, '2025-01-06', 28), (6, '2025-01-07', 35);

-- Number log with a gap in ids (7 is missing).
CREATE TABLE logs (
    id  INTEGER PRIMARY KEY,
    num INTEGER NOT NULL
);
INSERT INTO logs VALUES
    (1, 1), (2, 1), (3, 1), (4, 2), (5, 1), (6, 2), (8, 2), (9, 2), (10, 3), (11, 3);

-- Stadium traffic.
CREATE TABLE stadium (
    id         INTEGER PRIMARY KEY,
    visit_date DATE NOT NULL,
    people     INTEGER NOT NULL
);
INSERT INTO stadium VALUES
    (1, '2017-01-01', 10), (2, '2017-01-02', 109), (3, '2017-01-03', 150),
    (4, '2017-01-04', 99), (5, '2017-01-05', 145), (6, '2017-01-06', 1455),
    (7, '2017-01-07', 199), (8, '2017-01-09', 188), (9, '2017-01-10', 50),
    (10, '2017-01-11', 120), (11, '2017-01-12', 130);

-- Log ids with gaps.
CREATE TABLE log_ids (log_id INTEGER PRIMARY KEY);
INSERT INTO log_ids VALUES (1), (2), (3), (7), (8), (10);

-- Daily pipeline run outcomes. 2025-01-06 has no run at all.
CREATE TABLE task_runs (
    run_date DATE PRIMARY KEY,
    state    VARCHAR NOT NULL   -- 'succeeded' | 'failed'
);
INSERT INTO task_runs VALUES
    ('2025-01-01', 'succeeded'), ('2025-01-02', 'succeeded'), ('2025-01-03', 'failed'),
    ('2025-01-04', 'failed'), ('2025-01-05', 'succeeded'), ('2025-01-07', 'succeeded'),
    ('2025-01-08', 'failed'), ('2025-01-09', 'succeeded'), ('2025-01-10', 'succeeded');

-- Daily revenue with missing days (03, 06, 07).
CREATE TABLE daily_sales (
    sale_date DATE PRIMARY KEY,
    revenue   INTEGER NOT NULL
);
INSERT INTO daily_sales VALUES
    ('2025-01-01', 100), ('2025-01-02', 200), ('2025-01-04', 400), ('2025-01-05', 100),
    ('2025-01-08', 300), ('2025-01-09', 200), ('2025-01-10', 100);

-- Game activity (LeetCode 550 style).
CREATE TABLE activity (
    player_id    INTEGER NOT NULL,
    device_id    INTEGER NOT NULL,
    event_date   DATE NOT NULL,
    games_played INTEGER NOT NULL
);
INSERT INTO activity VALUES
    (1, 2, '2025-03-01', 5), (1, 2, '2025-03-02', 6),
    (2, 3, '2025-06-25', 1),
    (3, 1, '2025-03-02', 0), (3, 4, '2025-07-03', 5),
    (4, 1, '2025-01-10', 2), (4, 1, '2025-01-12', 3),
    (5, 2, '2025-02-28', 1), (5, 2, '2025-03-01', 1);

-- App sessions. end_ts is exclusive: a session ending at 11:00 is not live at 11:00.
CREATE TABLE user_sessions (
    session_id INTEGER PRIMARY KEY,
    user_id    INTEGER NOT NULL,
    start_ts   TIMESTAMP NOT NULL,
    end_ts     TIMESTAMP NOT NULL
);
INSERT INTO user_sessions VALUES
    (1, 1, '2025-05-01 10:00:00', '2025-05-01 11:00:00'),
    (2, 2, '2025-05-01 10:30:00', '2025-05-01 12:00:00'),
    (3, 3, '2025-05-01 11:00:00', '2025-05-01 11:30:00'),
    (4, 4, '2025-05-01 10:45:00', '2025-05-01 11:15:00'),
    (5, 5, '2025-05-01 12:00:00', '2025-05-01 12:30:00'),
    (6, 6, '2025-05-01 09:00:00', '2025-05-01 09:30:00');

-- Department revenue by month (LeetCode 1179 style).
CREATE TABLE dept_revenue (
    id      INTEGER NOT NULL,
    revenue INTEGER NOT NULL,
    month   VARCHAR NOT NULL
);
INSERT INTO dept_revenue VALUES
    (1, 8000, 'Jan'), (2, 9000, 'Jan'), (3, 10000, 'Feb'), (1, 7000, 'Feb'),
    (1, 6000, 'Mar'), (2, 4000, 'Apr'), (3, 2500, 'Apr');

-- Wide store price table (LeetCode 1795 style). NULL means not sold at that store.
CREATE TABLE products_wide (
    product_id INTEGER PRIMARY KEY,
    store1     INTEGER,
    store2     INTEGER,
    store3     INTEGER
);
INSERT INTO products_wide VALUES (0, 95, 100, 105), (1, 70, NULL, 80), (2, NULL, NULL, 60);

-- Products sold per day (LeetCode 1484 style), with a duplicate sale.
CREATE TABLE sales_log (
    sell_date DATE NOT NULL,
    product   VARCHAR NOT NULL
);
INSERT INTO sales_log VALUES
    ('2020-05-30', 'Headphone'), ('2020-06-01', 'Pencil'), ('2020-06-02', 'Mask'),
    ('2020-05-30', 'Basketball'), ('2020-06-01', 'Bible'), ('2020-06-02', 'Mask'),
    ('2020-05-30', 'T-Shirt');

-- Bill of materials. Only base parts have a unit_cost; assemblies are built from children.
CREATE TABLE parts (
    part_id   INTEGER PRIMARY KEY,
    name      VARCHAR NOT NULL,
    unit_cost DECIMAL(10, 2)
);
INSERT INTO parts VALUES
    (1, 'Bike', NULL), (2, 'Wheel', NULL), (3, 'Frame', 120), (4, 'Spoke', 0.5),
    (5, 'Rim', 15), (6, 'Tire', 20), (7, 'Scooter', NULL), (8, 'Deck', 40);

CREATE TABLE bom (
    parent_id INTEGER NOT NULL,
    child_id  INTEGER NOT NULL,
    qty       INTEGER NOT NULL
);
INSERT INTO bom VALUES
    (1, 2, 2), (1, 3, 1), (2, 4, 32), (2, 5, 1), (2, 6, 1), (7, 2, 2), (7, 8, 1);

-- Meeting room bookings. end_ts is exclusive; a meeting that starts exactly when
-- another ends should be merged with it.
CREATE TABLE meetings (
    room     VARCHAR NOT NULL,
    start_ts TIMESTAMP NOT NULL,
    end_ts   TIMESTAMP NOT NULL
);
INSERT INTO meetings VALUES
    ('A', '2025-05-01 09:00:00', '2025-05-01 10:00:00'),
    ('A', '2025-05-01 09:30:00', '2025-05-01 10:30:00'),
    ('A', '2025-05-01 10:30:00', '2025-05-01 11:00:00'),
    ('A', '2025-05-01 12:00:00', '2025-05-01 15:00:00'),
    ('A', '2025-05-01 12:30:00', '2025-05-01 13:00:00'),
    ('A', '2025-05-01 14:00:00', '2025-05-01 14:30:00'),
    ('B', '2025-05-01 09:00:00', '2025-05-01 09:15:00'),
    ('B', '2025-05-01 09:20:00', '2025-05-01 09:40:00');
