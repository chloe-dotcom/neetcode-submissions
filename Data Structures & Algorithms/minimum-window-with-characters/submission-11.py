class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1
        
        need = len(target)
        have = 0
        l = 0
        res = ""
        resLen = float('inf')
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if s[r] in target and freq[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                freq[s[l]] -= 1
                if s[l] in target and freq[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
                        
        return res
