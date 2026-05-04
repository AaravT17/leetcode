from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # return the union of the set of points from where water can flow to the pacific and the set of points
        # from where water can flow to the atlantic
        pac_q, pac_seen = deque(), set()
        atl_q, atl_seen = deque(), set()
        m, n = len(heights), len(heights[0])

        for j in range(n):
            pac_q.append((0, j))
            pac_seen.add((0, j))
        for i in range(1, m):
            pac_q.append((i, 0))
            pac_seen.add((i, 0))

        for j in range(n):
            atl_q.append((m - 1, j))
            atl_seen.add((m - 1, j))
        for i in range(m - 1):
            atl_q.append((i, n - 1))
            atl_seen.add((i, n - 1))

        def bfs(q: deque, seen: set):
            while q:
                i, j = q.popleft()
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    new_i, new_j = i + di, j + dj
                    if (
                        0 <= new_i < m
                        and 0 <= new_j < n
                        and heights[new_i][new_j] >= heights[i][j]
                        and (new_i, new_j) not in seen
                    ):
                        q.append((new_i, new_j))
                        seen.add((new_i, new_j))
            # once this function exits, seen consists of all points from where water can flow into the particular ocean
            # for which the function was called

        bfs(pac_q, pac_seen)
        bfs(atl_q, atl_seen)
        return list(pac_seen.intersection(atl_seen))
        # Time: O(mn), Space: O(mn)
