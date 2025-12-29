import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)
        # Time: O(n + klog(n))
        # Space: O(1)

        # Approach 2
        # k_largest = []
        # for i in range(len(nums)):  # n iterations
        #     if len(k_largest) < k:
        #         heapq.heappush(
        #             k_largest, nums[i]
        #         )  # O(log(k)), since the heap has at most k elements
        #     else:
        #         heapq.heappushpop(k_largest, nums[i])  # O(log(k))

        # # k_largest now contains the k largest elements in nums, and since it is a min-heap, the kth largest element
        # # in nums is the minimum element in k_largest
        # return k_largest[0]
        # Time: O(nlog(k))
        # Space: O(k), since we store the k largest elements in a heap
