class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = list(strs[0])
        for word in strs[1:]:
            for i in range(len(prefix)):
                if i < len(word) and word[i] == prefix[i]:
                    continue
                else:
                    while i < len(prefix):
                        prefix.pop()
                    break
        
        return "".join(prefix)
