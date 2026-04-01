class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) >= 2:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            if stone1 == stone2:
                continue
            elif abs(stone1) > abs(stone2):
                new_stone = (abs(stone1) - abs(stone2))
                heapq.heappush(max_heap, -new_stone)
        
        if max_heap:
            return abs(max_heap[0])
        else:
            return 0
