class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r,c,visited):
            area = 0
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))
            area += 1

            area += dfs(r + 1,c,visited)
            area += dfs(r,c + 1,visited)
            area += dfs(r - 1,c,visited)
            area += dfs(r,c - 1,visited)
            
            return area
        
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited:
                    continue
                elif grid[i][j] == 1:
                    pote_area = dfs(i,j,visited)
                    max_area = max(max_area, pote_area)
        return max_area
