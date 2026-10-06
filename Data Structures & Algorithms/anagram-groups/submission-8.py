class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord in seen:
                seen[sortedWord].append(word)
            else:
                seen[sortedWord] = [word]
        
        # result = []
        # for _, listWord in seen.items():
        #     result.append(listWord)
        
        return list(seen.values())