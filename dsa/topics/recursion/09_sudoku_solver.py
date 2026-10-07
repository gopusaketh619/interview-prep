# ============================================================
# PROBLEM: Sudoku Solver
# LeetCode: 37 | https://leetcode.com/problems/sudoku-solver/
# Difficulty: Hard | Time to Solve: 40 min
# ============================================================
# Write a program to solve a Sudoku puzzle by filling the
# empty cells. A valid solution fills every '.' with digits
# '1'-'9' satisfying all Sudoku rules.
#
# Constraints:
#   - board.length == 9
#   - board[i].length == 9
#   - board[i][j] is a digit or '.'
#   - The input board has a single unique solution
#
# Examples:
#   Input:  A 9x9 board with '.' for empty cells
#   Output: The board filled with a valid solution
# ============================================================

def solve_sudoku(board):
    # Pattern: Backtracking — try each digit, undo if it leads to dead end
    # Time: O(9^E) where E = number of empty cells (worst case) | Space: O(E) recursion depth
    #
    # Approach:
    #   1. Find the next empty cell ('.').
    #   2. Try digits '1'-'9' in that cell.
    #   3. Check if the digit is valid (not in same row, col, or 3x3 box).
    #   4. If valid, place it and recurse to solve the rest.
    #   5. If recursion fails, backtrack (reset cell to '.') and try next digit.
    #   6. If no empty cells remain, the puzzle is solved.

    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False

        # Check 3x3 box — find top-left corner of the box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        return True

    def backtrack(board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in '123456789':
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if backtrack(board):
                                return True
                            board[r][c] = '.'
                    # No valid digit works → dead end, backtrack
                    return False
        # No empty cells left → solved
        return True

    backtrack(board)


# --- Test Cases ---
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solve_sudoku(board)

expected = [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]

assert board == expected
print("All test cases passed!")
