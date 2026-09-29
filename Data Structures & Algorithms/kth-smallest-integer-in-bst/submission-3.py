# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        count = k
        def dfs(u):
            nonlocal count, res
            if not u:
                return
            dfs(u.left)
            if count == 0:
                return
            count -= 1
            if count == 0:
                res = u.val
                return
            dfs(u.right)
        dfs(root)
        return res