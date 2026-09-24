class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        (adj)
        cycle = set()
        visited = [False for _ in range(n+1)]
        cycleStart = -1

        def dfs(u, p):
            nonlocal cycleStart
            if visited[u]:
                cycleStart = u
                return True
            
            visited[u] = True
            for v in adj[u]:
                if v == p:
                    continue
                if dfs(v, u):
                    if cycleStart != -1:
                        cycle.add(u)
                    if u == cycleStart:
                        cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []