class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_visited = set()
        main_diag_visited = set()
        anti_diag_visited = set()
        board = [['.' for c in range(n)] for _ in range(n)]
        res = []

        def solve(row_index):
            if row_index == n:
                subset = []
                for row in board:
                    subset.append("".join(row))
                res.append(subset)
                return 
            
            for col_index in range(n):
                if (col_index in col_visited) or (row_index - col_index in main_diag_visited) or (row_index + col_index in anti_diag_visited):
                    continue
                col_visited.add(col_index)
                main_diag_visited.add(row_index - col_index)
                anti_diag_visited.add(row_index + col_index)
                board[row_index][col_index] = 'Q'
                
                solve(row_index + 1)

                col_visited.remove(col_index)
                main_diag_visited.remove(row_index - col_index)
                anti_diag_visited.remove(row_index + col_index)
                board[row_index][col_index] = '.'

            return 
        
        solve(0)
        return res
            





                


                
