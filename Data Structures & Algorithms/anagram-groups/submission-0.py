import heapq
class Solution:
    def hash_to_key(self, word):
        count = [0]*26
        for c in word:
            count[ord(c)-ord('a')]+=1
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_table = {}
        for word in strs:
            key = self.hash_to_key(word)
            val_list = lookup_table.get(key, [])
            val_list.append(word)
            lookup_table[key] = val_list
        return list(lookup_table.values())
        
        