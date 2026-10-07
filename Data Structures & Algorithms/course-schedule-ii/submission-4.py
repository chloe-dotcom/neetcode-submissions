class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v) # course -> prereq
        
        visited = [False for _ in range(numCourses)]
        rec_stack = [False for _ in range(numCourses)]
        res = []

        def dfs(u):
            nonlocal res
            if rec_stack[u]:
                return True
            
            rec_stack[u] = True
            visited[u] = True

            for v in adj[u]:
                if rec_stack[v]:
                    return True
                if not visited[v]:
                    if dfs(v):
                        return True
            rec_stack[u] = False
            res.append(u)
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return []
        return res