-- Subscriptions domain. end_date is inclusive; NULL end_date means the subscription is still active.
-- Traps: open-ended subscriptions, back-to-back (non-overlapping) renewals, a subscription nested
-- inside another, and two subscriptions that share exactly one day.

CREATE TABLE subscriptions (
    sub_id     INTEGER PRIMARY KEY,
    user_id    INTEGER NOT NULL,
    plan       VARCHAR NOT NULL,
    start_date DATE NOT NULL,
    end_date   DATE
);

INSERT INTO subscriptions VALUES
    (1,  1, 'basic', '2025-01-01', '2025-03-31'),
    (2,  1, 'pro',   '2025-03-15', '2025-06-30'),
    (3,  2, 'basic', '2025-01-01', '2025-01-31'),
    (4,  2, 'basic', '2025-02-01', '2025-02-28'),
    (5,  3, 'pro',   '2025-02-01', NULL),
    (6,  3, 'basic', '2025-05-01', '2025-05-31'),
    (7,  4, 'basic', '2025-04-01', '2025-04-30'),
    (8,  5, 'pro',   '2025-01-01', '2025-12-31'),
    (9,  5, 'basic', '2025-06-01', '2025-06-15'),
    (10, 4, 'pro',   '2025-04-30', '2025-05-31'),
    (11, 6, 'basic', '2025-01-01', '2025-01-31');
