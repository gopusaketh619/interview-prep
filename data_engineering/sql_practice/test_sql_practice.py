"""pytest entry point.

    pytest data_engineering/sql_practice              your attempts (unattempted problems are skipped)
    pytest data_engineering/sql_practice -k 24        a single problem
    SQL_SOLUTIONS=1 pytest data_engineering/sql_practice    verify the reference solutions instead
"""
import os

import pytest

import run
from catalog import PROBLEMS

USE_SOLUTIONS = os.environ.get("SQL_SOLUTIONS") == "1"


@pytest.mark.parametrize("problem", PROBLEMS, ids=lambda p: f"{p.key}_{p.slug}")
def test_problem(problem):
    sql = run.read_solution(problem) if USE_SOLUTIONS else run.read_attempt(problem)
    status, detail, _, _ = run.evaluate(problem, sql)
    if status == "TODO":
        pytest.skip(f"not attempted: problems/{problem.filename}")
    assert status == "PASS", detail
