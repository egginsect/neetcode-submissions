from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)
        f_max = max(freq.values())
        num_max = sum(1 for count in freq.values() if count == f_max)
        return max(len(tasks), (f_max - 1) * (n + 1) + num_max)
