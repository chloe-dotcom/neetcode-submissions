class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToWords = {}

        def getAna(s):
            freq = {}
            for ch in s:
                freq[ch] = freq.get(ch, 0) + 1
            return frozenset(freq.items())
        
        for s in strs:
            f = getAna(s)
            if f in freqToWords:
                freqToWords[f].append(s)
            else:
                freqToWords[f] = [s]
        
        return [w for s, w in freqToWords.items()]