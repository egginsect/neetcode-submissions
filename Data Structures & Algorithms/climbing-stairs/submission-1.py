class Solution:
    def climbStairs(self, n: int) -> int:
        # n=1 1
        # n=2 f(1)+1 or 2
        # n=3 f(2)+1 or f(3)+1
        if n==1:
            return 1
        elif n==2: 
            return 2
        n_1 = 1
        n_2 = 2
        for i in range(2, n):
            n = n_1 + n_2
            n_1, n_2 = n_2, n
        return n
