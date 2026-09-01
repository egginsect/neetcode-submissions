class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum+num, num)
            max_val = max(max_val, current_sum)
        return max_val