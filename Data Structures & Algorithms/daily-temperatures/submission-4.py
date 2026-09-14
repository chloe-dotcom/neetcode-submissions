class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        stack = deque()
        res = [0] * n

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:             
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))
        return res