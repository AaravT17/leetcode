from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]

        prev, curr = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            prev, curr = curr, max(curr, nums[i] + prev)

        return curr
        # Time: O(n), Space: O(1)
