from functools import cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = currmin = 1
        res = nums[0]
        for num in nums:
            maxprod = currmax*num
            minprod = currmin*num
            currmax = max(maxprod, minprod, num)
            currmin = min(maxprod, minprod, num)
            res = max(res, currmax)
        return res
            
        