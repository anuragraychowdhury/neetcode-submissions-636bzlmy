# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_count = 0
        def inorder(node):
            if node == None:
                return None
            
            res = inorder(node.left)
            if res != None:
                return res
            
            self.k_count += 1
            if self.k_count == k:
                return node.val
            
            res = inorder(node.right)
            return res
        return inorder(root)