class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.cap = capacity

    def get(self, i: int) -> int:
        if i<len(self.arr) and i>=0:
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i<len(self.arr) and i>=0: 
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if len(self.arr)==self.cap:
            self.resize()
        self.arr.append(n)

    def popback(self) -> int:
        if len(self.arr) > 0:
            return self.arr.pop(-1)

    def resize(self) -> None:
        self.cap = self.cap*2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.cap
