class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_sum_map = {0: 1}  # maps prefix sum -> number of times seen so far
        res = 0
        for num in nums:
            prefix_sum += num
            res += prefix_sum_map.get(prefix_sum - k, 0)
            prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1
        return res
