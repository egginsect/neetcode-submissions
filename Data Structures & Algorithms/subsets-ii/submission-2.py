class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        n = len(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                start = prevlen
            else:
                start = 0
        
            prevlen = len(res)
            for j in range(start, len(res)):
                res.append(res[j]+[nums[i]])
            
        return res
            