class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False for _ in range(n)]

        def dfs(u, p):
            visited[u] = True
            for v in adj[u]:
                if v == p:
                    continue
                if not visited[v]:
                    dfs(v, u)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i, -1)
    
        return count
