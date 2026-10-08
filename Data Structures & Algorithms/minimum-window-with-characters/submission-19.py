class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        need = len(target)
        has = 0

        l = 0
        freq = {}
        minLen = len(s)
        res = (-1, -1)
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if s[r] in target and freq[s[r]] == target[s[r]]:
                has += 1
            
            while has == need and l <= r:
                if r-l+1 <= minLen:
                    minLen = r-l+1
                    res = (l, r)
                freq[s[l]] -= 1
                if s[l] in target and freq[s[l]] < target[s[l]]:
                    has -= 1
                l += 1
        
        x, y = res
        if x == -1 and y == -1:
            return ""
        return s[x:y+1]
            
