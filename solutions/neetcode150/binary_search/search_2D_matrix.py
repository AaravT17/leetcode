class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1: First find the correct row, then search for the element within that row. The correct row is the
        # row such that its last element >= target and the last element of the previous row (if any) < target.
        # m, n = len(matrix), len(matrix[0])
        # top, bot = 0, m - 1
        # while top < bot:
        #     mid = top + ((bot - top) // 2)
        #     # if the last element of row mid < target, set top = mid + 1 (mid cannot be the correct row, exclude)
        #     # if the last element of row mid >= target, set bot = mid (mid could be the correct row, include)
        #     if matrix[mid][n - 1] < target:
        #         top = mid + 1
        #     else:
        #         bot = mid
        # # at this point, top = bot is the index of the correct row
        # row = top
        # # search the row
        # left, right = 0, n - 1
        # while left <= right:
        #     mid = left + ((right - left) // 2)
        #     if matrix[row][mid] == target:
        #         return True
        #     elif matrix[row][mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return False
        # Time: First loop takes O(log m) time, second takes O(log n) time, total = O(log m + log n) = O(log(m*n)),
        # Space: O(1)

        # Approach 2: Flatten the array
        m, n = len(matrix), len(matrix[0])
        left, right = 0, (m * n) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            r, c = mid // n, mid % n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        # Time: O(log(m*n)), Space: O(1)
