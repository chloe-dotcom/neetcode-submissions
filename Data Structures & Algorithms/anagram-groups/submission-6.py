class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getAna(s):
            freq = {}
            for ch in s:
                freq[ch] = freq.get(ch, 0)+ 1
            return frozenset(freq.items())

        freqToList = {}

        for s in strs:
            currAna = getAna(s)
            if currAna in freqToList.keys():
                freqToList[currAna].append(s)
            else:
                freqToList[currAna] = [s]
        
        res = []
        for f,v in freqToList.items():
            res.append(v)
        return res