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
        q = deque([root])
        while q:
            currNode = q.popleft()
            if not currNode:
                res.append("#")
            else:
                res.append(str(currNode.val))
                q.append(currNode.left)
                q.append(currNode.right)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodeList = data.split(',')
        if nodeList[0] == "#":
            return None
        root = TreeNode(int(nodeList[0]))
        q = deque([root])
        index = 1
        while q:
            currNode = q.popleft()
            if nodeList[index] != "#":
                currNode.left = TreeNode(int(nodeList[index]))
                q.append(currNode.left)
            index += 1
            if nodeList[index] != '#':
                currNode.right = TreeNode(int(nodeList[index]))
                q.append(currNode.right)
            index += 1
        return root
