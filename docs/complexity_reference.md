# Big-O Complexity Reference

---

## Data Structure Operations

### Arrays / Lists

| Operation | Average | Worst |
|-----------|---------|-------|
| Access by index | O(1) | O(1) |
| Search (unsorted) | O(n) | O(n) |
| Search (sorted) | O(log n) | O(log n) |
| Insert at end | O(1)* | O(n)* |
| Insert at index | O(n) | O(n) |
| Delete at end | O(1) | O(1) |
| Delete at index | O(n) | O(n) |

*Amortized O(1) due to dynamic resizing.

### Linked List

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Access by index | O(n) | O(n) |
| Search | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n)* | O(1) |
| Delete head | O(1) | O(1) |
| Delete given node | O(n)** | O(1) |

*O(1) if you maintain a tail pointer.
**O(1) if you have reference to the node (copy next node's value).

### Hash Table (dict / set)

| Operation | Average | Worst |
|-----------|---------|-------|
| Search | O(1) | O(n) |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |

Worst case only with pathological hash collisions.

### Stack (list or deque)

| Operation | Time |
|-----------|------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

### Queue (deque)

| Operation | Time |
|-----------|------|
| Enqueue (append) | O(1) |
| Dequeue (popleft) | O(1) |
| Peek front | O(1) |
| Search | O(n) |

**Warning:** Using `list.pop(0)` is O(n). Always use `collections.deque`.

### Binary Search Tree (balanced)

| Operation | Average | Worst (skewed) |
|-----------|---------|----------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |
| Find min/max | O(log n) | O(n) |

### Heap (Priority Queue)

| Operation | Time |
|-----------|------|
| Insert (push) | O(log n) |
| Delete min/max (pop) | O(log n) |
| Get min/max (peek) | O(1) |
| Heapify array | O(n) |
| Search | O(n) |

### Trie

| Operation | Time |
|-----------|------|
| Insert word | O(m) |
| Search word | O(m) |
| Search prefix | O(m) |
| Delete word | O(m) |

Where m = length of the word.

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(d*(n+k)) | O(d*(n+k)) | O(d*(n+k)) | O(n+k) | Yes |
| Tim Sort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

Python's built-in `sort()` and `sorted()` use Tim Sort.

---

## Graph Algorithms

| Algorithm | Time | Space | Notes |
|-----------|------|-------|-------|
| BFS | O(V + E) | O(V) | Shortest path (unweighted) |
| DFS | O(V + E) | O(V) | Cycle detection, paths |
| Topological Sort | O(V + E) | O(V) | DAG only |
| Dijkstra (binary heap) | O((V+E) log V) | O(V) | Shortest path (positive weights) |
| Bellman-Ford | O(V * E) | O(V) | Handles negative weights |
| Floyd-Warshall | O(V³) | O(V²) | All-pairs shortest path |
| Kruskal's (MST) | O(E log E) | O(V) | Minimum spanning tree |
| Prim's (MST) | O((V+E) log V) | O(V) | Minimum spanning tree |
| Union-Find | O(α(n)) ≈ O(1) | O(n) | Per operation (amortized) |

---

## Common Algorithm Patterns

| Pattern | Typical Complexity | Examples |
|---------|-------------------|----------|
| Two Pointers | O(n) | Two Sum (sorted), Container With Most Water |
| Sliding Window (fixed) | O(n) | Max Average Subarray, Count Anagrams |
| Sliding Window (variable) | O(n) | Longest Substring No Repeat, Min Window |
| Binary Search | O(log n) | Search Rotated Array, First Bad Version |
| Prefix Sum | O(n) build, O(1) query | Subarray Sum Equals K, Product Except Self |
| BFS/DFS | O(V + E) | Number of Islands, Course Schedule |
| Backtracking | O(2^n) or O(n!) | Permutations, Subsets, N-Queens |
| Dynamic Programming | varies | Coin Change O(n*amount), LCS O(n*m) |
| Divide and Conquer | O(n log n) | Merge Sort, Quick Select |
| Greedy | O(n log n) or O(n) | Intervals, Activity Selection |

---

## Space Complexity Guidelines

| Structure | Space |
|-----------|-------|
| Fixed variables | O(1) |
| Hash map of n elements | O(n) |
| Hash map with fixed alphabet (26 chars) | O(1) |
| Recursion stack (balanced tree) | O(log n) |
| Recursion stack (linear) | O(n) |
| BFS queue (tree level) | O(n/2) = O(n) |
| Adjacency list | O(V + E) |
| 2D DP table | O(n * m) |
| Prefix sum array | O(n) |

---

## Common Growth Rates (slowest to fastest)

```
O(1) < O(log n) < O(√n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2^n) < O(n!)
```

### Rough Scale at n = 1,000,000:

| Big-O | Operations | Feasible? |
|-------|-----------|-----------|
| O(1) | 1 | Always |
| O(log n) | ~20 | Always |
| O(n) | 1,000,000 | Yes |
| O(n log n) | ~20,000,000 | Yes |
| O(n²) | 10^12 | Too slow |
| O(2^n) | Infinite | Never for n > 25 |

**Rule of thumb:** Modern computers handle ~10^8 operations per second.
- O(n) works for n up to ~10^8
- O(n log n) works for n up to ~10^7
- O(n²) works for n up to ~10^4
- O(2^n) works for n up to ~25
