class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n, m = len(grid), len(grid[0])
        q = deque()
        # add all treasure spots to queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))

        # run bfs, modify graph in place
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        INF = 2147483647
        while q:
            i, j = q.popleft()
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == INF:
                    grid[nx][ny] = grid[i][j] + 1
                    q.append((nx, ny))
                    
