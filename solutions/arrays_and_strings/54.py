from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])
        count = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        curr_dir = 0

        i, j = 0, 0
        while count < m * n:
            result.append(matrix[i][j])
            matrix[i][j] = None
            count += 1
            # check if we can continue to move in the same direction i.e., the next square
            # in that direction is in bounds and has not been visited yet, if not then change direction
            new_i = i + directions[curr_dir][1]
            new_j = j + directions[curr_dir][0]
            if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] is not None:
                i = new_i
                j = new_j
            else:
                curr_dir = (curr_dir + 1) % 4
                i += directions[curr_dir][1]
                j += directions[curr_dir][0]

        return result
