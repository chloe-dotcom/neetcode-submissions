class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]

            k = i + j

            chooseS1 = False
            chooseS2 = False
            
            if i < len(s1) and s1[i] == s3[k]:
                chooseS1 = dfs(i+1, j)
            if j < len(s2) and s2[j] == s3[k]:
                chooseS2 = dfs(i, j+1)
            
            dp[(i, j)] = chooseS1 or chooseS2
            return dp[(i, j)]

        return dfs(0, 0)