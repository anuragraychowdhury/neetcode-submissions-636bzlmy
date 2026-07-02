# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        def recurse_tree(node):
            if node == None:
                return None
            
            left_node = recurse_tree(node.left)
            if left_node != None:
                return left_node
            
            count[0] += 1
            if count[0] == k:
                return node.val
            
            right_node = recurse_tree(node.right)

            return right_node
        return recurse_tree(root)

            