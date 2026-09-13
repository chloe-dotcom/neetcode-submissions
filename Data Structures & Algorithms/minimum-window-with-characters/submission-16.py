class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        target = {}
        for ch in t:
            target[ch] = target.get(ch, 0) + 1
        
        res = [-1, -1]
        freq = {}
        l = 0
        resLen = float('inf')
        has = 0
        need = len(target)
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            if ch in target and freq[ch] == target[ch]:
                has += 1
            while has == need:
                if (r - l + 1) < resLen:
                    resLen = r-l+1
                    res = [l, r]
                freq[s[l]] -= 1
                if s[l] in target and freq[s[l]] < target[s[l]]:
                    has -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
            
