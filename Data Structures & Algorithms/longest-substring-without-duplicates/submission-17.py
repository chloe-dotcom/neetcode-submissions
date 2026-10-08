class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l = 0
        r = 1
        maxLen = 1

        seen = set()
        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, len(seen))

        return maxLen


