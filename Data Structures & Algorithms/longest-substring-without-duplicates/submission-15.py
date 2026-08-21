class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = 0
        seen = set()

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            maxLen = max(maxLen, j-i+1)
        return maxLen