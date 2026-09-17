class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freq = sorted(freq.items(), key = lambda i: i[1], reverse=True)
        return [k for k, v in freq[:k]]