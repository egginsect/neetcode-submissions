from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        out = ""
        q = [(-freq, c) for c, freq in count.items()]
        heapq.heapify(q)
        while q:
            tmp = None
            if out and out[-1] == q[0][1]:
                negfreq, c = heapq.heappop(q)
                tmp = (negfreq, c)
            if not q:
                return ""
            negfreq, c = heapq.heappop(q)
            out += c
            negfreq += 1
            if negfreq < 0:
                heapq.heappush(q, (negfreq, c))
            if tmp is not None:
                heapq.heappush(q, tmp)
        return out

