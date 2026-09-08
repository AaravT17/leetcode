from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Approach 1
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                # the entire section is in ascending order, nums[l] is the minimum
                return nums[l]

            # the section is not in ascending order
            m = l + ((r - l) // 2)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m

        return nums[l]
        # Time: O(log n), Space: O(1)
    
        # Approach 2
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     m = l + ((r - l) // 2)
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        # return nums[l]
        # Time: O(log n), Space: O(1)
