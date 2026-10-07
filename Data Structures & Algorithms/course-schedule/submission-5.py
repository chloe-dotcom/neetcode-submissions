class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq: [a, b]. a -> b

        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v) # directed edge

        # search for cycles
        visited = [False for _ in range(numCourses)]
        rec_stack = [False for _ in range(numCourses)]
        def dfs(u):
            if rec_stack[u]:
                return True # cycle detected
            visited[u] = True
            rec_stack[u] = True
            for v in adj[u]:
                if rec_stack[v]:
                    return True
                if not visited[v]:
                    if dfs(v):
                        return True
            rec_stack[u] = False
            return False
        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False # cycle found, not possible to take
        return True

