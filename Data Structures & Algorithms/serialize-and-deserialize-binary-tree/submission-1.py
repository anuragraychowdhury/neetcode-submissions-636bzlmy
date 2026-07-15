# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        str_order = []
        def preorder(node):
            if node == None:
                str_order.append("n")
                return
            str_order.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            return
        
        preorder(root)
        serialized = ",".join(str_order)
        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serialized_list = data.split(",")
        bookmark = 0
        res = []

        def preorder_build():
            nonlocal bookmark 
            if serialized_list[bookmark] == 'n':
                bookmark += 1
                return None
            new_node = TreeNode(serialized_list[bookmark])
            bookmark += 1

            new_node.left = preorder_build()
            new_node.right = preorder_build()
            
            return new_node

        return preorder_build()



        
        