class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        # using first i nums, can we make sum j?
        dp=[[False for _ in range(target+1)]
            for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                num = nums[i-1]
                if num > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        return dp[n][target]