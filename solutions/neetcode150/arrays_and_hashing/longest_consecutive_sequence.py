from typing import List


class Solution:
    def get_longest_sequence(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 in s:
                continue
            curr = 1
            while num + 1 in s:
                curr += 1
                num += 1
            longest = max(curr, longest)

        return longest
        # Time: O(n), Space: O(n)
