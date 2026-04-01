# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        start_min = float('-inf')
        start_max = float('inf')

        def is_valid(node, curr_min, curr_max):
            if not node:
                return True
            elif not (curr_min < node.val < curr_max):
                return False
            else:
                return is_valid(node.left, curr_min, node.val) and is_valid(node.right, node.val, curr_max)
        
        return is_valid(root, start_min, start_max)