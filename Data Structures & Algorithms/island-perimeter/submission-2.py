class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r, c, visited):
            perimeter = 0
            if (r,c) in visited:
                return 0 
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            
            visited.add((r,c))
            
            perimeter += dfs(r + 1, c,visited)
            perimeter += dfs(r, c + 1,visited)
            perimeter += dfs(r - 1, c,visited)
            perimeter += dfs(r, c - 1,visited)

            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j,visited)
        

            
            

            

