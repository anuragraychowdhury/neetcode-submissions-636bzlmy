class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = set()
        for i in range(len(board)):
            for j in range(len(board[0])):

                if ((i == 0 or j == 0) or (i == len(board) - 1 or j == len(board[0]) - 1)) and board[i][j] == 'O':
                    border.add((i,j))
        
        def dfs(x,y,safe):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x,y) in safe or board[x][y] == 'X':
                return 
            safe.add((x,y))
            dfs(x,y + 1,safe)
            dfs(x,y - 1,safe)
            dfs(x + 1,y,safe)
            dfs(x - 1,y,safe)
            return 
        
        safe = set()
        for x,y in border:
            dfs(x,y,safe)
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in safe and board[i][j] == 'O':
                    board[i][j] = 'X'
        

                    
        