from functools import cache
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        wordset = set(words)
        @cache
        def dp(word):
            if not word or word not in wordset:
                return 0
            maxcount = 0
            for i in range(len(word)):
                maxcount = max(maxcount, dp(word[:i]+word[i+1:]))
            return 1+maxcount
        count = 0
        for word in words:
            count = max(dp(word), count)
        return count
