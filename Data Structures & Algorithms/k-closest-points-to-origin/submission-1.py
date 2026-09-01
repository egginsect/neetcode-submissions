import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(x**2+y**2, (x,y)) for x, y in points]
        heapq.heapify(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(k)]

        