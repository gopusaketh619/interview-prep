# ============================================================
# QUEUE - PATTERN TEMPLATE
# ============================================================
#
# A queue is a FIFO (First In, First Out) data structure.
# In Python, use collections.deque (NOT list.pop(0) which is O(n)).
#
# BASIC OPERATIONS:
#   from collections import deque
#   q = deque()
#   q.append(x)      # enqueue (back) O(1)
#   q.popleft()      # dequeue (front) O(1)
#   q[0]             # peek front O(1)
#   len(q) == 0      # is_empty
#
# KEY TECHNIQUES:
#
#   1. BFS (Level-order traversal):
#      queue = deque([start])
#      visited = {start}
#      while queue:
#          node = queue.popleft()
#          for neighbor in get_neighbors(node):
#              if neighbor not in visited:
#                  visited.add(neighbor)
#                  queue.append(neighbor)
#
#   2. BFS with Level Tracking:
#      queue = deque([start])
#      level = 0
#      while queue:
#          for _ in range(len(queue)):  # process entire level
#              node = queue.popleft()
#              # ... process node at current level ...
#              queue.append(neighbors)
#          level += 1
#
#   3. Monotonic Deque (Sliding Window Max/Min):
#      See array/sliding_window/04_sliding_window_maximum.py
#
# WHEN TO USE:
#   - BFS traversal (shortest path in unweighted graph)
#   - Level-order tree traversal
#   - Task scheduling (FIFO order)
#   - Sliding window max/min (deque)
#   - Multi-source BFS (rotting oranges, 01-matrix)
#
# WARNING:
#   list.pop(0) is O(n) — always use deque.popleft() for O(1)
#
# TIME: O(1) per enqueue/dequeue
# SPACE: O(n) for n elements in queue
# ============================================================
