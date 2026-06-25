class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        min_heap = []
        for number in nums:
            freq_map[number] = freq_map.get(number, 0) + 1
        
        for number, freq in freq_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, number))
                continue
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, number))
        res = []
        for freq, number in min_heap:
            res.append(number)
        return res
