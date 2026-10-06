class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1 for _ in range(n)] # prod from the left up to i
        R = [1 for _ in range(n)]

        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
        
        if zeroCount > 1:
            return [0 for _ in range(n)]


        # [1, 1, 2, 8]
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        
        # [48, 24, 6, 1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        
        res = []
        for i in range(n):
            res.append(L[i] * R[i])
        return res