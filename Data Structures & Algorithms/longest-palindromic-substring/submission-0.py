class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_str = [""]
        n = len(s)
        for i in range(n):
            for j in range(i, min(i+2, n)):
                left = i
                right = j
                while left>=0 and right<n :
                    if s[left] == s[right]:
                        if len(max_str[0])<right-left+1:
                            max_str[0] = s[left:right+1]
                        left-=1
                        right+=1
                    else:
                        break
        return max_str[0]