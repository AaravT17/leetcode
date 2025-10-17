from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1
        # return len(nums) > len(set(nums))

        # Approach 2
        nums_seen = set()
        for num in nums:
            if num in nums_seen:
                return True
            nums_seen.add(num)

        return False
