class Solution:
    def climbStairs(self, n: int) -> int:
        # we can get to n either by taking 1 step from n - 1 or 2 steps from n - 2
        # the total number of ways we can get to n is the sum of all the ways we can get to n - 1 (onto which we add
        # +1 step) and all the ways we can get to n - 2 (onto which we add +2 steps) i.e. f(n) = f(n - 1) + f(n - 2)
        if n == 1:
            return 1

        if n == 2:
            return 2

        prev, curr = 1, 2

        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr
        # Time: O(n)
        # Space: O(1)
