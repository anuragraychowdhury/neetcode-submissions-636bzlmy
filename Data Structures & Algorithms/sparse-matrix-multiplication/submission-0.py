class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        
        def dot_product(row, col):
            x = 0
            y = 0
            total = 0
            while x < len(row) and y < len(col):
                if row[x][0] == col[y][0]:
                    total += (row[x][1] * col[y][1])
                    x += 1
                    y += 1
                elif row[x][0] < col[y][0]:
                    x += 1
                else:
                    y += 1
            return total
                


        rows_mat_one = []
        cols_mat_two = []

        for i in range(len(mat1)):
            curr_row = []
            for j in range(len(mat1[0])):
                if mat1[i][j] != 0:
                    curr_row.append((j, mat1[i][j]))
            rows_mat_one.append(curr_row)
        
        for j in range(len(mat2[0])):
            curr_col = []
            for i in range(len(mat2)):
                if mat2[i][j] != 0:
                    curr_col.append((i, mat2[i][j]))
            cols_mat_two.append(curr_col)
        
        res = [[0] * len(mat2[0]) for _ in range(len(mat1))]

        for i in range(len(res)):
            for j in range(len(res[0])):
                res[i][j] = dot_product(rows_mat_one[i], cols_mat_two[j])
        return res


