class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if i >= len(nums):
                add = sorted(curr)
                if add not in res:
                    res.append(add[:])
                return
            
            curr.append(nums[i])
            dfs(i+1, curr)

            curr.pop()
            dfs(i+1, curr)
        
        dfs(0, [])
        return res