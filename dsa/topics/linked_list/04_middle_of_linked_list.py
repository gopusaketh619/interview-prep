# ============================================================
# PROBLEM: Middle of the Linked List
# LeetCode: 876 | https://leetcode.com/problems/middle-of-the-linked-list/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Given the head of a singly linked list, return the middle
# node of the linked list. If there are two middle nodes,
# return the second middle node.
#
# Constraints:
#   - The number of nodes is in the range [1, 100]
#   - 1 <= Node.val <= 100
#
# Examples:
#   Input:  head = [1, 2, 3, 4, 5]
#   Output: node with val 3
#
#   Input:  head = [1, 2, 3, 4, 5, 6]
#   Output: node with val 4 (second middle)
# ============================================================

from linked_list_template import ListNode, list_to_linked, linked_to_list


def middle_node(head):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
head = list_to_linked([1, 2, 3, 4, 5])
assert middle_node(head).val == 3

head = list_to_linked([1, 2, 3, 4, 5, 6])
assert middle_node(head).val == 4

head = list_to_linked([1])
assert middle_node(head).val == 1

print("All test cases passed!")
