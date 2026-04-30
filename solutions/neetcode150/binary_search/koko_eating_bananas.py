from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while (
            l < r
        ):  # O(log m) iterations, O(n) time per iteration (call to hrs_taken), where n = len(piles), m = max(piles)
            m = (l + r) // 2
            hrs = self.hrs_taken(piles, m)
            if hrs > h:
                # this speed is too slow, not a solution
                l = m + 1
            else:
                # this speed is a solution, but perhaps it can still be improved
                r = m
        # at this point, l = r, and this is the optimal rate
        return l
        # Time: O(n log m), Space: O(1)

    def hrs_taken(self, piles: List[int], speed: int) -> int:
        return sum(math.ceil(pile / speed) for pile in piles)
        # Time: O(n), where n = len(piles)
