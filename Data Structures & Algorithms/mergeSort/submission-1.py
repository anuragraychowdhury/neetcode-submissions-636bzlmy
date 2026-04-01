# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def partition(arr):
            if len(arr) <= 1:
                return arr
            
            midpoint = len(arr) // 2
            left_half = partition(arr[:midpoint])
            right_half = partition(arr[midpoint:])

            res = merge(left_half, right_half)

            return res
        
        def merge(arr1, arr2):
            arr_one_iter = 0
            arr_two_iter = 0
            merged = []

            while arr_one_iter < len(arr1) and arr_two_iter < len(arr2):
                if arr1[arr_one_iter].key <= arr2[arr_two_iter].key:
                    merged.append(arr1[arr_one_iter])
                    arr_one_iter += 1
                else:
                    merged.append(arr2[arr_two_iter])
                    arr_two_iter += 1
            
            while arr_one_iter < len(arr1):
                merged.append(arr1[arr_one_iter])
                arr_one_iter += 1
            
            while arr_two_iter < len(arr2):
                merged.append(arr2[arr_two_iter])
                arr_two_iter += 1
            
            return merged
        
        result = partition(pairs)
        return result
            

