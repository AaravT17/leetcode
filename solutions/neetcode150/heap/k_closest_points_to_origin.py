from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach 1: Min heap
        # dists = [(x**2 + y**2, x, y) for x, y in points]
        # heapq.heapify(dists)
        # res = []
        # for _ in range(k):
        #     elem = heapq.heappop(dists)
        #     res.append([elem[1], elem[2]])
        # return res
        # Time: O(n + klogn), Space: O(n)

        # Approach 2: Max heap
        max_heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(max_heap, (-dist, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for dist, x, y in max_heap]
        # Time: O(nlogk), Space: O(k)
