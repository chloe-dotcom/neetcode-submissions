class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False for _ in range(n)]
        def bfs(u, p):
            q = deque([(u, p)])
            while q:
                curr, p = q.popleft()
                visited[curr] = True
                for v in adj[curr]:
                    if v == p:
                        continue
                    if not visited[v]:
                        q.append((v, u))
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i, -1)
        return count