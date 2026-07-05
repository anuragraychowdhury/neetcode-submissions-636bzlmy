# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def house_robber(node):
            if node == None:
                return (0,0) 
            
            left_with_root, left_without_root = house_robber(node.left)
            right_with_root, right_without_root = house_robber(node.right)

            with_root = node.val + left_without_root + right_without_root
            without_root = max(left_with_root, left_without_root) + max(right_with_root, right_without_root)
            
            return with_root, without_root
        
        w_r, wo_r = house_robber(root)
        return max(w_r, wo_r)
        
