import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        maxscore = 0
        prevsum = 0
        queue = [] # (mut, maxsum)
        items = sorted(zip(nums2, nums1), reverse=True)
        for mut, add in items:
            heapq.heappush(queue, add)
            if len(queue)>k:
                lowest = heapq.heappop(queue)
                prevsum -= lowest
            prevsum += add
            if len(queue) == k:
                maxscore = max(mut*prevsum, maxscore)
        return maxscore