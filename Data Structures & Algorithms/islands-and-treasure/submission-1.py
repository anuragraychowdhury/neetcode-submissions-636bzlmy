class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        curr_dist = 1
        
        while q:
            size = len(q)
            for i in range(size):
                x,y = q.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == -1:
                        continue
                    elif grid[nx][ny] == 2147483647:
                        grid[nx][ny] = curr_dist
                        q.append((nx, ny))
            curr_dist += 1
        
        

                    