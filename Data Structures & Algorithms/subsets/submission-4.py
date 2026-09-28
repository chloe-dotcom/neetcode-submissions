class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i >= len(nums):
                res.append(curr[:])
                return
            
            # decision 1: take num
            curr.append(nums[i])
            dfs(i+1, curr)

            # decision 2: don't take num
            curr.pop()
            dfs(i+1, curr)
        
        dfs(0, [])
        return res