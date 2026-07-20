# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.best_value = 0

        def dfs(node):
            if node == None:
                # best path taking the node, best path without taking the node
                return 0,0
            included_left, excluded_left = dfs(node.left)
            included_right, excluded_right = dfs(node.right)

            include_curr = node.val + excluded_left + excluded_right
            skip_curr = max(included_left, excluded_left) + max(included_right, excluded_right)

            return include_curr, skip_curr
        
        a,b = dfs(root)
        return max(a,b)
        




