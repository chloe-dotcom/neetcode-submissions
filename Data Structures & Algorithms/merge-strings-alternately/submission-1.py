class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        i, j = 0, 0

        output = []
        while i < n and j < m:
            output.append(word1[i])
            output.append(word2[j])
            i += 1
            j += 1
        
        if i < n:
            output += word1[i:]
        if j < m:
            output += word2[j:]
        
        return "".join(output)