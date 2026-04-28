from typing import List
from collections import Counter
import heapq


class Solution:
    def find_k_most_freq(self, nums: List[int], k: int) -> List[int]:
        # Approach 1: Counter + PQ
        # counts = Counter(nums)
        # min_heap = []  # heapq only works with min heaps
        # for num, freq in counts.items():
        #     if len(min_heap) >= k:
        #         heapq.heappushpop(min_heap, (freq, num))
        #     else:
        #         heapq.heappush(min_heap, (freq, num))

        # return [num for freq, num in min_heap]
        # Time: O(nlogk), Space: O(n + k) = O(n)
        # Note: Can also use max heap and pop k times, that would be O(n + klogn) time and O(n) space

        # Approach 2: Bucket Sort
        n = len(nums)
        counts = Counter(nums)
        freq_buckets = [[] for _ in range(n + 1)]
        # must ensure that each bucket refers to a distinct list ([[]] * (n + 1) does not work because each
        # bucket would refer to the same list)
        for num, freq in counts.items():
            freq_buckets[freq].append(num)

        res = []
        for i in range(n, 0, -1):
            res.extend(freq_buckets[i])
            if len(res) >= k:
                # will never be > k, only == k, because the constraints guarantee that the answer is unique,
                # so there will never be a tie for the kth most frequent element
                break

        return res
        # Time: O(n), Space: O(n)
