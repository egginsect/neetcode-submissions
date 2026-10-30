from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = [0]
        n = len(nums)
        @lru_cache
        def sum_from_index(index, remaining):
            if index == n:
                return 1 if remaining == 0 else 0
            
            return sum_from_index(index+1, remaining+nums[index])+sum_from_index(index+1, remaining-nums[index])
        
        return sum_from_index(0, target)