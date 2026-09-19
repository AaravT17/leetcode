from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If the current day has the lowest price so far, set it to be the buy day.
        # If not, calculate profit if we were to sell on the current day and set max_profit = max(max_profit, profit).
        buy_day = 0
        max_profit = 0
        for curr_day in range(len(prices)):
            if prices[curr_day] < prices[buy_day]:
                buy_day = curr_day
            else:
                max_profit = max(max_profit, prices[curr_day] - prices[buy_day])
        return max_profit
