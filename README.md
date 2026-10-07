# DSA Practice

A structured collection of Data Structures and Algorithms problems organized by topic, with a comprehensive study guide, templates, and a 12-week study plan based on the [Tech Interview Handbook](https://www.techinterviewhandbook.org/).

---

## Documentation

| Doc | Description |
|-----|-------------|
| [DSA Study Guide](docs/dsa_study_guide.md) | Comprehensive visual guide for all 16 DSA topics |
| [Study Plan](docs/study_plan.md) | 12-week schedule with Grind 75 problems |
| [Python Tricks](docs/python_tricks.md) | Python-specific patterns for interviews |
| [Complexity Reference](docs/complexity_reference.md) | Big-O for all data structures and algorithms |
| [Kafka & Snowflake Guide](interview_prep/data_engineering_kafka_snowflake.md) | Data engineering technical and system design questions |
| [Data Platform & Governance Prep](interview_prep/data_platform_governance_interview.md) | Snowflake admin, RBAC/PII governance, Fivetran/Airflow/Hex, CDC cutovers |
| [SQL Practice Suite](interview_prep/sql_practice/README.md) | 50 medium/hard DE SQL problems with an in-memory DuckDB test runner |

---

## Topics

| # | Topic | Folder | Problems | Priority |
|---|-------|--------|----------|----------|
| 1 | Array | [array/](topics/array/) | 29 | High |
| 2 | String | [string/](topics/string/) | 5 | High |
| 3 | Hash Table | [hash_table/](topics/hash_table/) | 4 | Mid |
| 4 | Recursion / Backtracking | [recursion/](topics/recursion/) | 5 | Mid |
| 5 | Sorting Algorithms | [sorting_algorithms/](topics/sorting_algorithms/) | 3 | High |
| 6 | Matrix | [matrix/](topics/matrix/) | 2 | High |
| 7 | Linked List | [linked_list/](topics/linked_list/) | 5 | Mid |
| 8 | Queue | [queue/](topics/queue/) | 2 | Mid |
| 9 | Stack | [stack/](topics/stack/) | 4 | Mid |
| 10 | Tree | [tree/](topics/tree/) | 10 | High |
| 11 | Graph | [graph/](topics/graph/) | 7 | High |
| 12 | Heap | [heap/](topics/heap/) | 4 | Mid |
| 13 | Trie | [trie/](topics/trie/) | 1 | Mid |
| 14 | Interval | [interval/](topics/interval/) | 2 | Mid |
| 15 | Dynamic Programming | [dynamic_programming/](topics/dynamic_programming/) | 7 | Low |
| 16 | Binary / Math | [binary_and_math/](topics/binary_and_math/) | 1 | Low |

---

## Array Subtopics

The `topics/array/` folder is further organized by technique:

| Technique | Folder | Problems |
|-----------|--------|----------|
| Sliding Window | [array/sliding_window/](topics/array/sliding_window/) | 10 |
| Two Pointers | [array/two_pointers/](topics/array/two_pointers/) | 7 |
| Binary Search | [array/binary_search/](topics/array/binary_search/) | 4 |
| Prefix Sum | [array/prefix_sum/](topics/array/prefix_sum/) | 4 |
| Sorting | [array/sorting/](topics/array/sorting/) | 4 |

---

## File Structure

Each topic folder contains:
- **`*_template.py`** — Pattern overview with pseudocode, when-to-use signals, and complexity
- **`NN_problem_name.py`** — Numbered problem files with brute force + optimal solutions, comments, and test cases

---

## How to Run

```bash
python3 topics/array/sliding_window/01_max_average_subarray.py
```

Each file is self-contained with assertions. If it prints "All test cases passed!" — the solution is correct.

---

## Study Approach

1. Read the [DSA Study Guide](docs/dsa_study_guide.md) for a topic overview
2. Study the `*_template.py` file in the relevant folder
3. Attempt problems in numbered order (easier first)
4. Follow the [Study Plan](docs/study_plan.md) for structured 12-week prep
