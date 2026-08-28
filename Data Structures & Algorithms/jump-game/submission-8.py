class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]

        dp[-1] = True
    
        for i in range(n-2, -1, -1):
            jumprange = min(nums[i] + i + 1, n)
            for j in range(i+1, jumprange):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]