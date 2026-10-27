class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sFreq = {}
        for ch in s:
            sFreq[ch] = sFreq.get(ch, 0) + 1
    
        tFreq = {}
        for ch in t:
            tFreq[ch] = tFreq.get(ch, 0) + 1
        
        return sFreq == tFreq
    