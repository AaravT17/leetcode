from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # if some day has the lowest price so far, set that to be the day on which we buy, if not, calculate profit
        # if we were to sell on that day and set max_profit to max(profit, max_profit)
        buy, i = 0, 1
        while i < len(prices):
            if prices[i] < prices[buy]:
                buy = i  # prices[i] is the lowest price so far, so set the buy day to i
            else:
                max_profit = max(prices[i] - prices[buy], max_profit)
            i += 1
        return max_profit
