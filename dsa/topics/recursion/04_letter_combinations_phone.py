# ============================================================
# PROBLEM: Letter Combinations of a Phone Number
# LeetCode: 17 | https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Difficulty: Medium | Time to Solve: 20 min
# ============================================================
# Given a string containing digits from 2-9, return all possible
# letter combinations that the number could represent (phone keypad).
#
# Constraints:
#   - 0 <= len(digits) <= 4
#   - digits[i] is a digit in the range ['2', '9']
#
# Examples:
#   Input:  digits = "23"
#   Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#   Input:  digits = ""
#   Output: []
# ============================================================

def letter_combinations(digits):
    # Pattern: Backtracking — loop over choices for current digit
    # Time: O(n * 4^n) | Space: O(n) recursion depth
    #
    # Approach:
    #   1. Map each digit to its letters
    #   2. At each level, loop over letters for digits[i]
    #   3. Choose (append) → Explore (recurse i+1) → Unchoose (pop)

    if not digits:
        return []

    pkey_hm = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []

    def backtrack(i, path):
        if i == len(digits):
            result.append("".join(path))
            return

        # Loop over all letters mapped to the current digit
        for c in pkey_hm[digits[i]]:
            path.append(c)         # choose
            backtrack(i + 1, path) # explore next digit
            path.pop()             # unchoose (backtrack)

    backtrack(0, [])
    return result


# --- Test Cases ---
result = letter_combinations("23")
expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert sorted(result) == sorted(expected)

assert letter_combinations("") == []

result = letter_combinations("2")
assert sorted(result) == ["a", "b", "c"]
print("All test cases passed!")
