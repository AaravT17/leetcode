class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0

        def dfs_visit(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            grid[i][j] = '0'
            dfs_visit(i - 1, j)
            dfs_visit(i + 1, j)
            dfs_visit(i, j - 1)
            dfs_visit(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs_visit(i, j)

        return num_islands
        # Time: O(mn), Space: O(mn) (recursive call stack)
