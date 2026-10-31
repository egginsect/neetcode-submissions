import sys 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        mincost = prices[0]
        for num in prices[1:]:
            profit = max(profit, num-mincost)
            mincost = min(mincost, num)
        return profit

