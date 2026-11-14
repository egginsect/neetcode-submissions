from collections import OrderedDict
import random
class RandomizedSet:

    def __init__(self):
        self.valueidx = {}
        self.values = []
        

    def insert(self, val: int) -> bool:
        if val in self.valueidx:
            return False
        idx = len(self.values)
        self.values.append(val)
        self.valueidx[val] = idx
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueidx:
            return False

        idx = self.valueidx[val]
        lastval = self.values[-1]

        # Move the last value into the removed value's slot
        self.values[idx] = lastval
        self.valueidx[lastval] = idx

        # Remove the final element
        self.values.pop()
        del self.valueidx[val]

        return True
            

    def getRandom(self) -> int:
        select = random.randint(0,len(self.values)-1)
        return self.values[select]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()