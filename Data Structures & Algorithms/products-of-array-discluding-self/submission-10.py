class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        n = len(nums)
        prefix = [1] * n # from left: multiplied values to i
        suffix = [1] * n # from right: multiplied value to i

        # ex: p = [(1), 1, 2, 8]
        #     s = [48, 24, 6,(1)]

        for i, num in enumerate(nums):
            if num == 0:
                zeroCount += 1
            if zeroCount > 1:
                return [0] * n

            if i > 0:
                prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        res = [prefix[i] * suffix[i] for i in range(n)]
        return res
            
