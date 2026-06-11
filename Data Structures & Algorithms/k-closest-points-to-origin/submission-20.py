import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(i):
            x, y = points[i]
            return x * x + y * y
        
        def quickSelect(left, right):
            if left >= right:
                return
            
            frontier = left
            pivot = right
            pivot_dist = dist(pivot)

            for i in range(left, right):
                if dist(i) < pivot_dist:
                    points[i], points[frontier] = points[frontier], points[i]
                    frontier += 1
            points[pivot], points[frontier] = points[frontier], points[pivot]

            if frontier == k - 1:
                return
            elif frontier < k - 1:
                return quickSelect(frontier + 1, right)
            else:
                return quickSelect(left, frontier - 1)

        quickSelect(0, len(points) - 1)
        return points[:k]         
