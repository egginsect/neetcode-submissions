from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for freq in count.values() if freq == max_freq)
        
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_count
        
        return max(len(tasks), empty_slots)