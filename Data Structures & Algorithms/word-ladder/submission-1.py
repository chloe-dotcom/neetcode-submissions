class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i+1:]].append(word)
        
        visited = {beginWord}
        q = deque([(beginWord, 1)])

        while q:
            u, level = q.popleft()
            if u == endWord:
                return level
            for i in range(len(u)):
                oneAway = u[:i] + '*' + u[i+1:]
                for v in graph[oneAway]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, level + 1))
    
        return 0
        