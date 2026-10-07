# ============================================================
# PROBLEM: Implement Trie (Prefix Tree)
# LeetCode: 208 | https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium | Time to Solve: 25 min
# ============================================================
# Implement the Trie class:
#   - insert(word): Inserts the string word into the trie.
#   - search(word): Returns true if word is in the trie.
#   - startsWith(prefix): Returns true if any word has the prefix.
#
# Constraints:
#   - 1 <= word.length, prefix.length <= 2000
#   - word and prefix consist only of lowercase English letters
#   - At most 3 * 10^4 calls to insert, search, and startsWith
#
# Examples:
#   Input:  insert("apple"), search("apple") -> True
#           search("app") -> False, startsWith("app") -> True
# ============================================================

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    # Pattern: <pattern>
    # Time: O(?) per operation | Space: O(?)
    #
    # Approach:
    #   1. <step>


    def __init__(self):
        pass

    def insert(self, word):
        pass

    def search(self, word):
        pass

    def starts_with(self, prefix):
        pass


# --- Test Cases ---
trie = Trie()
trie.insert("apple")
assert trie.search("apple") == True
assert trie.search("app") == False
assert trie.starts_with("app") == True
trie.insert("app")
assert trie.search("app") == True
print("All test cases passed!")
