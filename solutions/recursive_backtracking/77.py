import math


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Approach 1
        # res, sol = [], []
        # nums_in_sol = set()
        # total_comb = math.comb(n, k)

        # def backtrack(i: int) -> None:
        #     if len(sol) == k:
        #         res.append(sol[:])
        #         return

        #     for num in range(i, n + 1):
        #         if len(res) == total_comb:
        #             return

        #         if num not in nums_in_sol:
        #             sol.append(num)
        #             nums_in_sol.add(num)
        #             backtrack(num + 1)
        #             sol.pop()
        #             nums_in_sol.remove(num)

        # backtrack(1)
        # return res

        # Approach 2
        res, sol = [], []

        def backtrack(x: int) -> None:
            if len(sol) == k:
                res.append(sol[:])
                return

            left = x
            needed = k - len(sol)
            if left > needed:
                backtrack(x - 1)

            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return res
