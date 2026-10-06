class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        remToIndx = {0:-1}
        currSum = 0
        for i, val in enumerate(nums):
            currSum += val
            remainder = currSum % k
            if remainder in remToIndx:
                if i - remToIndx[remainder] > 1:
                    print(remToIndx)
                    print(i, remToIndx[remainder])
                    return True
            else:
                remToIndx[remainder] = i
        
        return False