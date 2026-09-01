class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right=0, len(nums)-1
        min_elem = sys.maxsize
        while left<right:
            mid = (left+right)//2
            min_elem = min(nums[mid], min_elem)
            if nums[mid]>nums[right]:
                left = mid +1
            else:
                right = mid -1
        return min(min_elem, nums[right])

        # 0 1 2 3 4 5
        # 3 4 5 6 1 2
        # l   m     r
        #       l m r
        #       
        #       l r