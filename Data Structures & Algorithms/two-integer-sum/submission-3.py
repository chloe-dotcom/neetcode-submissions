class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numberToIndex = {}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in numberToIndex:
                return [numberToIndex[rem], i]
            else:
                numberToIndex[num] = i
        
        return
