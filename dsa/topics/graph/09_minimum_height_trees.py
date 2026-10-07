# ============================================================
# PROBLEM: Minimum Height Trees
# LeetCode: 310 | https://leetcode.com/problems/minimum-height-trees/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# A tree is an undirected graph with n nodes labeled 0 to n-1
# with exactly n-1 edges. Given n and edges, find all roots
# that minimize the tree height (MHTs). Return their labels.
#
# Constraints:
#   - 1 <= n <= 2 * 10^4
#   - len(edges) == n - 1
#   - 0 <= a, b < n
#   - All pairs (a, b) are distinct
#
# Examples:
#   Input:  n = 4, edges = [[1,0],[1,2],[1,3]]
#   Output: [1]
#
#   Input:  n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
#   Output: [3, 4]
# ============================================================

def find_min_height_trees(n, edges):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert find_min_height_trees(4, [[1,0],[1,2],[1,3]]) == [1]
assert sorted(find_min_height_trees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) == [3,4]
print("All test cases passed!")
