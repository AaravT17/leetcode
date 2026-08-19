from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def dp(amt: int) -> int:
            if amt not in memo:
                opt = float('inf')
                for coin in coins:
                    rem = amt - coin
                    if rem >= 0:
                        opt = min(opt, 1 + dp(rem))
                memo[amt] = opt

            return memo[amt]

        res = dp(amount)
        return res if res < float('inf') else -1
        # Time: O(amount * len(coins)), Space: O(amount)
