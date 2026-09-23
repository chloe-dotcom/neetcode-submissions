class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build into graph
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # detect cycles
        rec_stack = [False] * numCourses
        visited = [False] * numCourses
        def dfs(u):
            rec_stack[u] = True
            visited[u] = True
            for v in adj[u]:
                if rec_stack[v]:
                    return True # cycle found
                if not visited[v]:
                    if dfs(v):
                        return True
            rec_stack[u] = False
            return False
        
        for i in range(numCourses):
            if dfs(i):
                return False
        return True
