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

        def recurse_quadrant(start_x, start_y, size):
            is_leaf = True
            first_value = grid[start_x][start_y]
            for i in range(size):
                for j in range(size):
                    if grid[start_x + i][start_y + j] != first_value:
                        is_leaf = False
                        break
            
            if is_leaf == True:
                return Node(first_value, True, None, None, None, None)
            else:
                size = size // 2
                top_left = recurse_quadrant(start_x, start_y, size)
                top_right = recurse_quadrant(start_x, start_y + size, size)
                bottom_left = recurse_quadrant(start_x + size, start_y, size)
                bottom_right = recurse_quadrant(start_x + size, start_y + size, size)
            
            return Node(1, False, top_left, top_right, bottom_left, bottom_right)
        
        return recurse_quadrant(0,0,len(grid))

