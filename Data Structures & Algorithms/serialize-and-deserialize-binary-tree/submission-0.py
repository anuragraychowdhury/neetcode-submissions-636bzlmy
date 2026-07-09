# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        subset = []
        def preorder(node):
            if node == None:
                subset.append("n")
                return 
            subset.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(subset)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_lst = data.split(",")
        bookmark = 0
        def preorder_build():
            nonlocal bookmark
            if data_lst[bookmark] == 'n':
                bookmark += 1
                return
            processed_node = TreeNode(data_lst[bookmark])
            bookmark += 1

            processed_node.left = preorder_build()
            processed_node.right = preorder_build()

            return processed_node
        
        return preorder_build()


            

            

                





