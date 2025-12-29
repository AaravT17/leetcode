import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq is always a min-heap, negate the elements to make it work like a max-heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)  # O(n)

        while (
            len(stones) > 1
        ):  # at most n iterations, since we destroy at least one stone each time
            # the elements in the heap are negated before insertion, so we must negate again to get the correct weight
            y = -heapq.heappop(stones)  # O(log(n))
            x = -heapq.heappop(stones)  # O(log(n))
            if x != y:
                heapq.heappush(stones, x - y)  # O(log(n))

        return -stones[0] if len(stones) == 1 else 0
        # Time: O(nlog(n))
        # Space: O(1)
