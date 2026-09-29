class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        memo = {}
        def dfs(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i
            if (i, j) in memo:
                return memo[(i, j)]
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]
            
            # insert char, replace char
            res = min(1 + dfs(i, j+1), 1+dfs(i+1, j+1))
            # delete char
            res = min(res, 1+dfs(i+1, j))
            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)