from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # monotonic non-increasing queue
        res = []
        for r in range(len(nums)):
            # r marks the end of the window, compute l (the start of the window)
            l = r - k + 1  # k (window length) = r - l + 1 => l = r - k + 1
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                # leftmost element is now out of bounds, remove from consideration
                q.popleft()
            if l >= 0:
                res.append(nums[q[0]])
        return res
        # Time: O(n), Space: O(n)
