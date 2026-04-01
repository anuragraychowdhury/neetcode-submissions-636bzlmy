class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pacific.add((i,j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    atlantic.add((i,j))
        
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(x, y, visited, curr_max):
            if (x < 0 or x >= len(heights)) or (y < 0 or y >= len(heights[0])) or ((x,y) in visited) or (heights[x][y] < curr_max):
                return 
            visited.add((x,y))
            if heights[x][y] >= curr_max:
                curr_max = heights[x][y]
            
            dfs(x + 1, y, visited, curr_max)
            dfs(x, y + 1, visited, curr_max)
            dfs(x - 1, y, visited, curr_max)
            dfs(x, y - 1, visited, curr_max)
        
        for x, y in pacific:
            dfs(x, y, pacific_visited, heights[x][y])
        
        for x, y in atlantic:
            dfs(x, y, atlantic_visited, heights[x][y])
        
        union_set = atlantic_visited & pacific_visited
        res = []

        for x, y in union_set:
            res.append([x,y])
        
        return res