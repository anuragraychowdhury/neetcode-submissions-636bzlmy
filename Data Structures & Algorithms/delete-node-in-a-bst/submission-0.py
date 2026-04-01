# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def dfs(node, key_to_delete):
            if node is None:
                return None
            elif node.val < key_to_delete:
                node.right = dfs(node.right, key_to_delete)
                return node
            elif node.val > key_to_delete:
                node.left = dfs(node.left, key_to_delete)
                return node
            
            else:
                if not node.left and not node.right:
                    return None
                elif node.left and not node.right:
                    return node.left
                elif node.right and not node.left:
                    return node.right
                else:
                    curr = node
                    curr = curr.right
                    while curr.left:
                        curr = curr.left
                    # found the smallest node in the right subtree
                    # replace the parent node with that value and call delete 
                    replacement_val = curr.val
                    node.val = replacement_val
                    node.right = dfs(node.right, replacement_val)
                    return node
        
        return dfs(root, key)
                    

                
                    



