# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid_bst(curr_min, curr_max, node):
            if node == None:
                return True
            elif node.val <= curr_min or node.val >= curr_max:
                return False
            
            if valid_bst(curr_min, node.val, node.left) == False or valid_bst(node.val, curr_max, node.right) == False:
                return False
            
            return True
        
        return valid_bst(float("-inf"), float('inf'), root)
