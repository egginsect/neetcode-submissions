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

        """
        zxyzxyz
        0       {z:0}.   max_len=1
        01      {z:0, x:1} max_len=2
        0 2.    {z:0, x:1, y:2} max_len=3
         1 3.   {z:4, x:1, y:2} max_len=3

        """

