class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        maxheap = []
        heapq.heapify(maxheap)
        for num, cnt in freq.items():
            heapq.heappush(maxheap, (cnt, num))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [val for key,val in maxheap]