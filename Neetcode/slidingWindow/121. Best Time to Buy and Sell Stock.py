https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit =max(prices[right] - prices[left],max_profit)
            else:
                left = right
            right += 1
        return max_profit