# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def find_diameter(node):
            if node == None:
                return (0,0) # height, diameter
            left_height, left_diameter = find_diameter(node.left)
            right_height, right_diameter = find_diameter(node.right)

            max_diameter = max(left_diameter, right_diameter, left_height + right_height)
            height = 1 + max(left_height, right_height)
            return (height, max_diameter)
        
        h, d = find_diameter(root)
        return d
        