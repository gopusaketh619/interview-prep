# ============================================================
# PROBLEM: Merge Two Sorted Lists
# LeetCode: 21 | https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# Merge two sorted linked lists and return it as a new sorted
# list. The new list should be made by splicing together the
# nodes of the first two lists.
#
# Constraints:
#   - The number of nodes in both lists is in range [0, 50]
#   - -100 <= Node.val <= 100
#   - Both lists are sorted in non-decreasing order
#
# Examples:
#   Input:  list1 = [1, 2, 4], list2 = [1, 3, 4]
#   Output: [1, 1, 2, 3, 4, 4]
#
#   Input:  list1 = [], list2 = [0]
#   Output: [0]
# ============================================================

from linked_list_template import ListNode, list_to_linked, linked_to_list


def merge_two_lists(list1, list2):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
l1 = list_to_linked([1, 2, 4])
l2 = list_to_linked([1, 3, 4])
assert linked_to_list(merge_two_lists(l1, l2)) == [1, 1, 2, 3, 4, 4]

l1 = list_to_linked([])
l2 = list_to_linked([0])
assert linked_to_list(merge_two_lists(l1, l2)) == [0]

l1 = list_to_linked([])
l2 = list_to_linked([])
assert linked_to_list(merge_two_lists(l1, l2)) == []

print("All test cases passed!")
