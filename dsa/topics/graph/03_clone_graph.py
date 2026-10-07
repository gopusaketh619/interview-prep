# ============================================================
# PROBLEM: Clone Graph
# LeetCode: 133 | https://leetcode.com/problems/clone-graph/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Given a reference of a node in a connected undirected graph,
# return a deep copy (clone) of the graph. Each node contains
# a value and a list of its neighbors.
#
# Constraints:
#   - The number of nodes is in the range [0, 100]
#   - 1 <= Node.val <= 100
#   - Node.val is unique for each node
#   - No repeated edges and no self-loops
#
# Examples:
#   Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
#   Output: [[2,4],[1,3],[2,4],[1,3]] (deep copy)
# ============================================================

class Node:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
# Build graph: 1 -- 2
#              |    |
#              4 -- 3
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

clone = clone_graph(n1)
assert clone.val == 1
assert clone is not n1
assert len(clone.neighbors) == 2
assert clone.neighbors[0].val == 2
assert clone.neighbors[0] is not n2

assert clone_graph(None) is None
print("All test cases passed!")
