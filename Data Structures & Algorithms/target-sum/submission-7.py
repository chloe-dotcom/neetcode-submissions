class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def backtrack(i, currSum):
            if i == n:
                if currSum == target:
                    return 1
                else:
                    return 0
            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            memo[(i, currSum)] = backtrack(i+1, currSum-nums[i]) + backtrack(i+1, currSum+nums[i])
            return memo[(i, currSum)]

        return backtrack(0, 0)