class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        left = [-1 for _ in range(n)]
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            # stack[-1] if exists is less than or equal to currHeight
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        right = [n for _ in range(n)]
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            res = max(res, heights[i] * (right[i]-left[i]-1))
        return res

        