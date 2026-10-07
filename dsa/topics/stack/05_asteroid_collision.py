# ============================================================
# PROBLEM: Asteroid Collision
# LeetCode: 735 | https://leetcode.com/problems/asteroid-collision/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# We are given an array asteroids of integers representing
# asteroids in a row. The absolute value is size, the sign
# is direction (positive = right, negative = left).
# Find out the state after all collisions.
#
# Constraints:
#   - 2 <= len(asteroids) <= 10^4
#   - -1000 <= asteroids[i] <= 1000
#   - asteroids[i] != 0
#
# Examples:
#   Input:  asteroids = [5, 10, -5]
#   Output: [5, 10]
#
#   Input:  asteroids = [8, -8]
#   Output: []
# ============================================================

def asteroid_collision(asteroids):
    # Pattern: <pattern>
    # Time: O(?) | Space: O(?)
    #
    # Approach:
    #   1. <step>

    pass


# --- Test Cases ---
assert asteroid_collision([5,10,-5]) == [5,10]
assert asteroid_collision([8,-8]) == []
assert asteroid_collision([10,2,-5]) == [10]
print("All test cases passed!")
