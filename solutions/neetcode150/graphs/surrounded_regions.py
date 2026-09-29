from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = set()
        q = deque()
        for i in range(m):
            if board[i][0] == 'O':
                q.append((i, 0))
                visited.add((i, 0))
            if board[i][n - 1] == 'O':
                q.append((i, n - 1))
                visited.add((i, n - 1))

        for j in range(1, n - 1):
            if board[0][j] == 'O':
                q.append((0, j))
                visited.add((0, j))
            if board[m - 1][j] == 'O':
                q.append((m - 1, j))
                visited.add((m - 1, j))

        while q:
            i, j = q.popleft()
            for new_i, new_j in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if (
                    new_i < 0
                    or new_i >= m
                    or new_j < 0
                    or new_j >= n
                    or board[new_i][new_j] != 'O'
                    or (new_i, new_j) in visited
                ):
                    continue

                q.append((new_i, new_j))
                visited.add((new_i, new_j))

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
