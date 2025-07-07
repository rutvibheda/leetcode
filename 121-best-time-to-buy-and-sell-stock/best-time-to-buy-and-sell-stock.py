class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #left for buy and right for sell
        left, right = 0, 1 
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right = right + 1
        return max_profit