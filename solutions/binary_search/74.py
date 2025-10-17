from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1
        # Idea: First find the correct row, then search through the columns in
        # that row (both via binary search, first vertically, then horizontally)
        # Time: O(log m + log n) = O(log(mn)) (log m time to find the row,
        # log n time to search through the columns in that row)
        m, n = len(matrix), len(matrix[0])

        # first, find the correct row (if any)
        t, b = 0, m - 1
        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] > target:
                b = m - 1
            else:
                t = m + 1

        # at this point, b is the index of the row in which target may be found
        # now, we search within that row for target
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[b][m] == target:
                return True
            elif matrix[b][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False

        # Approach 2
        # Idea: Flatten out the 2D matrix and perform regular binary search, we
        # can calculate the row and column based on the flattened index as:
        # row = index // n, col = index % n
        # Time: O(log(mn)), m * n iterations, each taking constant time
        # m, n = len(matrix), len(matrix[0])

        # left, right = 0, (m * n) - 1
        # while left <= right:
        #     middle = (left + right) // 2
        #     elem = matrix[middle // n][middle % n]
        #     if elem == target:
        #         return True
        #     elif elem < target:
        #         left = middle + 1
        #     else:
        #         right = middle - 1

        # return False
