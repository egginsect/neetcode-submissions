import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        pq = [(-freq, key) for key, freq in counts.items()]
        heapq.heapify(pq)
        return [heapq.heappop(pq)[1] for _ in range(k)]