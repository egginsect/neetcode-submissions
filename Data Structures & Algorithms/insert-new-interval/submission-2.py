class Solution:
    def merge_interval(self, interval1, interval2):
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

    def is_overlapped(self, interval1, interval2):
        return any([interval2[0]<=interval1[0]<=interval2[1], 
                    interval2[0]<=interval1[1]<=interval2[1], 
                    interval1[0]<=interval2[0]<=interval1[1],
                    interval1[0]<=interval2[1]<=interval1[1],])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """  
            [6, 7] [1,2],[3,5],[9,10]
            [1, 2], [3,5],[6, 7] 
        """
        out = []
        current = newInterval.copy()
        for interval in intervals:
            if not current:
                out.append(interval)
            elif self.is_overlapped(current, interval):
                current = self.merge_interval(current, interval)
            else:
                if interval[0]>current[1]:
                    out.append(current)
                    current = []
                out.append(interval)
        if current:
            out.append(current)
        return out