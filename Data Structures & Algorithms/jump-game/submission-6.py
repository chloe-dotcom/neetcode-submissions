class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]

        dp[n-1] = True
    
        for i in range(n-2, -1, -1):
            jumprange = min(nums[i] + i, n-1)
            while jumprange > i:
                dp[i] = dp[i] or dp[jumprange]
                jumprange -= 1
        
        return dp[0]