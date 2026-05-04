from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # use BFS, starting frontier is all rotten oranges, at each iteration, pop all frontier oranges off the queue,
        # infect all fresh orange neighbours, add to frontier for next iteration, increment time by 1 per iteration,
        # stop once no fresh oranges remain, or no oranges remain on the frontier
        q = deque()
        m, n = len(grid), len(grid[0])
        seen = set()  # holds positions that have been added to the frontier at some point
        num_fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))

        t = 0
        while q and num_fresh:
            t += 1
            l = len(q)
            for _ in range(l):
                i, j = q.popleft()
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in seen:
                        # visit this cell, take the necessary action
                        if grid[new_i][new_j] == 1:
                            num_fresh -= 1
                            q.append((new_i, new_j))
                            seen.add((new_i, new_j))

        if not num_fresh:
            return t
        else:
            return -1
        # Time: O(mn), Space: O(mn)
