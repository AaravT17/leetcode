from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            val = nums[i]
            correct_idx = val - 1
            while 0 < val <= n and nums[correct_idx] != val:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                val = nums[i]
                correct_idx = val - 1
            # When the while loop terminates, nums[i] is either out of bounds (<= 0 or > n) or we already
            # have nums[correct_idx] = nums[i] (the value at nums[i] has been processed or does not need processing
            # since the value at its corresponding index is already set correctly), so if we move on we are not
            # losing any information/skipping any value that needs processing

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        # Time complexity: O(n). The outer for loop runs n times, and the inner while loop executes at most
        # n times since there are n elements to place into correct positions/n indices to mark, each position
        # is only marked once, and each iteration marks one index => O(n) total iterations
        # Space complexity: O(1)
