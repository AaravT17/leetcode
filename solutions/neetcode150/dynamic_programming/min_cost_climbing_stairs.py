from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev, curr = 0, 0
        for i in range(2, n + 1):
            prev, curr = curr, min(prev + cost[i - 2], curr + cost[i - 1])
        return curr
        # Time: O(n), Space: O(1)
