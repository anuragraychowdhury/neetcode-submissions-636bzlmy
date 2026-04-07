class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O':
                    border.add((i,j))
        
        untouchable = set()
        def dfs(x,y,visited):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x,y) in visited or board[x][y] == 'X':
                return
            visited.add((x,y))
            dfs(x+1,y,visited)
            dfs(x,y+1,visited)
            dfs(x-1,y,visited)
            dfs(x,y-1,visited)

        for x,y in border:
            dfs(x,y,untouchable)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in untouchable:
                    board[i][j] = 'X'
        