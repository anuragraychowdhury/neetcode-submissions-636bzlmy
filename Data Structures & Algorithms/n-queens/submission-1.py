class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        main_diag_set = set()
        anti_diag_set = set()
        res = []
        board = [["." for _ in range(n)] for c in range(n)]

        def solve(row_index):
            if row_index == n:
                subset = []
                for row in board:
                    subset.append("".join(row))
                res.append(subset)
                return
            
            for i in range(n):
                if (i in col_set) or (row_index - i in main_diag_set) or (row_index + i in anti_diag_set):
                    continue
                
                col_set.add(i)
                main_diag_set.add(row_index - i)
                anti_diag_set.add(row_index + i)
                board[row_index][i] = 'Q'
                
                solve(row_index + 1)

                col_set.remove(i)
                main_diag_set.remove(row_index - i)
                anti_diag_set.remove(row_index + i)
                board[row_index][i] = '.'
            
            return 
        
        solve(0)
        return res




                    