class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh_oranges = 0
        total_time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        if len(q) == 0 and fresh_oranges == 0:
            return 0
        elif len(q) == 0 and fresh_oranges > 0:
            return -1
        
        while q:
            size = len(q)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for i in range(size):
                x,y = q.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] == 0:
                        continue 
                    elif grid[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                        fresh_oranges -= 1
            
            total_time += 1
        
        
        if fresh_oranges == 0:
            return total_time - 1
        else:
            return -1