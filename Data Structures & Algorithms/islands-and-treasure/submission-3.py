class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1,0), (0, 1), (0, -1)]
        INF = 2147483647
        visit = set()
        q = deque()

        def bfs(i, j):
            if (i<0 or j <0 or i>=ROWS or j>=COLS or 
                grid[i][j] == -1 or (i,j) in visit):
                return
            visit.add((i,j))
            q.append((i, j))
    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
            
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                for dx, dy in directions:
                    nr, nc = r + dx, c + dy
                    bfs(nr, nc)
            distance += 1