class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s)+1)]
        dp[len(s)] = [""]

        wordDict = set(wordDict)
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)]==w:
                    for suffix in dp[i+len(w)]:
                        dp[i].append(w + (" " + suffix if suffix else ""))

        return dp[0]