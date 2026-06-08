# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        res = []
        res.append(pairs.copy())
        for i in range(1, len(pairs)):
            current_index = i
            while current_index > 0 and pairs[current_index].key < pairs[current_index - 1].key:
                pairs[current_index], pairs[current_index - 1] = pairs[current_index - 1], pairs[current_index]
                current_index -= 1
            res.append(pairs.copy())
        return res