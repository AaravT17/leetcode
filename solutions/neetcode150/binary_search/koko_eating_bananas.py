from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:  # O(log m) iterations (binary search between 1 and m = max(piles))
            rate = l + ((r - l) // 2)
            time_taken = sum(math.ceil(pile / rate) for pile in piles)  # O(n) per iteration (n = len(piles))
            if time_taken > h:
                # rate is not a viable solution, exclude from search range
                l = rate + 1
            else:
                # rate is a viable solution, however we do not yet know if it is the minimum viable rate
                r = rate
        # at this point, l = r = the optimal rate k
        return l
        # Time: O(n log m), Space: O(1)
