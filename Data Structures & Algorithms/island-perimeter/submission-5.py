class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def dfs(x,y,visited):
            perimeter = 0
            if (x,y) in visited:
                return 0
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 1
            
            visited.add((x,y))
            perimeter += dfs(x+1, y, visited)
            perimeter += dfs(x, y+1, visited)
            perimeter += dfs(x-1, y, visited)
            perimeter += dfs(x, y-1, visited)

            return perimeter
        
        vis = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j,vis) 
                        