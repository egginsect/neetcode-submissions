class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack:
                stack[-1][1] = stack[-1][1]%k
                if stack[-1][1] == 0:
                    stack.pop()
        out = ""
        for c, count in stack:
            out += c*count
        return out

        