class Solution:
    def jump(self, nums: List[int]) -> int:
        currIndex = 0
        currJumpRange = nums[0]
        count = 0

        while currIndex < len(nums)-1:
            print(currIndex, currJumpRange, count)
            temp = 0
            if currIndex + currJumpRange >= len(nums)-1:
                return count + 1
            count += 1
            for i in range(currIndex+1, currIndex+currJumpRange+1):
                if i + nums[i] >= temp:
                    temp = nums[i] + i
                    currIndex = i
            currJumpRange = nums[currIndex]
        
        return count
