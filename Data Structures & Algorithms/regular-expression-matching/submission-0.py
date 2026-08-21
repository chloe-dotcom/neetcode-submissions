class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j  == len(p):
                result = i == len(s)
            
            else:
                firstMatch = i < len(s) and (s[i]==p[j] or p[j]=='.')
            
                if j + 1 < len(p) and p[j+1] =='*':
                    result = dfs(i, j+2) or (firstMatch and dfs(i+1,j))
            
                else:
                    result = firstMatch and dfs(i+1, j+1)
            memo[(i, j)] = result
            return result
        
        return dfs(0, 0)