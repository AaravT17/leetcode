from typing import List


class Solution:
    def get_longest_sequence(self, nums: List[int]) -> int:
        s = set(nums)
        curr_len, max_len = 0, 0
        for num in s:
            if num - 1 in s:
                # num is not the start of a sequence
                continue
            while num in s:
                curr_len += 1
                num += 1
            max_len = max(curr_len, max_len)
            curr_len = 0
        return max_len
        # Time: O(n), Space: O(n)
