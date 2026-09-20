class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def bfs(i, j):
            if (i<0 or j<0 or i>=n or j>=m or 
                (i,j) in visited or grid[i][j] == -1):
                return
            visited.add((i,j))
            q.append((i,j))
                
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    bfs(r, c)

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                for dx, dy in directions:
                    bfs(r + dx, c + dy)
            distance += 1