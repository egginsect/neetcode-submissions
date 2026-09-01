class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index = {}
        max_len = 0
        left = 0
        for idx, c in enumerate(s):
            if c in index:
                left = max(left, index[c]+1)
            max_len = max(idx-left+1, max_len)
            index[c] = idx
        return max_len

            
        return max_len 
