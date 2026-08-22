from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Approach 1
        # n = len(position)  # = len(speed)
        # # sort by position (ascending order)
        # cars = [(position[i], speed[i]) for i in range(n)]
        # cars.sort(key=lambda x: x[0])
        # finish_times = []  # monotonic decreasing stack, each index represents the finish time of a single fleet
        # for p, s in cars:
        #     f = (target - p) / s
        #     while finish_times and finish_times[-1] <= f:
        #         # the previous fleet joins current car
        #         finish_times.pop()
        #     finish_times.append(f)
        # return len(finish_times)
        # Time: O(nlogn), Space: O(n)

        # Approach 2
        n = len(position)  # = len(speed)
        # sort by position (descending order)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(key=lambda x: x[0], reverse=True)
        finish_times = []
        for p, s in cars:
            f = (target - p) / s
            if not finish_times or finish_times[-1] < f:  # current car will not catch the fleet in front
                finish_times.append(f)
        return len(finish_times)
        # Time: O(nlogn), Space: O(n)
