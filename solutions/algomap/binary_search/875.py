from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if n == h:
            return max(piles)
        l, r = 1, max(piles)
        while (
            l < r
        ):  # O(log(max(piles))) iterations * O(n) per iteration -> O(nlog(max(piles)))
            m = (l + r) // 2
            if self.calculate_hrs_taken(piles, m, h) > h:  # O(n) per iteration
                l = m + 1
            else:
                r = m
        return r

    def calculate_hrs_taken(self, piles: List[int], k: int, h: int) -> int:
        hrs_taken = 0
        for pile in piles:
            hrs_taken += ceil(pile / k)
            if hrs_taken > h:
                return hrs_taken
        return hrs_taken
