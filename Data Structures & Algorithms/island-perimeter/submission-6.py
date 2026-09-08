class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x,y):
            perimeter = 0
            if (x,y) in visited:
                return 0
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                return 1
            visited.add((x,y))
            
            perimeter += dfs(x,y + 1)
            perimeter += dfs(x,y - 1)
            perimeter += dfs(x + 1,y)
            perimeter += dfs(x - 1,y)

            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
        
