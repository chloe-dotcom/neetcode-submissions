class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            adj[u].append((v, p))
            adj[v].append((u, p))
        
        max_prob = [0 for _ in range(n)]
        max_prob[start_node] = 1
        q = [(-1, start_node)]

        while q:
            currProb, currNode = heapq.heappop(q)
            currProb *= -1

            if currNode == end_node:
                return currProb
            
            if currProb < max_prob[currNode]:
                continue
            
            for v, p in adj[currNode]:
                nextProb = p * currProb
                if nextProb > max_prob[v]:
                    max_prob[v] = nextProb
                    heapq.heappush(q, (-nextProb, v))
    
        return 0.0