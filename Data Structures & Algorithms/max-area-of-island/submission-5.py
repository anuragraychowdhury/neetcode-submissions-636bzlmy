class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(x,y,visited):
            area = 1
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x,y) in visited or grid[x][y] == 0:
                return 0
            
            visited.add((x,y))
            area += dfs(x,y+1,visited)
            area += dfs(x,y-1,visited)
            area += dfs(x+1,y,visited)
            area += dfs(x-1,y,visited)

            return area
        
        visited_coords = set()
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited_coords:
                    pote_area = dfs(i,j,visited_coords)
                    max_area = max(max_area, pote_area)
        return max_area
        

        

            
