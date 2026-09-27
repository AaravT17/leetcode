import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # - Option 1: Use a max heap. Heapify, then pop points off until we are left with k points.
        #   Time: O(nlogn), Space: O(n).
        # - Option 2: Use a min heap. Heapify, then pop off k points.
        #   Time: O(n + klogn), Space: O(n).
        # - Option 3: Use a max heap of size <= k. Each time we add a point, if size > k, pop one off.
        #   Time: O(nlogk), Space: O(k).
        # Option 1 is a no-go, use option 2 or 3.
        # Option 3
        max_heap = []  # stores (-dist^2, x, y)
        for x, y in points:
            dist_sq = x**2 + y**2
            heapq.heappush(max_heap, (-dist_sq, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[x, y] for dist, x, y in max_heap]
