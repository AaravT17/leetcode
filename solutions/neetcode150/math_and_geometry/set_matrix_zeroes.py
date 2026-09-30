class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        clear_first_row, clear_first_col = False, False
        for j in range(n):
            if matrix[0][j] == 0:
                clear_first_row = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                clear_first_col = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        def _clear_row(i: int):
            for j in range(n):
                matrix[i][j] = 0

        def _clear_col(j: int):
            for i in range(m):
                matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                _clear_col(j)

        for i in range(1, m):
            if matrix[i][0] == 0:
                _clear_row(i)

        if clear_first_row:
            _clear_row(0)

        if clear_first_col:
            _clear_col(0)
