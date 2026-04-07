class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_coords = set()
        atlantic_coords = set()

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pacific_coords.add((i,j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    atlantic_coords.add((i,j))
        
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(x,y,visited,curr_max):
            if x < 0 or x >= len(heights) or y < 0 or y >= len(heights[0]) or (x,y) in visited or heights[x][y] < curr_max:
                return
            
            visited.add((x,y))
            
            dfs(x + 1,y,visited,heights[x][y])
            dfs(x,y + 1,visited,heights[x][y])
            dfs(x - 1,y,visited,heights[x][y])
            dfs(x,y - 1,visited,heights[x][y])
 
        
        for x,y in pacific_coords:
            dfs(x,y,pacific_visited,heights[x][y])
        
        for x,y in atlantic_coords:
            dfs(x,y,atlantic_visited,heights[x][y])
        
        union = pacific_visited & atlantic_visited
        return list(union)
        

            
            
            
            