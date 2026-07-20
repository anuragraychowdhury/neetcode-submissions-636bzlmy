# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if node == None:
                return float('-inf'), 0 # best overall path, best open path 

            left_best, left_open = dfs(node.left)
            right_best, right_open = dfs(node.right)

            left_clamped = max(0, left_open)
            right_clamped = max(0, right_open)

            best_path = max(left_best, right_best, node.val + left_clamped + right_clamped)
            best_open = node.val + max(left_clamped, right_clamped)

            return best_path, best_open
        
        path, height = dfs(root)
        return path

