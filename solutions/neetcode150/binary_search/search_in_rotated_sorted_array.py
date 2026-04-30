from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first, find the pivot point, since we need a monotonic array/subarray for binary search
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        # now, perform binary search in the correct subarray
        if target < nums[0]:
            # target won't be between 0 and pivot - 1, must be between pivot and n - 1 (if present)
            l, r = pivot, n - 1
        else:
            # target (if present) is either between 0 and pivot - 1, or 0 and n - 1 if the array is not rotated
            l, r = 0, pivot - 1 if pivot > 0 else n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
        # Time: O(log n), Space: O(1)
