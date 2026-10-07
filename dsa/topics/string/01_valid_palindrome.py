# ============================================================
# PROBLEM: Valid Palindrome
# LeetCode: 125 | https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy | Time to Solve: 15 min
# ============================================================
# A phrase is a palindrome if, after converting all uppercase
# letters to lowercase and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Given a string s, return true if it is a palindrome.
#
# Constraints:
#   - 1 <= len(s) <= 2 * 10^5
#   - s consists only of printable ASCII characters
#
# Examples:
#   Input:  s = "A man, a plan, a canal: Panama"
#   Output: True
#
#   Input:  s = "race a car"
#   Output: False
# ============================================================

def is_palindrome_brute(s):
    # Pattern: Clean string then reverse-compare
    # Time: O(n) | Space: O(n) — creates cleaned string + reversed copy
    #
    # Approach:
    #   1. Filter to alphanumeric and lowercase.
    #   2. Compare cleaned string with its reverse.

    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome(s):
    # Pattern: Two pointers — compare from both ends
    # Time: O(n) | Space: O(n) — creates cleaned string
    #
    # Approach:
    #   1. Filter to alphanumeric and lowercase.
    #   2. Two pointers from both ends, compare characters moving inward.
    #   3. If any mismatch → not a palindrome.

    sn = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(sn) - 1
    while left < right:
        if sn[left] != sn[right]:
            return False
        left += 1
        right -= 1
    return True

    


# --- Test Cases ---
assert is_palindrome("A man, a plan, a canal: Panama") == True
assert is_palindrome("race a car") == False
assert is_palindrome(" ") == True
assert is_palindrome("") == True
assert is_palindrome_brute("A man, a plan, a canal: Panama") == True
assert is_palindrome_brute("race a car") == False
assert is_palindrome_brute(" ") == True
assert is_palindrome_brute("") == True
print("All test cases passed!")
