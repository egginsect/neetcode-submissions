class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)

        for num in nums:
            if not num-1 in nums_set:
                current = num
                while current in nums_set:
                    max_len = max(max_len, current-num+1)
                    current+=1
        return max_len