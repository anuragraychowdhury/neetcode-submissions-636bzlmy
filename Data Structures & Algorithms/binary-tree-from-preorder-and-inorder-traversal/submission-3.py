# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_node = TreeNode(preorder[0])
        split_index = inorder.index(root_node.val)
        left_size = split_index
        right_size = len(inorder) - split_index - 1

        root_node.left = self.buildTree(preorder[1:1+left_size], inorder[:split_index])
        root_node.right = self.buildTree(preorder[len(preorder) - right_size:], inorder[split_index + 1:])  

        return root_node      