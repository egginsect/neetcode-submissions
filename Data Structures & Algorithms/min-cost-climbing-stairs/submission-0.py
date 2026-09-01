class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = prev1 = 0
        total = 0
        for idx in range(2, len(cost)+1):
            total = min(prev1+cost[idx-1], prev2+cost[idx-2])
            prev1, prev2 = total, prev1
        return total