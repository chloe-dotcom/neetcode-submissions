class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        q = deque()
        total = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))
                    total += 1
                elif grid[i][j] == 1:
                    total += 1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        has = len(q)
        while q:
            for i in range(len(q)):
                x, y = q.popleft()

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx>=0 and nx<r and ny>=0 and ny<c and grid[nx][ny]==1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
                        has += 1
            if q:
                count += 1
            
        return -1 if has != total else count