# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest_path = 0
        def postorder(node):
            nonlocal longest_path
            if node == None:
                return (0,0) # increasing path, decreasing path
            
            left_increasing, left_decreasing = postorder(node.left)
            right_increasing, right_decreasing = postorder(node.right)

            curr_left_increasing = 0
            curr_right_increasing = 0
            curr_left_decreasing = 0
            curr_right_decreasing = 0

            if node.left:
                if node.val == node.left.val - 1:
                    curr_left_increasing = 1 + left_increasing
                elif node.val == node.left.val + 1:
                    curr_left_decreasing = 1 + left_decreasing

            if node.right:
                if node.val == node.right.val - 1:
                    curr_right_increasing = 1 + right_increasing
                elif node.val == node.right.val + 1:
                    curr_right_decreasing = 1 + right_decreasing
            
            longest_path = max(longest_path, 1 + curr_left_increasing + curr_right_decreasing, 1 + curr_left_decreasing + curr_right_increasing)
                          
            increasing = max(curr_right_increasing, curr_left_increasing)
            decreasing = max(curr_right_decreasing, curr_left_decreasing)

            return (increasing, decreasing)
        
        postorder(root)
        return longest_path
            
        