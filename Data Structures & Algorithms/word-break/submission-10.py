class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True
        wordDict = set(wordDict)

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <=len(s) and s[i:i+len(w)] in w:
                    if not dp[i+len(w)]:
                        continue
                    dp[i] = True
        
        return dp[0]
                