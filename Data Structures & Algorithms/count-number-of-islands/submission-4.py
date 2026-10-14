class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return 0
            
            grid[i][j] = "0"
            count = 0
            for dx, dy in directions:
                dfs(i+dx, j+dy)
            return 1
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += dfs(i, j)
        return count