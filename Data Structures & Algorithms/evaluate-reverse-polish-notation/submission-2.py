class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in '+-*/':
                right = stack.pop()
                left = stack.pop()
                if tok == '+':
                    stack.append(left+right)
                elif tok == '-':
                    stack.append(left-right)
                elif tok == '*':
                    stack.append(left*right)
                else:
                    stack.append(int(left/right))
            else:
                stack.append(int(tok))
        return stack[0]