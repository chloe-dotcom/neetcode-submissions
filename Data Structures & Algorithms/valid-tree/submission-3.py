class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False for _ in range(n)]
        rec_stack = [False for _ in range(n)]
        def dfs(u, p):
            visited[u] = True
            rec_stack[u] = True

            for v in adj[u]:
                if v == p:
                    continue
                if rec_stack[v]:
                    return False
                if not visited[v]:
                    if not dfs(v, u):
                        return False
            rec_stack[u] = False
            return True
        
        return dfs(0, -1) and all(visited)
            