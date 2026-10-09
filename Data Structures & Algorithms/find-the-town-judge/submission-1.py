class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = {i+1 : 0 for i in range(n)}   
        adj = [[] for _ in range(n+1)]


        for p, t in trust:
            indegree[p] += 1 # how many people they trust
            adj[t].append(p)
        
        for i in range(n):
            if indegree[i+1] == 0 and len(adj[i+1]) == (n-1):
                return i+1
        
        return -1
