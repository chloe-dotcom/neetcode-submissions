class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2 :
            return len(s)
        maxRes = 0
        l, r = 0, 1
        seen = {s[0]}
        
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            maxRes = max(maxRes, r-l)
        
        return maxRes