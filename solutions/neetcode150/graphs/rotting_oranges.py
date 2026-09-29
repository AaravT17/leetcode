from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2
        num_fresh = 0
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    q.append((i, j))

        t = 0
        while q and num_fresh > 0:
            length = len(q)
            for i in range(length):
                i, j = q.popleft()
                for new_i, new_j in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] != FRESH:
                        continue
                    grid[new_i][new_j] = ROTTEN
                    num_fresh -= 1
                    q.append((new_i, new_j))
            t += 1

        return t if num_fresh == 0 else -1
