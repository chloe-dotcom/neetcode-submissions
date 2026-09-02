class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append((t, i))
        return res