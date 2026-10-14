# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if node is None:
                res.append('#')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodeList = data.split(',')
        self.i = 0

        def dfs():
            if self.i >= len(data) or nodeList[self.i] == '#':
                self.i += 1
                return None
            root = TreeNode(int(nodeList[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
    
        return dfs()
        