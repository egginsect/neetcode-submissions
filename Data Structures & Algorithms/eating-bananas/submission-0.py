import math
class Solution:
    def numHours(self, piles: List[int], rate: int) -> int:
        return sum([pile//rate+int(pile%rate>0) for pile in piles])

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left<=right:
            rate = (left+right)//2
            if self.numHours(piles, rate)>h:
                left = rate+1
            else:
                right = rate-1
        return left