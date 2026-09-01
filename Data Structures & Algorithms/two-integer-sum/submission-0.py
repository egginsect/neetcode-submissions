class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p_sum = {}
        for idx, num in enumerate(nums):
            if target-num in p_sum:
                return [p_sum[target-num], idx]
            p_sum[num] = idx
        