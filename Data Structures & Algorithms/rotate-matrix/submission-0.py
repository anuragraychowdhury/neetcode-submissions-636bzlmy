class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        1,2,3
        4,5,6
        7,8,9

        transposed
        1,4,7
        2,5,8
        3,6,9

        reversed
        7,4,1
        8,5,2
        9,6,3
        '''
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()
        






        