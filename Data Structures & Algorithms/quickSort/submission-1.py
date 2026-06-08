# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def partition(left, right):
            pivot = right
            i = left
            for j in range(left, right):
                if pairs[j].key < pairs[pivot].key:
                    pairs[i],pairs[j] = pairs[j],pairs[i]
                    i += 1
                else:
                    continue
            
            pairs[pivot], pairs[i] = pairs[i], pairs[pivot]
            return i
        
        def quick_sort(left, right):
            if left >= right:
                return
            
            pivot_placed = partition(left, right)
            quick_sort(left, pivot_placed - 1)
            quick_sort(pivot_placed + 1, right)

        quick_sort(0, len(pairs) - 1)
        return pairs
        

