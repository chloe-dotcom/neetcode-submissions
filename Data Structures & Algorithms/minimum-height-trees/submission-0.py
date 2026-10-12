class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # no cycles -- valid tree
        def bfs(u, p, h):
            q = deque([(u, p, h)])
            maxH = 0
            while q:
                u, p, h = q.popleft()
                maxH = max(maxH, h)
                for v in adj[u]:
                    if v == p:
                        continue
                    q.append((v, u, h+1))
            return maxH
        
        maxH = float('inf')
        res = []
        for i in range(n):
            cur = bfs(i, -1, 0)
            print(i, cur)
            if cur == maxH:
                res.append(i)
            elif cur < maxH:
                res = [i]
                maxH = min(maxH, cur)
            else:
                continue
        return res
