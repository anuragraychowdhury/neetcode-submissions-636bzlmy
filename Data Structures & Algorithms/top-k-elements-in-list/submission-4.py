import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in range(len(nums)):
            freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1
        
        freq_list = [[] for _ in range(len(nums) + 1)]
        for number, freq in freq_map.items():
            freq_list[freq].append(number)
        
        res = []
        for i in range(len(freq_list) - 1, -1, -1):
            if len(res) == k:
                return res
            res.extend(freq_list[i])
        return res