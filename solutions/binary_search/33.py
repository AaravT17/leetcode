from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:  # nums[m] > nums[r] (all elements are unique)
                l = m + 1

        # at this point, l is the index of the minimum element
        if target <= nums[-1]:
            # search between indices l and n - 1 (incl.)
            l, r = l, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
        else:
            # search between indices 0 and l - 1 (incl.)
            l, r = 0, l - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

        return -1
