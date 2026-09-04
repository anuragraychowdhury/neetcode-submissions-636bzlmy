# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        def inorder(node, arr):
            if node == None:
                return 
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
            return 
        
        arr1 = []
        arr2 = []

        inorder(root1, arr1)
        inorder(root2, arr2)

        left = 0
        right = len(arr2) - 1

        while left < len(arr1) and right >= 0:
            candidate = arr1[left] + arr2[right]
            if candidate == target:
                return True
            elif candidate < target:
                left += 1
            else:
                right -= 1
        return False

            
