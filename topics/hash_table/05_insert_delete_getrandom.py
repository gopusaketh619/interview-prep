# ============================================================
# PROBLEM: Insert Delete GetRandom O(1)
# LeetCode: 380 | https://leetcode.com/problems/insert-delete-getrandom-o1/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Implement the RandomizedSet class:
#   - insert(val): Inserts val if not present. Returns true if added.
#   - remove(val): Removes val if present. Returns true if removed.
#   - getRandom(): Returns a random element (each equally likely).
# Each function must work in average O(1) time complexity.
#
# Constraints:
#   - -2^31 <= val <= 2^31 - 1
#   - At most 2 * 10^5 calls to insert, remove, and getRandom
#   - There will be at least one element when getRandom is called
#
# Examples:
#   Input:  insert(1) -> True, remove(2) -> False, insert(2) -> True
#           getRandom() -> 1 or 2, remove(1) -> True, getRandom() -> 2
# ============================================================

import random

class RandomizedSet:
    # Pattern: Hashmap + list — O(1) lookup, insert, delete, and random access
    # Time: O(1) average per operation | Space: O(n)
    #
    # Approach:
    #   1. Use a list to store values (enables O(1) random access).
    #   2. Use a hashmap {val: index} for O(1) existence checks and lookups.
    #   3. For remove: swap target with the last element, then pop from end.
    #      This avoids O(n) shifting that a normal list.remove() would cause.
    #
    # Key insight: list.pop() from the END is O(1), but removing from the
    # middle is O(n). Swapping with the last element lets us always pop from the end.

    def __init__(self):
        self.val_to_idx = {}
        self.vals = []

    def insert(self, val):
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        if val not in self.val_to_idx:
            return False
        idx = self.val_to_idx[val]
        last_val = self.vals[-1]
        # Swap target with last element
        self.vals[idx] = last_val
        self.val_to_idx[last_val] = idx
        # Remove the last element
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def get_random(self):
        return random.choice(self.vals)


# --- Test Cases ---
rs = RandomizedSet()
assert rs.insert(1) == True
assert rs.remove(2) == False
assert rs.insert(2) == True
assert rs.remove(1) == True
print("All test cases passed!")
