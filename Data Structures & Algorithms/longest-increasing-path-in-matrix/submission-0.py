class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        dp = {}

        def dfs(i, j, v):
            if (min(i, j) < 0 or i >= m or j >= n or matrix[i][j] <= v):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1
            for d in directions:
                res = max(res, 1 + dfs(i+d[0], j+d[1], matrix[i][j]))
            dp[(i, j)] = res
            return res
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, float('-inf')))
        return max(dp.values())
            
            

        