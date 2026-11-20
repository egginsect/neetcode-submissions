class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        numway = [0]*(amount+1)
        numway[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                numway[i] += numway[i-coin]
        return numway[-1]
            