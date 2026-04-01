# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def partition(left, right):
            pivot = pairs[right]
            left_bound = left

            for i in range(left, right):
                if pairs[i].key < pivot.key:
                    pairs[left_bound], pairs[i] = pairs[i], pairs[left_bound]
                    left_bound += 1
            
            pairs[right], pairs[left_bound] = pairs[left_bound], pairs[right]
            return left_bound
        
        def quicksort(left, right):
            if left >= right:
                return 
            pivot_index = partition(left, right)
            quicksort(left, pivot_index - 1)
            quicksort(pivot_index + 1, right)
        
        quicksort(0, len(pairs) - 1)
        return pairs