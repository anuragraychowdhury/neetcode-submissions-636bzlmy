class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()
            directions = [[1, 0], [0, 1], [-1 ,0], [0, -1]]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == 2147483647:
                    grid[row][col] = 1 + grid[r][c]
                    queue.append((row,col))