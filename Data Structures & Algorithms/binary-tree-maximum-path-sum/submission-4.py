# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def postorder(node):
            if node == None:
                return (float("-inf"), 0)
            left_path, left_height = postorder(node.left)
            right_path, right_height = postorder(node.right)

            curr_path = node.val + max(0, left_height) + max(0, right_height)
            best_path = max(curr_path, left_path, right_path)

            return (best_path, node.val + max(0, left_height, right_height))
        
        res, _ = postorder(root)
        return res



