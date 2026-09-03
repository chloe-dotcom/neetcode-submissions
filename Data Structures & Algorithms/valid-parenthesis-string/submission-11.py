class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False] * (n+1) for _ in range(n+1)]
        dp[n][0] = True

        for i in range(n-1, -1, -1):
            for openNum in range(n):
                result = False
                if s[i] == '*':
                    result |= dp[i+1][openNum+1]
                    if openNum > 0:
                        result |= dp[i+1][openNum-1]
                    result |= dp[i+1][openNum]
                elif s[i] == '(':
                    result |= dp[i+1][openNum+1]
                else:
                    if openNum > 0:
                        result |= dp[i+1][openNum-1]
                dp[i][openNum] = result
        
        return dp[0][0]
