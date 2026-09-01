from bisect import bisect_left
class MyCalendar:
    
    def __init__(self):
        self.meetings = []

    def book(self, startTime: int, endTime: int) -> bool:
        new_interval = (startTime, endTime)
        idx = bisect_left(self.meetings, new_interval)
        if idx<len(self.meetings) and self.meetings[idx][0]<endTime:
            return False
        if idx>0 and self.meetings[idx-1][1]>startTime:
            return False
        self.meetings.insert(idx, new_interval)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)