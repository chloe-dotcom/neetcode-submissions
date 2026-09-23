class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, p in prerequisites:
            adj[course].append(p)
        
        visited = [False for _ in range(numCourses)]
        rec_stack = [False for _ in range(numCourses)]
        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            for v in adj[u]:
                if rec_stack[v]:
                    return True
                if not visited[v]:
                    if dfs(v):
                        return True # found cycle
            rec_stack[u] = False
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True