class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        key = tuple(point)
        self.points[key] = self.points.get(key, 0) + 1
        

    def count(self, point: List[int]) -> int:
        count = 0
        for key in self.points.keys():
            x2 = (point[0]-key[0])**2
            y2 = (point[1]-key[1])**2
            if x2>0 and y2>0 and x2 == y2 :
                k1 = (key[0], point[1])
                k2 = (point[0], key[1])
                count += self.points[key]*self.points.get(k1, 0)*self.points.get(k2, 0)
        return count

        
