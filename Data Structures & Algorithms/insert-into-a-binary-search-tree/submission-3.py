# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        curr = root
        while curr:
            if curr.left and val < curr.val:
                curr = curr.left
            elif curr.right and val > curr.val:
                curr = curr.right
            else:
                new_node = TreeNode(val)
                if curr.val < new_node.val:
                    curr.right = new_node
                else:
                    curr.left = new_node
                
                return root

