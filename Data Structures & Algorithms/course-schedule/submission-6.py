class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course) # p -> c
        
        rec_stack = [False for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        def dfs(u):
            rec_stack[u] = True
            visited[u] = True
            for v in adj[u]:
                if rec_stack[v]:
                    return False # cycle detected
                if not visited[v]:
                    if not dfs(v):
                        return False
            rec_stack[u] = False
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i): 
                    return False
        return True
        
