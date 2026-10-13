class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        maxLen = max(len(word) for word in wordDict)

        for i in range(len(s)):
            if not dp[i]:
                continue
            for w in wordDict:
                if i + len(w) <= len(s) and (s[i:i+len(w)] == w):
                    dp[i+len(w)] = True
    
        return dp[len(s)]