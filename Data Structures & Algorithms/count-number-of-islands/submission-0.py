class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if (i<0 or j<0 or i>=n or j>=m or grid[i][j] == "0"):
                return
            
            grid[i][j] = "0"
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
    
        return count
