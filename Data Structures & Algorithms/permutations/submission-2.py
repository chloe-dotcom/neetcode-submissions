class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0 for _ in range(len(nums))]
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if used[i] == 0:
                    curr.append(nums[i])
                    used[i] = 1
                    dfs(curr)
                    curr.pop()
                    used[i] = 0
        
        dfs([])
        return res