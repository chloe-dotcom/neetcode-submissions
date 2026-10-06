class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        L = [0 for _ in range(n)]
        R = [0 for _ in range(n)]
        L[0] = nums[0]
        R[n-1] = nums[n-1]
        for i in range(1, n):
            if i % k == 0:
                L[i] = nums[i]
            else:
                L[i] = max(L[i-1], nums[i])
        for i in range(n-2, -1, -1):
            if i % k == 0:
                R[i] = nums[i]
            else:
                R[i] = max(R[i+1], nums[i])
                
        res = []
        for i in range(n-k+1):
            res.append(max(L[i+k-1], R[i]))
        return res