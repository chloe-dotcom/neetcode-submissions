class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def helper(mid):
            i = 0
            count = 0
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= mid:
                    i+=2
                    count += 1
                else:
                    i+=1
                if count >= p:
                    return True
            return count >= p
        
        l = 0
        r = nums[-1] - nums[0]
        res = r
        while l <= r:
            mid = (l+r)//2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
