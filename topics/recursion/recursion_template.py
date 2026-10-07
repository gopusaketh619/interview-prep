# ============================================================
# RECURSION / BACKTRACKING - PATTERN TEMPLATE
# ============================================================
#
# Recursion: solving a problem by breaking it into smaller
# instances of the same problem. Must have a base case.
#
# Backtracking: a refined recursion that explores all candidates
# and abandons ("backtracks") invalid paths early.
#
# THE TWO RULES OF RECURSION:
#   1. Every recursive function MUST have a base case
#   2. Every recursive call MUST move toward the base case
#
# WHEN TO USE:
#   - "Generate all..." (subsets, permutations, combinations)
#   - "Find all valid..." (paths, arrangements)
#   - "Can you partition/split into..."
#   - Constraint satisfaction (Sudoku, N-Queens)
#
# COMMON MISTAKES:
#   - Forgetting base case → infinite recursion
#   - Not copying path (result.append(path[:]) not path)
#   - Not un-choosing after exploration (missing pop)
#   - Not skipping duplicates → duplicate results
#
# ============================================================
# TEMPLATE DECISION FLOWCHART:
#
#   "Does order matter?"
#        │
#     YES → Permutation (loop from 0, used[])
#     NO  → "Fixed size k?"
#              │
#           YES → Combination (loop from start, stop at k)
#           NO  → Subset (loop from start, save every node)
#
#   "Has duplicates?" → sort() + add skip line
#
# ============================================================
# GENERIC BACKTRACKING TEMPLATE:
#
#   def backtrack(state):
#       if base_case(state):
#           save_result()
#           return
#       for choice in available_choices(state):
#           make_choice(choice)          # append, mark used
#           backtrack(next_state)        # recurse deeper
#           undo_choice(choice)          # pop, unmark
#
# ============================================================


# ============================================================
# 1. SUBSETS (no duplicates)
# ============================================================
# Save at every node, loop forward from start.
# Each element: pick or don't pick → 2^n total subsets.
#
# Time: O(n * 2^n) | Space: O(n) recursion depth

def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])        # choose
            backtrack(i + 1, path)      # explore (move forward)
            path.pop()                  # unchoose

    backtrack(0, [])
    return result


# Decision tree for subsets([1, 2, 3]):
#
#                      []  ← SAVE
#                /      |      \
#           pick 1    pick 2    pick 3
#             |         |         |
#           [1] SAVE  [2] SAVE  [3] SAVE
#          /    \       |
#     pick 2  pick 3  pick 3
#       |       |       |
#    [1,2]   [1,3]   [2,3]
#     SAVE    SAVE    SAVE
#       |
#    pick 3
#       |
#   [1,2,3] SAVE
#
# Result: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

print("--- 1. Subsets ---")
print(subsets([1, 2, 3]))


# ============================================================
# 2. SUBSETS WITH DUPLICATES
# ============================================================
# Sort so duplicates are adjacent, skip same value at same level.
# Skip rule: if i > start and nums[i] == nums[i-1]: continue
#
# Time: O(n * 2^n) | Space: O(n) recursion depth

def subsets_with_dup(nums):
    nums.sort()
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            # "Don't pick the same value twice at the same decision level"
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])        # choose
            backtrack(i + 1, path)      # explore
            path.pop()                  # unchoose

    backtrack(0, [])
    return result


# Decision tree for subsets_with_dup([1, 2, 2]):
# After sort: [1, 2, 2]
#
#                    []
#              ┌──────┴──────┐
#             [1]           [2]
#          ┌───┘             │
#        [1,2]             [2,2]
#          │
#       [1,2,2]
#
# Skipped branches:
#   - At root, j=2: nums[2]==nums[1] (2==2), j>start → SKIP
#   - Inside [1], j=2: nums[2]==nums[1] (2==2), j>start → SKIP

print("\n--- 2. Subsets with dups ---")
print(subsets_with_dup([1, 2, 2]))


# ============================================================
# 3. COMBINATIONS (no duplicates)
# ============================================================
# Like subsets but only save when path has exactly k elements.
# Loop forward from start to avoid duplicate sets.
#
# Time: O(k * C(n,k)) | Space: O(k) recursion depth

def combinations(nums, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, len(nums)):
            path.append(nums[i])        # choose
            backtrack(i + 1, path)      # explore
            path.pop()                  # unchoose

    backtrack(0, [])
    return result


# Decision tree for combinations([1,2,3,4], k=2):
#
#   path=[]
#   ├── pick 1 → [1]
#   │   ├── pick 2 → [1,2] SAVE ✓
#   │   ├── pick 3 → [1,3] SAVE ✓
#   │   └── pick 4 → [1,4] SAVE ✓
#   ├── pick 2 → [2]
#   │   ├── pick 3 → [2,3] SAVE ✓
#   │   └── pick 4 → [2,4] SAVE ✓
#   ├── pick 3 → [3]
#   │   └── pick 4 → [3,4] SAVE ✓
#   └── pick 4 → [4]
#       └── (no more, len < k)
#
# Result: C(4,2) = 6

print("\n--- 3. Combinations ---")
print(combinations([1, 2, 3, 4], 2))


# ============================================================
# 4. COMBINATIONS WITH DUPLICATES
# ============================================================
# Sort + skip same value at same level. Identical skip rule to
# subsets with dups.
#
# Time: O(k * C(n,k)) | Space: O(k) recursion depth

def combinations_with_dup(nums, k):
    nums.sort()
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])        # choose
            backtrack(i + 1, path)      # explore
            path.pop()                  # unchoose

    backtrack(0, [])
    return result


# Decision tree for combinations_with_dup([4,5,5,7], k=2):
# After sort: [4, 5, 5, 7]
#
#   path=[]
#   ├── pick 4 → [4]
#   │   ├── pick 5 → [4,5] SAVE ✓
#   │   ├── pick 5 → SKIP (nums[2]==nums[1], i>start)
#   │   └── pick 7 → [4,7] SAVE ✓
#   ├── pick 5 → [5]
#   │   ├── pick 5 → [5,5] SAVE ✓ (i==start, NOT skipped)
#   │   └── pick 7 → [5,7] SAVE ✓
#   ├── pick 5 → SKIP (nums[2]==nums[1], i>start)
#   └── pick 7 → [7] (len < k, nothing saved)

print("\n--- 4. Combinations with dups ---")
print(combinations_with_dup([4, 5, 5, 7], 2))


# ============================================================
# 5. PERMUTATIONS (no duplicates)
# ============================================================
# Order matters: [1,2] and [2,1] are different permutations.
# Loop always starts from 0, use used[] to skip items already
# in the current path.
#
# Time: O(n * n!) | Space: O(n) recursion depth

def permutations(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):      # always start from 0
            if used[i]:
                continue                # skip items already in path
            used[i] = True
            path.append(nums[i])        # choose
            backtrack(path)             # explore
            path.pop()                  # unchoose
            used[i] = False

    backtrack([])
    return result


# Decision tree for permutations([1, 2, 3]):
#
#                           path=[]
#                    /         |         \
#               pick 1       pick 2       pick 3
#                 |             |             |
#              [1]           [2]           [3]
#             /    \        /    \        /    \
#         pick 2  pick 3  pick 1  pick 3  pick 1  pick 2
#           |       |       |       |       |       |
#        [1,2]   [1,3]   [2,1]   [2,3]   [3,1]   [3,2]
#           |       |       |       |       |       |
#        pick 3  pick 2  pick 3  pick 1  pick 2  pick 1
#           |       |       |       |       |       |
#       [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
#         SAVE    SAVE    SAVE    SAVE    SAVE    SAVE
#
# Result: 3! = 6 permutations

print("\n--- 5. Permutations ---")
print(permutations([1, 2, 3]))


# ============================================================
# 6. PERMUTATIONS WITH DUPLICATES
# ============================================================
# Sort + skip using used[] check.
# Rule: "Use duplicates in order — only pick nums[i] if
# the previous identical value nums[i-1] is already in use."
#
# Skip: if i > 0 and nums[i] == nums[i-1] and not used[i-1]
#   - not used[i-1] means the previous dup was backtracked,
#     so picking this one would duplicate its entire subtree.
#
# Time: O(n * n!) | Space: O(n) recursion depth

def permutations_with_dup(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            # "If previous identical value is NOT in use, skip —
            # it already explored this exact subtree."
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])        # choose
            backtrack(path)             # explore
            path.pop()                  # unchoose
            used[i] = False

    backtrack([])
    return result


# Decision tree for permutations_with_dup([1, 1, 2]):
# After sort: [1a, 1b, 2]
#
#                         path=[]
#                  /         |         \
#             pick 1a    pick 1b     pick 2
#               |        SKIP ✗        |
#            [1a]       (1a not      [2]
#           /     \      in use)       |
#      pick 1b  pick 2            pick 1a
#        |        |                  |
#     [1a,1b]  [1a,2]            [2,1a]
#        |        |                  |
#     pick 2   pick 1b           pick 1b
#        |        |                  |
#    [1a,1b,2] [1a,2,1b]       [2,1a,1b]
#      SAVE      SAVE             SAVE
#
# Result: [1,1,2], [1,2,1], [2,1,1] — 3 unique (pruned from 6)

print("\n--- 6. Permutations with dups ---")
print(permutations_with_dup([1, 1, 2]))


# ============================================================
# QUICK REFERENCE — THE 3 KNOBS
# ============================================================
#
# | Problem      | When to save?  | Loop starts at? | Reuse prevented by? |
# |--------------|----------------|-----------------|---------------------|
# | Subsets      | Every node     | start (forward) | i + 1               |
# | Combinations | len == k       | start (forward) | i + 1               |
# | Permutations | len == n       | 0 (always)      | used[]              |
#
# DUPLICATE SKIP CONDITIONS (add after sort):
#
# | Problem        | Skip line                                            |
# |----------------|------------------------------------------------------|
# | Subsets/Combos | if i > start and nums[i] == nums[i-1]: continue     |
# | Permutations   | if i > 0 and nums[i] == nums[i-1] and not used[i-1] |
#
# RESULT COUNTS:
#
# | Problem      | No Dups       | With Dups          |
# |--------------|---------------|--------------------|
# | Subsets      | 2^n           | ≤ 2^n (pruned)     |
# | Combinations | C(n,k)        | ≤ C(n,k) (pruned)  |
# | Permutations | n!            | ≤ n! (pruned)      |
#
# ============================================================
# TIPS FOR VISUALIZING RECURSION
# ============================================================
#
# The Maze Mental Model:
#   path.append() = walk through a door
#   backtrack()   = keep exploring deeper
#   path.pop()    = walk back to the fork, try the next door
#
# How to Practice:
#   - Trace TINY inputs first (n=1, n=2)
#   - Draw the decision tree on paper
#   - Add print(f"path={path}") to see recursion in real time
#   - Focus on ONE level at a time
#   - Trust the pattern once verified on small input
#   - Memorize the 3 templates, not the traces
# ============================================================
