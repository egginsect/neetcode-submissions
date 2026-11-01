import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        pq = []
        for key, freq in counts.items():
            heapq.heappush(pq, (freq, key))
            if len(pq)>k:
                heapq.heappop(pq)
        return [item[1] for item in pq]