# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0,0) # with_node, without_node
            
            with_left_child, without_left_child = dfs(node.left)
            with_right_child, without_right_child = dfs(node.right)

            with_current_node = node.val + without_left_child + without_right_child
            without_current_node = max(with_left_child, without_left_child) + max(with_right_child, without_right_child)

            return (with_current_node, without_current_node)
        
        final_with, final_without = dfs(root)

        return max(final_with, final_without)
