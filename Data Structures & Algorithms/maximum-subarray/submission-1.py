class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        max_prefix = 0
        """
        2, -3, 4, -2, 2, 1, -1 4
        .   
            .
        """
        for num in nums:
            max_prefix = max(0, max_prefix) + num
            max_sum = max(max_prefix, max_sum)
        return max_sum

