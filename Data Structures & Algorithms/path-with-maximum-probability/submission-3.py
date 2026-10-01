class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            adj[u].append((v, p))
            adj[v].append((u, p))

        maxProb = [0 for _ in range(n)]
        q = [(-1, start_node)]
        heapq.heapify(q)

        while q:
            currProb, currNode = heapq.heappop(q)
            currProb *= -1

            if currNode == end_node:
                return currProb

            if currProb < maxProb[currNode]:
                continue
            
            for v, p in adj[currNode]:
                newProb = p * currProb
                if newProb > maxProb[v]:
                    maxProb[v] = newProb
                    heapq.heappush(q, (-newProb, v))
        
        return 0