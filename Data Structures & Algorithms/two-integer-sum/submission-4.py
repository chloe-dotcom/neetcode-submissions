class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenRem = {} # remainders to index

        for i, val in enumerate(nums):
            rem = target - val
            if rem in seenRem:
                return [seenRem[rem], i]
            seenRem[val] = i
        
        return [None]