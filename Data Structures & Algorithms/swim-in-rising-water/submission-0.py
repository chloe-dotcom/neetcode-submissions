class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def valid(mid):
            visited = [[False for _ in range(n)] for _ in range(n)]
            def dfs(i, j, m):
                if i>=n or j>=n or i<0 or j<0 or grid[i][j] > m or visited[i][j]:
                    return
                if i == n-1 and j == n-1:
                    return True
                visited[i][j] = True    
                for dx, dy in directions:
                    if dfs(dx + i, dy + j, m):
                        return True
                return False
            return dfs(0,0,mid)

        r = max(max(row) for row in grid)
        l = min(min(row) for row in grid)
        ans = -1
        while l <= r:
            mid = (l+r)//2
            print(mid)
            if valid(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans