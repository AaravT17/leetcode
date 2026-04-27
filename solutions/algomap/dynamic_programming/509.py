class Solution:
    def fib(self, n: int) -> int:
        # Approach 1: Recursion
        # if n == 0:
        #     return 0

        # if n == 1:
        #     return 1

        # return self.fib(n - 1) + self.fib(n - 2)
        # Time: O(2^n)
        # Space: O(n)

        # Approach 2: Top-down Memoization (cache the result of previous function calls)
        # memo = {0: 0, 1: 1}

        # def f(x: int) -> int:
        #     if x not in memo:
        #         memo[x] = memo[x - 1] + memo[x - 2]

        #     return memo[x]

        # return f(n)
        # Time: O(n)
        # Space: O(n)

        # Approach 3: Bottom-up Tabulation
        # if n == 0:
        #     return 0

        # if n == 1:
        #     return 1

        # table = [0] * (n + 1)
        # table[1] = 1

        # for x in range(2, n + 1):
        #     table[x] = table[x - 1] + table[x - 2]

        # return table[n]
        # Time: O(n)
        # Space: O(n)

        # Approach 4: Bottom-up with constant space (only keep relevant values)
        if n == 0:
            return 0

        if n == 1:
            return 1

        prev, curr = 0, 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr
        # Time: O(n)
        # Space: O(1)
