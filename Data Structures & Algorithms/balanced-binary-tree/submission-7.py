# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height_check(root):
            if root == None:
                return 0
            
            left_depth = height_check(root.left)
            right_depth = height_check(root.right)

            if (left_depth == -1 or right_depth == -1) or (abs(right_depth - left_depth ) > 1):
                return -1
            
            return 1 + max(left_depth, right_depth)
        
        if height_check(root) == -1:
            return False
        return True 
            