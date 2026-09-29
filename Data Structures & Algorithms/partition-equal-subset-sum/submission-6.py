class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        memo = {}
        def dfs(i, j):
            if j == 0:
                return True
            if j < 0 or i >= n:
                return False
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i,j)] = (dfs(i+1, j - nums[i]) or dfs(i+1, j))
            return memo[(i, j)]
        return dfs(0, target)