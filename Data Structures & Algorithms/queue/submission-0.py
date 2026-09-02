class Deque:
    
    def __init__(self):
        self.buf = []

    def isEmpty(self) -> bool:
        return len(self.buf) == 0

    def append(self, value: int) -> None:
        self.buf.append(value)

    def appendleft(self, value: int) -> None:
        self.buf.insert(0, value)

    def pop(self) -> int:
        if len(self.buf) == 0:
            return -1
        return self.buf.pop(-1)

    def popleft(self) -> int:
        if len(self.buf) == 0:
            return -1
        return self.buf.pop(0)
