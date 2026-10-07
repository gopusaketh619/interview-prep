# DSA Study Guide

A comprehensive, visual guide to all major data structures and algorithms topics for coding interviews. Work through each topic, internalize the patterns, then solve the practice problems.

**How to use this guide:**
1. Read through a topic section before attempting any problems
2. Pay attention to the visual diagrams — they build intuition faster than text alone
3. Study the "How to Recognize" section to pattern-match during interviews
4. Attempt the Essential Questions first, then move to Recommended
5. Refer back to techniques when you get stuck on a problem

---

## 1. Array

### What Is It?

A contiguous block of memory where elements sit side by side, each accessible instantly by its index.

```
  Index:    0     1     2     3     4
         +-----+-----+-----+-----+-----+
  Array: |  10 |  20 |  30 |  40 |  50 |
         +-----+-----+-----+-----+-----+
  Addr:  0x100 0x104 0x108 0x10C 0x110

  arr[3] → jump directly to 0x100 + (3 × 4 bytes) = 0x10C → 40  ✓ O(1)
```

Because elements are packed together, the CPU can calculate any element's address with simple arithmetic — that's what makes random access O(1). The flip side: inserting in the middle requires shifting everything after the insertion point.

```
  Insert 25 at index 2:

  Before: [ 10 | 20 | 30 | 40 | 50 ]
                      ↓ shift right →
  After:  [ 10 | 20 | 25 | 30 | 40 | 50 ]
```

In Python, `list` is a dynamic array — it auto-resizes by allocating a bigger block and copying elements when capacity is exceeded. This makes `.append()` amortized O(1).

| Operation | Time | Why |
|-----------|------|-----|
| Access by index | O(1) | Address arithmetic |
| Search (unsorted) | O(n) | Must check every element |
| Search (sorted) | O(log n) | Binary search |
| Insert / Remove (end) | O(1)* | No shifting (*amortized for dynamic arrays) |
| Insert / Remove (middle) | O(n) | Must shift remaining elements |

### Key Patterns & Techniques

**Pattern 1: Sliding Window**

A window that slides across the array, maintaining some invariant (sum, count, set of characters). Two pointers move in the same direction and never overtake each other.

```
  Find max sum subarray of size 3:

  [ 2 | 1 | 5 | 1 | 3 | 2 ]
    └─────────┘                 window sum = 8
        └─────────┘             window sum = 7
            └─────────┘         window sum = 9  ← max
                └─────────┘     window sum = 6

  Instead of recalculating from scratch each time:
    new_sum = old_sum - arr[left] + arr[right+1]    → O(1) per slide
```

*Fixed window:* Window size stays constant. Slide right, add new element, remove leftmost.
*Variable window:* Expand right until condition breaks, then shrink from left until condition holds again.

```python
# Variable sliding window template
left = 0
for right in range(len(arr)):
    # expand: add arr[right] to window state
    while window_condition_broken():
        # shrink: remove arr[left] from window state
        left += 1
    # update answer with current window
```

**Pattern 2: Two Pointers**

Two pointers that move toward each other, away from each other, or at different speeds.

```
  Two Sum (sorted array) — pointers move inward:

  [ 1 | 3 | 5 | 7 | 11 | 15 ]    target = 12
    L                      R       1+15=16 > 12, move R left
    L                 R            1+11=12 ✓ found!

  Remove duplicates in-place — slow/fast pointers:

  [ 1 | 1 | 2 | 2 | 3 ]
    S   F                          1==1, skip
    S       F                      1≠2, write: arr[S+1]=2, S++
        S       F                  2==2, skip
        S           F              2≠3, write: arr[S+1]=3, S++
  Result: [ 1 | 2 | 3 | _ | _ ]
```

**Pattern 3: Prefix Sum**

Pre-compute cumulative sums so any subarray sum becomes a single subtraction.

```
  arr:        [ 3 |  1 |  4 |  1 |  5 ]
  prefix:  [ 0 | 3 |  4 |  8 |  9 | 14 ]

  Sum of arr[1..3] = prefix[4] - prefix[1] = 9 - 3 = 6

  Build:   prefix[i] = prefix[i-1] + arr[i-1]
  Query:   sum(i, j) = prefix[j+1] - prefix[i]       → O(1) per query
```

**Pattern 4: Sorting First**

If order doesn't matter, sorting the array can unlock simpler solutions. A sorted array enables binary search and makes duplicates adjacent.

**Pattern 5: Index as Hash Key**

When values are in range [1, N] and the interviewer wants O(1) space, use the array itself as a hash table — mark presence by negating values at index (val-1).

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Subarray of size k" or "window" | Sliding window |
| "Sorted array" + "find pair" | Two pointers from both ends |
| "Sum of subarray" or "range query" | Prefix sum |
| "In-place" + "O(1) space" | Two pointers or index-as-hash |
| "Contiguous subarray with property X" | Sliding window (variable) |
| "Find missing/duplicate in [1..N]" | Index as hash key |

### Common Mistakes
- Off-by-one errors on boundaries
- Forgetting that Python slicing creates a copy — O(n) time and space
- Using `in` on a list (O(n)) when a set (O(1)) would work

### Corner Cases
- Empty array
- Single element
- All duplicates
- Already sorted / reverse sorted

**Essential Questions:**
- [Two Sum](../topics/hash_table/01_two_sum.py)
- [Best Time to Buy and Sell Stock](../topics/array/sliding_window/12_buy_sell_stock.py)
- [Product of Array Except Self](../topics/array/prefix_sum/01_product_except_self.py)
- [Maximum Subarray](../topics/dynamic_programming/15_maximum_subarray.py)

**Recommended Practice Questions:**
- [Contains Duplicate](../topics/hash_table/09_contains_duplicate.py)
- [Maximum Product Subarray](../topics/dynamic_programming/16_maximum_product_subarray.py)
- [Search in Rotated Sorted Array](../topics/array/binary_search/02_search_rotated_sorted.py)
- [3Sum](../topics/array/two_pointers/02_three_sum.py)
- [Container With Most Water](../topics/array/two_pointers/03_container_with_most_water.py)
- [Sliding Window Maximum](../topics/array/sliding_window/04_sliding_window_maximum.py)

