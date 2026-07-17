class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x,y,visited):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x,y) in visited or grid[x][y] == '0':
                return 
            
            visited.add((x,y))
            
            dfs(x,y + 1,visited)
            dfs(x,y - 1,visited)
            dfs(x + 1,y,visited)
            dfs(x - 1,y,visited)
            
            return 
        
        visited_coords = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited_coords and grid[i][j] == '1':
                    dfs(i,j,visited_coords)
                    islands += 1
        return islands
