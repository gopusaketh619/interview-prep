# ============================================================
# PROBLEM: Binary Tree Maximum Path Sum
# LeetCode: 124 | https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Difficulty: Hard | Time to Solve: 35 min
# ============================================================
# A path in a binary tree is a sequence of nodes where each pair
# of adjacent nodes has an edge connecting them. A node can only
# appear at most once. The path sum is the sum of node values.
# Return the maximum path sum of any non-empty path.
#
# Constraints:
#   - The number of nodes is in the range [1, 3 * 10^4]
#   - -1000 <= Node.val <= 1000
#
# Examples:
#   Input:  root = [1, 2, 3]
#   Output: 6 (path: 2 -> 1 -> 3)
#
#   Input:  root = [-10, 9, 20, null, null, 15, 7]
#   Output: 42 (path: 15 -> 20 -> 7)
# ============================================================

class TreeNode:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert max_path_sum(root) == 42
print("All test cases passed!")
