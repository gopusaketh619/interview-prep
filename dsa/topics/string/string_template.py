# ============================================================
# STRING - PATTERN TEMPLATE
# ============================================================
#
# A string is a sequence of characters (immutable in Python).
# Most array techniques apply since a string is an array of chars.
#
# KEY TECHNIQUES:
#
#   1. Frequency Counting:
#      from collections import Counter
#      freq = Counter(s)
#
#   2. Sliding Window (for substring problems):
#      Same as array sliding window — use a hashmap to track
#      character frequencies within the window.
#
#   3. Two Pointers (for palindromes):
#      left, right = 0, len(s) - 1
#      while left < right:
#          if s[left] != s[right]: return False
#          left += 1; right -= 1
#
#   4. Expand from Center (palindromic substrings):
#      For each index i, expand outward while s[l] == s[r].
#      Check both odd (center=i) and even (center=i,i+1).
#
#   5. Bitmask for Unique Chars:
#      mask = 0
#      for c in word:
#          mask |= (1 << (ord(c) - ord('a')))
#
# WHEN TO USE:
#   - Anagram / permutation detection
#   - Palindrome check or enumeration
#   - Substring search (sliding window)
#   - Character frequency problems
#   - String matching / pattern finding
#
# COMMON MISTAKES:
#   - Forgetting strings are immutable: s += ch is O(n), not O(1)
#   - Off-by-one with slicing: s[i:j] excludes index j
#   - Not clarifying case sensitivity with interviewer
#
# PYTHON TIPS:
#   - s.isalnum(), s.lower() for cleaning
#   - ord(c) - ord('a') for 0-25 index
#   - "".join(list) for efficient string building
#
# TIME: Varies by technique
# SPACE: O(1) if alphabet is fixed (26 lowercase letters)
# ============================================================
