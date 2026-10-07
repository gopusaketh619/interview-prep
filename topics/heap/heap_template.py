# ============================================================
# HEAP / PRIORITY QUEUE - PATTERN TEMPLATE
# ============================================================
#
# A heap is a complete binary tree satisfying the heap property:
#   Min-heap: parent <= children (root = minimum)
#   Max-heap: parent >= children (root = maximum)
#
# Python's heapq module implements a MIN-HEAP.
#
# BASIC OPERATIONS:
#   import heapq
#   heap = []
#   heapq.heappush(heap, val)      # push O(log n)
#   heapq.heappop(heap)            # pop min O(log n)
#   heap[0]                        # peek min O(1)
#   heapq.heapify(arr)             # build heap O(n)
#
# MAX-HEAP TRICK:
#   heapq.heappush(heap, -val)     # negate on push
#   max_val = -heapq.heappop(heap) # negate on pop
#
# HEAP WITH TUPLES (for priority + data):
#   heapq.heappush(heap, (priority, counter, data))
#   # counter breaks ties when priorities are equal
#
# KEY PATTERNS:
#
#   1. Top-K Largest:
#      Use a min-heap of size K. Push elements, pop when size > K.
#      After processing all elements, heap contains K largest.
#
#   2. Top-K Smallest:
#      Use a max-heap of size K (negate values).
#
#   3. Merge K Sorted:
#      Push first element of each list. Pop min, push next from same list.
#
#   4. Running Median (Two Heaps):
#      max_heap (left half) + min_heap (right half)
#      Balance: sizes differ by at most 1.
#      Median = top of larger heap (or average of both tops).
#
# WHEN TO USE:
#   - "K-th largest/smallest"
#   - "Top K frequent"
#   - "Merge K sorted"
#   - "Running/streaming median"
#   - Dijkstra's shortest path
#   - Task scheduling with priorities
#
# TIME: O(log n) push/pop, O(1) peek, O(n) heapify
# SPACE: O(n) or O(k) depending on constraint
# ============================================================
