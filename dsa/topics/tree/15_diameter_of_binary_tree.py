# ============================================================
# PROBLEM: Diameter of Binary Tree
# LeetCode: 543 | https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the root of a binary tree, return the length of the
# diameter of the tree. The diameter is the length of the
# longest path between any two nodes (may not pass through root).
# The length is the number of edges between them.
#
# Constraints:
#   - The number of nodes is in the range [1, 10^4]
#   - -100 <= Node.val <= 100
#
# Examples:
#   Input:  root = [1, 2, 3, 4, 5]
#   Output: 3 (path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
#
#   Input:  root = [1, 2]
#   Output: 1
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


def diameter_of_binary_tree(root):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
assert diameter_of_binary_tree(root) == 3
print("All test cases passed!")
