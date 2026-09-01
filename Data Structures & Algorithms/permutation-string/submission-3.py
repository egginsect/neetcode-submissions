from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        counts = Counter(s1)
        window = Counter()
        for i, c in enumerate(s2):
            window[c] += 1
            if i>=len(s1):
                left_char = s2[i-len(s1)]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            if window == counts:
                return True
        return False
