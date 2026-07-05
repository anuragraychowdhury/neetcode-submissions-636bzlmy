class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        distance = 0

        while queue:
            size = len(queue)
            for i in range(size):
                x,y = queue.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = distance + 1
                        queue.append((nx,ny))
            distance += 1
        