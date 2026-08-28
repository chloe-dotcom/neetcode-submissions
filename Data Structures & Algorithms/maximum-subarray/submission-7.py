class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        n = len(nums)
        dp[n-1][1] = dp[n-1][0] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i][1] = max(nums[i], nums[i] + dp[i+1][1])
            dp[i][0] = max(dp[i+1][0], dp[i][1])
        return dp[0][0]