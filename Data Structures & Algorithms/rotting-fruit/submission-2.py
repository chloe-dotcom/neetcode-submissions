class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        # add initially rotten to q - count needed
        needed = 0
        q = deque()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    needed += 1
                elif grid[r][c]==2:
                    q.append((r,c))
                    # visited.add((r,c))
                else:
                    continue

        if needed == 0:
            return 0

        # bfs, tracking number
        minute = 0
        have = 0
        directions = [(-1, 0),(1,0),(0,1),(0,-1)]
        while q:
            if have == needed:
                return minute
            for i in range(len(q)):
                currR, currC = q.popleft()
                for dx, dy in directions:
                    nr, nc = currR + dx, currC + dy
                    if (nr>=0 and nc>=0 and nr<n and nc<m and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        have += 1
                        q.append((nr,nc))
            minute+=1

        return minute if have == needed else -1