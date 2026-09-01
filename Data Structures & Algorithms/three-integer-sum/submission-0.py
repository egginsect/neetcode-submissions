class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        out = []
        i=0
        for i, num in enumerate(nums):
            if num>0:
                break
            if i>0 and num==nums[i-1]:
                continue
            j, k= i+1, len(nums)-1
            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                if total == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif total<0:
                    j+=1
                else:
                    k-=1
            i+=1
        return out