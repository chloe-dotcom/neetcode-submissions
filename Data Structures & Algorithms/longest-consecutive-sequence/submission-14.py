class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 1
        curr = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
        return res