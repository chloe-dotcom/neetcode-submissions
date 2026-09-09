class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        listFreq = [[] for i in range(len(nums)+1)]
        for val, cnt in freq.items():
            listFreq[cnt].append(val)
        
        res = []
        for i in range(len(listFreq)-1, 0, -1):
            for num in listFreq[i]:
                res.append(num)
                if len(res) == k:
                    return res
