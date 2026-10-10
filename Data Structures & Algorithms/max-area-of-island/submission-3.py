class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]

        def dfs(i, j):
            if i < 0 or j <0 or i >=n or j>=m or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            currArea = 1
            for dx, dy in directions:
                currArea += dfs(i+dx, j+dy)
            
            return currArea
        
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea

