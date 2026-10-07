# ============================================================
# GRAPH - PATTERN TEMPLATE
# ============================================================
#
# A graph is a set of nodes (vertices) connected by edges.
# Can be directed/undirected, weighted/unweighted.
#
# REPRESENTATIONS:
#
#   1. Adjacency List (most common in interviews):
#      graph = defaultdict(list)
#      graph[u].append(v)
#
#   2. Adjacency Matrix:
#      matrix[i][j] = 1 if edge from i to j
#
#   3. Edge List:
#      edges = [(u, v, weight), ...]
#
#   4. Grid/Matrix as Graph:
#      Each cell = node, neighbors = up/down/left/right
#      directions = [(0,1), (0,-1), (1,0), (-1,0)]
#
# DFS TEMPLATE (Recursive):
#
#   def dfs(node, visited):
#       visited.add(node)
#       for neighbor in graph[node]:
#           if neighbor not in visited:
#               dfs(neighbor, visited)
#
# DFS ON GRID:
#
#   def dfs(grid, r, c, visited):
#       if (r < 0 or r >= rows or c < 0 or c >= cols
#           or (r,c) in visited or grid[r][c] == 0):
#           return
#       visited.add((r, c))
#       for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
#           dfs(grid, r+dr, c+dc, visited)
#
# BFS TEMPLATE:
#
#   from collections import deque
#   def bfs(start):
#       queue = deque([start])
#       visited = {start}
#       while queue:
#           node = queue.popleft()
#           for neighbor in graph[node]:
#               if neighbor not in visited:
#                   visited.add(neighbor)
#                   queue.append(neighbor)
#
# TOPOLOGICAL SORT (Kahn's Algorithm — BFS-based):
#
#   from collections import deque
#   in_degree = {node: 0 for node in graph}
#   for node in graph:
#       for neighbor in graph[node]:
#           in_degree[neighbor] += 1
#   queue = deque([n for n in in_degree if in_degree[n] == 0])
#   order = []
#   while queue:
#       node = queue.popleft()
#       order.append(node)
#       for neighbor in graph[node]:
#           in_degree[neighbor] -= 1
#           if in_degree[neighbor] == 0:
#               queue.append(neighbor)
#   # if len(order) != num_nodes → cycle exists
#
# WHEN TO USE:
#   - Connected components (DFS/BFS/Union-Find)
#   - Shortest path (BFS for unweighted, Dijkstra for weighted)
#   - Cycle detection (DFS with coloring or topo sort)
#   - Topological ordering (course scheduling)
#   - Island/region counting (grid DFS/BFS)
#
# TIME: O(V + E) for DFS/BFS
# SPACE: O(V) for visited set + O(V + E) for adjacency list
# ============================================================
