from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        TREASURE, INF = 0, 2**31 - 1

        # run BFS, initial frontier consists of all treasure locations
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == TREASURE:
                    q.append((i, j, 0))

        while q:
            i, j, dist = q.popleft()
            new_dist = dist + 1
            for new_i, new_j in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or grid[new_i][new_j] != INF:
                    continue
                grid[new_i][new_j] = new_dist
                q.append((new_i, new_j, new_dist))
