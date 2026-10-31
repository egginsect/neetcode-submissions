from collections import defaultdict
class Solution:
    def get_key(self, word):
        key = [0]*26
        for c in word:
            key[ord(c)-ord('a')] += 1
        return tuple(key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = self.get_key(word)
            groups[key].append(word)
        return list(groups.values())
