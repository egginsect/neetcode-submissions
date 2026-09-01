class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while len(stack)>0 and stack[-1][1] > height:
                start, h_pop = stack.pop(-1)
                max_area = max((i-start)*h_pop ,max_area)
            stack.append((start, height))
        n = len(heights)
        for start, height in stack:
            max_area = max((n-start)*height, max_area)
        return max_area

        