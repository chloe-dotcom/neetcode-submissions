class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def backtrack(i, path):
            if i == len(nums):
                output.append(path[:])
                return

            # decision 2: don't take i
            backtrack(i+1, path)
            
            # decision 1: we can take i
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
        
        backtrack(0, [])
        return output