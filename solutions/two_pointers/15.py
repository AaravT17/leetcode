from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Approach 1
        # Idea: For all x, y, we can check if z = -x - y is in s i.e., a
        # triplet exists for given x, y
        # found = set()
        # h = {nums[i]: i for i in range(len(nums))}

        # for i in range(len(nums)):
        #     x = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         y = nums[j]
        #         z = -x - y
        #         if z in h and h[z] != i and h[z] != j:
        #             found.add(tuple(sorted([x, y, z])))

        # return [list(triplet) for triplet in found]
        # Not quite brute force, but very inefficient, O(n^2), plus the constant
        # work in each iteration, i.e. sorting and hashing, is expensive

        # Approach 2
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            target = -nums[i]
            while left < right:
                val = nums[left] + nums[right]
                if val == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif val < target:
                    left += 1
                else:
                    right -= 1

        return result
