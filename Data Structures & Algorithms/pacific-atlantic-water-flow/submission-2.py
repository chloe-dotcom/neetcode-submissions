class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        R, C = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean.add((r, c))
                for dx, dy in directions:
                    nr, nc = dx+r, dy+c
                    if (nr>=0 and nc>=0 and nr<R and nc<C and heights[nr][nc] >= heights[r][c] and (nr, nc) not in ocean):
                        q.append((nr, nc))

        pacificSources = []
        atlanticSources = []
        for r in range(R):
            pacificSources.append((r, 0))
            atlanticSources.append((r, C-1))
        for c in range(C):
            pacificSources.append((0, c))
            atlanticSources.append((R-1, c))

        bfs(pacificSources, pacific)
        bfs(atlanticSources, atlantic)

        res = [island for island in pacific if island in atlantic]
        return res
