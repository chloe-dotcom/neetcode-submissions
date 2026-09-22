class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c,visit,prevHeight):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or
                heights[r][c] < prevHeight or (r, c) in visit):
                return
            currHeight = heights[r][c]
            visit.add((r, c))
            dfs(r+1, c, visit, currHeight)
            dfs(r-1, c, visit, currHeight)
            dfs(r, c+1, visit, currHeight)
            dfs(r, c-1, visit, currHeight)
                
        # pacific: for bordered elements, run dfs, mark reachable
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        # do the same for atlantic
        res = [island for island in pacific if island in atlantic]
        # find overlap and return
        return res