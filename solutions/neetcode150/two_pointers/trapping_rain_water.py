from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach 1
        # The water stored over a particular index i equals the min of tallest height to its 
        # left and right - the height at i
        # n = len(height)
        # tallest_left, tallest_right = [0] * n, [0] * n
        # for l in range(1, n):
        #     r = n - l - 1
        #     tallest_left[l] = max(tallest_left[l - 1], height[l - 1])
        #     tallest_right[r] = max(tallest_right[r + 1], height[r + 1])

        # total = 0
        # for i in range(1, n - 1):
        #     total += max(0, min(tallest_left[i], tallest_right[i]) - height[i])

        # return total
        # Time: O(n), Space: O(n)

        # Approach 2
        total = 0
        l, r = 0, len(height) - 1
        tallest_left, tallest_right = 0, 0
        while l <= r:
            if tallest_left < tallest_right:
                total += max(0, tallest_left - height[l])
                tallest_left = max(height[l], tallest_left)
                l += 1
            else:
                total += max(0, tallest_right - height[r])
                tallest_right = max(height[r], tallest_right)
                r -= 1
        return total
        # Time: O(n), Space: O(1)

        # Approach 3
        # tallest = 0
        # for i in range(1, len(height)):
        #     if height[i] > height[tallest]:
        #         tallest = i

        # total = 0
        # l, r = 0, 1
        # while l < tallest:
        #     while height[l] > height[r]:
        #         # the shorter of the two walls of the well will be the left wall in this pass from 0 -> tallest
        #         total += height[l] - height[r]
        #         r += 1
        #     l, r = r, r + 1

        # r, l = len(height) - 1, len(height) - 2
        # while r > tallest:
        #     while height[r] > height[l]:
        #         total += height[r] - height[l]
        #         l -= 1
        #     r, l = l, l - 1

        # return total
        # Time: O(n), Space: O(1)
