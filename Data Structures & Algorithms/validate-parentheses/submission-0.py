class Solution:
    def isValid(self, s: str) -> bool:
        buf = []
        pair = {')':'(', '}':'{', ']':'['}
        left_p = list(pair.values())
        for c in s:
            if c in left_p:
                buf.append(c)
            else:
                right = pair[c]
                if not buf or buf[-1] != right:
                    return False
                else:
                    buf.pop(-1)
        return len(buf)==0