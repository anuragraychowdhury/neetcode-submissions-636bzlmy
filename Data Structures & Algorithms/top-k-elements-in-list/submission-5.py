class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for number in nums:
            freq_map[number] = freq_map.get(number, 0) + 1
        
        numbers = list(freq_map.keys())

        def quickSelect(left, right):
            if left >= right:
                return
            
            frontier = left
            pivot = freq_map[numbers[right]]

            for i in range(left, right):
                if freq_map[numbers[i]] < pivot:
                    numbers[frontier], numbers[i] = numbers[i], numbers[frontier]
                    frontier += 1
            
            numbers[right], numbers[frontier] = numbers[frontier], numbers[right]

            target_index = len(numbers) - k
            if frontier == target_index:
                return
            elif frontier < target_index:
                return quickSelect(frontier + 1, right)
            else:
                return quickSelect(left, frontier - 1)
        
        quickSelect(0, len(numbers) - 1)
        return numbers[len(numbers) - k:]