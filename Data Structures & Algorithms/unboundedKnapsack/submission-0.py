from functools import cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        @cache
        def dp(i, capacity):
            if i == len(profit):
                return 0
            # skip i
            max_profit = dp(i+1, capacity)
            remaining_capacity = capacity-weight[i]
            if remaining_capacity >= 0:
                max_profit = max(profit[i]+dp(i, capacity-weight[i]), max_profit)
            return max_profit
        return dp(0, capacity)
