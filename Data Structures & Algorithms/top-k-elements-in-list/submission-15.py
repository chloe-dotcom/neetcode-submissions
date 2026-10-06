class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        h = list((value, key) for key, value in freq.items())
        heapq.heapify(h)

        while len(h) > k:
            heapq.heappop(h)
        
        return [key for (val, key) in h]