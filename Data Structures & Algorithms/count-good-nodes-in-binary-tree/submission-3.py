# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = [0]

        def count_good_nodes(node, previous_max):
            if node.val >= previous_max:
                good_nodes[0] += 1
                previous_max = node.val
            
            if node.left:
                count_good_nodes(node.left, previous_max)
            if node.right:
                count_good_nodes(node.right, previous_max)
            return
        
        count_good_nodes(root, root.val)
        return good_nodes[0]

            