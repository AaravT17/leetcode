from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                # we cannot find a triplet [nums[i], x, y] with nums[i] <= x <= y and sum = 0 if nums[i] > 0
                break
            # run two sum on the remainder of nums with target = -nums[i]
            l, r = i + 1, n - 1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    # find a new second value to ensure that, if we find another triplet, it is distinct
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
            # find a new starting value so that we get a distinct triplet the next time
            i += 1
            while i < n - 2 and nums[i] == nums[i - 1]:
                i += 1

        return res
        # Time: O(nlogn) + O(n^2) = O(n^2), Space: O(1)
