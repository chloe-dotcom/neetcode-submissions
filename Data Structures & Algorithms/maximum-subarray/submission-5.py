class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = float('-inf')
        for num in nums:
            if num + currSum > num:
                currSum = num+currSum
            else:
                currSum = num
            maxSum = max(maxSum, currSum)
        return maxSum