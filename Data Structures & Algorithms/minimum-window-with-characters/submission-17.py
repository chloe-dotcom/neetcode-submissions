class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        target = {} # frequency of each letter in t
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
    
        need = len(target)
        have = 0
        l = 0
        freq = {}
        resLen = len(s)+1
        res = (-1, -1)
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if s[r] in target and freq[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = (l, r)
                freq[s[l]] -= 1
                if s[l] in target and freq[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        if l == -1 and r == -1:
            return ""
        else:
            return s[l:r+1]
            