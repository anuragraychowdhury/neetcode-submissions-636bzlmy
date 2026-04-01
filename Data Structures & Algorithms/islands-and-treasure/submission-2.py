class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        distance = 0

        while q:
            size = len(q)
            for i in range(size):
                x,y = q.popleft()    
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = distance + 1
                        q.append((nx, ny))
            distance += 1
        
        

                    