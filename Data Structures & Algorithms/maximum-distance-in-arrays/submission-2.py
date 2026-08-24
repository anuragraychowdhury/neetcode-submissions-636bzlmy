class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        res = 0

        for array in arrays[1:]:
            res = max(res, array[-1] - smallest, biggest - array[0])
            biggest = max(biggest, array[-1])
            smallest = min(smallest, array[0])
        return res
        
        
