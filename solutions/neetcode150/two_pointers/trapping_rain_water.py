from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach 1
        tallest = 0
        for i in range(1, len(height)):
            if height[i] > height[tallest]:
                tallest = i

        total = 0
        l, r = 0, 1
        while l < tallest:
            while height[l] > height[r]:
                # the shorter of the two walls of the well will be the left wall in this pass from 0 -> tallest
                total += height[l] - height[r]
                r += 1
            l, r = r, r + 1

        r, l = len(height) - 1, len(height) - 2
        while r > tallest:
            while height[r] > height[l]:
                total += height[r] - height[l]
                l -= 1
            r, l = l, l - 1

        return total
        # Time: O(n), Space: O(1)

        # Approach 2
        # The water stored over a particular index equals the min of tallest height on its left and right - the
        # height at that index
        # n = len(height)
        # max_height_left = [0] * n
        # max_height_right = [0] * n
        # for i in range(1, n):
        #     r = n - i - 1
        #     max_height_left[i] = max(max_height_left[i - 1], height[i - 1])
        #     max_height_right[r] = max(max_height_right[r + 1], height[r + 1])
        # return sum(
        #     max(0, min(max_height_left[i], max_height_right[i]) - height[i])
        #     for i in range(n)
        # )
        # Time: O(n), Space: O(n)

        # Approach 3
        # l, r = 0, len(height) - 1
        # max_height_left, max_height_right = height[l], height[r]
        # total = 0
        # while l < r:
        #     if max_height_left < max_height_right:
        #         l += 1
        #         max_height_left = max(max_height_left, height[l])
        #         total += max_height_left - height[l]
        #     else:
        #         r -= 1
        #         max_height_right = max(max_height_right, height[r])
        #         total += max_height_right - height[r]

        # return total
        # Time: O(n), Space: O(1)
