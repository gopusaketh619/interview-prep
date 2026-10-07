-- Social domain: undirected friendships stored once (user_a < user_b) and posts.
-- Traps: friendships are stored in one direction only, and posts from 2024 must be excluded.

CREATE TABLE friendships (
    user_a INTEGER NOT NULL,
    user_b INTEGER NOT NULL,
    CHECK (user_a < user_b)
);

INSERT INTO friendships VALUES
    (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5), (1, 6), (5, 6), (3, 5), (4, 6);

CREATE TABLE posts (
    post_id    INTEGER PRIMARY KEY,
    user_id    INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL
);

INSERT INTO posts VALUES
    (1,  1, '2024-12-31 23:59:00'),
    (2,  1, '2025-01-01 00:00:00'),
    (3,  1, '2025-02-14 10:00:00'),
    (4,  1, '2025-06-01 10:00:00'),
    (5,  2, '2025-03-03 10:00:00'),
    (6,  3, '2025-01-05 10:00:00'),
    (7,  3, '2025-01-06 10:00:00'),
    (8,  3, '2025-01-07 10:00:00'),
    (9,  4, '2025-04-01 10:00:00'),
    (10, 4, '2025-04-02 10:00:00'),
    (11, 5, '2025-05-05 10:00:00'),
    (12, 6, '2024-05-05 10:00:00'),
    (13, 6, '2024-06-05 10:00:00');
