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
                return (0,float('-inf')) # best_side, best_overall
            
            best_left_side, best_left_overall = dfs(node.left)
            best_right_side, best_right_overall = dfs(node.right)

            best_side = node.val + max(0, best_left_side, best_right_side)
            best_overall = max(best_left_overall, best_right_overall, node.val + max(0, best_left_side) + max(0, best_right_side))

            return (best_side, best_overall)
        
        bs, bo = dfs(root)
        return bo