from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Approach 1
        res, sol = [], []

        def permute_recursive() -> None:
            n = len(nums)
            if n == 0:
                res.append(sol[:])
                return

            for i in range(n):
                sol.append(nums.pop(i))
                permute_recursive()
                nums.insert(i, sol.pop())

        permute_recursive()
        return res

        # Approach 2
        # res, sol = [], []
        # nums_in_sol = set()

        # def backtrack() -> None:
        #     if len(sol) == len(nums):
        #         res.append(sol[:])
        #         return

        #     for num in nums:
        #         if num not in nums_in_sol:
        #             sol.append(num)
        #             nums_in_sol.add(num)
        #             backtrack()
        #             sol.pop()
        #             nums_in_sol.remove(num)

        # backtrack()
        # return res
