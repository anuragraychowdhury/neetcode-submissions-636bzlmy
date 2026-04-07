class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row = False
        first_col = False

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True

        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[0][j] = 0
        
        if first_col:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    matrix[i][0] = 0



                    
        