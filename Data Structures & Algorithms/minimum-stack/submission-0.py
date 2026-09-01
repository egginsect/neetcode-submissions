class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = val
        if self.minimums:
            minimum = min(minimum, self.minimums[-1])
        self.minimums.append(minimum)
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minimums.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimums[-1]
