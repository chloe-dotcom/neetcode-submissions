class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        for p, c in prerequisites:
            adj[p].append(c) # directed edge from p -> c
            indegrees[c] += 1

        prereqs = [set() for _ in range(numCourses)]
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            u = q.popleft()
            
            for v in adj[u]:
                prereqs[v].update(prereqs[u])
                prereqs[v].add(u)

                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
            
        return [a in prereqs[b] for a, b in queries]