class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        for number in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, number)
                continue
            else:
                if min_heap[0] < number:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, number)
        return min_heap[0]