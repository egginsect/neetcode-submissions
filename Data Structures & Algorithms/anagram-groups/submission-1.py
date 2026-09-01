from collections import defaultdict
class Solution:
    def to_key(self, s):
        out = [0]*26
        for c in s:
            out[ord(c.lower())-ord('a')]+=1
        return tuple(out)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            out[self.to_key(s)].append(s)
        return list(out.values())

        