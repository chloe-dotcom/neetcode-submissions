class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = "0"
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nc < 0 or nr >= n or nc >= m or grid[nr][nc]=="0":
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)
        return res

            