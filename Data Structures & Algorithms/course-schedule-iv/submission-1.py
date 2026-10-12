class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for p, c in prerequisites:
            adj[p].append(c) # p -> c
            indegrees[c] += 1
        
        pre = [set() for _ in range(numCourses)]
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            u = q.popleft()
            for v in adj[u]:
                pre[v].add(u)
                pre[v].update(pre[u])
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
        
        res = [p in pre[c] for p, c in queries]
        return res