-- Product analytics domain: users, logins, clickstream events.
-- Traps: multiple logins on the same day, a streak that crosses a month boundary,
-- a user who signed up but never logged in (still part of their cohort), events exactly
-- 30 minutes apart, a cart event that happens before any view, and a purchase that lands
-- outside the 7-day funnel window.

CREATE TABLE users (
    user_id     INTEGER PRIMARY KEY,
    signup_date DATE NOT NULL,
    country     VARCHAR
);

INSERT INTO users VALUES
    (1, '2025-01-01', 'US'),
    (2, '2025-01-03', 'US'),
    (3, '2025-01-03', 'IN'),
    (4, '2025-01-07', 'UK'),
    (5, '2025-02-02', 'US'),
    (6, '2025-02-10', 'DE'),
    (7, '2025-03-05', 'IN'),
    (8, '2025-01-09', 'BR');

CREATE TABLE logins (
    user_id  INTEGER NOT NULL,
    login_ts TIMESTAMP NOT NULL
);

INSERT INTO logins VALUES
    (1, '2025-01-01 09:00:00'), (1, '2025-01-02 08:00:00'), (1, '2025-01-02 20:00:00'),
    (1, '2025-01-03 07:00:00'), (1, '2025-01-05 10:00:00'), (1, '2025-01-06 10:00:00'),
    (1, '2025-01-07 10:00:00'), (1, '2025-01-08 10:00:00'), (1, '2025-02-10 10:00:00'),
    (1, '2025-03-01 10:00:00'),
    (2, '2025-01-03 12:00:00'), (2, '2025-01-04 12:00:00'), (2, '2025-02-01 12:00:00'),
    (2, '2025-02-02 12:00:00'), (2, '2025-02-03 12:00:00'), (2, '2025-04-01 12:00:00'),
    (3, '2025-01-03 18:00:00'),
    (4, '2025-01-07 09:00:00'), (4, '2025-01-31 23:00:00'), (4, '2025-02-01 01:00:00'),
    (4, '2025-02-02 09:00:00'), (4, '2025-03-15 09:00:00'),
    (5, '2025-02-02 09:00:00'), (5, '2025-02-03 09:00:00'), (5, '2025-03-02 09:00:00'),
    (5, '2025-04-05 09:00:00'),
    (6, '2025-02-10 09:00:00'), (6, '2025-04-10 09:00:00'),
    (7, '2025-03-05 10:00:00'), (7, '2025-03-05 11:00:00'), (7, '2025-03-06 10:00:00');

CREATE TABLE events (
    user_id    INTEGER NOT NULL,
    event_ts   TIMESTAMP NOT NULL,
    event_type VARCHAR NOT NULL   -- 'view' | 'add_to_cart' | 'purchase'
);

INSERT INTO events VALUES
    (1, '2025-03-01 10:00:00', 'view'),
    (1, '2025-03-01 10:10:00', 'add_to_cart'),
    (1, '2025-03-01 10:40:00', 'purchase'),
    (1, '2025-03-01 11:20:00', 'view'),
    (1, '2025-03-01 11:25:00', 'view'),
    (2, '2025-03-01 09:00:00', 'view'),
    (2, '2025-03-02 09:00:00', 'add_to_cart'),
    (2, '2025-03-12 09:00:00', 'purchase'),
    (3, '2025-03-03 12:00:00', 'add_to_cart'),
    (3, '2025-03-03 12:05:00', 'view'),
    (3, '2025-03-03 12:31:00', 'purchase'),
    (4, '2025-03-04 08:00:00', 'view'),
    (4, '2025-03-05 08:00:00', 'add_to_cart'),
    (4, '2025-03-06 08:00:00', 'purchase'),
    (5, '2025-03-05 14:00:00', 'view');
