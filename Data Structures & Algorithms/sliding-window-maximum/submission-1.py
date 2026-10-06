class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []
        for i in range(len(nums)):
            heapq.heappush(h, (-nums[i], i))
            if i >= k-1:
                while h[0][1] <= i-k:
                    heapq.heappop(h)
                res.append(-1 * h[0][0])
        return res