class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target = self.getFreq(t)

        l = 0
        res = float('inf')
        have = 0
        need = len(target)
        currBest = ""
        freq = {}
        for i, char in enumerate(s):
            freq[char] = freq.get(char, 0) + 1
            if char in target and freq[char] == target[char]:
                have += 1
            while have == need:
                if (i-l+1) < res:
                    res = i-l+1
                    currBest = s[l:i+1]
                
                freq[s[l]] -= 1
                if s[l] in target and freq[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
            
        return currBest
            
    
    def getFreq(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq
    
    def equal(self, curr, target):
        for char in target:
            if char not in curr:
                return False
            if curr[char] < target[char]:
                return False
        return True
            