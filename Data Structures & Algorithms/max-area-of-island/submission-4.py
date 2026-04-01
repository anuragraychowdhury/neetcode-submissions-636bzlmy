class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0 or (x,y) in visited:
                return 0
            visited.add((x,y))
            area = 1

            area += dfs(x + 1, y)
            area += dfs(x, y + 1)
            area += dfs(x - 1, y)
            area += dfs(x, y - 1)

            return area 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    pote_area = dfs(i,j)
                    max_area = max(pote_area, max_area)
        return max_area

            
