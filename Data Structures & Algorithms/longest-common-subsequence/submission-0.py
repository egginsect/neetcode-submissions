from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache
        def dfs(s1, s2, i=0, j=0):
            if i == len(s1) or j == len(s2):
                return 0
            if s1[i] == s2[j]:
                return 1+dfs(s1, s2, i+1, j+1)
            return max(dfs(s1, s2, i, j+1), dfs(s1, s2, i+1, j))
        return dfs(text1, text2)
        