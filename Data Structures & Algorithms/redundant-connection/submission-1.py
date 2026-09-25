class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs function
        # find cycle, add all cycle edges to set
        # reverse edges, return first cycle edge in edges

        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        n = len(edges)
        visited = [False for _ in range(n+1)]
        cycleStart = -1
        cycleEdges = set()

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
                        cycleEdges.add((min(u, v), max(u, v)))
                    if cycleStart == u:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)
        print(cycleEdges)
        for u, v in reversed(edges):
            if ((min(u,v), max(u, v)) in cycleEdges):
                return [u, v]
        return []