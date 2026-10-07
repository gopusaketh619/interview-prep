# ============================================================
# SORTING ALGORITHMS - PATTERN TEMPLATE
# ============================================================
#
# Sorting arranges elements in a specific order (ascending/descending).
# Python's built-in sort() uses TimSort: O(n log n), stable.
#
# KEY ALGORITHMS:
#
#   1. Merge Sort — Divide and Conquer, stable, O(n log n)
#      - Split array in half, sort each half, merge.
#      - Space: O(n) for merging.
#
#   2. Quick Sort — Divide and Conquer, not stable, O(n log n) avg
#      - Pick pivot, partition around it, recurse on halves.
#      - Space: O(log n) for recursion stack.
#      - Worst case: O(n²) if pivot is always min/max.
#
#   3. Counting Sort — Non-comparison, O(n + k)
#      - Count occurrences of each value, reconstruct sorted array.
#      - Only works for bounded integer ranges.
#
#   4. Heap Sort — In-place, not stable, O(n log n)
#      - Build max-heap, repeatedly extract max.
#
# PYTHON BUILT-IN:
#   arr.sort()           # in-place, returns None
#   sorted(arr)          # returns new sorted list
#   arr.sort(key=func)   # custom sort key
#   arr.sort(reverse=True)  # descending
#
# WHEN TO USE:
#   - Quick Sort: general purpose, best average case
#   - Merge Sort: need stability or sorting linked lists
#   - Counting Sort: integers in small range
#   - Python built-in: almost always (unless asked to implement)
#
# STABILITY: A stable sort preserves relative order of equal elements.
#   Stable: Merge Sort, Insertion Sort, Tim Sort
#   Unstable: Quick Sort, Heap Sort
#
# TIME: O(n log n) comparison-based lower bound
# SPACE: Varies (O(1) heap sort to O(n) merge sort)
# ============================================================
