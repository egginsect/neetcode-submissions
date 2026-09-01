import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            heapq.heappush(min_heap, (x**2+y**2, (x,y)))
        return [heapq.heappop(min_heap)[1] for _ in range(k)]

        