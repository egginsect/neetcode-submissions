class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = 0
        self.string = compressedString
        self.c = ""
        self.count = 0
        

    def next(self) -> str:
        if not self.hasNext():
            return " "
        self.count -= 1 
        return self.c

    def hasNext(self) -> bool:
        if self.count > 0:
            return True
        if self.idx == len(self.string):
            return False
        self.c = self.string[self.idx]
        self.idx += 1
        while self.idx<len(self.string) and self.string[self.idx].isnumeric():
            self.count = self.count * 10 + int(self.string[self.idx])
            self.idx += 1
        return self.count > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
