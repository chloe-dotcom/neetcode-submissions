class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        for c, p in prerequisites:
            adj[c].append(p)
        
        visited = [False] * numCourses
        rec_stack = [False] * numCourses

        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            
            for v in adj[u]:
                if rec_stack[v]:
                    return True # cycle detected
                if not visited[v]:
                    if dfs(v):
                        return True
            rec_stack[u] = False
            res.append(u)
            return False
        
        res = []
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        return res
        
        