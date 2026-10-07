# ============================================================
# PROBLEM: Time Based Key-Value Store
# LeetCode: 981 | https://leetcode.com/problems/time-based-key-value-store/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
#
# Design a time-based key-value data structure that can store multiple
# values for the same key at different timestamps and retrieve the
# value at a certain timestamp.
# ============================================================

class TimeMap:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self):
        pass

    def set(self, key, value, timestamp):
        pass

    def get(self, key, timestamp):
        pass


# --- Test Cases ---
tm = TimeMap()
tm.set("foo", "bar", 1)
assert tm.get("foo", 1) == "bar"
assert tm.get("foo", 3) == "bar"
tm.set("foo", "bar2", 4)
assert tm.get("foo", 4) == "bar2"
assert tm.get("foo", 5) == "bar2"
print("All test cases passed!")
