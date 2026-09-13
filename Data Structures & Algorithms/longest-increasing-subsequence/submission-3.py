class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        n = len(nums)

        for i in range(1, len(nums)):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                l, r = 0, len(sub)-1
                while l < r:
                    m = (l+r)//2
                    if nums[i] > sub[m]:
                        l = m + 1
                    else:
                        r = m
                sub[l] = nums[i]
        return len(sub)