**Further Reading:**
- [Sliding Window Technique](https://leetcode.com/problems/minimum-window-substring/solutions/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems/) — the 10-line template that solves most substring problems
- [Two Pointer Technique](https://leetcode.com/articles/two-pointer-technique/) — LeetCode guide
- [VisuAlgo: Sorting & Array](https://visualgo.net/en/sorting) — watch how array operations work

---

## 2. String

### What Is It?

A string is an array of characters. In Python, strings are **immutable** — every modification creates a new string object.

```
  s = "HELLO"

  Index:   0    1    2    3    4
         +----+----+----+----+----+
         | H  | E  | L  | L  | O  |
         +----+----+----+----+----+

  s[0] → 'H'     O(1) access, just like arrays
  s[1:4] → 'ELL'  O(k) slice — creates a new string

  ⚠️  s += "!" creates a BRAND NEW string "HELLO!"
      The old "HELLO" is discarded.
      Doing this in a loop is O(n²) — use ''.join(list) instead!
```

### Key Patterns & Techniques

**Pattern 1: Character Frequency Counting**

Most string problems boil down to "count characters and compare." Python's `Counter` does this in one line.

```
  "anagram" → Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})

  Two strings are anagrams ⟺ they have the same Counter
```

Space for character counting is O(1), not O(n) — there are at most 26 lowercase letters (a fixed constant).

**Pattern 2: Palindrome — Expand from Center**

Instead of checking every substring (O(n³)), expand outward from each possible center.

```
  Check "racecar":

  For center index 3 ('e'):
      r  a  c  e  c  a  r
               ↑
            c  e  c         match? c==c ✓
         a  c  e  c  a      match? a==a ✓
      r  a  c  e  c  a  r   match? r==r ✓  → palindrome of length 7

  Check BOTH odd-length (single center) and even-length (between two chars):
      Odd:  expand(i, i)
      Even: expand(i, i+1)
```

```python
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1  # length of palindrome
```

**Pattern 3: Bitmask for Unique Characters**

When dealing with lowercase-only strings and uniqueness, a 26-bit integer can replace a set:

```python
mask = 0
for c in word:
    bit = 1 << (ord(c) - ord('a'))
    if mask & bit:  # already seen
        return False
    mask |= bit
```

**Pattern 4: String Building**

```python
# BAD — O(n²) because strings are immutable
result = ""
for char in data:
    result += char

# GOOD — O(n) using list + join
parts = []
for char in data:
    parts.append(char)
result = ''.join(parts)
```

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Anagram" | Counter / sorting |
| "Palindrome" | Two pointers (outside-in or expand from center) |
| "Substring with condition" | Sliding window |
| "Pattern matching" | KMP / Rabin-Karp (rare in interviews) |
| "All lowercase letters" | 26-element array or bitmask |

### Common Mistakes
- Building strings with `+=` in a loop (O(n²))
- Forgetting case sensitivity — always clarify
- Off-by-one in substring indices

### Corner Cases
- Empty string
- Single character
- All same characters
- Case sensitivity (clarify!)

**Essential Questions:**
- [Valid Anagram](../topics/string/02_valid_anagram.py)
- [Valid Palindrome](../topics/string/01_valid_palindrome.py)
- [Longest Substring Without Repeating Characters](../topics/array/sliding_window/05_longest_substr_no_repeat.py)

**Recommended Practice Questions:**
- [Longest Repeating Character Replacement](../topics/string/05_longest_repeating_char_replacement.py)
- [Find All Anagrams in a String](../topics/array/sliding_window/03_count_anagrams.py)
- [Minimum Window Substring](../topics/array/sliding_window/09_minimum_window_substring.py)
- [Group Anagrams](../topics/string/04_group_anagrams.py)
- [Longest Palindromic Substring](../topics/string/03_longest_palindromic_substring.py)
- [Encode and Decode Strings](../topics/string/06_encode_decode_strings.py) (Premium)

**Further Reading:**
- [Rabin-Karp Algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) — rolling hash for substring search
- [KMP Algorithm Visualized](https://www.youtube.com/watch?v=V5-7GzOfADQ) — Back to Back SWE

---

## 3. Hash Table

### What Is It?

A hash table maps keys to values using a hash function. Think of it as a magical dictionary — you give it a word (key) and it instantly finds the definition (value).

```
  How hashing works:

  key "apple" → hash("apple") → 3    ┌──────────────────┐
  key "banana"→ hash("banana")→ 1    │ Bucket Array     │
  key "cherry"→ hash("cherry")→ 3    │                  │
                                      │ [0] → empty      │
       ┌──────────────────┐           │ [1] → "banana"   │
       │   Collision!     │           │ [2] → empty      │
       │ "apple" & "cherry"│──────────│ [3] → "apple" →  │
       │  both hash to 3  │           │        "cherry"  │
       └──────────────────┘           │ [4] → empty      │
                                      └──────────────────┘
  Collision resolution: chain collided items in a linked list (separate chaining)
```

The core insight: hashing converts **any** key into an **integer index** in O(1) on average. This is the most common **space-time tradeoff** in interviews — use O(n) extra space to go from O(n) search to O(1) search.

| Operation | Average | Worst (all collisions) |
|-----------|---------|------------------------|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

*In interviews, we always assume average case for hash tables.*

### Python's Hash Table Arsenal

```python
from collections import defaultdict, Counter

# Regular dict
seen = {}
seen["key"] = "value"

# defaultdict — auto-creates missing keys
graph = defaultdict(list)       # graph["A"].append("B") — no KeyError
freq = defaultdict(int)         # freq["x"] += 1 — starts at 0

# Counter — frequency counting in one line
Counter("abracadabra")  # → {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# set — O(1) existence checks
seen = set()
seen.add(42)
42 in seen  # → True, O(1)
```

### Key Patterns & Techniques

**Pattern 1: Complement Lookup (Two Sum pattern)**

Instead of checking all pairs (O(n²)), store what you've seen and look for the complement.

```
  nums = [2, 7, 11, 15], target = 9

  Step 1: see 2, need 9-2=7, not in map → store {2: idx0}
  Step 2: see 7, need 9-7=2, found in map! → return [idx0, idx1]
```

**Pattern 2: Grouping by Key**

Use `defaultdict(list)` to group items that share a property.

```
  Group anagrams:  ["eat", "tea", "tan", "ate", "nat", "bat"]

  Sort each word as key:
    "aet" → ["eat", "tea", "ate"]
    "ant" → ["tan", "nat"]
    "abt" → ["bat"]
```

**Pattern 3: Seen Set for Deduplication**

Track what you've visited to avoid revisiting.

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Find pair that sums to X" | Hash map (complement lookup) |
| "Count frequency of..." | Counter |
| "Group items by property" | defaultdict(list) |
| "Check if exists" or "duplicates" | Set |
| "O(1) lookup needed" | Hash map or set |

### Corner Cases
- Empty input
- All keys identical
- Key doesn't exist (use `.get(key, default)`)

**Essential Questions:**
- [Two Sum](../topics/hash_table/01_two_sum.py)
- [Ransom Note](../topics/hash_table/02_ransom_note.py)

**Recommended Practice Questions:**
- [Group Anagrams](../topics/string/04_group_anagrams.py)
- [Insert Delete GetRandom O(1)](../topics/hash_table/05_insert_delete_getrandom.py)
- [First Missing Positive](../topics/hash_table/08_first_missing_positive.py)
- [LRU Cache](../topics/hash_table/06_lru_cache.py)
- [All O`one Data Structure](../topics/hash_table/07_all_o_one.py)

**Further Reading:**
- [Taking Hash Tables Off The Shelf](https://medium.com/basecs/taking-hash-tables-off-the-shelf-139cbf4752f0) — basecs (beautifully illustrated)
- [Hash Table Visualization](https://www.cs.usfca.edu/~galles/visualization/OpenHash.html) — interactive

---

## 4. Recursion / Backtracking

### What Is It?

Recursion solves a problem by solving smaller versions of itself. Backtracking is recursion + "undo" — explore a path, and if it doesn't work out, undo your last choice and try another.

```
  Recursion is like Russian nesting dolls:

  factorial(4)
    → 4 × factorial(3)
              → 3 × factorial(2)
                        → 2 × factorial(1)
                                  → return 1     ← base case
                        → return 2 × 1 = 2
              → return 3 × 2 = 6
    → return 4 × 6 = 24


  The call stack during recursion:

  ┌─────────────────┐
  │ factorial(1) = 1 │  ← top of stack (base case, starts returning)
  ├─────────────────┤
  │ factorial(2)     │  waiting for factorial(1)
  ├─────────────────┤
  │ factorial(3)     │  waiting for factorial(2)
  ├─────────────────┤
  │ factorial(4)     │  waiting for factorial(3)
  └─────────────────┘
```

**Backtracking visualized — generating subsets of [1, 2, 3]:**

```
                          []
                   /             \
              [1]                  []
            /     \            /      \
        [1,2]    [1]       [2]        []
        /  \    /   \     /  \      /   \
   [1,2,3][1,2][1,3][1] [2,3][2] [3]   []

  At each level: choose to INCLUDE or EXCLUDE the current element
  Leaves = all possible subsets: [1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]
```

### The Two Rules of Recursion
1. **Every recursive function MUST have a base case** — the condition where it stops calling itself
2. **Every recursive call MUST move toward the base case** — otherwise infinite recursion

### Key Patterns & Techniques

**Pattern 1: Choose → Explore → Unchoose (Backtracking)**

```python
def backtrack(candidates, start, path, result):
    if goal_reached(path):
        result.append(path[:])      # save a COPY of the current path
        return
    for i in range(start, len(candidates)):
        path.append(candidates[i])             # CHOOSE
        backtrack(candidates, i + 1, path, result)  # EXPLORE
        path.pop()                             # UNCHOOSE (backtrack)
```

**Pattern 2: Memoization (Top-Down DP)**

Cache results of expensive recursive calls. Transforms exponential time into polynomial.

```
  Fibonacci without memo:        With memo:

  fib(5)                         fib(5)
  ├─ fib(4)                      ├─ fib(4)
  │  ├─ fib(3)                   │  ├─ fib(3)
  │  │  ├─ fib(2) ←repeated     │  │  ├─ fib(2) → cache
  │  │  └─ fib(1)               │  │  └─ fib(1)
  │  └─ fib(2) ←repeated        │  └─ fib(2) → HIT!
  └─ fib(3) ←repeated           └─ fib(3) → HIT!

  O(2^n) → O(n)
```

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Pattern 3: Handling Duplicates**

Sort the input, then skip duplicate elements at the same recursion level:

```python
candidates.sort()
for i in range(start, len(candidates)):
    if i > start and candidates[i] == candidates[i - 1]:
        continue  # skip duplicate
```

### The 6 Backtracking Templates

All backtracking = 3 templates × with/without duplicates. Full code in [recursion/recursion_template.py](../topics/recursion/recursion_template.py).

**Template Decision Flowchart:**

```
  "Does order matter?"
       │
    YES → Permutation (loop from 0, used[])
    NO  → "Fixed size k?"
             │
          YES → Combination (loop from start, stop at k)
          NO  → Subset (loop from start, save every node)

  "Has duplicates?" → YES: sort() + add skip line
```

**The 3 Knobs:**

| Problem | When to save? | Loop starts at? | Prevents reuse via? |
|---------|---------------|-----------------|---------------------|
| Subsets | Every node | `start` (forward) | `i + 1` |
| Combinations | `len(path) == k` | `start` (forward) | `i + 1` |
| Permutations | `len(path) == n` | `0` (always) | `used[]` |

**Duplicate Skip Conditions (add after sort):**

| Problem | Skip line |
|---------|-----------|
| Subsets/Combos | `if i > start and nums[i] == nums[i-1]: continue` |
| Permutations | `if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue` |

**Result Counts:**

| Problem | No Dups | With Dups |
|---------|---------|-----------|
| Subsets | 2^n | ≤ 2^n (pruned) |
| Combinations C(n,k) | n!/(k!(n-k)!) | ≤ C(n,k) (pruned) |
| Permutations P(n) | n! | ≤ n! (pruned) |

### Tips for Visualizing Recursion

**The Maze Mental Model:**

```
  path.append()  = walk through a door
  backtrack()    = keep exploring deeper
  path.pop()     = walk back to the fork and try the next door
```

| Tip | Why it helps |
|-----|-------------|
| Trace TINY inputs (n=1, n=2) | Build intuition before scaling up |
| Draw the tree on paper | Your brain processes visuals > code |
| Add `print(f"path={path}")` | See recursion happen in real time |
| Focus on ONE level at a time | Don't think 3 levels deep |
| Trust the pattern, not the trace | Once verified on small input, scale |
| Memorize 3 templates, not traces | Pick the right template, fill it in |

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Generate all combinations/permutations/subsets" | Backtracking |
| "All possible ways" | Backtracking |
| "Can you partition/split into..." | Backtracking with pruning |
| "Overlapping subproblems" | Memoization |
| "Constraint satisfaction" (Sudoku, N-Queens) | Backtracking |

### Common Mistakes
- Forgetting the base case → infinite recursion → stack overflow (Python limit: 1000)
- Appending `path` instead of `path[:]` → all results point to the same mutated list
- Not skipping duplicates → duplicate results

### Corner Cases
- `n = 0`
- `n = 1`
- Empty input
- All duplicate elements

**Essential Questions:**
- [Generate Parentheses](../topics/recursion/06_generate_parentheses.py)
- [Combinations](../topics/recursion/07_combinations.py)
- [Subsets](../topics/recursion/03_subsets.py)

**Recommended Practice Questions:**
- [Letter Combinations of a Phone Number](../topics/recursion/04_letter_combinations_phone.py)
- [Subsets II](../topics/recursion/08_subsets_ii.py)
- [Permutations](../topics/recursion/02_permutations.py)
- [Sudoku Solver](../topics/recursion/09_sudoku_solver.py)

**Further Reading:**
- [Recursion and Backtracking Visualized](https://medium.com/basecs/recursion-revisited-8c1d58858e9e) — basecs
- [Backtracking Template](https://leetcode.com/problems/permutations/solutions/18239/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/) — the classic LeetCode post covering 6 problems with one template

---

## 5. Sorting and Searching

### What Is It?

Sorting arranges elements in order. Searching finds elements efficiently — especially binary search on sorted data.

**Sorting algorithm comparison:**

```
                    ┌─────────────┐
                    │  Need to    │
                    │  sort?      │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        Comparison    Non-Comparison   Already
        Based         Based            Mostly Sorted?
        O(n log n)    O(n+k)           │
              │            │            ▼
     ┌────────┴────┐    Counting    Insertion Sort
     │             │    Sort        (O(n) best case)
  Stable?      In-place?
     │             │
  Merge Sort   Quick Sort
  (+ O(n) space) (O(1) extra)
```

| Algorithm | Best | Average | Worst | Space | Stable | Notes |
|-----------|------|---------|-------|-------|--------|-------|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Guaranteed performance, great for linked lists |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Fast in practice, bad worst case |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | In-place but not stable |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | Only for integers in known range [0..k] |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Yes | Python's built-in, hybrid merge+insertion |

**Python's sort:** `list.sort()` and `sorted()` use TimSort. Know this!

### Binary Search — The Most Important Search Algorithm

Binary search eliminates half the remaining elements with each comparison. Only works on sorted data.

```
  Search for 7 in [1, 3, 5, 7, 9, 11, 13]:

  Step 1:  [ 1  3  5  7  9  11  13 ]
             L        M           R     mid=7, found!

  Search for 4:

  Step 1:  [ 1  3  5  7  9  11  13 ]
             L        M           R     mid=7 > 4, go left
  Step 2:  [ 1  3  5 ]
             L  M  R                    mid=3 < 4, go right
  Step 3:  [ 5 ]
             L=M=R                      mid=5 ≠ 4, not found
```

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # avoids overflow in other languages
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Binary Search on Answer Space:**

Sometimes you don't search an array — you search a range of possible answers and check if each is feasible.

```
  "Minimum capacity to ship packages in D days"

  Answer range: [max(weights), sum(weights)]
  For each candidate capacity: can we ship in ≤ D days?  (greedy check)
  Binary search for the minimum capacity where the answer is "yes"
```

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Sorted array" + "find X" | Binary search |
| "Find minimum/maximum satisfying condition" | Binary search on answer |
| "O(log n) required" | Binary search |
| "Kth largest/smallest" | Quick select O(n) avg, or heap O(n log k) |

### Python Shortcuts

```python
import bisect

# Find insertion point for target in sorted array
i = bisect.bisect_left(arr, target)    # leftmost position
i = bisect.bisect_right(arr, target)   # rightmost position + 1

# Check if target exists
i = bisect.bisect_left(arr, target)
found = i < len(arr) and arr[i] == target
```

### Corner Cases
- Empty sequence
- Single element
- All duplicates
- Target smaller than min or larger than max

**Essential Questions:**
- [Binary Search](../topics/array/binary_search/01_binary_search.py)
- [Search in Rotated Sorted Array](../topics/array/binary_search/02_search_rotated_sorted.py)

**Recommended Practice Questions:**
- [Kth Smallest Element in a Sorted Matrix](../topics/array/binary_search/03_kth_smallest_sorted_matrix.py)
- [Search a 2D Matrix](../topics/array/binary_search/04_search_2d_matrix.py)
- [Kth Largest Element in an Array](../topics/heap/05_kth_largest_element.py)
- [Find Minimum in Rotated Sorted Array](../topics/array/binary_search/05_find_min_rotated_sorted.py)
- [Median of Two Sorted Arrays](../topics/array/binary_search/06_median_two_sorted_arrays.py)

**Further Reading:**
- [Binary Search 101](https://leetcode.com/problems/binary-search/solutions/423162/binary-search-101/) — the definitive LeetCode post
- [VisuAlgo: Sorting](https://visualgo.net/en/sorting) — watch every sorting algorithm animated

---

## 6. Matrix

### What Is It?

A 2D array. Think of it as a grid where every cell has coordinates (row, col). Many matrix problems are really graph problems in disguise — each cell is a node connected to its 4 neighbors.

```
  A 3×4 matrix:

       col→  0    1    2    3
  row  ┌────┬────┬────┬────┐
   0   │  1 │  2 │  3 │  4 │
       ├────┼────┼────┼────┤
   1   │  5 │  6 │  7 │  8 │
       ├────┼────┼────┼────┤
   2   │  9 │ 10 │ 11 │ 12 │
       └────┴────┴────┴────┘

  Cell (1,2) = 7
  Neighbors of (1,2): up(0,2)=3, down(2,2)=11, left(1,1)=6, right(1,3)=8
```

### Key Patterns & Techniques

**4-Directional Traversal:**

```python
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

for dr, dc in directions:
    nr, nc = row + dr, col + dc
    if 0 <= nr < rows and 0 <= nc < cols:  # boundary check
        # process (nr, nc)
```

**Spiral Traversal:**

```
  ┌→→→→→→→→→→┐
  ↑ 1→ 2→ 3→ 4↓
  ↑           ↓
  ↑ 10 11 12  5↓
  ↑  ←  ←     ↓
  ↑ 9← 8← 7← 6↓
  └←←←←←←←←←←┘

  Order: top row → right col → bottom row (reversed) → left col (reversed)
  Then shrink boundaries and repeat.
```

**Transpose (rows ↔ columns):**

```
  Original:       Transposed:
  1  2  3         1  4  7
  4  5  6    →    2  5  8
  7  8  9         3  6  9

  transposed[j][i] = original[i][j]
```

**Rotate 90° clockwise = Transpose + Reverse each row**

```python
# Create zero matrix
zero = [[0] * cols for _ in range(rows)]

# Copy matrix
copy = [row[:] for row in matrix]

# Transpose
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transposed[j][i] = matrix[i][j]
```

### Corner Cases
- Empty matrix (`[]` or `[[]]`)
- 1x1 matrix
- Single row or single column

**Essential Questions:**
- [Set Matrix Zeroes](../topics/matrix/03_set_matrix_zeroes.py)
- [Spiral Matrix](../topics/matrix/01_spiral_matrix.py)

**Recommended Practice Questions:**
- [Rotate Image](../topics/matrix/04_rotate_image.py)
- [Valid Sudoku](../topics/matrix/05_valid_sudoku.py)

---

## 7. Linked List

### What Is It?

A chain of nodes where each node holds data and a pointer to the next node. Unlike arrays, nodes can live anywhere in memory — they're connected by pointers, not physical proximity.

```
  Singly Linked List:

  head
   ↓
  [10|→]──→[20|→]──→[30|→]──→[40|→]──→ None
  node.val  node.val
  node.next node.next

  Doubly Linked List:

  None ←[←|10|→]⟷[←|20|→]⟷[←|30|→]→ None
          head                  tail


  Inserting 25 between 20 and 30 (O(1) — no shifting!):

  Before: [20|→]──────→[30|→]
                 [25|→]

  After:  [20|→]──→[25|→]──→[30|→]
```

| | Array | Linked List |
|--|-------|-------------|
| Access by index | O(1) | O(n) |
| Insert/delete at known position | O(n) | O(1) |
| Memory | Contiguous block | Scattered nodes |
| Cache performance | Excellent | Poor |

### Key Patterns & Techniques

**Pattern 1: Dummy Head Node**

A dummy (sentinel) node before the real head eliminates special cases for operations at the head.

```
  Without dummy:              With dummy:
  Must check "is head null?"  Always: dummy.next = real_head
  Must handle "delete head"   Delete head? Just update dummy.next
  Return head (might change)  Return dummy.next (always correct)
```

```python
dummy = ListNode(0)
dummy.next = head
# ... do operations ...
return dummy.next  # the real head (may have changed)
```

**Pattern 2: Fast & Slow Pointers (Floyd's)**

```
  Find middle:     slow moves 1 step, fast moves 2 steps

  1 → 2 → 3 → 4 → 5 → None
  S                          start
  F

  1 → 2 → 3 → 4 → 5 → None
      S                      step 1
          F

  1 → 2 → 3 → 4 → 5 → None
          S                  step 2: fast at end, slow at middle!
                  F

  Detect cycle:    if fast and slow ever meet → cycle exists

  1 → 2 → 3 → 4
              ↗ ↓
          6 ← 5         slow and fast will meet inside the cycle
```

**Pattern 3: In-Place Reversal**

```
  Reverse: 1 → 2 → 3 → None

  Step 0:  None   1 → 2 → 3 → None
           prev  curr

  Step 1:  None ← 1    2 → 3 → None     (curr.next = prev)
                 prev  curr

  Step 2:  None ← 1 ← 2    3 → None
                      prev  curr

  Step 3:  None ← 1 ← 2 ← 3
                           prev  curr=None → done!
```

```python
prev, curr = None, head
while curr:
    nxt = curr.next      # save next
    curr.next = prev     # reverse pointer
    prev = curr          # advance prev
    curr = nxt           # advance curr
return prev              # new head
```

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Reverse a linked list" | Iterative: prev/curr/next |
| "Find middle" or "is palindrome" | Fast/slow pointers |
| "Detect cycle" | Fast/slow pointers (Floyd's) |
| "Merge two sorted lists" | Two pointers + dummy head |
| "Remove Nth from end" | Two pointers, N apart |

### Common Mistakes
- Losing reference to the next node before redirecting pointers
- Not handling empty list or single-node list
- Forgetting to return the new head after reversal

### Corner Cases
- Empty list (head is None)
- Single node
- Two nodes
- Cycle in list (clarify with interviewer!)

**Essential Questions:**
- [Reverse Linked List](../topics/linked_list/01_reverse_linked_list.py)
- [Linked List Cycle](../topics/linked_list/02_linked_list_cycle.py)

**Recommended Practice Questions:**
- [Merge Two Sorted Lists](../topics/linked_list/03_merge_two_sorted_lists.py)
- [Merge K Sorted Lists](../topics/linked_list/05_merge_k_sorted_lists.py)
- [Remove Nth Node From End of List](../topics/linked_list/06_remove_nth_from_end.py)
- [Reorder List](../topics/linked_list/07_reorder_list.py)

**Further Reading:**
- [What's a Linked List Anyway?](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d) — basecs (part 1 & 2)

---

## 8. Stack

### What Is It?

A Last-In-First-Out (LIFO) container. Think of a stack of plates — you can only add or remove from the top.

```
  Push 10, 20, 30:              Pop:

  ┌────┐                        ┌────┐
  │ 30 │ ← top (last in)       │ 30 │ ← popped first (last in, first out)
  ├────┤                        └────┘
  │ 20 │                        ┌────┐
  ├────┤                        │ 20 │ ← new top
  │ 10 │                        ├────┤
  └────┘                        │ 10 │
                                └────┘
```

**Python:** Just use a `list` — `append()` = push, `pop()` = pop. Both O(1).

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| Peek (top) | O(1) |
| Search | O(n) |

### Key Patterns & Techniques

**Pattern 1: Matching / Nesting**

Any problem involving matched pairs (parentheses, HTML tags, nested structures) is a stack problem.

```
  Validate "({[]})" :

  Read (  → push   stack: [(]
  Read {  → push   stack: [(, {]
  Read [  → push   stack: [(, {, []
  Read ]  → pop [  match! stack: [(, {]
  Read }  → pop {  match! stack: [(]
  Read )  → pop (  match! stack: []
  Empty stack → VALID ✓

  Validate "({)}" :
  Read (  → push   stack: [(]
  Read {  → push   stack: [(, {]
  Read )  → pop {  MISMATCH! { ≠ ) → INVALID ✗
```

**Pattern 2: Monotonic Stack**

A stack where elements are kept in sorted order (always increasing or always decreasing). This is the key technique for "next greater element" and "next smaller element" problems.

```
  Find next greater element for each position:

  arr = [2, 1, 4, 3]
  result = [-1, -1, -1, -1]

  i=0: push 0          stack: [0]        (indices)
  i=1: arr[1]=1 < arr[0]=2, push  stack: [0, 1]
  i=2: arr[2]=4 > arr[1]=1 → pop 1, result[1]=4
       arr[2]=4 > arr[0]=2 → pop 0, result[0]=4
       push 2              stack: [2]
  i=3: arr[3]=3 < arr[2]=4, push  stack: [2, 3]

  result = [4, 4, -1, -1]
        "next greater for 2 is 4, for 1 is 4, nothing for 4 and 3"
```

```python
def next_greater(arr):
    result = [-1] * len(arr)
    stack = []  # stores indices
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    return result
```

**Pattern 3: Expression Evaluation**

Evaluate arithmetic expressions using two stacks (operands + operators) or convert to postfix first.

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Valid parentheses" or "balanced" | Stack for matching |
| "Next greater/smaller element" | Monotonic stack |
| "Evaluate expression" | Stack(s) for operands/operators |
| "Undo" operation | Stack (push actions, pop to undo) |
| "Nearest greater/smaller on left/right" | Monotonic stack |
| "Histogram" or "trapping water" | Monotonic stack |

### Corner Cases
- Empty stack (popping from empty)
- Stack with one item
- All elements identical

**Essential Questions:**
- [Valid Parentheses](../topics/stack/01_valid_parentheses.py)
- [Implement Queue using Stacks](../topics/queue/01_implement_queue_using_stacks.py)

**Recommended Practice Questions:**
- [Implement Stack using Queues](../topics/queue/02_implement_stack_using_queues.py)
- [Min Stack](../topics/stack/02_min_stack.py)
- [Asteroid Collision](../topics/stack/05_asteroid_collision.py)
- [Evaluate Reverse Polish Notation](../topics/stack/03_evaluate_reverse_polish.py)
- [Basic Calculator](../topics/stack/06_basic_calculator.py)
- [Basic Calculator II](../topics/stack/07_basic_calculator_ii.py)
- [Daily Temperatures](../topics/stack/08_daily_temperatures.py)
- [Trapping Rain Water](../topics/array/two_pointers/07_trapping_rain_water.py)
- [Largest Rectangle in Histogram](../topics/stack/04_largest_rectangle_histogram.py)

**Further Reading:**
- [Stacks and Overflows](https://medium.com/basecs/stacks-and-overflows-dbcf7854dc67) — basecs
- [Monotonic Stack Explained](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems) — comprehensive LeetCode guide

---

## 9. Queue

### What Is It?

A First-In-First-Out (FIFO) container. Think of a line at a ticket counter — first person in line is the first to be served.

```
  Enqueue (add to back):              Dequeue (remove from front):

  front                    back       front                    back
    ↓                       ↓           ↓                       ↓
  ┌────┬────┬────┬────┐              ┌────┬────┬────┐
  │ 10 │ 20 │ 30 │ 40 │              │ 20 │ 30 │ 40 │
  └────┴────┴────┴────┘              └────┴────┴────┘
    ↑                                  ↑
    first in = first out               10 was removed (FIFO)
```

**Critical Python detail:** NEVER use `list` as a queue. `list.pop(0)` is O(n) because it shifts every element. Use `collections.deque` — both `append()` and `popleft()` are O(1).

```python
from collections import deque

q = deque()
q.append(10)        # enqueue to back
q.append(20)
q.popleft()         # dequeue from front → 10
```

| Operation | deque | list (DON'T use) |
|-----------|-------|-------------------|
| Enqueue (append) | O(1) | O(1) |
| Dequeue (popleft) | O(1) | O(n) !!! |

### Key Patterns & Techniques

**Pattern 1: BFS (Breadth-First Search)**

The canonical use for queues. BFS explores nodes level by level — first all neighbors, then all neighbors' neighbors, etc.

```
  BFS from node A:

      A
     / \
    B   C          Level 0: [A]
   / \   \         Level 1: [B, C]
  D   E   F       Level 2: [D, E, F]

  Queue trace:
  [A] → process A, enqueue B, C
  [B, C] → process B, enqueue D, E
  [C, D, E] → process C, enqueue F
  [D, E, F] → process D, E, F
```

**Level-by-level BFS (when you need the level number):**

```python
from collections import deque

queue = deque([root])
level = 0
while queue:
    level_size = len(queue)           # how many nodes at this level
    for _ in range(level_size):
        node = queue.popleft()
        # process node at 'level'
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    level += 1
```

**Why BFS finds shortest path in unweighted graphs:** BFS explores all nodes at distance 1 before any node at distance 2. So the first time you reach a node, it's via the shortest path.

**Pattern 2: Monotonic Deque (Sliding Window Max/Min)**

Maintain a deque of candidates where the front is always the max (or min) of the current window.

### Corner Cases
- Empty queue
- Queue with one item

**Essential Questions:**
- [Implement Stack using Queues](../topics/queue/02_implement_stack_using_queues.py)

**Recommended Practice Questions:**
- [Implement Queue using Stacks](../topics/queue/01_implement_queue_using_stacks.py)
- [Design Circular Queue](../topics/queue/03_design_circular_queue.py)

**Further Reading:**
- [To Queue Or Not To Queue](https://medium.com/basecs/to-queue-or-not-to-queue-2653bcde5b04) — basecs

---

## 10. Tree

### What Is It?

A hierarchical data structure with a root node and children. Each node has exactly one parent (except the root, which has none). A tree with at most 2 children per node is a **binary tree**.

```
  Binary Tree:                    Binary Search Tree (BST):

         1                              8
        / \                           /   \
       2   3                         4     12
      / \   \                       / \   /  \
     4   5   6                     2   6 10   14
                                  BST rule: left < parent < right

  Key terms:
  ┌──── Root: node with no parent (1)
  │  ┌─ Leaf: node with no children (4, 5, 6)
  │  │  ┌ Height: longest path from root to leaf (root=1 has height 2)
  │  │  │ Depth: distance from root (root depth=0, node 4 depth=2)
  ▼  ▼  ▼
```

### Traversal Orders

The four ways to visit every node — memorize these:

```
          1
         / \
        2   3
       / \
      4   5

  In-Order (Left → Root → Right):     4, 2, 5, 1, 3
    └→ For BST: gives sorted order!

  Pre-Order (Root → Left → Right):    1, 2, 4, 5, 3
    └→ Use case: serialize/copy a tree

  Post-Order (Left → Right → Root):   4, 5, 2, 3, 1
    └→ Use case: delete tree, calculate size

  Level-Order (BFS):                  [1], [2, 3], [4, 5]
    └→ Use case: level-by-level processing
```

```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    process(node.val)       # between left and right
    inorder(node.right)

def preorder(node):
    if not node:
        return
    process(node.val)       # before children
    preorder(node.left)
    preorder(node.right)

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    process(node.val)       # after children
```

### BST Properties

The left subtree of every node contains only values **less than** the node. The right subtree contains only values **greater than** the node.

```
  In a BST, binary search works:

  Search for 6:
         8                8 > 6 → go left
        / \
       4   12             4 < 6 → go right
      / \
     2   6    ← found!    O(log n) for balanced tree, O(n) for skewed
```

| BST Operation | Balanced | Skewed (worst) |
|---------------|----------|----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

### Key Patterns & Techniques

**Pattern 1: Recursive Structure**

Most tree problems decompose into: solve for left subtree, solve for right subtree, combine results.

```python
def max_depth(root):
    if not root:                               # base case
        return 0
    left_depth = max_depth(root.left)          # solve left
    right_depth = max_depth(root.right)        # solve right
    return 1 + max(left_depth, right_depth)    # combine
```

**Pattern 2: Returning Multiple Values**

Sometimes a recursive call needs to return more than one thing (e.g. is_balanced AND height).

```python
def is_balanced(root):
    def helper(node):
        if not node:
            return (True, 0)  # (is_balanced, height)
        left_bal, left_h = helper(node.left)
        right_bal, right_h = helper(node.right)
        balanced = left_bal and right_bal and abs(left_h - right_h) <= 1
        return (balanced, 1 + max(left_h, right_h))

    return helper(root)[0]
```

**Pattern 3: Level-Order with Queue**

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
```

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Maximum depth / height" | Recursion (post-order) |
| "Level order" or "by level" | BFS with queue |
| "Validate BST" | In-order traversal (should be sorted) or recursive range check |
| "Lowest common ancestor" | Recursion — where do left and right results both exist? |
| "Serialize / deserialize" | Pre-order + null markers |
| "Path sum" | DFS, track running sum |

### Common Mistakes
- Forgetting `if not node: return` base case
- Confusing depth (from root) vs height (from leaf)
- Not considering that nodes can have negative values in path sum problems

### Corner Cases
- Empty tree (root is None)
- Single node
- Skewed tree (every node has only one child — degenerates to a linked list)

**Essential Questions:**
- [Maximum Depth of Binary Tree](../topics/tree/01_max_depth_binary_tree.py)
- [Invert Binary Tree](../topics/tree/02_invert_binary_tree.py)
- [Lowest Common Ancestor of a BST](../topics/tree/05_lowest_common_ancestor_bst.py)

**Recommended Practice Questions:**
- [Same Tree](../topics/tree/11_same_tree.py)
- [Binary Tree Maximum Path Sum](../topics/tree/12_binary_tree_max_path_sum.py)
- [Binary Tree Level Order Traversal](../topics/tree/04_binary_tree_level_order.py)
- [Lowest Common Ancestor of a Binary Tree](../topics/tree/13_lowest_common_ancestor_bt.py)
- [Binary Tree Right Side View](../topics/tree/08_binary_tree_right_side_view.py)
- [Subtree of Another Tree](../topics/tree/14_subtree_of_another_tree.py)
- [Construct Binary Tree from Preorder and Inorder Traversal](../topics/tree/09_construct_from_preorder_inorder.py)
- [Serialize and Deserialize Binary Tree](../topics/tree/10_serialize_deserialize.py)
- [Validate Binary Search Tree](../topics/tree/06_validate_bst.py)
- [Kth Smallest Element in a BST](../topics/tree/07_kth_smallest_in_bst.py)

**Further Reading:**
- [How To Not Be Stumped By Trees](https://medium.com/basecs/how-to-not-be-stumped-by-trees-5f36208f68a7) — basecs
- [Leaf It Up To Binary Trees](https://medium.com/basecs/leaf-it-up-to-binary-trees-11001aaf746d) — basecs
- [Tree Traversal Visualization](https://visualgo.net/en/bst) — VisuAlgo

---

## 11. Graph

### What Is It?

A graph is a collection of **nodes** (vertices) connected by **edges**. Unlike trees, graphs can have cycles, disconnected components, and edges that go in both directions.

```
  Undirected Graph:           Directed Graph (Digraph):

     A --- B                     A → B
     |   / |                     ↑   ↓
     |  /  |                     D ← C
     C --- D

  Weighted Graph:

     A --5-- B
     |      /|
     3    2  4
     |  /    |
     C --1-- D

  The world runs on graphs:
  • Social networks (people = nodes, friendships = edges)
  • Maps (intersections = nodes, roads = edges with distances)
  • Dependencies (tasks = nodes, prerequisites = directed edges)
```

### Representations

```
  Graph:  A → B, A → C, B → D, C → D

  Adjacency List (most common in interviews):
  {
      'A': ['B', 'C'],
      'B': ['D'],
      'C': ['D'],
      'D': []
  }

  Adjacency Matrix:
       A  B  C  D
  A  [ 0  1  1  0 ]
  B  [ 0  0  0  1 ]
  C  [ 0  0  0  1 ]
  D  [ 0  0  0  0 ]
```

| | Adj List | Adj Matrix |
|--|----------|------------|
| Space | O(V + E) | O(V²) |
| Check if edge exists | O(degree) | O(1) |
| Find all neighbors | O(degree) | O(V) |
| Best for | Sparse graphs | Dense graphs |

### DFS vs BFS — The Two Core Traversals

```
  Graph:
       1
      / \
     2   3
    / \   \
   4   5   6

  DFS (go deep first):  1 → 2 → 4 → 5 → 3 → 6    (uses Stack)
  BFS (go wide first):  1 → 2 → 3 → 4 → 5 → 6    (uses Queue)

  DFS explores one branch completely before backtracking.
  BFS explores all neighbors before moving to the next level.
```

**DFS Template (recursive — for adjacency list):**

```python
def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    # process node
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)
```

**BFS Template:**

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        # process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**DFS on a 2D Grid (very common in interviews):**

```python
def dfs_grid(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if (r, c) in visited or grid[r][c] == '0':
        return
    visited.add((r, c))
    for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
        dfs_grid(grid, r + dr, c + dc, visited)
```

### Topological Sort — Ordering with Dependencies

Used when tasks have prerequisites. Only works on **Directed Acyclic Graphs (DAGs)**.

```
  Course prerequisites:
  Course 1 requires Course 0
  Course 2 requires Course 0
  Course 3 requires Course 1 and Course 2

     0 → 1 → 3
     ↓       ↑
     2 ──────┘

  Topological order: [0, 1, 2, 3] or [0, 2, 1, 3]
  (0 must come first, 3 must come last)

  Kahn's Algorithm (BFS-based):
  1. Count in-degrees (how many edges point INTO each node)
  2. Start with all nodes that have in-degree = 0 (no prerequisites)
  3. Process them, reduce in-degree of their neighbors
  4. When a neighbor's in-degree hits 0, add it to the queue
  5. If all nodes processed → valid order. Otherwise → cycle exists!
```

```python
from collections import deque, defaultdict

def topo_sort(num_nodes, prerequisites):
    graph = defaultdict(list)
    in_degree = [0] * num_nodes
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    queue = deque(i for i in range(num_nodes) if in_degree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return order if len(order) == num_nodes else []  # empty = cycle
```

### When to Use DFS vs BFS

| Use DFS when... | Use BFS when... |
|-----------------|-----------------|
| Finding connected components | Finding **shortest path** (unweighted) |
| Detecting cycles | Level-order traversal |
| Topological sorting | Finding nearest node |
| Exploring all paths | Spreading outward (rotting oranges) |

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Number of islands" or "connected components" | DFS/BFS on grid |
| "Shortest path" (unweighted) | BFS |
| "Course schedule" or "prerequisites" | Topological sort |
| "Clone graph" | BFS/DFS + hash map |
| "Detect cycle" | DFS with coloring (white/gray/black) |

### Common Mistakes
- Forgetting the visited set → infinite loop on cycles
- Modifying the grid during DFS instead of using a visited set (can work, but be careful)
- Using DFS for shortest path (DFS doesn't guarantee shortest!)

### Corner Cases
- Empty graph
- Single node, no edges
- Disconnected graph (multiple components)
- Graph with self-loops
- Graph with cycles

**Essential Questions:**
- [Number of Islands](../topics/graph/01_number_of_islands.py)
- [Flood Fill](../topics/graph/02_flood_fill.py)
- [01 Matrix](../topics/matrix/02_01_matrix.py)

**Recommended Practice Questions:**
- [Rotting Oranges](../topics/graph/05_rotting_oranges.py)
- [Clone Graph](../topics/graph/03_clone_graph.py)
- [Pacific Atlantic Water Flow](../topics/graph/08_pacific_atlantic_water_flow.py)
- [Course Schedule](../topics/graph/04_course_schedule.py)

**Further Reading:**
- [From Theory To Practice: Representing Graphs](https://medium.com/basecs/from-theory-to-practice-representing-graphs-cfd782c5be38) — basecs
- [Deep Dive Through A Graph: DFS](https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13) — basecs
- [Going Broad In A Graph: BFS](https://medium.com/basecs/going-broad-in-a-graph-bfs-traversal-959bd1a09255) — basecs
- [Graph Visualization](https://visualgo.net/en/dfsbfs) — VisuAlgo

---

## 12. Heap / Priority Queue

### What Is It?

A heap is a complete binary tree where every parent is smaller (min-heap) or larger (max-heap) than its children. It's stored as a flat array — no actual tree nodes needed.

```
  Min-Heap (parent ≤ children):

  As a tree:            As an array:
       1                [1, 3, 5, 7, 4, 8]
      / \               idx: 0  1  2  3  4  5
     3   5
    / \  /              Parent of i:    (i-1) // 2
   7  4 8              Left child of i:  2*i + 1
                        Right child of i: 2*i + 2

  The root is ALWAYS the minimum. That's the magic.

  Insert 2:                    Pop (remove min):
  1. Add to end: [..., 2]      1. Replace root with last: [8, 3, 5, 7, 4]
  2. "Bubble up" — swap with   2. "Bubble down" — swap with smaller child
     parent until heap valid      until heap valid

       1            1                8            3
      / \          / \              / \          / \
     3   5   →    3   2    →      3   5   →    4   5
    / \  / \     / \  / \        / \          / \
   7  4 8  2   7  4 8  5       7   4        7   8
```

| Operation | Time | Why |
|-----------|------|-----|
| Find min/max | O(1) | Always at root |
| Insert | O(log n) | Bubble up at most tree height |
| Remove min/max | O(log n) | Bubble down at most tree height |
| Build heap from array | O(n) | Not O(n log n)! Bottom-up heapify is O(n) |

### Python heapq (min-heap only)

```python
import heapq

h = []
heapq.heappush(h, 5)         # insert
heapq.heappush(h, 2)
heapq.heappush(h, 8)
heapq.heappop(h)              # → 2 (smallest)
h[0]                           # → 5 (peek at min, don't pop)

heapq.heapify(some_list)      # convert list to heap in O(n)

# Max-heap trick: negate values
heapq.heappush(h, -val)       # push negative
max_val = -heapq.heappop(h)   # pop and negate back
```

### Key Patterns & Techniques

**Pattern 1: Top-K Elements**

If the problem says "top K" or "K largest/smallest", think heap.

```
  Find 3 largest from [4, 1, 7, 3, 9, 2]:

  Use a MIN-heap of size 3 (keeps the 3 largest):
  Process 4: heap = [4]          size ≤ 3, just push
  Process 1: heap = [1, 4]       size ≤ 3, just push
  Process 7: heap = [1, 4, 7]    size = 3, just push
  Process 3: heap = [1, 3, 4, 7] size > 3, pop min(1) → heap = [3, 4, 7]
  Process 9: heap = [3, 4, 7, 9] size > 3, pop min(3) → heap = [4, 7, 9]
  Process 2: 2 < heap[0]=4, skip (too small to be in top 3)

  Result: [4, 7, 9]   Time: O(n log k)
```

**Pattern 2: Two Heaps for Median**

```
  Find median of streaming numbers:

  Split numbers into two halves:
  ┌──────────────────┬──────────────────┐
  │   MAX-Heap       │   MIN-Heap       │
  │ (lower half)     │ (upper half)     │
  │ gives largest of │ gives smallest   │
  │ the small nums   │ of the big nums  │
  └──────────────────┴──────────────────┘

  Median = top of the larger heap (or average of both tops)
  Keep heaps balanced: sizes differ by at most 1
```

**Pattern 3: Merge K Sorted Lists**

Push the head of each list into a min-heap. Pop the smallest, advance that list, push next element. Repeat.

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "K largest" or "K closest" | Min-heap of size K |
| "K smallest" | Max-heap of size K |
| "Median from stream" | Two heaps (max + min) |
| "Merge K sorted..." | Min-heap with K entries |
| "Continuously find min/max" | Heap |

**Essential Questions:**
- [Merge K Sorted Lists](../topics/linked_list/05_merge_k_sorted_lists.py)
- [K Closest Points to Origin](../topics/heap/01_k_closest_points.py)

**Recommended Practice Questions:**
- [Top K Frequent Elements](../topics/heap/04_top_k_frequent_elements.py)
- [Find Median from Data Stream](../topics/heap/02_find_median_data_stream.py)

**Further Reading:**
- [Learning to Love Heaps](https://medium.com/basecs/learning-to-love-heaps-cef2b273a238) — basecs
- [Heap Visualization](https://visualgo.net/en/heap) — VisuAlgo

---

## 13. Trie (Prefix Tree)

### What Is It?

A tree where each path from root to a node represents a prefix. Tries make prefix operations blazingly fast — O(m) where m is the word length, regardless of how many words are stored.

```
  Trie storing: ["app", "apple", "ape", "bat", "ball"]

               (root)
              /      \
            a          b
            |          |
            p          a
           / \         |  \
          p   e*       t*  l
          |                |
          l                l*
          |
          e*

  * = marks end of a complete word

  Search "ape":  root → a → p → e* → found! ✓
  Search "api":  root → a → p → no 'i' child → not found ✗
  Prefix "ap":   root → a → p → exists! (both "app*", "apple*", "ape*" share this prefix)
```

### Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}     # char → TrieNode
        self.is_end = False    # marks complete word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._traverse(prefix) is not None

    def _traverse(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
```

### When to Use a Trie

| Scenario | Why Trie wins |
|----------|---------------|
| Autocomplete / typeahead | Find all words starting with prefix |
| Spell checker | Check if word exists, suggest corrections |
| Word search in grid | DFS + trie prunes dead-end paths |
| Longest common prefix | Traverse until paths diverge |
| Search among N words of length M | O(M) per search vs O(N*M) brute force |

### Corner Cases
- Empty string
- Searching an empty trie
- Words that are prefixes of other words ("app" vs "apple")

**Essential Questions:**
- [Implement Trie (Prefix Tree)](../topics/trie/01_implement_trie.py)

**Recommended Practice Questions:**
- [Add and Search Word](../topics/trie/02_add_search_word.py)
- [Word Break](../topics/dynamic_programming/03_word_break.py)
- [Word Search II](../topics/trie/03_word_search_ii.py)

**Further Reading:**
- [Trying to Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014) — basecs

---

## 14. Interval

### What Is It?

Interval problems deal with ranges `[start, end]`. The core challenge is handling overlapping intervals correctly.

```
  Timeline visualization:

  Interval A: [1, 5]     ████████████
  Interval B: [3, 7]           ██████████████
  Interval C: [9, 12]                           █████████
  Interval D: [10, 11]                            ████

  Overlap cases:
  ┌───────────────────────────────────────────┐
  │  A: ████████     B: ████████              │  Partial overlap
  │  A: ████████████████                      │  A contains B
  │  B:     ████████                          │
  │  A: ████████  B:   ████████               │  No overlap (gap)
  │  A: ████████  B: ████████                 │  Touch at endpoint
  └───────────────────────────────────────────┘
```

### Key Patterns & Techniques

**Step 1 (Almost Always): Sort by Start Time**

```python
intervals.sort(key=lambda x: x[0])
```

**Check Overlap:**

```python
def overlaps(a, b):
    return a[0] < b[1] and b[0] < a[1]
    #      a starts before b ends AND b starts before a ends
```

**Merge Overlapping Intervals:**

```
  Input:  [1,3], [2,6], [8,10], [15,18]

  Sort:   [1,3], [2,6], [8,10], [15,18]  (already sorted)

  [1,3] + [2,6] → overlap! merge to [1,6]
  [1,6] + [8,10] → no overlap, start new
  [8,10] + [15,18] → no overlap, start new

  Output: [1,6], [8,10], [15,18]
```

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:                  # overlap
            merged[-1][1] = max(merged[-1][1], end) # extend
        else:
            merged.append([start, end])             # new interval
    return merged
```

**Sweep Line (for complex counting):**

When you need "max number of overlapping intervals" (e.g. meeting rooms), use events:

```
  Meetings: [0,30], [5,10], [15,20]

  Events: [(0,+1), (5,+1), (10,-1), (15,+1), (20,-1), (30,-1)]
  Sort:   [(0,+1), (5,+1), (10,-1), (15,+1), (20,-1), (30,-1)]

  Sweep: count=0
  t=0:  count=1
  t=5:  count=2  ← max overlap = 2 rooms needed
  t=10: count=1
  t=15: count=2
  t=20: count=1
  t=30: count=0
```

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Merge intervals" | Sort + merge |
| "Insert interval" | Find position, merge neighbors |
| "Meeting rooms" | Sweep line or sort starts/ends |
| "Non-overlapping" | Sort + greedy (pick earliest ending) |

### Corner Cases
- Empty list of intervals
- Single interval
- All intervals overlap
- Intervals touching at endpoints (clarify if this counts as overlap!)
- Intervals not sorted

**Essential Questions:**
- [Merge Intervals](../topics/interval/01_merge_intervals.py)
- [Insert Interval](../topics/interval/02_insert_interval.py)

**Recommended Practice Questions:**
- [Non-overlapping Intervals](../topics/interval/03_non_overlapping_intervals.py)

---

## 15. Dynamic Programming

### What Is It?

Dynamic Programming (DP) solves problems by breaking them into overlapping subproblems and caching results. It's recursion + memoization, or equivalently, building solutions bottom-up from smaller cases.

```
  The DP insight — Fibonacci:

  Without DP (exponential):       With DP (linear):

  fib(5)                          fib(5) — just look up cached results!
  ├── fib(4)
  │   ├── fib(3)                  dp = [0, 1, 1, 2, 3, 5]
  │   │   ├── fib(2)                        ↑  ↑  ↑
  │   │   │   ├── fib(1) = 1       each entry computed ONCE
  │   │   │   └── fib(0) = 0       using the previous two
  │   │   └── fib(1) = 1
  │   └── fib(2)          ← REPEATED!
  │       ├── fib(1) = 1
  │       └── fib(0) = 0
  └── fib(3)               ← REPEATED!
      ├── fib(2)           ← REPEATED!
      └── fib(1) = 1

  O(2^n) calls              O(n) computations
```

### How to Solve Any DP Problem (5-Step Framework)

```
  1. DEFINE STATE
     "What does dp[i] represent?"
     e.g., dp[i] = minimum coins needed for amount i

  2. FIND RECURRENCE
     "How does dp[i] relate to smaller states?"
     e.g., dp[i] = min(dp[i - coin] + 1) for each coin

  3. SET BASE CASE
     "What are the trivial answers?"
     e.g., dp[0] = 0 (zero coins for amount 0)

  4. DETERMINE ORDER
     "What must be computed first?"
     e.g., dp[0], dp[1], dp[2], ... (left to right)

  5. RETURN ANSWER
     "Where is the final answer?"
     e.g., dp[amount]
```

### Top-Down vs Bottom-Up

```
  Top-Down (Memoization):           Bottom-Up (Tabulation):

  Start from the answer,            Start from base case,
  recurse down to base case,        build up to the answer,
  cache along the way               fill a table iteratively

  fib(5) → fib(4) → fib(3)...      dp[0]=0, dp[1]=1, dp[2]=1...dp[5]=5

  Pros: Only computes needed        Pros: No recursion overhead,
        subproblems                        no stack overflow risk
  Cons: Recursion overhead,         Cons: May compute unnecessary
        stack depth limit                  subproblems
```

```python
# Top-Down
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Bottom-Up
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space-Optimized Bottom-Up (only keep last 2)
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
```

### Common DP Patterns

**Pattern 1: Linear DP** — `dp[i]` depends on previous elements

```
  Climbing Stairs: dp[i] = dp[i-1] + dp[i-2]
  House Robber:    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

**Pattern 2: 0/1 Knapsack** — include or exclude each item

```
  "Can you partition array into two equal-sum subsets?"

  For each number: either include in subset or don't
  dp[i][s] = "can first i numbers make sum s?"
  dp[i][s] = dp[i-1][s] OR dp[i-1][s - nums[i]]
```

**Pattern 3: Two-String DP** — compare/align two sequences

```
  Longest Common Subsequence of "ABCDE" and "ACE":

       ""  A  C  E
  ""  [ 0  0  0  0 ]
   A  [ 0  1  1  1 ]     if chars match: dp[i][j] = dp[i-1][j-1] + 1
   B  [ 0  1  1  1 ]     if not:         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
   C  [ 0  1  2  2 ]
   D  [ 0  1  2  2 ]     Answer: dp[5][3] = 3  ("ACE")
   E  [ 0  1  2  3 ]
```

**Pattern 4: Interval DP** — optimal solution for a range

```
  dp[i][j] = best answer for subarray arr[i..j]
  Try every split point k: dp[i][j] = best(dp[i][k] + dp[k+1][j] + cost)
```

### How to Recognize

| If the problem says... | Think about... |
|------------------------|----------------|
| "Minimum / maximum number of..." | DP optimization |
| "How many ways to..." | DP counting |
| "Is it possible to..." | DP feasibility (boolean) |
| "Longest / shortest subsequence" | DP on sequences |
| Previous choices affect future options | DP (not greedy) |

### Space Optimization Tip

If `dp[i]` only depends on `dp[i-1]` (and maybe `dp[i-2]`), you don't need the entire array — just keep the last 1-2 values. For 2D DP where each row depends only on the previous row, keep just 2 rows.

### Common Mistakes
- Wrong base case or missing base case
- Wrong traversal order (especially in 2D DP)
- Not considering negative numbers in "max subarray" problems
- Confusing subsequence (skip elements OK) with subarray (must be contiguous)

### Corner Cases
- Empty input
- Single element
- All negative values
- Very large inputs (watch for integer overflow in other languages)

**Essential Questions:**
- [Climbing Stairs](../topics/dynamic_programming/01_climbing_stairs.py)
- [Coin Change](../topics/dynamic_programming/02_coin_change.py)
- [House Robber](../topics/dynamic_programming/08_house_robber.py)
- [Longest Increasing Subsequence](../topics/dynamic_programming/09_longest_increasing_subsequence.py)

**Recommended Practice Questions:**
- [Partition Equal Subset Sum](../topics/dynamic_programming/06_partition_equal_subset_sum.py)
- [Longest Common Subsequence](../topics/dynamic_programming/10_longest_common_subsequence.py)
- [Word Break](../topics/dynamic_programming/03_word_break.py)
- [Combination Sum IV](../topics/dynamic_programming/11_combination_sum_iv.py)
- [House Robber II](../topics/dynamic_programming/12_house_robber_ii.py)
- [Decode Ways](../topics/dynamic_programming/13_decode_ways.py)
- [Unique Paths](../topics/dynamic_programming/05_unique_paths.py)
- [Jump Game](../topics/dynamic_programming/14_jump_game.py)

**Further Reading:**
- [Dynamic Programming — 7 Steps to Solve Any DP Problem](https://dev.to/nikolaotasevic/dynamic-programming--7-steps-to-solve-any-dp-interview-problem-3870) — clear step-by-step framework
- [Demystifying Dynamic Programming](https://www.freecodecamp.org/news/demystifying-dynamic-programming-3efafb8d4296) — freeCodeCamp
- [Less Repetition, More DP](https://medium.com/basecs/less-repetition-more-dynamic-programming-43d29830a630) — basecs
- [NeetCode DP Playlist](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_yhUmJp3xzeDYG6LoLy) — video walkthroughs

---

## 16. Bit Manipulation / Math

### Bit Manipulation

Computers think in binary. Bit manipulation operates directly on the 0s and 1s, which can lead to elegant O(1) space solutions.

```
  Decimal → Binary:

  13 = 8 + 4 + 1 = 2³ + 2² + 2⁰ = 1101 in binary

  Position:  3  2  1  0
  Bits:      1  1  0  1  = 13
             ↑        ↑
         MSB (most   LSB (least
          significant) significant)

  Bitwise Operations:

  AND (&):   1101        OR (|):    1101        XOR (^):   1101
             1010                   1010                    1010
           ──────                 ──────                  ──────
             1000 (8)              1111 (15)               0111 (7)

  NOT (~):  ~1101 = 0010   (flips all bits)
  LEFT SHIFT (<<):  1101 << 1 = 11010  (×2)
  RIGHT SHIFT (>>): 1101 >> 1 = 0110   (÷2)
```

### Key Bit Tricks

| Trick | Code | Why It Works |
|-------|------|--------------|
| Check if odd | `n & 1` | Last bit is 1 for odd numbers |
| Check if power of 2 | `n & (n-1) == 0` | Powers of 2 have exactly one set bit |
| Clear lowest set bit | `n & (n-1)` | Turns off the rightmost 1-bit |
| Get lowest set bit | `n & (-n)` | Isolates the rightmost 1-bit |
| XOR to find single | `a ^ a == 0` | XOR of a number with itself is 0 |
| Count set bits | `while n: n &= n-1; count+=1` | Brian Kernighan's algorithm |
| Set bit at position k | `n \| (1 << k)` | OR with a mask |
| Clear bit at position k | `n & ~(1 << k)` | AND with inverted mask |

**The XOR Trick:**

```
  Find the single number in [4, 1, 2, 1, 2]:

  4 ^ 1 ^ 2 ^ 1 ^ 2
  = 4 ^ (1 ^ 1) ^ (2 ^ 2)     XOR is commutative & associative
  = 4 ^ 0 ^ 0
  = 4  ✓

  XOR properties: a ^ 0 = a,  a ^ a = 0,  a ^ b ^ a = b
```

### Math for Interviews

**Common Formulas:**

| Formula | Expression |
|---------|------------|
| Sum of 1 to N | `N * (N + 1) // 2` |
| Check if even | `n % 2 == 0` (or `n & 1 == 0`) |
| Permutations (k from n) | `n! / (n-k)!` |
| Combinations (k from n) | `n! / (k! * (n-k)!)` |

**Comparing Floats:**
Never use `==` with floats. Use: `abs(x - y) <= 1e-9`

**Fast Exponentiation (O(log n)):**
To compute x^n, square the base and halve the exponent each step instead of multiplying n times.

```
  2^10:
  2^10 = (2^5)² = ((2^2)² × 2)² = 1024

  Instead of 10 multiplications → only 4
```

### Corner Cases
- Negative numbers (two's complement in most languages)
- Division/modulo by 0
- Integer overflow (less relevant in Python, but mention in interviews)
- Floating point precision

**Essential Questions (TIH - Binary):**
- [Sum of Two Integers](../topics/binary_and_math/02_sum_of_two_integers.py)
- [Number of 1 Bits](../topics/binary_and_math/03_number_of_1_bits.py)

**Recommended Practice Questions (TIH - Binary):**
- [Counting Bits](../topics/binary_and_math/04_counting_bits.py)
- [Missing Number](../topics/binary_and_math/05_missing_number.py)
- [Reverse Bits](../topics/binary_and_math/06_reverse_bits.py)
- [Single Number](../topics/binary_and_math/07_single_number.py)

**Essential Questions (TIH - Math):**
- [Pow(x, n)](../topics/binary_and_math/08_pow_x_n.py)
- [Sqrt(x)](../topics/binary_and_math/09_sqrt_x.py)

---

## Quick Reference: Python Toolkit for Interviews

| Need | Tool | Example |
|------|------|---------|
| Hash map | `dict` / `defaultdict` | `d = defaultdict(list)` |
| Count things | `Counter` | `Counter("aab") → {'a':2, 'b':1}` |
| O(1) membership | `set` | `if x in seen` |
| Queue (BFS) | `deque` | `q.append(x)`, `q.popleft()` |
| Min-heap | `heapq` | `heappush(h, val)`, `heappop(h)` |
| Max-heap | `heapq` (negate) | `heappush(h, -val)` |
| Stable sort | `sorted()` / `.sort()` | `sorted(arr, key=lambda x: x[0])` |
| Binary search | `bisect` | `bisect_left(arr, target)` |
| Infinity | `float('inf')` | `min_val = float('inf')` |
| Permutations | `itertools.permutations` | `permutations([1,2,3])` |
| Combinations | `itertools.combinations` | `combinations([1,2,3], 2)` |
| Cache recursion | `@lru_cache(None)` | Memoize recursive calls |

---

## The Problem-Solving Flowchart

When you see a new problem, run through this mental checklist:

```
  ┌──────────────────────────────┐
  │  Read the problem carefully  │
  └──────────────┬───────────────┘
                 ▼
  ┌──────────────────────────────┐
  │  What data structure is the  │
  │  input? Array? String? Tree? │
  └──────────────┬───────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  Is the input sorted?        │──→  │ Binary Search        │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  Need O(1) lookup?           │──→  │ Hash Map / Set       │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  Subarray / substring?       │──→  │ Sliding Window       │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  "Top K" / "Kth largest"?    │──→  │ Heap                 │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  Tree / graph traversal?     │──→  │ DFS / BFS            │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  "All combinations/perms"?   │──→  │ Backtracking         │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  "Min/max" with choices?     │──→  │ Dynamic Programming  │
  └──────────────┬───────────────┘     └─────────────────────┘
                 ▼
  ┌──────────────────────────────┐     ┌─────────────────────┐
  │  Intervals / scheduling?     │──→  │ Sort + Sweep / Merge │
  └──────────────────────────────┘     └─────────────────────┘
```

---

*Study resources referenced throughout this guide:*
- *[VisuAlgo](https://visualgo.net/) — algorithm visualizations*
- *[basecs](https://medium.com/basecs) — illustrated CS fundamentals by Vaidehi Joshi*
- *[NeetCode](https://neetcode.io/) — structured problem roadmap and video explanations*
- *[LeetCode Discuss](https://leetcode.com/discuss/) — community solutions and pattern guides*
