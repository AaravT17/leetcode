from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach 1
        # result = []
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)

        # for i in range(len(nums)):
        #     if i > 0:
        #         prefix[i] = prefix[i - 1] * nums[i - 1]
        #         suffix[-i - 1] = suffix[-i] * nums[-i]

        # for i in range(len(nums)):
        #     result.append(prefix[i] * suffix[i])

        # return result

        # Approach 2
        result = [1] * len(nums)

        for i in range(len(nums)):
            if i > 0:
                result[i] = result[i - 1] * nums[i - 1]
                # To reuse nums to temporarily store the suffix products, we
                # can first left shift the array so that values required later
                # don't get overwritten
                nums[i - 1] = nums[i]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                nums[i] = 1
            else:
                nums[i] *= nums[i + 1]
            result[i] *= nums[i]

        return result
