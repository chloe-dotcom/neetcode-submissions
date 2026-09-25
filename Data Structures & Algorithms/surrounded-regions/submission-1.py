class Solution:
    def solve(self, board: List[List[str]]) -> None:
        borderSet = set()
        n, m = len(board), len(board[0])

        visited = [[False for _ in range(m)] for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(n):
            for c in range(m):
                if ((r == 0 or c == 0 or r == n-1 or c == m-1) and board[r][c] == "O"):
                    q.append((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if (r>=0 and r<n and c>=0 and c<m and not visited[r][c] and board[r][c] == "O"):
                    borderSet.add((r, c))
                    visited[r][c] = True
                    for dx, dy in directions:
                        q.append((r+dx, c+dy))
        
        for r in range(n):
            for c in range(m):
                if (r, c) in borderSet or board[r][c] == "X":
                    continue
                board[r][c] = "X"
