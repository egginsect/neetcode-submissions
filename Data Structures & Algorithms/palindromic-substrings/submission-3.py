class Solution:


    def countSubstrings(self, s: str) -> int:
        count = 0

        def isPalindrome(left, right):
            nonlocal count
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    count+=1
                else:
                    break
                left-=1
                right+=1

        for i in range(len(s)):
            isPalindrome(i, i)
            isPalindrome(i, i+1)
        return count