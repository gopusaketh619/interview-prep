# ============================================================
# PROBLEM: Design Add and Search Words Data Structure
# LeetCode: 211 | https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Design a data structure that supports adding words and
# searching with '.' as a wildcard that can match any letter.
#
# Constraints:
#   - 1 <= word.length <= 25
#   - word in addWord consists of lowercase English letters
#   - word in search contains '.' or lowercase English letters
#   - At most 10^4 calls to addWord and search
#
# Examples:
#   Input:  addWord("bad"), addWord("dad"), search(".ad") -> True
#           search("b..") -> True, search("b.") -> False
# ============================================================

class WordDictionary:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>

    def __init__(self):
        pass

    def add_word(self, word):
        pass

    def search(self, word):
        pass


# --- Test Cases ---
wd = WordDictionary()
wd.add_word("bad")
wd.add_word("dad")
wd.add_word("mad")
assert wd.search("pad") == False
assert wd.search("bad") == True
assert wd.search(".ad") == True
assert wd.search("b..") == True
print("All test cases passed!")
