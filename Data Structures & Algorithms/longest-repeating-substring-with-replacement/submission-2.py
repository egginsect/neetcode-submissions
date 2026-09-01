class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        A A A B A B B
        l r
        l   r
        l     r
        l       r
        l         r
          l         r
        """
        freq_map = {}
        left = 0
        max_len = 0

        def max_freq():
            return sorted(freq_map.items(), key=lambda x:-x[1])[0][1]

        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right],0)+1
            length = right-left+1
            if length-max_freq()<=k:
                max_len = max(length, max_len)
            else:
                freq_map[s[left]]-=1
                left+=1
        return max_len
                
            
        