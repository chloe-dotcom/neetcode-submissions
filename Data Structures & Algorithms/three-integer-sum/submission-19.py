class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            target = -1 * num
            l = i+1
            r = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr < target:
                    l += 1
                else:
                    r -= 1
            
        return res