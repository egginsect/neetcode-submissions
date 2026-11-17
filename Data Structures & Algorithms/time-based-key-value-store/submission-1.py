from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:   
        if self.values[key] and self.values[key][-1][1] == value:
            return 
        self.values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        history = self.values.get(key, [])
        idx = bisect.bisect_right(history, timestamp, key=lambda x: x[0])
        if idx == 0:
            return ""
        return history[idx-1][1]
        

        
