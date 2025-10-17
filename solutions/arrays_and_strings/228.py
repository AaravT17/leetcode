from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        start, end = 0, 0

        while start < len(nums):
            if end < len(nums) - 1 and nums[end] == nums[end + 1] - 1:
                end += 1
            else:
                if start == end:
                    result.append(str(nums[start]))
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                end += 1
                start = end

        return result
