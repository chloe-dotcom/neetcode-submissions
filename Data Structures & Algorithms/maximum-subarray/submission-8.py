class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def dfs(l, r):
            if l > r:
                return float("-inf")
            m = (l+r) >> 1
            leftSum = rightSum = currSum = 0
            for i in range(m-1, l-1, -1):
                currSum += nums[i]
                leftSum = max(leftSum, currSum)
            currSum = 0
            for i in range(m+1, r+1):
                currSum += nums[i]
                rightSum = max(rightSum, currSum)
            return max(dfs(l,m-1), dfs(m+1,r),leftSum+nums[m]+rightSum)
        
        return dfs(0, len(nums)-1)