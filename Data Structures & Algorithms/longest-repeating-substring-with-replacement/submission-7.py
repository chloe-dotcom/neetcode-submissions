class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        maxInWindow = 1
        res = 1

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxInWindow = max(freq[s[r]], maxInWindow)

            while l < r and (r-l+1) - maxInWindow > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res
