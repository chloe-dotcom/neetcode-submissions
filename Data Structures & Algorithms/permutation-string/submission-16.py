class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {} # freq of s1 letters
        for char in s1:
            target[char] = 1 + target.get(char, 0)
        
        n = len(s1)
        for i in range(0, len(s2)-n+1):
            curr = self.getFreq(s2[i:i+n])
            if curr == target:
                return True
        
        return False
    
    def getFreq(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        return freq