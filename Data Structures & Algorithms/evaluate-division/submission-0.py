class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # construct graph
        graph = defaultdict(list)
        for (u, v), w in zip(equations, values):
            # undirected graph
            graph[u].append((v, float(w))) 
            graph[v].append((u, float(1/w)))
        
        def dfs(u, dest, visited):
            # how to traverse graph, find greatest path from s -> d
            if u in visited:
                return -1
            if u == dest:
                return 1
            visited.add(u)
            for v, w in graph[u]:
                if v not in visited:
                    sub = dfs(v, dest, visited)
                    if sub != -1:
                        return w * sub
            return -1

        res = []
        for s, d in queries:
            if s not in graph or d not in graph:
                res.append(-1)
            else:
                res.append(dfs(s, d, set()))
        
        return res