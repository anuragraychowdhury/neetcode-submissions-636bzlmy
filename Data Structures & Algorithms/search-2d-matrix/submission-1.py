class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        target_row = None

        while top <= bottom:
            middle_row = (top + bottom) // 2
            if target == matrix[middle_row][0] or target == matrix[middle_row][-1]:
                return True
            elif target < matrix[middle_row][0]:
                bottom = middle_row - 1
            elif target > matrix[middle_row][-1]:
                top = middle_row + 1
            else:
                target_row = middle_row
                break
        
        if target_row == None:
            return False
        
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            middle_elem = (left + right) // 2
            if matrix[target_row][middle_elem] == target:
                return True
            elif matrix[target_row][middle_elem] < target:
                left = middle_elem + 1
            elif matrix[target_row][middle_elem] > target:
                right = middle_elem - 1
        return False
                
            







