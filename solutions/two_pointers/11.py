from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Idea: Start as wide as possible to maximise width, then on each
        # iteration, as we move the two pointers inwards and narrow the
        # container, try to maximise the height i.e. keep the taller side and
        # move away from the shorter wall since there is no way keeping the
        # shorter wall can give us a new max volume since, in doing so, we
        # would narrow the width and at best maintain the height
        max_vol = 0
        left, right = 0, len(height) - 1

        while left < right:
            vol = (right - left) * min(height[left], height[right])
            if vol > max_vol:
                max_vol = vol
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol
