from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def _get_reachable_coords(q: deque) -> set:
            visited = set()
            for i, j in q:
                visited.add((i, j))

            while q:
                i, j = q.popleft()
                for new_i, new_j in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if _can_flow(i, j, new_i, new_j) and (new_i, new_j) not in visited:
                        q.append((new_i, new_j))
                        visited.add((new_i, new_j))

            return visited

        def _can_flow(curr_i: int, curr_j: int, new_i: int, new_j: int) -> bool:
            if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                return False

            return heights[curr_i][curr_j] <= heights[new_i][new_j]

        q = deque()

        # pacific
        for i in range(m):
            q.append((i, 0))
        for j in range(n):
            q.append((0, j))
        pacific = _get_reachable_coords(q)
        # q is empty after the function returns

        # atlantic
        for i in range(m):
            q.append((i, n - 1))
        for j in range(n):
            q.append((m - 1, j))
        atlantic = _get_reachable_coords(q)

        res = []
        for i, j in pacific:
            if (i, j) in atlantic:
                res.append([i, j])
        return res
