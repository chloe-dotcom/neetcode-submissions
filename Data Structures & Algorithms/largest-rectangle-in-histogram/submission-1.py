class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for i, val in enumerate(heights):
            start = i
            while stack and val < stack[-1][1]:
                popIndex, popHeight = stack.pop()
                area = max(area, popHeight*(i-popIndex))
                start = popIndex
            
            stack.append((start, val))
        
        for i, height in stack:
            area = max(area, height * (len(heights)-i))
        return area