class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Kadane's algorithm
        res = float('-inf')
        running_sum = 0
        for num in nums:
            running_sum += num
            res = max(res, running_sum)
            if running_sum < 0:
                running_sum = 0
        return res
