class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        valid_char = set("abcdefghijklmnopqrstuvwxyz1234567890")
        while i<j:
            while(s[i].lower() not in valid_char and i<j):
                i+=1
            while(s[j].lower() not in valid_char and j>i):
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True