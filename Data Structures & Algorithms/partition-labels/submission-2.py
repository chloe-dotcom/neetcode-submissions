class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterToLastIndex = {}
        for i, char in enumerate(s):
            letterToLastIndex[char] = i
        
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end = max(end, letterToLastIndex[s[i]])

            if i == end:
                res.append(end-start+1)
                start = end + 1
        
        return res
