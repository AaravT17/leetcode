from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return max_heap[0]
        # Time: O(nlogk), Space: O(k)
