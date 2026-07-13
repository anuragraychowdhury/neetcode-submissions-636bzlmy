# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        
        else:
            if root.left == None and root.right == None:
                return None
            elif root.left and root.right == None:
                return root.left
            elif root.right and root.left == None:
                return root.right
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, root.val)
                return root


