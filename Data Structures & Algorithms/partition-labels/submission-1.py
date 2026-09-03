class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterToLast = {}
        for i, v in enumerate(s):
            if letterToLast.get(v, -1) < i:
                letterToLast[v] = i
        
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, letterToLast[s[i]])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res