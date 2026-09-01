from functools import cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        @cache
        def dfs(i, capacity):
            if i == len(profit):
                return 0
            maxProfit = dfs(i+1, capacity)
            new_capacity = capacity-weight[i]
            if new_capacity>=0:
                maxProfit = max(profit[i]+dfs(i+1, new_capacity), maxProfit)
            return maxProfit
        return dfs(0, capacity)
