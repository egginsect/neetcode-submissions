
class Freq:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq
    
    def __lt__(self, right):
        return self.freq > right.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freqs = []
        out = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for key, freq in counter.items():
            freqs.append(Freq(key, freq))
        heapq.heapify(freqs)
        for _ in range(k):
            try:
                freq = heapq.heappop(freqs)
                out.append(freq.val)
            except:
                pass
        return out