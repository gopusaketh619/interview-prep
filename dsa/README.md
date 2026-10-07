# DSA Practice

Data Structures and Algorithms problems organized by topic, with a study guide, templates, and a 12-week study plan based on the [Tech Interview Handbook](https://www.techinterviewhandbook.org/).

---

## Documentation

| Doc | Description |
|-----|-------------|
| [DSA Study Guide](docs/dsa_study_guide.md) | Visual guide for all 16 DSA topics |
| [Study Plan](docs/study_plan.md) | 12-week schedule with Grind 75 problems |
| [Python Tricks](docs/python_tricks.md) | Python-specific patterns for interviews |
| [Complexity Reference](docs/complexity_reference.md) | Big-O for all data structures and algorithms |

---

## Topics

| # | Topic | Folder | Problems | Priority |
|---|-------|--------|----------|----------|
| 1 | Array | [array/](topics/array/) | 29 | High |
| 2 | String | [string/](topics/string/) | 7 | High |
| 3 | Hash Table | [hash_table/](topics/hash_table/) | 9 | Mid |
| 4 | Recursion / Backtracking | [recursion/](topics/recursion/) | 9 | Mid |
| 5 | Sorting Algorithms | [sorting_algorithms/](topics/sorting_algorithms/) | 3 implementations | High |
| 6 | Matrix | [matrix/](topics/matrix/) | 5 | High |
| 7 | Linked List | [linked_list/](topics/linked_list/) | 7 | Mid |
| 8 | Queue | [queue/](topics/queue/) | 3 | Mid |
| 9 | Stack | [stack/](topics/stack/) | 8 | Mid |
| 10 | Tree | [tree/](topics/tree/) | 15 | High |
| 11 | Graph | [graph/](topics/graph/) | 9 | High |
| 12 | Heap | [heap/](topics/heap/) | 5 | Mid |
| 13 | Trie | [trie/](topics/trie/) | 3 | Mid |
| 14 | Interval | [interval/](topics/interval/) | 3 | Mid |
| 15 | Dynamic Programming | [dynamic_programming/](topics/dynamic_programming/) | 16 | Low |
| 16 | Binary / Math | [binary_and_math/](topics/binary_and_math/) | 9 | Low |

137 numbered problems in total.

---

## Array Subtopics

The `topics/array/` folder is further organized by technique:

| Technique | Folder | Problems |
|-----------|--------|----------|
| Sliding Window | [array/sliding_window/](topics/array/sliding_window/) | 12 |
| Two Pointers | [array/two_pointers/](topics/array/two_pointers/) | 7 |
| Binary Search | [array/binary_search/](topics/array/binary_search/) | 8 |
| Prefix Sum | [array/prefix_sum/](topics/array/prefix_sum/) | 2 |

Problems live under the technique that solves them. Kadane's problems (maximum subarray, maximum product subarray) are in `dynamic_programming/`, interval problems are in `interval/`, and hash-set/index-hashing problems (contains duplicate, first missing positive) are in `hash_table/`.

---

## File Structure

Each topic folder contains:
- **`*_template.py`**: pattern overview with pseudocode, when-to-use signals, and complexity
- **`NN_problem_name.py`**: numbered problem files (easier first) with a stub or solution and assertion tests

---

## How to Run

```bash
python3 dsa/topics/array/sliding_window/01_max_average_subarray.py
```

Each file is self-contained with assertions. If it prints "All test cases passed!", the solution is correct.

---

## Study Approach

1. Read the [DSA Study Guide](docs/dsa_study_guide.md) for a topic overview
2. Study the `*_template.py` file in the relevant folder
3. Attempt problems in numbered order (easier first)
4. Follow the [Study Plan](docs/study_plan.md) for structured 12-week prep
