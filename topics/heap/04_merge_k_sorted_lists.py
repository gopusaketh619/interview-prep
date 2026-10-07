# ============================================================
# PROBLEM: Merge k Sorted Lists (Heap)
# LeetCode: 23 | https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# You are given an array of k linked-lists, each sorted in
# ascending order. Merge all the linked-lists into one sorted
# linked-list using a min-heap approach.
#
# Constraints:
#   - k == len(lists)
#   - 0 <= k <= 10^4
#   - 0 <= lists[i].length <= 500
#   - -10^4 <= lists[i][j] <= 10^4
#
# Examples:
#   Input:  lists = [[1,4,5],[1,3,4],[2,6]]
#   Output: [1,1,2,3,4,4,5,6]
# ============================================================

class ListNode:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
def list_to_linked(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

lists = [list_to_linked([1, 4, 5]), list_to_linked([1, 3, 4]), list_to_linked([2, 6])]
assert linked_to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
assert merge_k_lists([]) is None
print("All test cases passed!")
