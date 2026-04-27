from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        shortest = (
            n + 1
        )  # length of valid window will always be <= n, so this is equivalent to setting the initial value to infinity
        l = 0
        curr_sum = 0

        for r in range(n):
            curr_sum += nums[r]
            while curr_sum >= target:
                shortest = min(shortest, (r - l) + 1)
                curr_sum -= nums[l]
                l += 1

        return 0 if shortest > n else shortest
