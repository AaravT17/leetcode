from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1: Use a hashset to track visited positions
        # m, n = len(grid), len(grid[0])
        # num_islands = 0
        # visited = set()

        # def dfs_visit(i: int, j: int) -> None:
        #     if (
        #         i < 0
        #         or i >= m
        #         or j < 0
        #         or j >= n
        #         or grid[i][j] == '0'
        #         or (i, j) in visited
        #     ):
        #         return

        #     visited.add((i, j))
        #     dfs_visit(i + 1, j)
        #     dfs_visit(i - 1, j)
        #     dfs_visit(i, j + 1)
        #     dfs_visit(i, j - 1)

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1' and (i, j) not in visited:
        #             num_islands += 1
        #             dfs_visit(i, j)

        # return num_islands

        # Approach 2: Set visited positions in the grid to '0' so that we do not visit them again
        m, n = len(grid), len(grid[0])
        num_islands = 0

        def dfs_visit(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs_visit(i + 1, j)
            dfs_visit(i - 1, j)
            dfs_visit(i, j + 1)
            dfs_visit(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs_visit(i, j)

        return num_islands
