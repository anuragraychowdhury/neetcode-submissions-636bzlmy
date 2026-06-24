import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i):
            x,y = points[i]
            return math.sqrt((x)**2 + (y)**2)
        
        def quickSelect(left, right):
            if left >= right:
                return 
            
            frontier = left
            pivot = distance(right)

            for i in range(left, right):
                if distance(i) <= pivot:
                    points[i], points[frontier] = points[frontier], points[i]
                    frontier += 1
            points[right], points[frontier] = points[frontier], points[right]

            if frontier == k - 1:
                return 
            elif frontier > k - 1:
                quickSelect(left, frontier - 1)
            else:
                quickSelect(frontier + 1, right)
        
        quickSelect(0, len(points) - 1)
        return points[:k]



