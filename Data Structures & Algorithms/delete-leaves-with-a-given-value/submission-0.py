# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val == target and node.left == None and node.right == None:
                return None
            
            return node
            
        return dfs(root)
