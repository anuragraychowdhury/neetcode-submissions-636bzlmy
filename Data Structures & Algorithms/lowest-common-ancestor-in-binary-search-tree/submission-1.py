# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
if you are ever at a point where the current value we are on is between p and q, we can return that value since
there is not a lower common ancestor (node before the two nodes) than that value (since this is BST, everything is sorted)

if we equal any of the two values, we can also return that value (the value itself counts if it is p or q)
'''

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if p.val <= curr.val <= q.val or q.val <= curr.val <= p.val:
                return curr
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                curr = curr.left
        

