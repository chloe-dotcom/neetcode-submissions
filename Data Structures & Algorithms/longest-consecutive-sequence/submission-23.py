class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()

        curr = 1
        maxLen = 1


        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                curr += 1
                maxLen = max(curr, maxLen)
            else:
                curr = 1
        
        return maxLen
