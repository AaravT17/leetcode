from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = [
            -weight for weight in stones
        ]  # need -weight because heapq works with min heaps
        heapq.heapify(weights)
        while len(weights) >= 2:
            y = -heapq.heappop(weights)  # heaviest
            x = -heapq.heappop(weights)  # second heaviest
            if x < y:
                # push new stone of weight y - x onto the heap
                # since the heap contains -weight, push x - y
                heapq.heappush(weights, x - y)
        return -weights[0] if weights else 0
