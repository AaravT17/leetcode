from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        potential_buy = 0  # index at which we may potentially buy

        for i in range(len(prices)):
            if prices[i] < prices[potential_buy]:
                potential_buy = i
            elif prices[i] - prices[potential_buy] > max_profit:
                max_profit = prices[i] - prices[potential_buy]

        return max_profit
