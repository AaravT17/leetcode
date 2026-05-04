from typing import List
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # schedule the task with the highest frequency earliest
        freqs = Counter(tasks)
        max_heap = []  # holds elements of the form (-freq, task)
        q = deque()  # holds elements of the form (task, freq, next_runnable_at)
        for task, freq in freqs.items():
            heapq.heappush(max_heap, (-freq, task))

        t = 0
        while max_heap or q:
            # either we have tasks currently ready to run, or we have tasks on the queue that will run eventually
            t += 1
            if max_heap:
                elem = heapq.heappop(max_heap)
                if (
                    elem[0] < -1
                ):  # this task must be executed at least once more, add to queue
                    q.append((elem[1], -elem[0] - 1, t + n))

            if q and q[0][2] == t:
                # only one task from the queue becomes runnable at a given time, so we need only check the first
                # element in the queue
                task, freq, next_runnable_at = q.popleft()
                heapq.heappush(max_heap, (-freq, task))

        return t
