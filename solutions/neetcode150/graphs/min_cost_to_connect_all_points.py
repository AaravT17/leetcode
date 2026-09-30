import heapq


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Prim's algorithm
        n = len(points)
        seen = set()

        def _get_neighbours(i: int) -> list[tuple[int, int]]:
            x_i, y_i = points[i]
            neighbours = []
            for j in range(n):
                if j == i:
                    continue
                x_j, y_j = points[j]
                weight = abs(x_i - x_j) + abs(y_i - y_j)
                neighbours.append((j, weight))
            return neighbours

        total_cost = 0
        min_heap = [(0, 0)]
        while min_heap and len(seen) < n:
            cost, pt = heapq.heappop(min_heap)
            if pt in seen:
                continue
            seen.add(pt)
            total_cost += cost
            neighbours = _get_neighbours(pt)
            for nei, weight in neighbours:
                if nei not in seen:
                    heapq.heappush(min_heap, (weight, nei))

        return total_cost
