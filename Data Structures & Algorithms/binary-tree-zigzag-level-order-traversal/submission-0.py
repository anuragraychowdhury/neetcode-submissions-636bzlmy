# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        [1, [3,2], [4,5,6,7], [15,14,13,12,11,10,9,8]]

        algo:
            level order traversal
            take the length of the queue as size
            popleft() for i in range(len(size))
            level.append(node) -> node that you poppped left
            if the level_count % 2 == 0:
                append the level to res as it
            else:
                append the level to res in reverse (level[::-1])
            after every for loop iteration, level_count += 1
        '''
        if not root:
            return []
        
        q = deque()
        q.append(root)
        level_count = 0
        res = []

        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if level_count % 2 == 0:
                res.append(level)
            else:
                res.append(level[::-1])
            
            level_count += 1
        return res











