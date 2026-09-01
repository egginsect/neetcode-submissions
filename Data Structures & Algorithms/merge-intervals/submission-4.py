class Solution:
    def merge_interval(self, left, right):
        return [min(left[0], right[0]), max(left[1], right[1])]

    def is_overlapped(self, left, right):
        return any(
            [right[0]<=left[0]<=right[1], 
            right[0]<=left[1]<=right[1], 
            left[0]<=right[0]<=left[1],
            left[0]<=right[1]<=left[1]])


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        output = [intervals[0]]
        for interval in intervals[1:]:
            if self.is_overlapped(interval, output[-1]):
                output.append(self.merge_interval(output.pop(-1), interval))
            else:
                output.append(interval)
        return output

