class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.p1 = 0
        self.p2 = 0

    def next(self) -> int:
        if self.p1>=len(self.v1): 
            val = self.v2[self.p2]
            self.p2+=1
        elif self.p2 >= len(self.v2):
            val = self.v1[self.p1]
            self.p1+=1
        else:
            if self.p1 == self.p2:
                val = self.v1[self.p1]
                self.p1+=1
            else:
                val = self.v2[self.p2]
                self.p2+=1
        return val


        

    def hasNext(self) -> bool:
        return self.p1 + self.p2 < len(self.v1)+len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
