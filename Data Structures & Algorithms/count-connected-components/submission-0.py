class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        (adj)
        visited = [False for _ in range(n)]
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count