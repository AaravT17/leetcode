from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        # validate rows
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[i][j]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)

        # validate columns
        for j in range(9):
            seen = set()
            for i in range(9):
                item = board[i][j]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)

        # validate sub-boxes
        for n in range(9):
            start_row, start_col = 3 * (n // 3), 3 * (n % 3)
            seen = set()
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    item = board[i][j]
                    if item in seen:
                        return False
                    elif item != '.':
                        seen.add(item)

        return True
