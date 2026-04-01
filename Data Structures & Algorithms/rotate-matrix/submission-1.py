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
        # for i in range(len(matrix)):
        #     for j in range(i, len(matrix[0])):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # for row in matrix:
        #     row.reverse()

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            left = top
            right = bottom 

            for i in range(right - left):
                top_left = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = top_left
            top += 1
            bottom -= 1
        