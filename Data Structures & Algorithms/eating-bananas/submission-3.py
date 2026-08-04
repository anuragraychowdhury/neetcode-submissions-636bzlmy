class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best_k = max(piles)

        while left <= right:
            k = (left + right) // 2
            total_hours = 0
            for p in piles:
                time_taken = math.ceil(p/k)
                total_hours += time_taken
            
            if total_hours > h:
                left = k + 1
            else:
                best_k = k
                right = k - 1
        return best_k