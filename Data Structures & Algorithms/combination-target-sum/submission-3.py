class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(i, s, path):
            if s > target or i>=len(nums):
                return
            
            if s == target:
                if path not in output:
                    output.append(path[:])
            

            path.append(nums[i])
            backtrack(i, s+nums[i], path)

            path.pop()
            backtrack(i+1, s, path)
        
        backtrack(0, 0, [])
        return output