class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(r,c,visited):
            if (r,c) in visited:
                return 
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == "0":
                return 
            visited.add((r,c))
            dfs(r+1,c,visited)
            dfs(r,c+1,visited)
            dfs(r-1,c,visited)
            dfs(r,c-1,visited)

            return
        
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j,visited)
                    total += 1
        return total 