class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_vol = 0
        while left<right:
            height = min(heights[right], heights[left])
            max_vol = max((right-left)*height, max_vol)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return max_vol
