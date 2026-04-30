from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                val = stack.pop()
                res[val[0]] = i - val[0]
            stack.append((i, t))
        return res
        # Time: O(n), Space: O(n)
