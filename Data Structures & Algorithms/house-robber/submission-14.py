class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]

        dp = [-1 for _ in range(n)] # max robber has at house i

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[n-1]