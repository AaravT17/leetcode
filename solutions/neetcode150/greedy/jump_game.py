class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Approach 1
        n = len(nums)
        target = n - 1
        furthest = 0
        i = 0
        while i <= furthest:
            furthest = max(furthest, i + nums[i])
            if furthest >= target:
                return True
            i += 1
        return False

        # Approach 2
        # n = len(nums)
        # target = n - 1

        # for i in range(n - 1, -1, -1):
        #     if i + nums[i] >= target:
        #         target = i

        # return target == 0
