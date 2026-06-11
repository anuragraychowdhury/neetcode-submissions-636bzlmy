import math 
import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(i):
            x, y = points[i]
            return x * x + y * y

        def quickSelect(left, right):
            if left >= right:
                return

            pivot_idx = random.randint(left, right)
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            pivot_dist = dist(right)

            frontier = left
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    points[i], points[frontier] = points[frontier], points[i]
                    frontier += 1

            points[frontier], points[right] = points[right], points[frontier]

            if frontier == k - 1:
                return
            elif frontier < k - 1:
                quickSelect(frontier + 1, right)
            else:
                quickSelect(left, frontier - 1)

        quickSelect(0, len(points) - 1)
        return points[:k]