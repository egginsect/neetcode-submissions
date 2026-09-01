from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]*len(nums)
        right_prod = [1]*len(nums)
        
        for idx in range(1, len(nums)):
            r_id = len(nums)-idx-1
            left_prod[idx] = left_prod[idx-1]*nums[idx-1]
            right_prod[r_id] = right_prod[r_id+1]*nums[r_id+1]
        return [l*r for l, r in zip(left_prod, right_prod)]
