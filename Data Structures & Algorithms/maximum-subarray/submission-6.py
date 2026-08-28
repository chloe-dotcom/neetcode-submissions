class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currAmount = nums[0]
        maxAmount = nums[0]

        for num in nums[1:]:
            currAmount = max(num, num + currAmount)
            maxAmount = max(maxAmount, currAmount)
        
        return maxAmount
