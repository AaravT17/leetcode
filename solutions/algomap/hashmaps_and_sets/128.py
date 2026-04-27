from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Approach 1
        # if len(nums) == 0:
        #     return 0

        # s = set(nums)
        # max_seq = 0
        # curr_seq = 0
        # i = 0
        # curr = curr_upper = curr_lower = nums[0]

        # while s:
        #     curr_seq += 1
        #     s.remove(curr)
        #     if not s:
        #         return max(max_seq, curr_seq)
        #     if curr_upper + 1 in s:
        #         curr = curr_upper = curr_upper + 1
        #     elif curr_lower - 1 in s:
        #         curr = curr_lower = curr_lower - 1
        #     else:
        #         max_seq = max(max_seq, curr_seq)
        #         curr_seq = 0
        #         i += 1
        #         while nums[i] not in s:
        #             i += 1
        #         curr = curr_upper = curr_lower = nums[i]

        # return max_seq

        # Approach 2
        if len(nums) == 0:
            return 0

        s = set(nums)
        max_seq = 0
        curr_seq = 0

        for num in s:
            if num - 1 not in s:  # then num starts a sequence
                curr_seq = 1
                while num + 1 in s:
                    curr_seq += 1
                    num += 1
                max_seq = max(max_seq, curr_seq)
                curr_seq = 0

        return max_seq
