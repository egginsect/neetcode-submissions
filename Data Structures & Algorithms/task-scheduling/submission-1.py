from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)
        cycle = 0
        while max_heap:
            buf = []
            for _ in range(n+1):
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    cnt += 1 
                    if cnt<0:
                        buf.append(cnt)
                cycle+=1
                if not (max_heap or buf):
                    break
            for cnt in buf:
                heapq.heappush(max_heap, cnt)
        return cycle
