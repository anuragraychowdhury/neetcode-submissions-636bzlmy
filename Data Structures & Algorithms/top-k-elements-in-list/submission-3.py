import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        freq_map = {}

        for number in nums:
            freq_map[number] = freq_map.get(number, 0) + 1
        print(freq_map)
        
        for number, freq in freq_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, number))
            elif freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, number))
        
        res = []
        for elem in min_heap:
            res.append(elem[1])
        return res