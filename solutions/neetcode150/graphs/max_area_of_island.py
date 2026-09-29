class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs_visit(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return 1 + dfs_visit(i - 1, j) + dfs_visit(i + 1, j) + dfs_visit(i, j - 1) + dfs_visit(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs_visit(i, j)
                    max_area = max(area, max_area)

        return max_area
        # Time: O(mn), Space: O(mn) (recursive call stack)
