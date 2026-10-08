class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        graph = defaultdict(list)
        for word in words | {beginWord}:
            for i in range(len(word)):
                graph[word[:i] + "*" + word[i+1:]].append(word)
            
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            w, dist = queue.popleft()
            if w == endWord:
                return dist
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i+1:]
                for v in graph[pattern]:
                    if v not in visited:
                        visited.add(v)
                        queue.append((v, dist + 1))
        return 0