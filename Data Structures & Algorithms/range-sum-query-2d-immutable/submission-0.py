class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.prefix = [([0] * (self.cols + 1)) for _ in range(self.rows + 1)]
        
        for i in range(1, len(self.prefix)):
            for j in range(1, len(self.prefix[0])):
                self.prefix[i][j] = matrix[i-1][j-1] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]
        return

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1]