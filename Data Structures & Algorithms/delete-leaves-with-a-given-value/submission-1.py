# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def delete_leaves(node):
            if node == None:
                return
            
            node.left = delete_leaves(node.left)
            node.right = delete_leaves(node.right)

            if node.val == target and node.left == None and node.right == None:
                return None
            
            return node
        
        return delete_leaves(root)