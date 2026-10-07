# ============================================================
# PROBLEM: Reorder List
# LeetCode: 143 | https://leetcode.com/problems/reorder-list/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given the head of a singly linked list:
# L0 -> L1 -> ... -> Ln-1 -> Ln
# Reorder it to:
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
# You may not modify the values, only the nodes themselves.
#
# Constraints:
#   - The number of nodes is in the range [1, 5 * 10^4]
#   - 1 <= Node.val <= 1000
#
# Examples:
#   Input:  head = [1, 2, 3, 4]
#   Output: [1, 4, 2, 3]
#
#   Input:  head = [1, 2, 3, 4, 5]
#   Output: [1, 5, 2, 4, 3]
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
# Build: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
# reorder_list(head) should give 1 -> 4 -> 2 -> 3
print("Stub created - add implementation and tests.")
