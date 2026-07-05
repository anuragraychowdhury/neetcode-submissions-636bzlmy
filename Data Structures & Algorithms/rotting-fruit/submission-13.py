class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        fresh_fruit = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_fruit += 1
        
        if not queue and fresh_fruit > 0:
            return -1
        elif not queue:
            return 0
        
        minutes = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx,ny))
                        fresh_fruit -= 1
            minutes += 1
        
        if fresh_fruit == 0:
            return minutes - 1
        else:
            return -1

