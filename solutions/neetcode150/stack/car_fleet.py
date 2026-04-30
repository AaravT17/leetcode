from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_indices = [
            item[0] for item in sorted(enumerate(position), key=lambda x: x[1])
        ]
        finish_times = [(target - position[i]) / speed[i] for i in sorted_indices]
        stack = []
        for t in finish_times:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)

        return len(stack)
        # Time: O(nlogn), Space: O(n)
