class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(x,y,index):
            if index == len(word):
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (x,y) in visited or board[x][y] != word[index]:
                return False
            
            visited.add((x,y))
            
            down = dfs(x + 1, y, index + 1)
            right = dfs(x, y + 1, index + 1)
            up = dfs(x - 1, y, index + 1)
            left = dfs(x, y - 1, index + 1)    
            
            visited.remove((x,y))        

            return (up or down or left or right)
        
        index = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,index):
                    return True
        return False
        