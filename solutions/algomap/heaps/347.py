from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approach 1
        # counts = Counter(nums)  # O(n)
        # k_most_freq = []
        # for num, count in counts.items():  # at most n iterations
        #     if len(k_most_freq) < k:
        #         heapq.heappush(
        #             k_most_freq, (count, num)
        #         )  # O(log(k)), since the heap has at most k elements
        #     else:
        #         heapq.heappushpop(k_most_freq, (count, num))

        # return [item[1] for item in k_most_freq]  # O(k)
        # Time: O(n + nlog(k) + k), which is O(nlog(k))
        # Space: O(k)

        # Approach 2
        n = len(nums)
        counts = Counter(nums)
        freq_buckets = [0] * (n + 1)

        for num, freq in counts.items():
            if freq_buckets[freq] == 0:
                freq_buckets[freq] = [num]
            else:
                freq_buckets[freq].append(num)

        k_most_freq = []
        for i in range(n, -1, -1):
            if freq_buckets[i] != 0:
                k_most_freq.extend(freq_buckets[i])
            if len(k_most_freq) == k:
                break

        return k_most_freq
        # Time: O(n)
        # Space: O(n)
