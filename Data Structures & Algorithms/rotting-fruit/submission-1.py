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
                    needed += 1
                    # visited.add((r,c))
                else:
                    continue

        # bfs, tracking number
        minute = 0
        have = 0
        directions = [(-1, 0),(1,0),(0,1),(0,-1)]
        while q:
            for i in range(len(q)):
                currR, currC = q.popleft()
                if have == needed:
                    return minute
                if (currR<0 or currC<0 or currR>=n or currC>=m or (currR, currC) in visited or grid[currR][currC]==0):
                    continue
                have += 1
                visited.add((currR, currC))
                if have == needed:
                    return minute
                for dx, dy in directions:
                    q.append((dx+currR, dy+currC))
            minute+=1

        # check if needed met
        return minute if have == needed else -1