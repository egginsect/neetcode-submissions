class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = 0
        for price in prices[1:]:
            profit = max(profit, price-cost)
            cost = min(price, cost)
        return profit
        