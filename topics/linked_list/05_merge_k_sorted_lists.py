# ============================================================
# PROBLEM: Merge k Sorted Lists
# LeetCode: 23 | https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# You are given an array of k linked-lists, each sorted in
# ascending order. Merge all the linked-lists into one sorted
# linked-list and return it.
#
# Constraints:
#   - k == len(lists)
#   - 0 <= k <= 10^4
#   - 0 <= lists[i].length <= 500
#   - -10^4 <= lists[i][j] <= 10^4
#   - Total number of nodes does not exceed 10^4
#
# Examples:
#   Input:  lists = [[1,4,5],[1,3,4],[2,6]]
#   Output: [1,1,2,3,4,4,5,6]
#
#   Input:  lists = []
#   Output: []
# ============================================================

import heapq
from linked_list_template import ListNode, list_to_linked, linked_to_list


def merge_k_lists(lists):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


def merge_k_lists_divide_conquer(lists):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
lists = [list_to_linked([1, 4, 5]), list_to_linked([1, 3, 4]), list_to_linked([2, 6])]
assert linked_to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

lists = [list_to_linked([1, 4, 5]), list_to_linked([1, 3, 4]), list_to_linked([2, 6])]
assert linked_to_list(merge_k_lists_divide_conquer(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]

assert merge_k_lists([]) is None
assert linked_to_list(merge_k_lists([list_to_linked([])])) == []

print("All test cases passed!")
