# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if (not node1) and (not node2):
                return True
            elif (not node1 and node2) or (not node2 and node1):
                return False
            elif node1.val != node2.val:
                return False
            else:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
        
        if (root and not subRoot) or (subRoot and not root):
            return False
        if isSame(root, subRoot) == True:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        return self.isSubtree(root, subRoot)
