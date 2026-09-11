class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        res = 1
        for num in nums:
            if num - 1 not in nums:
                start = num
                curr = 1
                while start + 1 in nums:
                    curr += 1
                    start = start + 1
                res = max(res, curr)
    
        return res
