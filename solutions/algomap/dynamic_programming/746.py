class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # the cheapest path to level n will be the cheaper of the following:
        #   - the cheapest way to get to n - 1 + the cost at n - 1
        #   - the cheapest way to get to n - 2 + the cost at n - 2

        # Top-down memoization
        # memo = {0: 0, 1: 0}

        # def f(x: int) -> int:
        #     if x not in memo:
        #         memo[x] = min(f(x - 1) + cost[x - 1], f(x - 2) + cost[x - 2])

        #     return memo[x]

        # return f(len(cost))

        # Bottom-up tabulation
        # n = len(cost)
        # table = [0] * (n + 1)

        # for i in range(2, n + 1):
        #     table[i] = min(table[i - 1] + cost[i - 1], table[i - 2] + cost[i - 2])

        # return table[n]

        # Bottom-up with constant space
        n = len(cost)
        prev, curr = 0, 0

        for i in range(2, n + 1):
            prev, curr = curr, min(prev + cost[i - 2], curr + cost[i - 1])

        return curr
