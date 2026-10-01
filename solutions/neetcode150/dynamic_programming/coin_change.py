class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)

        for amt in range(1, amount + 1):
            opt = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    continue
                opt = min(opt, 1 + dp[diff])
            dp[amt] = opt

        return dp[amount] if dp[amount] < float('inf') else -1
        # Time: O(amount * len(coins)), Space: O(amount)
