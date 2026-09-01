import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        num_coins = [0]+[sys.maxsize]*amount
        for i in range(amount+1):
            for coin in coins:
                if i>=coin:
                   num_coins[i] = min(num_coins[i], num_coins[i-coin]+1)
        return -1 if num_coins[-1] == sys.maxsize else num_coins[-1]