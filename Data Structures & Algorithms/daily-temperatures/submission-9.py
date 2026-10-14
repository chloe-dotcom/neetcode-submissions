class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        output = [0 for _ in range(n)]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp, prevIndx = stack.pop()
                output[prevIndx] = i - prevIndx
            stack.append((t, i))

        return output