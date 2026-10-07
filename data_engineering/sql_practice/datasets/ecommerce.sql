-- E-commerce domain: customers, products, orders, order_items, card transactions,
-- yearly product spend, and multi-currency orders with FX rates.
-- Traps: a guest order with NULL customer_id, duplicate product lines inside one order,
-- discounted unit prices, customers who never order, NULL country, same-day transaction ties,
-- a missing year in product_spend, an FX rate that takes effect exactly at an order timestamp,
-- and an order placed before its currency has any rate.

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name        VARCHAR NOT NULL,
    country     VARCHAR,
    signup_date DATE NOT NULL
);

INSERT INTO customers VALUES
    (1, 'Ana',  'US', '2024-11-03'),
    (2, 'Ben',  'US', '2024-12-15'),
    (3, 'Chen', 'CN', '2025-01-02'),
    (4, 'Dara', 'IN', '2025-01-20'),
    (5, 'Eli',  'US', '2025-02-05'),
    (6, 'Fay',  'UK', '2025-02-14'),
    (7, 'Gus',  'UK', '2025-03-01'),
    (8, 'Hana', 'JP', '2025-03-10');

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name       VARCHAR NOT NULL,
    category   VARCHAR NOT NULL,
    price      DECIMAL(10, 2) NOT NULL
);

INSERT INTO products VALUES
    (101, 'Laptop',     'Electronics', 1200),
    (102, 'Phone',      'Electronics',  800),
    (103, 'Headphones', 'Electronics',  150),
    (104, 'Desk',       'Furniture',    300),
    (105, 'Chair',      'Furniture',    150),
    (106, 'Lamp',       'Furniture',     40),
    (107, 'Novel',      'Books',         20),
    (108, 'Cookbook',   'Books',         35);

CREATE TABLE orders (
    order_id                INTEGER PRIMARY KEY,
    customer_id             INTEGER,
    order_date              DATE NOT NULL,
    preferred_delivery_date DATE NOT NULL
);

INSERT INTO orders VALUES
    (1,  1,    '2025-01-05', '2025-01-05'),
    (2,  1,    '2025-01-20', '2025-01-25'),
    (3,  2,    '2025-01-10', '2025-01-12'),
    (4,  3,    '2025-01-15', '2025-01-15'),
    (5,  1,    '2025-02-02', '2025-02-02'),
    (6,  2,    '2025-02-03', '2025-02-03'),
    (7,  4,    '2025-02-10', '2025-02-14'),
    (8,  5,    '2025-02-10', '2025-02-10'),
    (9,  3,    '2025-02-25', '2025-02-28'),
    (10, 4,    '2025-03-05', '2025-03-05'),
    (11, 5,    '2025-03-15', '2025-03-20'),
    (12, 8,    '2025-03-20', '2025-03-20'),
    (13, NULL, '2025-03-22', '2025-03-22'),
    (14, 1,    '2025-03-28', '2025-03-30'),
    (15, 2,    '2025-04-02', '2025-04-02'),
    (16, 4,    '2025-04-03', '2025-04-08');

CREATE TABLE order_items (
    order_id   INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity   INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL
);

INSERT INTO order_items VALUES
    (1,  101, 1, 1200), (1,  103, 1, 150),
    (2,  107, 2,   20),
    (3,  102, 1,  800), (3,  103, 1, 150),
    (4,  101, 1, 1200), (4,  102, 1, 800), (4, 103, 1, 150),
    (5,  104, 1,  300), (5,  105, 2, 150),
    (6,  103, 1,  150), (6,  106, 1,  40),
    (7,  101, 1, 1100), (7,  103, 1, 150), (7, 104, 1, 300),
    (8,  107, 1,   20), (8,  108, 1,  35),
    (9,  105, 1,  150), (9,  104, 1, 300),
    (10, 102, 1,  800), (10, 103, 2, 150),
    (11, 107, 3,   20), (11, 108, 1,  35),
    (12, 101, 1, 1200), (12, 102, 1, 750),
    (13, 106, 2,   40),
    (14, 104, 1,  300), (14, 106, 1,  40),
    (15, 106, 1,   40),
    (16, 103, 1,  150), (16, 103, 1, 150), (16, 101, 1, 1200);

CREATE TABLE transactions (
    trans_id   INTEGER PRIMARY KEY,
    user_id    INTEGER NOT NULL,
    country    VARCHAR,
    state      VARCHAR NOT NULL,   -- 'approved' | 'declined'
    amount     INTEGER NOT NULL,
    trans_date DATE NOT NULL
);

INSERT INTO transactions VALUES
    (121, 1, 'US', 'approved', 1000, '2024-12-18'),
    (122, 1, 'US', 'declined', 2000, '2024-12-19'),
    (123, 2, 'US', 'approved', 2000, '2025-01-01'),
    (124, 2, 'DE', 'approved', 2000, '2025-01-07'),
    (125, 1, 'US', 'approved',  500, '2025-01-10'),
    (126, 3, NULL, 'approved',  300, '2025-01-15'),
    (127, 3, NULL, 'declined',  100, '2025-01-20'),
    (128, 1, 'US', 'declined',  700, '2025-01-21'),
    (129, 2, 'DE', 'approved',  900, '2025-01-25'),
    (130, 3, 'DE', 'approved',   50, '2025-02-01'),
    (131, 4, 'FR', 'approved',   80, '2025-02-03'),
    (132, 4, 'FR', 'declined',   40, '2025-02-03'),
    (133, 3, 'DE', 'approved',   75, '2025-01-20');

CREATE TABLE product_spend (
    transaction_id   INTEGER PRIMARY KEY,
    product_id       INTEGER NOT NULL,
    spend            DECIMAL(10, 2) NOT NULL,
    transaction_date DATE NOT NULL
);

INSERT INTO product_spend VALUES
    (1,  1, 1000, '2022-03-01'),
    (2,  1,  700, '2023-02-11'),
    (3,  1,  800, '2023-09-30'),
    (4,  1, 1200, '2024-05-05'),
    (5,  1, 1800, '2025-01-20'),
    (6,  2,  500, '2022-07-14'),
    (7,  2,  800, '2024-03-03'),
    (8,  2,  400, '2025-06-06');

CREATE TABLE intl_orders (
    order_id INTEGER PRIMARY KEY,
    currency VARCHAR NOT NULL,
    amount   DECIMAL(10, 2) NOT NULL,
    order_ts TIMESTAMP NOT NULL
);

INSERT INTO intl_orders VALUES
    (1, 'EUR', 100, '2025-01-10 12:00:00'),
    (2, 'EUR', 200, '2025-01-15 00:00:00'),
    (3, 'EUR',  50, '2025-02-01 08:59:00'),
    (4, 'EUR',  50, '2025-02-01 09:00:00'),
    (5, 'GBP',  80, '2025-01-05 00:00:00'),
    (6, 'GBP', 100, '2025-03-01 00:00:00'),
    (7, 'GBP',  40, '2025-01-20 00:00:00');

CREATE TABLE fx_rates (
    currency     VARCHAR NOT NULL,
    rate_to_usd  DECIMAL(10, 4) NOT NULL,
    effective_ts TIMESTAMP NOT NULL
);

INSERT INTO fx_rates VALUES
    ('EUR', 1.10, '2025-01-01 00:00:00'),
    ('EUR', 1.12, '2025-01-15 00:00:00'),
    ('EUR', 1.08, '2025-02-01 09:00:00'),
    ('GBP', 1.25, '2025-01-10 00:00:00'),
    ('GBP', 1.27, '2025-02-01 00:00:00');
