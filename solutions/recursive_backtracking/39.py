from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Approach 1
        # res, sol = [], []
        # curr_sum = [0]
        # found = set()

        # def backtrack():
        #     for num in candidates:
        #         sol.append(num)
        #         curr_sum[0] += num
        #         if curr_sum[0] < target:
        #             backtrack()
        #         elif curr_sum[0] == target:
        #             sorted_sol = tuple(sorted(sol))
        #             if sorted_sol not in found:
        #                 res.append(sol[:])
        #                 found.add(sorted_sol)
        #         sol.pop()
        #         curr_sum[0] -= num

        # backtrack()
        # return res

        # Approach 2
        res, sol = [], []

        def backtrack(i: int, curr_sum: int) -> None:
            if curr_sum == target:
                res.append(sol[:])
                return

            if curr_sum > target or i == len(candidates):
                return

            # path 1: do not include nums[i], and do not consider nums[i] for further inclusion
            backtrack(i + 1, curr_sum)

            # path 2: include nums[i]
            sol.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            sol.pop()

        backtrack(0, 0)
        return res
