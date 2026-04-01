class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        put all the rotten oranges into a queue
        directions array
        while the q is full, check the cells next to the rotten orange
        mark the orange as rotten and then add it to the queue to check neighboring directions to it
        keep track of fresh oranges as a whole
        as you mark one as rotten, decrement the fresh one
        by the end of the queue, if you don't have fresh_oranges == 0, return -1 (not possible)
        otherwise, for every time you clear our a queue, increment time (each wave of oranges is one minute); return time
        '''

        time = 0
        fresh = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q and fresh > 0:
            size = len(q)
            for i in range(size):
                x,y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        fresh -= 1
                        grid[nx][ny] = 2
                        q.append((nx,ny))
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1

