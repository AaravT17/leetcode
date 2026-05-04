import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k_largest = nums
        self.k = k
        heapq.heapify(self.k_largest)
        while len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_largest, val)
        if len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)
        return self.k_largest[0]
