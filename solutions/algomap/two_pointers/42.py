from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach 1
        # n = len(height)
        # total = 0
        # left, right = 0, 1
        # curr_seq = []

        # while right < n:
        #     if height[left] > height[right]:
        #         curr_seq.append(height[right])
        #         right += 1
        #     else:
        #         curr_seq_height = min(height[left], height[right])
        #         for h in curr_seq:
        #             total += curr_seq_height - h
        #         curr_seq = []
        #         left, right = right, right + 1

        # return total
        # Note that this approach doesn't work, it's shortcoming is mentioned
        # in the notes, but it does form the basis for Approach 2, which works,
        # and solves the problem in O(n) time and uses O(1) extra space

        # Approach 2
        n = len(height)
        max_height = 0

        for i in range(1, n):
            if height[i] >= height[max_height]:
                max_height = i

        total = 0
        left, right = 0, 1

        while right <= max_height:
            if height[left] > height[right]:
                total += height[left] - height[right]
                right += 1
            else:
                left, right = right, right + 1

        left, right = n - 2, n - 1

        while left >= max_height:
            if height[right] > height[left]:
                total += height[right] - height[left]
                left -= 1
            else:
                left, right = left - 1, left

        return total

        # Approach 3
        # Idea: The volume of water stored at each index/the volume of water
        # that collects over each index is equal to the minimum of the heights
        # of the tallest walls to the left and right of that index (i.e., the
        # potential water that could collect there) minus the height at that
        # index itself, this height is only added to the total if it is > 0 (a
        # negative volume of water cannot collect, so any volume <= 0 defaults
        # to 0)
        # n = len(height)
        # l_wall = r_wall = 0
        # max_left = [0] * n
        # max_right = [0] * n

        # for i in range(n):
        #     max_left[i] = l_wall
        #     max_right[-i - 1] = r_wall
        #     if height[i] > l_wall:
        #         l_wall = height[i]
        #     if height[-i - 1] > r_wall:
        #         r_wall = height[-i - 1]

        # total = 0
        # for i in range(n):
        #     potential = min(max_left[i], max_right[i])
        #     vol = potential - height[i]
        #     if vol > 0:
        #         total += vol

        # return total
