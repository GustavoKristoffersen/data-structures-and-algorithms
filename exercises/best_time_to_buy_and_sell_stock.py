# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        smallest = prices[0]
        for p in prices[1:]:
            if p <= smallest:
                smallest = p
            elif (p - smallest) > max_profit:
                max_profit = p - smallest
        return max_profit

