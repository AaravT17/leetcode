import heapq
from collections import deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # use a max heap that stores runnable tasks sorted by count
        # use a wait queue to add tasks back onto the heap once they become runnable
        runnable_heap = []  # stores (-count, task)
        wait_queue = deque()  # stores (next_runnable_at, -count, task)

        task_count = {}
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1

        for task, count in task_count.items():
            heapq.heappush(runnable_heap, (-count, task))

        t = 0
        while runnable_heap or wait_queue:
            if runnable_heap:
                count, task = heapq.heappop(runnable_heap)
                t += 1
                if count < -1:
                    wait_queue.append((t + n, count + 1, task))
                if wait_queue and wait_queue[0][0] == t:
                    next_runnable_at, count, task = wait_queue.popleft()
                    heapq.heappush(runnable_heap, (count, task))
            else:
                t = wait_queue[0][0]
                next_runnable_at, count, task = wait_queue.popleft()
                heapq.heappush(runnable_heap, (count, task))
        return t
