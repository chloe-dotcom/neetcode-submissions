class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True
        wordDict = set(wordDict)

        for i in range(len(s)-1, -1, -1):
            print(i)
            for w in wordDict:
                if i + len(w) <=len(s) and s[i:i+len(w)] in w:
                    print("enter loop")
                    if not dp[i+len(w)]:
                        print(w, "break")
                        continue
                    dp[i] = True
        
        return dp[0]
                