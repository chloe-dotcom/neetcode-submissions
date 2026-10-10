class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >=n or j>= m or grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            visited.add((i, j))
            currArea = 1
            for dr, dc in directions:
                currArea += dfs(i + dr, j + dc)

            return currArea
        
        maxArea = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea