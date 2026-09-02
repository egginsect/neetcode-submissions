class Solution:
    def isUgly(self, n: int) -> bool:
        for num in [2, 3, 5]:
            while n%num == 0:
                n = n//num
        return n == 1