from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_vol = 0
        while l < r:
            vol = (r - l) * min(height[l], height[r])
            max_vol = max(vol, max_vol)
            # keep the taller wall, maximises potential volume we can achieve
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_vol
        # Time: O(n), Space: O(1)
