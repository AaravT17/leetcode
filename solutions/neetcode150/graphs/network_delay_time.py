import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Dijkstra's algorithm
        neighbours = {i: [] for i in range(n + 1)}
        for a, b, dt in times:
            neighbours[a].append((b, dt))

        min_heap = [(0, k)]
        seen = set()
        res = 0
        while min_heap and len(seen) < n:
            time, curr = heapq.heappop(min_heap)
            if curr in seen:
                continue
            seen.add(curr)
            res = max(res, time)
            for nei, dt in neighbours[curr]:
                if nei not in seen:
                    heapq.heappush(min_heap, (time + dt, nei))

        return -1 if len(seen) < n else res
