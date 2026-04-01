# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            level = []
            for i in range(size):
                curr = q.popleft()
                if curr and curr.left:
                    q.append(curr.left)
                if curr and curr.right:
                    q.append(curr.right)
                level.append(curr.val)
            
            if level[-1]:
                res.append(level[-1])
        return res
                




            