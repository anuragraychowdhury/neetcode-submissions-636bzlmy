"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        size = len(grid)
        
        def dfs(x, y, size):
            reference_element = grid[x][y]
            leaf_flag = True
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != reference_element:
                        leaf_flag = False
                        break
            
            if leaf_flag == True:
                return Node(reference_element, True, None, None, None, None)
            
            halfed = size // 2
            topLeft = dfs(x, y, halfed)
            topRight = dfs(x, y + halfed, halfed)
            bottomLeft = dfs(x + halfed, y, halfed)
            bottomRight = dfs(x + halfed, y + halfed, halfed)

            return Node(reference_element, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(0, 0, size)

