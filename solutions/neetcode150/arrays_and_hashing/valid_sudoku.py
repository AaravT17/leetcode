from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board) # = len(board[0])
        # validate rows
        for row in range(n):
            seen = set()
            for j in range(n):
                if board[row][j] != '.':
                    if board[row][j] in seen:
                        return False
                    seen.add(board[row][j])

        # validate cols
        for col in range(n):
            seen = set()
            for i in range(n):
                if board[i][col] != '.':
                    if board[i][col] in seen:
                        return False
                    seen.add(board[i][col])

        # validate boxes
        for i in range(n):
            box_corner = (3 * (i // 3), 3 * (i % 3))
            seen = set()
            for i in range(box_corner[0], box_corner[0] + 3):
                for j in range(box_corner[1], box_corner[1] + 3):
                    if board[i][j] != '.':
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True