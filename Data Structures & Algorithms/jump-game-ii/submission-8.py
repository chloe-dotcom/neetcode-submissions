class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [10000] * len(nums)
        dp[len(nums)-1] = 0

        for i in range(len(nums)-2, -1, -1):
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i+1, end):
                dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[0]