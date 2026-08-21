class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        target = {} # freq of s1 letters
        for char in s1:
            target[char] = 1 + target.get(char, 0)
        
        n = len(s1)
        curr = {}
        for i in range(0, len(s2)-n+1):
            if i == 0: # on the first comparison
                curr = self.getFreq(s2[i:i+n])
            else:
                curr[s2[i+n-1]] = curr.get(s2[i+n-1], 0) + 1
                curr[s2[i-1]] -= 1
                if curr[s2[i-1]] == 0:
                    curr.pop(s2[i-1])
            print(curr)
            if curr == target:
                return True
        
        return False
    
    def getFreq(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq