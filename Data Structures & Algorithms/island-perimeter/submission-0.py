class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(r, c):            
            if (r, c) in visited:
                return 0

            if r < 0 or c < 0 or r >= n or c >=m or grid[r][c] == 0:
                return 1
            
            visited.add((r, c))
            perim = 0
            for dx, dy in direction:
                perim += dfs(r + dx, c + dy)
            return perim
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0