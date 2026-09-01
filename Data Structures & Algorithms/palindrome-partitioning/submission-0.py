from functools import cache
class Solution:
    @cache
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        n = len(s)
        def dfs(i):
            if i >= n:
                res.append(path.copy())
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return res
    
        
                