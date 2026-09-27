import heapq
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1: Create a max heap and pop k elements, kth element popped = kth largest element
        # max_heap = [-n for n in nums]
        # heapq.heapify(max_heap)
        # # pop k-1 times
        # for i in range(k-1):
        #     heapq.heappop(max_heap)
        # # pop once more (for the kth time) and return the popped number
        # return -heapq.heappop(max_heap)
        # Time: O(n + klogn), Space: O(n)

        # Approach 2: Maintain a min heap of the k largest elements, topmost element of heap = kth largest element
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
        # Time: O(nlogk), Space: O(k)

        # Approach 3: Quick select
        # n = len(nums)
        # reqd_idx = n - k
        # l, r = 0, n - 1
        # while True:
        #     pivot = nums[random.randint(l, r)]
        #     lt, gt = l, r
        #     i = l
        #     while i <= gt:
        #         if nums[i] < pivot:
        #             nums[lt], nums[i] = nums[i], nums[lt]
        #             lt += 1
        #             i += 1
        #         elif nums[i] > pivot:
        #             nums[gt], nums[i] = nums[i], nums[gt]
        #             gt -= 1
        #         else:
        #             i += 1

        #     if reqd_idx < lt:
        #         r = lt - 1
        #     elif reqd_idx > gt:
        #         l = gt + 1
        #     else:
        #         return pivot
        # Time: O(n) avg, O(n^2) worst case, Space: O(1)
