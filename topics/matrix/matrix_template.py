# ============================================================
# MATRIX - PATTERN TEMPLATE
# ============================================================
#
# A matrix is a 2D array. In graph problems, each cell is a node
# with up/down/left/right neighbors.
#
# GRID TRAVERSAL SETUP:
#   rows, cols = len(matrix), len(matrix[0])
#   directions = [(0,1), (0,-1), (1,0), (-1,0)]  # right, left, down, up
#
#   # Boundary check:
#   if 0 <= r < rows and 0 <= c < cols:
#
# KEY TECHNIQUES:
#
#   1. DFS/BFS on Grid:
#      Treat cells as graph nodes. Use visited set or mark in-place.
#      See graph/01_number_of_islands.py for example.
#
#   2. Spiral Traversal:
#      Maintain boundaries: top, bottom, left, right.
#      Shrink inward after traversing each edge.
#
#   3. Layer-by-layer rotation:
#      Rotate matrix 90 degrees: transpose + reverse rows.
#
#   4. Multi-source BFS:
#      Start BFS from all "source" cells simultaneously.
#      Example: 01 Matrix (distance from nearest 0).
#
#   5. Dynamic Programming on Grid:
#      dp[r][c] = f(dp[r-1][c], dp[r][c-1], ...)
#      Example: Unique Paths, Minimum Path Sum.
#
# WHEN TO USE:
#   - Grid/island problems (DFS/BFS)
#   - Spiral order traversal
#   - Rotation / transposition
#   - Shortest distance in grid (BFS)
#   - Path counting (DP)
#
# COMMON MISTAKES:
#   - Forgetting boundary checks
#   - Not marking visited (infinite loop)
#   - Confusing rows/cols with x/y
#
# TIME: O(m * n) for full traversal
# SPACE: O(m * n) for visited set (or O(1) if marking in-place)
# ============================================================
