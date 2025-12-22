from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Approach 1
        # n = len(nums)
        # flipped = set()  # tracks which indices we have flipped from 0 to 1

        # l, r = 0, 0
        # longest = 0

        # while r < n:
        #     if nums[r] == 1 or k > 0:
        #         if nums[r] == 0:
        #             # we must flip the 0 to 1 to progress R
        #             flipped.add(r)
        #             k -= 1
        #         r += 1
        #         longest = max(longest, r - l)
        #     else:  # nums[r] == 0 and k == 0, so we cannot progress R
        #         # progress L, and if it overtakes R, increase R to match L (will only be +1 in practice)
        #         if l in flipped:
        #             flipped.remove(l)
        #             k += 1
        #         l += 1
        #         if l > r:
        #             r += 1

        # return longest
        # Time: O(n)
        # Space: O(k)

        # Approach 2
        n = len(nums)
        num_zeros = 0
        l = 0
        longest = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:  # window is currently invalid, make it valid again
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            # we have a valid window from L to R, inclusive, update longest sequence
            longest = max(longest, (r - l) + 1)

        return longest
        # Time: O(n)
        # Space: O(1)
