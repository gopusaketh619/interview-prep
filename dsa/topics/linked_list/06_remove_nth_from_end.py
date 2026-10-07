# ============================================================
# PROBLEM: Remove Nth Node From End of List
# LeetCode: 19 | https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given the head of a linked list, remove the nth node from
# the end of the list and return its head.
#
# Constraints:
#   - The number of nodes is sz, 1 <= sz <= 30
#   - 0 <= Node.val <= 100
#   - 1 <= n <= sz
#
# Examples:
#   Input:  head = [1,2,3,4,5], n = 2
#   Output: [1,2,3,5]
#
#   Input:  head = [1], n = 1
#   Output: []
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
# Build: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# remove_nth_from_end(head, 2) should give 1 -> 2 -> 3 -> 5
print("Stub created - add implementation and tests.")
