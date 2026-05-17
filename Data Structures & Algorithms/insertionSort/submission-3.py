# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        states = []
        states.append(pairs[:])
        for i in range(1, len(pairs)):
            curr_index = i
            while curr_index > 0 and pairs[curr_index].key < pairs[curr_index - 1].key:
                pairs[curr_index], pairs[curr_index - 1] = pairs[curr_index - 1], pairs[curr_index]
                curr_index -= 1
            states.append(pairs[:])
        return states 
