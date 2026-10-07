# ============================================================
# PROBLEM: Reverse Linked List
# LeetCode: 206 | https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the head of a singly linked list, reverse the list,
# and return the reversed list.
#
# Constraints:
#   - The number of nodes is in the range [0, 5000]
#   - -5000 <= Node.val <= 5000
#
# Examples:
#   Input:  head = [1, 2, 3, 4, 5]
#   Output: [5, 4, 3, 2, 1]
#
#   Input:  head = [1, 2]
#   Output: [2, 1]
# ============================================================

from linked_list_template import ListNode, list_to_linked, linked_to_list


def reverse_list(head):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def reverse_list_recursive(head):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
head = list_to_linked([1, 2, 3, 4, 5])
assert linked_to_list(reverse_list(head)) == [5, 4, 3, 2, 1]

head = list_to_linked([1, 2])
assert linked_to_list(reverse_list_recursive(head)) == [2, 1]

head = list_to_linked([])
assert linked_to_list(reverse_list(head)) == []

print("All test cases passed!")
