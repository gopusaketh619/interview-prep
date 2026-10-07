# ============================================================
# PROBLEM: Find Median from Data Stream
# LeetCode: 295 | https://leetcode.com/problems/find-median-from-data-stream/
# Difficulty: Hard | Time to Solve: 30 min
# ============================================================
# Implement the MedianFinder class:
#   - addNum(num): Adds num to the data structure.
#   - findMedian(): Returns the median of all added elements.
#
# Constraints:
#   - -10^5 <= num <= 10^5
#   - At most 5 * 10^4 calls to addNum and findMedian
#   - findMedian called only after at least one addNum
#
# Examples:
#   Input:  addNum(1), addNum(2), findMedian() -> 1.5, addNum(3), findMedian() -> 2.0
# ============================================================

class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num):
        pass

    def findMedian(self):
        pass


# --- Test Cases ---
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
assert mf.findMedian() == 1.5
mf.addNum(3)
assert mf.findMedian() == 2.0
print("All test cases passed!")
