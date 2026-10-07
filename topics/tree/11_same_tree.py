# ============================================================
# PROBLEM: Same Tree
# LeetCode: 100 | https://leetcode.com/problems/same-tree/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the roots of two binary trees p and q, write a function
# to check if they are the same or not. Two binary trees are
# the same if they are structurally identical and nodes have
# the same value.
#
# Constraints:
#   - The number of nodes in both trees is in the range [0, 100]
#   - -10^4 <= Node.val <= 10^4
#
# Examples:
#   Input:  p = [1, 2, 3], q = [1, 2, 3]
#   Output: True
#
#   Input:  p = [1, 2], q = [1, null, 2]
#   Output: False
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


def is_same_tree(p, q):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
t1 = TreeNode(1, TreeNode(2), TreeNode(3))
t2 = TreeNode(1, TreeNode(2), TreeNode(3))
assert is_same_tree(t1, t2) == True
assert is_same_tree(t1, None) == False
print("All test cases passed!")
