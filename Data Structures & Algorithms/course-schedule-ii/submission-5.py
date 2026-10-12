class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq) # c->p
        
        schedule = []
        visited = [False for _ in range(numCourses)]
        rec_stack = [False for _ in range(numCourses)]
        def dfs(u):
            rec_stack[u] = True
            visited[u] = True
            for v in adj[u]:
                if rec_stack[v]:
                    return False # cycle detected
                if not visited[v]:
                    if not dfs(v):
                        return False
            schedule.append(u)
            rec_stack[u] = False
            return True
        
        for i in range(numCourses):
            if not visited[i]:
                if not dfs(i):
                    return []
        return schedule