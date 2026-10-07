"""Registry of all practice problems.

Each problem's prompt lives in problems/NN_slug.sql, its reference answer in
solutions/NN_slug.sql, and its expected result in expected/NN.json.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Problem:
    id: int
    slug: str
    title: str
    topic: str
    difficulty: str  # "medium" | "hard"
    datasets: tuple
    ordered: bool = False

    @property
    def key(self) -> str:
        return f"{self.id:02d}"

    @property
    def filename(self) -> str:
        return f"{self.key}_{self.slug}.sql"


M, H = "medium", "hard"

JOINS = "Joins and set logic"
AGG = "Aggregation"
RANK = "Ranking windows"
WIN = "Window aggregates and LAG/LEAD"
GAPS = "Gaps and islands"
EVENTS = "Event analytics"
RETENTION = "Retention and growth"
RECURSIVE = "Recursive CTEs"
PIVOT = "Pivot, unpivot, and strings"
DE = "Data engineering specific"
INTERVALS = "Intervals"

PROBLEMS = [
    Problem(1, "customers_never_ordered", "Customers who never ordered", JOINS, M, ("ecommerce",)),
    Problem(2, "second_highest_salary_per_dept", "Second-highest salary per department", JOINS, M, ("hr",)),
    Problem(3, "frequently_bought_together", "Products frequently bought together", JOINS, H, ("ecommerce",), ordered=True),
    Problem(4, "bought_all_in_category", "Customers who bought every Electronics product", JOINS, H, ("ecommerce",)),
    Problem(5, "friend_recommendations", "Friend recommendations by mutual friends", JOINS, H, ("social",)),

    Problem(6, "monthly_approval_by_country", "Monthly transactions by country", AGG, M, ("ecommerce",)),
    Problem(7, "depts_above_company_avg", "Departments above the company average salary", AGG, M, ("hr",)),
    Problem(8, "median_salary_per_dept", "Median salary per department", AGG, H, ("hr",)),
    Problem(9, "posts_histogram", "Histogram of posts per user", AGG, M, ("social",), ordered=True),
    Problem(10, "immediate_first_orders", "Percentage of immediate first orders", AGG, M, ("ecommerce",)),

    Problem(11, "top3_salaries_per_dept", "Top 3 distinct salaries per department", RANK, H, ("hr",)),
    Problem(12, "top_product_per_category_month", "Top-selling product per category per month", RANK, M, ("ecommerce",)),
    Problem(13, "top2_grossing_per_category", "Top 2 grossing products per category", RANK, M, ("ecommerce",)),
    Problem(14, "top_quartile_customers", "Top-quartile customers by spend", RANK, M, ("ecommerce",)),
    Problem(15, "salary_rank_dropped", "Employees whose salary rank dropped", RANK, H, ("hr",)),
    Problem(16, "third_transaction", "Each user's third transaction", RANK, M, ("ecommerce",)),

    Problem(17, "running_revenue_monthly_reset", "Running revenue that resets each month", WIN, M, ("ecommerce",), ordered=True),
    Problem(18, "rolling_7d_avg_with_gaps", "7-day rolling average with missing days", WIN, H, ("misc",), ordered=True),
    Problem(19, "mom_revenue_growth", "Month-over-month revenue growth", WIN, M, ("ecommerce",), ordered=True),
    Problem(20, "yoy_product_spend", "Year-over-year spend growth per product", WIN, M, ("ecommerce",)),
    Problem(21, "last_person_on_bus", "Last person to fit on the bus", WIN, M, ("misc",)),
    Problem(22, "warmer_than_yesterday", "Warmer than the previous calendar day", WIN, M, ("misc",)),

    Problem(23, "consecutive_numbers", "Numbers appearing 3+ times consecutively", GAPS, M, ("misc",)),
    Problem(24, "longest_login_streak", "Longest login streak per user", GAPS, H, ("events",)),
    Problem(25, "stadium_traffic", "3+ consecutive high-traffic rows", GAPS, H, ("misc",), ordered=True),
    Problem(26, "continuous_ranges", "Collapse ids into continuous ranges", GAPS, M, ("misc",)),
    Problem(27, "status_periods", "Compress daily run states into periods", GAPS, H, ("misc",), ordered=True),

    Problem(28, "sessionize_clickstream", "Sessionize a clickstream", EVENTS, H, ("events",)),
    Problem(29, "ordered_funnel", "Ordered conversion funnel within 7 days", EVENTS, H, ("events",), ordered=True),
    Problem(30, "first_to_second_purchase", "Average days from first to second order", EVENTS, M, ("ecommerce",)),
    Problem(31, "next_day_retention", "Fraction of players back the day after first login", EVENTS, M, ("misc",)),
    Problem(32, "peak_concurrent_sessions", "Peak concurrent sessions", EVENTS, H, ("misc",)),

    Problem(33, "mom_retained_users", "Month-over-month retained users", RETENTION, H, ("events",), ordered=True),
    Problem(34, "cohort_retention", "Cohort retention matrix", RETENTION, H, ("events",)),
    Problem(35, "dau_mau_stickiness", "DAU/MAU stickiness", RETENTION, M, ("events",), ordered=True),
    Problem(36, "growth_accounting", "Growth accounting: new, retained, resurrected, churned", RETENTION, H, ("events",)),
    Problem(37, "repeat_purchase_rate", "Repeat-purchase rate within 30 days", RETENTION, M, ("ecommerce",)),

    Problem(38, "org_chart", "Org chart with depth and path", RECURSIVE, H, ("hr",), ordered=True),
    Problem(39, "date_spine_fill", "Daily signups with a date spine", RECURSIVE, M, ("events",), ordered=True),
    Problem(40, "bill_of_materials", "Bill of materials cost roll-up", RECURSIVE, H, ("misc",)),

    Problem(41, "pivot_dept_revenue", "Pivot monthly revenue into columns", PIVOT, M, ("misc",)),
    Problem(42, "unpivot_store_prices", "Unpivot store prices", PIVOT, M, ("misc",)),
    Problem(43, "products_sold_per_date", "Distinct products sold per date", PIVOT, M, ("misc",), ordered=True),

    Problem(44, "latest_record_per_key", "Latest record per key with tie-breaker", DE, M, ("cdc",)),
    Problem(45, "apply_cdc_log", "Apply a CDC log to get current state", DE, H, ("cdc",)),
    Problem(46, "scd2_from_snapshots", "Build SCD Type 2 from daily snapshots", DE, H, ("cdc",)),
    Problem(47, "asof_fx_conversion", "Point-in-time FX conversion (as-of join)", DE, H, ("ecommerce",)),
    Problem(48, "data_quality_report", "One-query data quality report", DE, M, ("quality",)),

    Problem(49, "merge_meeting_intervals", "Merge overlapping meetings per room", INTERVALS, H, ("misc",)),
    Problem(50, "overlapping_subscriptions", "Users with overlapping subscriptions", INTERVALS, H, ("subscriptions",)),
]

TOPICS = list(dict.fromkeys(p.topic for p in PROBLEMS))

_BY_ID = {p.id: p for p in PROBLEMS}


def by_id(problem_id) -> Problem:
    pid = int(problem_id)
    if pid not in _BY_ID:
        raise SystemExit(f"Unknown problem {problem_id!r}. Valid ids: 1-{len(PROBLEMS)}")
    return _BY_ID[pid]
