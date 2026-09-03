# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.bookmark = 0
        index_map = {}
        for index, value in enumerate(inorder):
            index_map[value] = index
        
        def build_tree(left, right):
            if left > right:
                return None            
            root_value = preorder[self.bookmark]
            self.bookmark += 1
            root_index = index_map[root_value]
            new_node = TreeNode(root_value)
            new_node.left = build_tree(left, root_index - 1)
            new_node.right = build_tree(root_index + 1, right)
            return new_node
        
        return build_tree(0, len(inorder) - 1)