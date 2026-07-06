# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = [-float('inf')]
        
        def postorder(node):
            if node == None:
                return 0
            
            left_path = postorder(node.left)
            right_path = postorder(node.right)

            bent_path = node.val + max(0, left_path) + max(0, right_path)
            if bent_path > best[0]:
                best[0] = bent_path
            
            best_open_path = node.val + max(0, left_path, right_path)

            return best_open_path
        
        postorder(root)
        return best[0]