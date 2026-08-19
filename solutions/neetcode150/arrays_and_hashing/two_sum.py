from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for i in range(len(nums)):
            reqd = target - nums[i]
            if reqd in num_index_map:
                return [num_index_map[reqd], i]
            num_index_map[nums[i]] = i

        return [-1, -1]  # will never reach here since it is guaranteed that there is a solution
