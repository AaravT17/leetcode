class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        target = n - 1
        jumps = 0
        l, r = 0, 0
        while r < target:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l, r = r + 1, furthest
            jumps += 1
        return jumps
