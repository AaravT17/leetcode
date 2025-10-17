from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Approach 1
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        # l == r at this point
        return l if nums[l] >= target else l + 1
