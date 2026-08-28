class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]

            l = i + 1
            r = len(nums)-1
            while l < r:
                curr = nums[l]+nums[r]
                if curr == target and [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    r -= 1
        
        return res