class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        heapq.heapify(nums)
        res = 1
        curr = 1
        
        prev = heapq.heappop(nums)
        for i in range(len(nums)):
            item = heapq.heappop(nums)
            if item == prev + 1:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
            prev = item
        
        return res
        