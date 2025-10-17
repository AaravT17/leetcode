from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:  # nums[m] > nums[r] (all elements are unique)
                l = m + 1

        return nums[l]  # l == r at this point
