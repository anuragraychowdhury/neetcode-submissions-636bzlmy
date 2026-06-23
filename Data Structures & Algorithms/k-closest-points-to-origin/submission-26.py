import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i):
            x,y = points[i]
            return math.sqrt(x**2 + y**2)
        
        max_heap = []
        for i in range(len(points)):
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance(i), i))
                continue
            if -distance(i) > max_heap[0][0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance(i), i))
        res = []
        for dist, index in max_heap:
            res.append(points[index])
        return res
                

