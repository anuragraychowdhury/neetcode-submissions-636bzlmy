class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(x,y):
            return math.sqrt((x - 0)**2 + (y - 0)**2)
        
        min_heap = []
        for x,y in points:
            dist = distance(x,y)
            if len(min_heap) < k:
                heapq.heappush(min_heap, (-dist, x, y))
                continue
            else:
                if dist < -min_heap[0][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (-dist, x, y))
        
        res = []
        while min_heap:
            dist, x_coord, y_coord = heapq.heappop(min_heap)
            res.append([x_coord, y_coord])
        
        return res