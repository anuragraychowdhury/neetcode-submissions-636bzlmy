class Solution:
    def totalNQueens(self, n: int) -> int:
        counter = [0]
        col_set = set()
        main_diag = set()
        anti_diag = set()
        board = [['.' for c in range(n)] for r in range(n)]

        def solve(row_index):
            if row_index == n:
                counter[0] += 1
                return 
            
            for i in range(n):
                if (i in col_set) or (row_index - i in main_diag) or (row_index + i in anti_diag):
                    continue
                col_set.add(i)
                main_diag.add(row_index - i)
                anti_diag.add(row_index + i)
                board[row_index][i] = 'Q'

                solve(row_index + 1)

                col_set.remove(i)
                main_diag.remove(row_index - i)
                anti_diag.remove(row_index + i)
                board[row_index][i] = '.'
            return 
        
        solve(0)
        return counter[0]
