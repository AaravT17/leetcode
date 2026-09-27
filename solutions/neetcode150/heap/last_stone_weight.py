import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap since we want the heaviest stones
        weights = [-stone for stone in stones]
        heapq.heapify(weights)
        while len(weights) > 1:
            y = -heapq.heappop(weights)  # weight of heaviest stone
            x = -heapq.heappop(weights)  # weight of second heaviest stone
            if x < y:
                heapq.heappush(weights, x - y)  # weight is y - x, but we store -weight on the heap
        return -weights[0] if weights else 0
