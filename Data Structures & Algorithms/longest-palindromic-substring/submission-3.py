class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resLen = 0
        resIdx = 0
        for i in range(n):
            l = r = i
            while l>=0 and r<n and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resIdx = l
                l -= 1
                r += 1

            l = i
            r = i + 1
            while l>=0 and r<n and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resIdx = l
                l -= 1
                r += 1
            
        return s[resIdx:resIdx+resLen]