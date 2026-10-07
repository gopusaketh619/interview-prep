-- HR domain: departments, employees (self-referencing manager_id), salary history.
-- Traps: salary ties (Carol/Dan, Ken/Leo), a department with no employees (Research),
-- a single-employee department (Legal), and an employee missing from 2024 history (Leo).

CREATE TABLE departments (
    dept_id   INTEGER PRIMARY KEY,
    dept_name VARCHAR NOT NULL
);

INSERT INTO departments VALUES
    (1, 'Engineering'),
    (2, 'Sales'),
    (3, 'Marketing'),
    (4, 'Legal'),
    (5, 'Research');

CREATE TABLE employees (
    emp_id     INTEGER PRIMARY KEY,
    name       VARCHAR NOT NULL,
    dept_id    INTEGER,
    manager_id INTEGER,
    salary     INTEGER NOT NULL,
    hire_date  DATE NOT NULL
);

INSERT INTO employees VALUES
    (1,  'Alice', 1, NULL, 250000, '2018-01-15'),
    (2,  'Bob',   1, 1,    180000, '2019-03-01'),
    (3,  'Carol', 1, 2,    150000, '2020-06-10'),
    (4,  'Dan',   1, 2,    150000, '2021-02-20'),
    (5,  'Eve',   1, 3,    120000, '2022-08-01'),
    (6,  'Frank', 1, 3,    110000, '2023-01-09'),
    (7,  'Grace', 2, 1,    160000, '2019-07-07'),
    (8,  'Heidi', 2, 7,     90000, '2020-11-11'),
    (9,  'Ivan',  2, 7,    100000, '2021-04-04'),
    (10, 'Judy',  2, 8,     70000, '2023-05-05'),
    (11, 'Ken',   3, 1,     95000, '2020-02-02'),
    (12, 'Leo',   3, 11,    95000, '2022-09-09'),
    (13, 'Mia',   4, 1,    130000, '2021-10-10');

CREATE TABLE salary_history (
    emp_id INTEGER NOT NULL,
    year   INTEGER NOT NULL,
    salary INTEGER NOT NULL
);

INSERT INTO salary_history VALUES
    (2, 2024, 170000), (3, 2024, 140000), (4, 2024, 130000), (5, 2024, 175000), (6, 2024, 100000),
    (7, 2024, 150000), (8, 2024,  85000), (9, 2024,  88000), (10, 2024, 95000),
    (11, 2024, 90000),
    (2, 2025, 180000), (3, 2025, 150000), (4, 2025, 150000), (5, 2025, 120000), (6, 2025, 110000),
    (7, 2025, 160000), (8, 2025,  90000), (9, 2025, 100000), (10, 2025, 70000),
    (11, 2025, 95000), (12, 2025, 95000);
