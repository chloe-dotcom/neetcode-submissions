class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False for _ in range(n)]
        q = deque([(0, -1)])
        while q:
            curr, p = q.popleft()
            visited[curr] = True
            for n in adj[curr]:
                if n == p:
                    continue
                if visited[n]:
                    return False
                q.append((n, curr))
        
        return True if all(visited) else False