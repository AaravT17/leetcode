from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {nums[i]: i for i in range(len(nums))}

        for i in range(len(nums)):
            y = target - nums[i]
            if y in value_to_index and i != value_to_index[y]:
                return [i, value_to_index[y]]

        return None  # this will never be reached, a solution is guaranteed to exist
